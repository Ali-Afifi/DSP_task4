import cv2
import numpy as np


class Image:
    def __init__(self, path):
        
        self.img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        self.fourier_transform = np.fft.fft2((self.img)) # fft2 for 2d fourier transform as the variation of the image happend in two dimension
        self.fourier_shifted = np.fft.fftshift((self.fourier_transform)) # to avoid the repeation in the frequencies
        self.phase = np.angle((self.fourier_shifted))  # the phase after fourier


    def get_mag(self):
        return np.abs((self.fourier_shifted))  # the magnitude after fourier

    def get_phase(self):
        return np.exp(1j*(self.phase))

    def get_mag_shape(self):
        return (np.abs((self.fourier_shifted))).shape

    def get_phase_shape(self):
        return self.phase.shape

        if self.value == 1:
            arr = np.abs(fourier_shifted)  # the magnitude after fourier
            # arr = self.update(arr)
            if self.uniform_magnitude == True:
                arr = np.ones(arr.shape)

        elif self.value == 0:
            if self.uniform_phase == True:
                # print(type(self.uniform_phase))
                arr = np.angle(fourier_shifted)
                arr = np.zeros(arr.shape)
                arr = np.exp(1j*arr)
            else:
                arr = np.angle(fourier_shifted)  # the phase after fourier
                # arr = self.update(arr)
                arr = np.exp(1j*arr)

        return arr
