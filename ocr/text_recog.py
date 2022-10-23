import cv2
import numpy as np
import os
import time
import pytesseract
from PIL import Image


def text_recog(text_im, lang):
    # apply thresholding to preprocess the image
    text_im = cv2.threshold(text_im, 210, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('Thrs', text_im)
    cv2.waitKey()

    # write the image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, text_im)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file

    # The variable lang represents the traned data of tesseract ocr
    text = pytesseract.image_to_string(Image.open(filename), lang=lang)
    os.remove(filename)
    text = text.replace("", "")

    save_content(text, "hinario.txt")

    return text


def save_content(text, filename):
    # A text file is created and flushed
    file = open(filename, "a")
    # Appending the text into file
    file.write("\n")
    file.write("NEXT IMAGE")
    file.write("\n")
    file.write(text)
    file.write("\n")
    # Close the file
    file.close
