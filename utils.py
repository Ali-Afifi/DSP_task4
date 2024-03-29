import cv2
import numpy as np
from PIL import Image as pil_img

from img import Image 


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



def get_combined_v2(option, path1, path2, uniform_phase, uniform_magnitude):
    img1 = Image(path1)
    img2 = Image(path2)
    
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
