import cv2

# Load an image (Replace 'test.jpg' with an actual image path)
image = cv2.imread("test.jpg")

if image is None:
    print("Error: Image not found. Place a test.jpg file in the same directory.")
else:
    # Show the image
    cv2.imshow("Test Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
