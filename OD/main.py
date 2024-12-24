from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Run inference on an image
results = model('scarlet.png')  # Replace with your image path

# Extract detection information
for result in results:
    boxes = result.boxes  # Bounding boxes and other details

    for box in boxes:
        cls_id = int(box.cls)  # Class ID
        confidence = float(box.conf)  # Confidence score
        bbox = box.xyxy[0].tolist()  # Bounding box [x_min, y_min, x_max, y_max]

        # Get the class name from the `names` attribute
        class_name = result.names[cls_id]

        # Print the extracted details
        print(f"Detected: {class_name}")
        print(f"Confidence: {confidence:.2f}")
        print(f"Bounding Box: {bbox}")
