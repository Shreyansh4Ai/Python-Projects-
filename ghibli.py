import cv2
import numpy as np

def cartoonize_image(image_path):
    # Read the image
    print("Image path:", image_path)
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to load image from {image_path}")
        return

    # Resize the image
    img = cv2.resize(img, (800, 600))

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    # Detect edges
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10
    )

    # Apply bilateral filters to smooth colors
    color = cv2.bilateralFilter(img, 9, 250, 250)

    # Combine edges and color
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Display the cartoonized image
    cv2.imshow("Cartoonized Image", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    # Replace with the actual path to your image
    cartoonize_image(r"D:\canva projects\download.jpeg")