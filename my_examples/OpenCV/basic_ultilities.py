import cv2

path = "capture.jpg"
image = cv2.imread(path)

def write_to_disk(image):
    cv2.imwrite('capture.jpg', image)

def blur(image):
    ksize = (10, 10)
    blur = cv2.blur(image, ksize)
    return blur

def resize(image):
    half = cv2.resize(image, (0, 0), fx = 0.5, fy = 0.5)
    return half

image = resize(image)
cv2.imshow("Image", image)

cv2.waitKey(0)