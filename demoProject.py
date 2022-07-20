from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import cv2
import imutils

data = []
labels = []
classes = 43

classs = {1: "Speed limit (20km/h)",
          2: "Speed limit (30km/h)",
          3: "Speed limit (50km/h)",
          4: "Speed limit (60km/h)",
          5: "Speed limit (70km/h)",
          6: "Speed limit (80km/h)",
          7: "End of speed limit (80km/h)",
          8: "Speed limit (100km/h)",
          9: "Speed limit (120km/h)",
          10: "No passing",
          11: "No passing veh over 3.5 tons",
          12: "Right-of-way at intersection",
          13: "Priority road",
          14: "Yield",
          15: "Stop",
          16: "No vehicles",
          17: "Veh > 3.5 tons prohibited",
          18: "No entry",
          19: "General caution",
          20: "Dangerous curve left",
          21: "Dangerous curve right",
          22: "Double curve",
          23: "Bumpy road",
          24: "Slippery road",
          25: "Road narrows on the right",
          26: "Road work",
          27: "Traffic signals",
          28: "Pedestrians",
          29: "Children crossing",
          30: "Bicycles crossing",
          31: "Beware of ice/snow",
          32: "Wild animals crossing",
          33: "End speed + passing limits",
          34: "Turn right ahead",
          35: "Turn left ahead",
          36: "Ahead only",
          37: "Go straight or right",
          38: "Go straight or left",
          39: "Keep right",
          40: "Keep left",
          41: "Roundabout mandatory",
          42: "End of no passing",
          43: "End no passing veh > 3.5 tons"}

print("Loading Model...")
model = load_model("D:\\Study\\AI internship\\Day_21\\code\\my_model.h5", compile=False)
print("Model Loaded!")

print("Starting Camera...")
cam = cv2.VideoCapture(0)

while True:
    _,frame = cam.read()
    img = Image.fromarray(frame, "RGB")
    img = img.resize((30, 30))
    img = np.expand_dims(img, axis=0)
    img = np.array(img)

    result = model.predict_classes(img)[0]
    sign = classs[result + 1]
    print("The sign says: ", sign)

    cv2.putText(frame, sign, (10, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5, (0, 0, 255), 1)
    frame = imutils.resize(frame, width=500)
    cv2.imshow("Caputering", frame)

    if (cv2.waitKey(1)) == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()