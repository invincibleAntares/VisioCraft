import cv2
import numpy as np

# Load the image
image = cv2.imread("test.jpg")

if image is None:
    print("Error: Image not found. Place a test.jpg file in the same directory.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Initialize SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and descriptors
keypoints, descriptors = sift.detectAndCompute(gray, None)

# Draw keypoints on the image
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show the image with keypoints
cv2.imshow("Feature Detection", image_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
