import cv2
import numpy as np

# Load left and right images
left_img = cv2.imread("left.jpg", cv2.IMREAD_GRAYSCALE)
right_img = cv2.imread("right.jpg", cv2.IMREAD_GRAYSCALE)

if left_img is None or right_img is None:
    print("Error: Images not found. Place left.jpg and right.jpg in the same directory.")
    exit()

# Resize both images to the same size
width, height = 640, 480  # You can adjust based on your images
left_img = cv2.resize(left_img, (width, height))
right_img = cv2.resize(right_img, (width, height))

# Create StereoBM matcher
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)

# Compute disparity (depth map)
disparity = stereo.compute(left_img, right_img)

# Normalize the disparity map for better visualization
disparity_norm = cv2.normalize(disparity, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
disparity_norm = np.uint8(disparity_norm)

# Show disparity map
cv2.imshow("Depth Map", disparity_norm)
cv2.waitKey(0)
cv2.destroyAllWindows()
