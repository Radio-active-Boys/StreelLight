import cv2
import numpy as np

# Load YOLO model configuration and weights
net = cv2.dnn.readNet("darknet/yolov3.cfg", "darknet/yolov3.weights")

# Load class names (e.g., "person" for humans)
classes = []
with open("darknet/coco.names", "r") as f:
    classes = f.read().strip().split("\n")

# Create a VideoCapture object to capture video from the webcam (usually webcam index 0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        break

    # Calculate the frame center
    frame_height, frame_width = frame.shape[:2]
    frame_center_x = frame_width // 2
    frame_center_y = frame_height // 2

    # Prepare the frame for YOLO
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)

    # Set the input to the network
    net.setInput(blob)

    # Run forward pass
    outs = net.forward(net.getUnconnectedOutLayersNames())

    # Process the outputs for object detection
    conf_threshold = 0.5
    nms_threshold = 0.4

    detected_humans = []  # List to store detected humans

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > conf_threshold and classes[class_id] == "person":
                # Calculate bounding box coordinates
                center_x = int(detection[0] * frame_width)
                center_y = int(detection[1] * frame_height)
                w = int(detection[2] * frame_width)
                h = int(detection[3] * frame_height)
                
                # Calculate distances from frame center to bounding box center
                box_center_x = center_x + w // 2
                box_center_y = center_y + h // 2
                distance_x = frame_center_x - box_center_x
                distance_y = frame_center_y - box_center_y

                # Draw bounding box
                cv2.rectangle(frame, (center_x - w // 2, center_y - h // 2), (center_x + w // 2, center_y + h // 2), (0, 255, 0), 2)

                # Add detected human and their distances to the list
                detected_humans.append((distance_x, distance_y))

    # Display the distances for detected humans
    for i, (distance_x, distance_y) in enumerate(detected_humans):
        cv2.putText(frame, f"Human {i + 1}: X={distance_x}, Y={distance_y}", (10, 30 + i * 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame with detected humans and distances
    cv2.imshow("Human Detection", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
