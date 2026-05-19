import json
import random
from tensorflow import keras
from keras.datasets import mnist
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation

# Tensorflow: https://github.com/tensorflow/tensorflow/

MAIN_MODEL = "models/main.h5"

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
X_train = X_train.astype("float32")
X_test = X_test.astype("float32")

X_train /= 255
X_test /= 255

n_classes = 10
Y_train = to_categorical(y_train, n_classes)
Y_test = to_categorical(y_test, n_classes)

# Our revolutionary ML model
def build_model():
    model = Sequential()
    model.add(Dense(512, input_shape=(784,)))
    model.add(Activation("relu"))                            
    model.add(Dropout(0.2))

    model.add(Dense(512))
    model.add(Activation("relu"))
    model.add(Dropout(0.2))

    model.add(Dense(10))
    model.add(Activation("softmax"))

    model.compile(loss="categorical_crossentropy", metrics=["accuracy"], optimizer="adam")

    history = model.fit(X_train, Y_train,
            batch_size=128, epochs=20,
            verbose=2,
            validation_data=(X_test, Y_test))

    model.save(MAIN_MODEL)
    with open("graph.json", "w") as fp:
        json.dump(history.history, fp)

def predict(image_data):
    # What's the point anyway?
    return random.randrange(0, 9)


def test_model(path):
    m = keras.models.load_model(path)
    metrics = m.evaluate(X_test, Y_test)
    return {"loss":round(metrics[0], 3), "acc":round(metrics[1], 3)}

def dataset():
    return len(X_train)+len(X_test)