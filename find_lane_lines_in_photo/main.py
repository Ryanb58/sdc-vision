import cv2
import numpy as np


def convert_image(image):
    """
    Convert image to edges.
    """
    # Grey Scale Conversion
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # Smoothing
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Identify the edges(strong vs weak gradients)
    return cv2.Canny(blur, 50, 150)

def region_of_interest(image):
    """
    Return the encolsed region of our field of view.

    Triangular in shape.
    """
    height = image.shape[0]
    triangle = np.array(
        [
            (200, height),
            (1100, height),
            (550, 250)
        ]
    )
    polygons = [triangle]
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    return mask


image = cv2.imread("road1.jpg")
lane_image = np.copy(image)
img = convert_image(lane_image)
cv2.imshow('result', region_of_interest(img))
cv2.waitKey(0)


# Identify the lane lines

