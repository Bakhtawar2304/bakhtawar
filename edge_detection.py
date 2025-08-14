import cv2
import os

image_path = r"F:\AI_Expert\lesson_1_1\example.jpg"
if not os.path.exists(image_path):
    print("Image file not found!")
else:
    image = cv2.imread(image_path)

    if image is None:
        print("Failed to load image. Check file format or path.")
    else:
        cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Loaded Image', 800, 500)
        cv2.imshow('Loaded Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(f"Image Dimensions: {image.shape}")
