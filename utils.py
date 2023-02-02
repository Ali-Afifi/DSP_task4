import cv2
import numpy as np
from image import Image
from PIL import Image as pil_img

from img import Image as test_img_class


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


def get_combined(option, path1, path2, uniform_phase, uniform_magnitude):
    img_1 = Image(value=(option == "option1"), path=path1, uniform_phase=uniform_phase,
                  uniform_magnitude=uniform_magnitude)
    img_2 = Image(value=(option != "option1"), path=path2, uniform_phase=uniform_phase,
                  uniform_magnitude=uniform_magnitude)

    mag_1_phase_sphinx = np.multiply(img_1.get_ft(), img_2.get_ft())

    img_combined = np.real(np.fft.ifft2(np.fft.ifftshift(mag_1_phase_sphinx)))
    path_img = "output/result.png"
    cv2.imwrite(path_img, img_combined)
    return path_img


def get_combined_v2(option, path1, path2, uniform_phase, uniform_magnitude):
    img1 = test_img_class(path1)
    img2 = test_img_class(path2)
    
    if option == "option1":
        if uniform_magnitude == True:
            data1 = np.ones(img1.get_mag_shape())
        else:
            data1 = img1.get_mag()
        
        if uniform_phase == True:
            arr = np.zeros(img2.get_phase_shape())
            data2 = np.exp(1j*(arr))
        else:
            data2 = img2.get_phase()
    elif option == "option2":
        if uniform_magnitude == True:
            data1 = np.ones(img2.get_mag_shape())
        else:
            data1 = img2.get_mag()
        
        if uniform_phase == True:
            arr = np.zeros(img1.get_phase_shape())
            data2 = np.exp(1j*(arr))
        else:
            data2 = img1.get_phase()
                        
    
    img_combined = np.real(np.fft.ifft2(np.fft.ifftshift(np.multiply(data1, data2))))
    img_path = "output/result.png"
    cv2.imwrite(img_path, img_combined)
    return img_path
