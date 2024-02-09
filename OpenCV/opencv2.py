import cv2

# Load the pre-trained human detection model
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Initialize the webcam capture
cap = cv2.VideoCapture(0)  # Use 0 to select the default camera (you can change it if you have multiple cameras)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        print("Error: Could not read frame")
        break

    # Detect humans in the frame
    humans, _ = hog.detectMultiScale(frame)

    # Get the center coordinates of the frame
    frame_center_x = frame.shape[1] // 2
    frame_center_y = frame.shape[0] // 2

    # Iterate through detected humans
    for (x, y, w, h) in humans:
        # Calculate the center coordinates of the detected human
        center_x = x + w // 2
        center_y = y + h // 2

        # Calculate the distance from the frame center in x and y axes
        distance_x = center_x - frame_center_x
        distance_y = center_y - frame_center_y

        # Draw rectangles around detected humans
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the center coordinates and distance from center
        center_text = f"Center: ({center_x}, {center_y})"
        distance_text = f"Distance from Center: (dx={distance_x}, dy={distance_y})"
        cv2.putText(frame, center_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(frame, distance_text, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the frame with detected humans and center coordinates
    cv2.imshow('Human Tracking', frame)

    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam capture and close all windows
cap.release()
cv2.destroyAllWindows()
