import os
from libs.process_image import*
from libs.text_recog import*
import cv2

def get_text(image):
    lang = 'por'

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    picture = process_image(gray)
    text = text_recog(picture, lang)

    return text

# def process_text():
#
#
# def save_file():


if __name__ == '__main__':
    pathToimages = "C:/Users/ander/dev/hinario/lestras/letras_jpg/"

    caminhos = [os.path.join(pathToimages, nome) for nome in os.listdir(pathToimages)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    jpgs = [arq for arq in arquivos if arq.lower().endswith(".png")]

    for image_path in jpgs:
        image = cv2.imread(image_path)
        text = get_text(image)
