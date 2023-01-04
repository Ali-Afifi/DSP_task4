import cv2
import numpy as np

from image import Image


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

