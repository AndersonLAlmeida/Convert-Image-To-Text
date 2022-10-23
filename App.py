from ocr.text_recog import*
from process_image.process_image import process_image

if __name__ == '__main__':
    path_to_images = "/home/anderson/dev/Convert-Image-To-Text/images/"
    lang = 'por'

    caminhos = [os.path.join(path_to_images, nome) for nome in os.listdir(path_to_images)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    jpgs = [arq for arq in arquivos if arq.lower().endswith(".png")]
    jpgs.sort()


    for image_path in jpgs:
        texts_image = process_image(image_path)

        for text in texts_image:
            text_recog(text, lang)
