import cv2
import numpy as np


cap = cv2.VideoCapture(0)

print("اضغط على 'q' للخروج")

while True:
    ret, frame = cap.read()
    if not ret:
        print("فشل في قراءة الإطار من الكاميرا")
        break

    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    
    mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
       
        if area > 800:
           
            x, y, w, h = cv2.boundingRect(contour)
            
       
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
           
            cv2.putText(frame, "Blue Object Detected", (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

   
    cv2.imshow("Original Frame with Tracking", frame)
    cv2.imshow("Mask (Binary Image)", mask)
    cv2.imshow("Result (Blue Only)", result)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()