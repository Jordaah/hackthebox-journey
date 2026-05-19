import os
import json
import uuid
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


COMPLAINS_STORAGE = "complaints/"

def add_complaint(description, image_data, prediction):
    complaint = {
        "description": description,
        "image_data": image_data,
        "prediction": prediction,
    }

    with open(os.path.join(COMPLAINS_STORAGE, f"{uuid.uuid4()}.json"), "w") as f:
        f.write(json.dumps(complaint))


def get_all_complaints():
    complaints = []
    for complaint in os.listdir(COMPLAINS_STORAGE):
        with open(os.path.join(COMPLAINS_STORAGE, complaint)) as f:
            complaints.append(json.loads(f.read()))

    return complaints

def check_complaints(username, password):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(options=options)

    browser.get("http://127.0.0.1:1337/dashboard")

    browser.find_element(By.NAME, "username").send_keys(username)
    browser.find_element(By.NAME, "password").send_keys(password)
    browser.find_element(By.CLASS_NAME, "button-container").click()

    time.sleep(10)

    browser.quit()
