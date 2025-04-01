import cv2
import numpy as np
import json
import open3d as o3d

# Load left and right images
left_img = cv2.imread("left.jpg", cv2.IMREAD_GRAYSCALE)
right_img = cv2.imread("right.jpg", cv2.IMREAD_GRAYSCALE)

if left_img is None or right_img is None:
    print("Error: Images not found. Place left.jpg and right.jpg in the same directory.")
    exit()

# Resize both images to the same size
width, height = 640, 480
left_img = cv2.resize(left_img, (width, height))
right_img = cv2.resize(right_img, (width, height))

# Create StereoBM matcher
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)

# Compute disparity (depth map)
disparity = stereo.compute(left_img, right_img)

# Normalize the disparity map for better visualization
disparity_norm = cv2.normalize(disparity, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
disparity_norm = np.uint8(disparity_norm)

# Convert disparity map to 3D point cloud
focal_length = 1.0
baseline = 1.0

h, w = disparity.shape
f = focal_length
b = baseline

points = []
for v in range(h):
    for u in range(w):
        d = disparity[v, u] / 16.0
        if d > 0:
            Z = (f * b) / d
            X = (u - w / 2) * Z / f
            Y = (v - h / 2) * Z / f
            points.append([X, Y, Z])

# Save the point cloud data to a JSON file
with open("point_cloud.json", "w") as f:
    json.dump(points, f)

print("Point cloud data saved in point_cloud.json.")
