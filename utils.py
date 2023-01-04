import cv2
import numpy as np
from image import Image
from PIL import Image as pil_img


def adjust_images(path1, path2):

    img1 = pil_img.open(path1)
    img2 = pil_img.open(path2)

    width1, height1 = img1.size
    width2, height2 = img2.size

    dim1 = width1 + height1
    dim2 = width2 + height2

    if (dim1 >= dim2):
        img2_resized = img2.resize((width1, height1))
        img2_resized.save(path2)
    else:
        img1_resized = img1.resize((width2, height2))
        img1_resized.save(path1)




def get_combined(option, path1, path2,uniform_phase, uniform_magnitude):
    img_1 = Image(value=(option == "option1"), path=path1, uniform_phase=uniform_phase,
                  uniform_magnitude=uniform_magnitude)
    img_2 = Image(value=(option != "option1"), path=path2, uniform_phase=uniform_phase,
                  uniform_magnitude=uniform_magnitude)

    mag_1_phase_sphinx = np.multiply(img_1.get_ft(), img_2.get_ft())

    img_combined = np.real(np.fft.ifft2(np.fft.ifftshift(mag_1_phase_sphinx)))
    path_img = "output/result.png"
    cv2.imwrite(path_img, img_combined)
    return path_img

