from ultralytics import YOLO



model=YOLO('1type.pt')

model.predict(source=0,show=True ,conf=0.7)

