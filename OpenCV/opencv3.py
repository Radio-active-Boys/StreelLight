import cv2

cap = cv2.VideoCapture(0)

while True:
    read,frame = cap.read()
    
    if not read:
        print("frame not found")
        break
    
    cv2.imshow('Vishal',frame)
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break
   
cap.release()
cv2.destroyAllWindows()
    
    