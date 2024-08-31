from ultralytics import YOLO

model = YOLO('yolov8n.pt')

results = model.train(
    data="train.yaml",
    epochs=50,
    patience=50,
    imgsz=640,
    device=0,
    cache=True,
    project='models',
    name='classification_of_dog_and_cat_v1',
    batch=16,
    optimizer='Adam',
    lr0=0.001,
    weight_decay=0.0005,
    mosaic=True
)
