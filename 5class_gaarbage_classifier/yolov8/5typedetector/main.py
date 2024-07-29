from ultralytics import YOLO


model=YOLO('5type.pt')

model.predict(source=0,show=True ,conf=0.6)