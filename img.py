import cv2
import numpy as np


class Image:
    def __init__(self, path):
        
        self.img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        self.fourier_transform = np.fft.fft2((self.img)) # fft2 for 2d fourier transform as the variation of the image happend in two dimension
        self.fourier_shifted = np.fft.fftshift((self.fourier_transform)) # to avoid the repeation in the frequencies
        self.phase = np.angle((self.fourier_shifted))  # the phase after fourier


    def get_mag(self):
        return np.abs((self.fourier_shifted))  

    def get_phase(self):
        return np.exp(1j*(self.phase)) 

    def get_mag_shape(self):
        return (np.abs((self.fourier_shifted))).shape

    def get_phase_shape(self):
        return self.phase.shape
