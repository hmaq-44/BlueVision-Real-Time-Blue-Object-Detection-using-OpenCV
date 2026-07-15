# BlueVision-Real-Time-Blue-Object-Detection-using-OpenCV
📖 Overview of OpenCV

OpenCV (Open Source Computer Vision Library) is an open-source library specialized in computer vision and image processing, originally developed by Intel. It is one of the most widely used libraries in this field today.

OpenCV allows developers and researchers to perform a wide range of tasks, including:


Reading and processing images and video in real time.
Converting images between different color spaces (RGB, BGR, HSV, Grayscale, etc.).
Edge and contour detection.
Object tracking and motion detection.
Face and pattern recognition, along with broader computer vision AI applications.


OpenCV is widely used in robotics, self-driving cars, security systems, and augmented reality applications, thanks to its high processing speed and support for multiple languages such as Python and C++.

In this project, OpenCV is used to convert camera frames into the HSV color space, since it is far better suited for isolating a specific color (such as blue) compared to the traditional RGB space — because it separates Hue, Saturation, and Value into independent components.


⚙️ Code Explanation (Step by Step)

1. Importing Libraries

pythonimport cv2
import numpy as np

cv2 is imported to handle the camera and image processing, and numpy is used to create the numerical arrays that define the blue color range (lower and upper bounds).

2. Opening the Camera

pythoncap = cv2.VideoCapture(0)

This line opens a live connection with the device's default camera (index 0), preparing it to continuously capture frames.

3. Continuous Reading Loop

pythonwhile True:
    ret, frame = cap.read()
    if not ret:
        print("فشل في قراءة الإطار من الكاميرا")
        break

The loop reads a new frame from the camera on every iteration. ret is a boolean indicating whether the read was successful, and frame holds the captured image.

4. Converting the Frame to HSV

pythonhsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

The frame is converted from OpenCV's default BGR color space to HSV, making it much easier to isolate the blue color accurately regardless of lighting conditions.

5. Defining the Blue Color Range

pythonlower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

The lower and upper bounds of the blue color in the HSV space are defined here. Any pixel whose value falls within this range is considered part of the blue color.

6. Creating the Binary Mask

pythonmask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

This function produces a binary (black/white) image: white pixels represent regions that fall within the blue color range, while black represents everything else.

7. Extracting the Blue Regions Only

pythonresult = cv2.bitwise_and(frame, frame, mask=mask)

The original frame is combined with the mask using a bitwise AND operation, so the original colors appear only in the regions identified as "blue," while the rest of the image is hidden (shown as black).

8. Detecting Contours

pythoncontours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

This function searches for the outer boundaries of the white regions in the mask, effectively identifying the connected blobs of blue color as separate objects that can be measured and analyzed.

9. Filtering Objects by Area and Drawing the Bounding Box

pythonfor contour in contours:
    area = cv2.contourArea(contour)
    if area > 800:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Blue Object Detected", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

For every detected contour, its area is calculated in order to filter out noise and small unwanted spots. If the area exceeds 800 pixels, the object is considered significant enough to be treated as a "real" object, so a green rectangle is drawn around it along with the label "Blue Object Detected."

10. Displaying the Results

pythoncv2.imshow("Original Frame with Tracking", frame)
cv2.imshow("Mask (Binary Image)", mask)
cv2.imshow("Result (Blue Only)", result)

Three windows are displayed simultaneously:


Original Frame with Tracking: the original frame with a green bounding box drawn around the detected blue object.
Mask (Binary Image): the binary mask (black/white) produced by the color thresholding step.
Result (Blue Only): the frame after extracting only the blue-colored regions from the background.


11. Ending the Program

pythonif cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

When the q key is pressed, the loop ends, the camera is released, and all windows are safely closed.


📊 Results Explanation

The image above shows the program running live, with three synchronized windows:


Original Frame with Tracking: A mobile phone with a blue screen is being held up in front of the camera and has been successfully detected. A green bounding box is drawn around it along with the label "Blue Object Detected," confirming that the algorithm correctly recognized the blue object and calculated its dimensions accurately.
Mask (Binary Image): This shows the binary mask produced by the inRange function, where the region matching the blue color (the phone's screen) appears white, while the rest of the image is completely black — reflecting the accuracy of the color range thresholding.
Result (Blue Only): This displays the original colors of the blue region only, after applying bitwise_and, while the rest of the frame appears black — proving that the algorithm successfully isolated the blue object from the rest of the scene.


Technical note: A small additional white patch appears in the top-left corner of both the mask and result windows. This is most likely caused by a light reflection or another background element that happens to fall within the same blue color range. Accuracy could be improved in the future by:


Narrowing the lower_blue and upper_blue range more precisely.
Increasing the area threshold (area > 800) to filter out small, unwanted blobs.
Applying morphological operations (Erosion / Dilation) to clean up noise in the mask.



🛠️ Requirements

opencv-python
numpy

Install them using:

bashpip install opencv-python numpy

▶️ How to Run

bashpython blue_detection.py

Press the q key to stop the camera and close the program.


📌 Project Summary

ItemDescriptionProject NameBlueVision – Real-Time Blue Object DetectionLanguagePythonLibrariesOpenCV, NumPyColor SpaceHSVCore FunctionDetecting and tracking blue-colored objects live via webcam
