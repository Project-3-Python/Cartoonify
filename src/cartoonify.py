import cv2

def cartoonify_image(image_path):
    image = cv2.imread(image_path)
    # Convert image to grayscale and apply cartoonification effects
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    cartoon = cv2.bitwise_and(image, image, mask=edges)

    # Save the cartoonified image
    cv2.imwrite("cartoonified_image.png", cartoon)
    print("Cartoonified image saved as cartoonified_image.png")
