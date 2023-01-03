import cv2
import numpy as np
from random import randint
from combine2 import ImageProcess


def get_combined(option,edges1,edges2, uniform_phase_bool,uniform_Magnitude_bool):
    img_1 = ImageProcess(edges1,(option == "option1"),1,uniform_phase_bool,uniform_Magnitude_bool)
    img_2 = ImageProcess(edges2,(option != "option1"),2,uniform_phase_bool,uniform_Magnitude_bool)
    
    mag_1_phase_sphinx= np.multiply(img_1.fourier(),img_2.fourier())
        
    img_combined=np.real(np.fft.ifft2(np.fft.ifftshift(mag_1_phase_sphinx)))
    path_img = f"output/{randint(1,100000)}.png"
    cv2.imwrite(path_img,img_combined)
    return path_img


