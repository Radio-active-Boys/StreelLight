import cv2
import numpy as np

# Load YOLO model configuration and weights
net = cv2.dnn.readNet("darknet\yolov3.cfg", "darknet\yolov3.weights")

# Load class names (e.g., "person" for humans)
classes = []
with open("darknet\coco.names", "r") as f:
    classes = f.read().strip().split("\n")

# Load an image for detection
image = cv2.imread("image.jpg")

# Prepare the image for YOLO
blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)

# Set the input to the network
net.setInput(blob)

# Run forward pass
outs = net.forward(net.getUnconnectedOutLayersNames())

# Process the outputs for object detection
conf_threshold = 0.5
nms_threshold = 0.4
height, width = image.shape[:2]

for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > conf_threshold and classes[class_id] == "person":
            # Calculate bounding box coordinates
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            x = center_x - w // 2
            y = center_y - h // 2

            # Draw bounding box
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show the image with detected humans
cv2.imshow("Human Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
