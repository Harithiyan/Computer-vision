import cv2
import numpy as np
from google.colab import files
from google.colab.patches import cv2_imshow

# Upload the image
uploaded = files.upload()
image_name = list(uploaded.keys())[0]  # Get the uploaded image's filename

# Load the image
img = cv2.imread(image_name)

if img is None:
    print(f"Error: Could not load image '{image_name}'")
else:
    # Line
    cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 3)  # Red line, thickness 3

    # Rectangle
    cv2.rectangle(img, (100, 100), (200, 200), (0, 255, 0), 2) # Green rectangle, thickness 2

    # Filled Circle
    cv2.circle(img, (300, 150), 50, (255, 0, 0), -1) # Blue filled circle

    # Ellipse
    cv2.ellipse(img, (450, 250), (50, 30), 0, 0, 360, (255, 255, 0), 2) # Cyan ellipse, thickness 2

    # Text
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'OpenCV Annotation', (10, 50), font, 1, (255, 0, 255), 2, cv2.LINE_AA)  # Purple text

    # Display the image with annotations using cv2_imshow
    cv2_imshow(img) 
    # cv2.waitKey(0)  #
