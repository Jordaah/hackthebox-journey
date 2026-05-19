import os
import string
import random
from threading import Thread
from dotenv import load_dotenv
from flask_session import Session
from flask import Flask, jsonify, request, send_from_directory, session

import complaints
from auth import authenticated
from csrf import csrf_protection
from model import test_model, dataset, predict

load_dotenv()

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = 'sessions/'
app.config['SESSION_COOKIE_NAME'] = 'space_cookie'
app.config['SESSION_COOKIE_SECURE'] = False 
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

app.secret_key = os.environ.get("FLASK_SECRET_KEY")

Session(app)

ALIEN_USERNAME = os.environ.get("ALIENT_USERNAME")
ALIENT_PASSWORD = os.environ.get("ALIENT_PASSWORD")

MODELS = "models/"
MAIN_MODEL = "models/main.h5"
    
def message(content: str):
    return jsonify({"message": content})

@app.route("/api/login", methods=["POST"])
def api_login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        return message("Paramters 'username' and 'password' required"), 400
    
    if username == ALIEN_USERNAME and password == ALIENT_PASSWORD:
        session['username'] = username
        return jsonify(), 200
    else:
        return message("Invalid credentials"), 401


@app.route("/api/metrics", methods=["GET"])
def get_metrics():
    metrics = test_model(MAIN_MODEL)
    return jsonify(metrics)


@app.route("/api/data", methods=["GET"])
def get_dataset():
    return jsonify({"count":dataset()})


@app.route("/api/predict", methods=["POST"])
@csrf_protection
def do_predition():
    image_data = request.json.get("image_data", None)
    if image_data == None:
        return message("Parameter 'image_data' required!"), 400
    
    prediction = predict(image_data)
    return jsonify({"prediction": prediction}), 200

@app.route("/api/complaint", methods=["POST"])
@csrf_protection
def submit_complaint():
    description = request.json.get("description", None)
    image_data = request.json.get("image_data", None)
    prediction = request.json.get("prediction", None)
    if not description or not image_data or prediction == None:
        return message("Parameters 'description', 'image_data' and 'prediction' requred"), 400
    
    complaints.add_complaint(description, image_data, prediction)

    Thread(target=complaints.check_complaints, args=(ALIEN_USERNAME, ALIENT_PASSWORD,)).start()

    return jsonify(), 204


@app.route("/api/internal/model", methods=["POST"])
@authenticated
@csrf_protection
def submit_model():
    if "file" not in request.files:
        return message("Failed to upload model! You must specify a file!"), 400

    file = request.files["file"]
    
    if file and ".h5" in file.filename:
        name = "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(12))
        name += ".h5"
        # Save model
        file.save(os.path.join(MODELS, name))
        try:
            test_model(MODELS+name)
            return message(f"Success, model saved at: /models/{name}")
            
        except Exception as e:
            print(e)
            return message("Model was uploaded but there were some errors during testing"), 422
    else:
        return message("Failed to upload model!"), 400


@app.route("/api/internal/models/<path:path>")
@authenticated
def serve_models(path):
    return send_from_directory("models", path)


@app.route("/api/internal/complaints", methods=["GET"])
@authenticated
def get_complaints():
    return jsonify(complaints.get_all_complaints()), 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)