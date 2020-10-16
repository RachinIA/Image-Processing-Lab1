from tkinter.filedialog import askopenfilename
import cv2
from math import log10, sqrt
import numpy as np
import matplotlib

def PSNR(im1, im2):
    mse = np.mean((im1 - im2) ** 2)
    if (mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

def file_open_cv():
    f = askopenfilename(title="Select file", filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"), ("jpeg files", "*.jpeg")))
    if f:
        return cv2.imread(f, cv2.IMREAD_COLOR)

def main():
    image_1 = file_open_cv()
    image_2 = file_open_cv()
    result = PSNR(image_1, image_2)
    print("Изображения схожи на", result, "%")

if __name__ == "__main__":
    main()

