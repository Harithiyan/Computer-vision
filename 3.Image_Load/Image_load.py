import cv2
from google.colab import files
from google.colab.patches import cv2_imshow

# Upload the image
uploaded = files.upload()
image_name = list(uploaded.keys())[0]  # Get the uploaded image's filename

# Load the image
image = cv2.imread(image_name)

# Check if image is loaded successfully
if image is None:
    print(f"Error: Could not load image '{image_name}'")
else:
    # Display the image using cv2_imshow
    cv2_imshow(image)
