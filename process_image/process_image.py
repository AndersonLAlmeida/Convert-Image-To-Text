import cv2
import numpy as np
from PIL import Image

from utils.manipulate_images import *
from ocr.text_recog import *


def process_image(path_to_image):
    original_image = cv2.imread(path_to_image)

    image_copy = original_image.copy()
    gray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    # show_image("Gray Image", gray)

    # downscaled_image = downscale_image(gray)
    _, threshold_image = get_threshold_image(gray, lower_threshold=200)
    dilated_image = dilate_image(threshold_image, x_rect=33, y_rect=33, iterations=5)
    contours, _ = get_contours(dilated_image)
    borders = get_borders_from_contours(contours)
    draw_borders(borders, gray)

    return crop_text_image(borders, gray)


def get_threshold_image(image, lower_threshold=230, upper_threshold=255):
    return cv2.threshold(image, lower_threshold, upper_threshold, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)


def dilate_image(image, x_rect=18, y_rect=18, iterations=1):
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (x_rect, y_rect))
    return cv2.dilate(image, rect_kernel, iterations=iterations)


def get_contours(image, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE):
    return cv2.findContours(image, mode, method)


def get_borders_from_contours(contours):
    borders = []
    for i, c in enumerate(contours):
        x, y, w, h = cv2.boundingRect(c)
        perimetro = ((w - x) * 2) + ((h - y) * 2)
        if perimetro > 3000:
            borders.append((i, x, y, x + w - 1, y + h - 1))

    return borders


def get_edges_image(image, t_lower=100, t_upper=200, aperture_size=5):
    """Get image with Edges"""
    return cv2.Canny(np.asarray(image), t_lower, t_upper, aperture_size)
