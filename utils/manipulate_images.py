from PIL import Image
import cv2 as cv


def draw_borders(borders, image):
    for border in borders:
        x, y, w, h = border[1], border[2], border[3], border[4]
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), 1)

    cv.imshow("Border", image)
    cv.waitKey()


def crop_text_image(borders, image):
    texts_image = []
    for border in borders:
        image_copy = image.copy()
        x, y, w, h = border[1], border[2], border[3], border[4]

        texts_image.append(image_copy[y:h, x:w])

    return texts_image


def downscale_image(im, max_dim=2048):
    """Shrink im until its longest dimension is <= max_dim.
    Returns new_image, scale (where scale <= 1).
    """
    a, b = im.shape
    if max(a, b) <= max_dim:
        return 1.0, im

    scale = 1.0 * max_dim / max(a, b)
    downscaled_image = im.resize((int(a * scale), int(b * scale)), Image.ANTIALIAS)

    return scale, downscaled_image
