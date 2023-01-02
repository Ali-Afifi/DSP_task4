import cv2
import numpy as np
from skimage.color import rgb2gray
from random import randint
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

class ImageProcess:
    def __init__(self,edges,value,num,uniform_phase_bool,uniform_Magnitude_bool):
        self.edges = edges
        self.value = int(value)
        self.img = cv2.imread(f"input/original{num}.png",cv2.IMREAD_GRAYSCALE)
        self.num = num
        self.uniform_phase_bool = uniform_phase_bool
        self.uniform_Magnitude_bool = uniform_Magnitude_bool
        
        
    def update(self,arr):
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                if (i < self.edges[0][0] or i>=self.edges[0][1] )or (j<=self.edges[1][0] or j >=self.edges[1][1] ): #the i and j axis are obtined according to the cropped image
                    arr[i][j]=self.value
        return arr
    def resize(self,x,y):
        self.img = cv2.resize(self.img ,(y , x))
    
    def fourier(self):
        fourier_=np.fft.fft2((self.img)) #fft2 for 2d fourier transform as the variation of the image happend in two dimension 
        fourier_shifted = np.fft.fftshift(fourier_) # to avoid the repeation in the frequencies
        if self.value == 1:
            arr_=np.abs(fourier_shifted) # the magnitude after fourier
            arr_ = self.update(arr_)
            if self.uniform_Magnitude_bool=="true":
                arr_ = np.ones(arr_.shape)
                
        elif self.value == 0:
            if self.uniform_phase_bool == 'true':
                print(type(self.uniform_phase_bool))
                arr_=np.angle(fourier_shifted)
                arr_ = np.zeros(arr_.shape)
                arr_ = np.exp(1j*arr_) 
            else:
                arr_=np.angle(fourier_shifted)# the phase after fourier
                arr_ = self.update(arr_)
                arr_ = np.exp(1j*arr_)
            
        return arr_





    
