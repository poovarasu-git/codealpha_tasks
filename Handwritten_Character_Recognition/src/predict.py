
import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("model/handwritten_char_model.h5")

def predict_character(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28))
    img = img.reshape(1, 28, 28, 1) / 255.0
    pred = model.predict(img)
    return chr(np.argmax(pred) + ord('A'))

if __name__ == "__main__":
    print(predict_character("sample_image.png"))
