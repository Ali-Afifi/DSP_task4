import cv2
import numpy as np

class Image:
    def __init__(self,value,path,uniform_phase,uniform_magnitude):
        self.value = int(value)
        self.img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        self.uniform_phase = uniform_phase
        self.uniform_magnitude = uniform_magnitude
    
    def get_ft(self):
        fourier_transform = np.fft.fft2((self.img)) #fft2 for 2d fourier transform as the variation of the image happend in two dimension 
        fourier_shifted = np.fft.fftshift(fourier_transform) # to avoid the repeation in the frequencies
        if self.value == 1:
            arr = np.abs(fourier_shifted) # the magnitude after fourier
            # arr = self.update(arr)
            if self.uniform_magnitude == True:
                arr = np.ones(arr.shape)
                
        elif self.value == 0:
            if self.uniform_phase == True:
                print(type(self.uniform_phase))
                arr=np.angle(fourier_shifted)
                arr = np.zeros(arr.shape)
                arr = np.exp(1j*arr) 
            else:
                arr=np.angle(fourier_shifted)# the phase after fourier
                # arr = self.update(arr)
                arr = np.exp(1j*arr)
            
        return arr