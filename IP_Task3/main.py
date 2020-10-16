import numpy as np
import sys
import time
import cv2
import math
import easygui
import tkinter as tk
from tkinter import messagebox as mb
from PIL import Image, ImageTk
    
def fileOpen():
    ###Choose image on local machin###
    fIn=tk.filedialog.askopenfilename(title="Select image", filetypes=(("jpg", "*.jpg"), ("png", "*.png"), ("jpeg", "*.jpeg")))
    if(fIn):  ##Success
        return fIn
    else:  ##Fail
        return -1
    
###Max/Min limit###
def clamp(val, max, min):
    if(val <= min):
        return min
    elif(val >= max):
        return max
    else:
        return val
    
###Convert rgb pixel to hsv algorithm###
def pixToHsv(b, g, r):
    r = r/255
    g = g/255
    b = b/255
    high = max(r, g, b)
    low = min(r, g, b)
    v = high
    d = high - low
    s = 0 if high == 0 else d/high
    if d == 0:
        h = 0.0
    elif(high == r):
        h=60*((g-b)/d%6)
    elif(high == g):
        h=60*((b-r)/d+2)
    elif(high == b):
        h=60*((r-g)/d+4)
    v=255*v
    s=255*s
    h=255*(h/360)
    return v, s, h

###Convert hsv pixel to rgb algorithm###
def pixToBgr(v, s, h):
    h = h/255*360
    s /= 255
    v /= 255
    c = v*s
    x = c*(1-abs((h/60)%2-1))
    m = v-c
    if(h >= 0 and h < 60):
        (r, g, b)=(c, x, 0)
    elif(h >= 60 and h < 120):
        (r, g, b)=(x, c, 0)
    elif(h >= 120 and h < 180):
        (r, g, b)=(0, c, x)
    elif(h > 180 and h < 240):
        (r, g, b)=(0, x, c)
    elif(h >= 240 and h < 300):
        (r, g, b)=(x, 0, c)
    elif(h >= 300 and h < 360):
        (r, g, b)=(c, 0, x)
    else:
        (r, g, b)=(c, x, 0)
    r = (r+m)*255
    g = (g+m)*255
    b = (b+m)*255
    return b, g, r

###Convert rgb image to hsv function###
def rgbToHsv():
    file = fileOpen()
    if (file == -1):
        return -1
    imageArr = cv2.imread(file)
    cv2.imshow('RGB(Press any key to close window)',imageArr)
    #cv2.imshow('CV2(Press any key to close window)',cv2.cvtColor(imageArr, cv2.COLOR_BGR2HSV))
    ###Loop for each pixel###
    for i in range(imageArr.shape[0]):
        for j in range(imageArr.shape[1]):
            (b, g, r) = imageArr[i,j]
            imageArr[i,j] = pixToHsv(b, g, r)
    cv2.imshow('HSV(Press any key to close window)',imageArr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 1

###Convert hsv image to rgb function###
def hsvToBgr():
    file = fileOpen()
    if (file == -1):
        return -1
    imageArr = cv2.imread(file)
    cv2.imshow('RGB(Press any key to close window)',imageArr)
    #cv2.imshow('CV2(Press any key to close window)',cv2.cvtColor(imageArr, cv2.COLOR_BGR2HSV))
    ###Loop for each pixel###
    for i in range(imageArr.shape[0]):
        for j in range(imageArr.shape[1]):
            (b, g, r) = imageArr[i,j]
            imageArr[i,j] = pixToHsv(b, g, r)
    cv2.imshow('HSV(Press any key to close window)',imageArr)
    ###Loop for each pixel###
    for i in range(imageArr.shape[0]):
        for j in range(imageArr.shape[1]):
            (v, s, h) = imageArr[i,j]
            imageArr[i,j] = pixToBgr(v, s, h)
    cv2.imshow('HSVtoRGB(Press any key to close window)',imageArr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 1

def rgbToHsvCV():
    file = fileOpen()
    if (file == -1):
        return -1
    imageArr = cv2.imread(file)
    cv2.imshow('RGB(Press any key to close window)',imageArr)
    imageArr = cv2.cvtColor(imageArr, cv2.COLOR_BGR2HSV)
    cv2.imshow('CV2 to HSV(Press any key to close window)',imageArr)           
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 1

def hsvToBgrCV():
    file = fileOpen()
    if (file == -1):
        return -1
    imageArr = cv2.imread(file)
    cv2.imshow('RGB(Press any key to close window)',imageArr)
    imageArr = cv2.cvtColor(imageArr, cv2.COLOR_BGR2HSV)
    cv2.imshow('CV2 to HSV(Press any key to close window)',imageArr)
    imageArr = cv2.cvtColor(imageArr, cv2.COLOR_HSV2BGR)
    cv2.imshow('CV2 to BGR(Press any key to close window)',imageArr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 1

def compareMyWithCv():
    ###############
    """Read File"""
    file = fileOpen()
    if (file == -1):
        return -1
    imageArr = cv2.imread(file)
    #cv2.imshow('RGB(Press any key to close window)',imageArr)  #Uncomment to output image on this step
    ################################
    """Create window with results"""
    windowResults = tk.Toplevel(root)
    lbMy=tk.Label(windowResults, text="||\n||\n||\n||\n||").grid(row = 0, column = 1,rowspan = 5)
    lbMy=tk.Label(windowResults, text="To HSV").grid(row = 0, column = 2)
    lbMy=tk.Label(windowResults, text="||\n||\n||\n||\n||").grid(row = 0, column = 3,rowspan = 5)
    lbMy=tk.Label(windowResults, text="From HSV to RGB").grid(row = 0, column = 4)
    lbMy=tk.Label(windowResults, text="My realization").grid(row = 1, column = 0)
    lbCV=tk.Label(windowResults, text="CV realization").grid(row = 2, column = 0)
    ############################
    """My convertation to HSV"""
    startTime = time.time()
    ###Loop for each pixel###
    for i in range(imageArr.shape[0]):
        for j in range(imageArr.shape[1]):
            
            (b,g,r) = imageArr[i,j]
            imageArr[i,j] = pixToHsv(b,g,r)
    myResultTimeHSV = time.time() - startTime
    #cv2.imshow('my HSV(Press any key to close window)',imageArr)  #Uncomment to output image on this step
    ############################
    """My convertation to RGB"""
    startTime = time.time()
    ###Loop for each pixel###
    for i in range(imageArr.shape[0]):
        for j in range(imageArr.shape[1]):
            (b,g,r) = imageArr[i,j]
            imageArr[i,j] = pixToHsv(b,g,r)
    myResultTimeBGR = time.time() - startTime
    #cv2.imshow('my RGB(Press any key to close window)',imageArr)  #Uncomment to output image on this step
    ############################
    """CV convertation to HSV"""
    imageArrCV = cv2.imread(file)
    startTime = time.time()
    imageArrCV = cv2.cvtColor(imageArrCV, cv2.COLOR_BGR2HSV)
    cvResultTimeHSV = time.time() - startTime
    #cv2.imshow('CV HSV(Press any key to close window)',imageArrCV)  #Uncomment to output image on this step
    ############################
    """CV convertation to RGB"""
    startTime = time.time()
    imageArrCV = cv2.cvtColor(imageArrCV, cv2.COLOR_HSV2BGR)
    cvResultTimeBGR = time.time() - startTime
    #cv2.imshow('CV RGB(Press any key to close window)',imageArrCV)  #Uncomment to output image on this step
    ################################
    """Change window with results"""
    lbMy=tk.Label(windowResults, text=str(round(myResultTimeHSV,4))).grid(row = 1, column = 2)
    lbMy=tk.Label(windowResults, text=str(round(myResultTimeBGR,4))).grid(row = 1, column = 4)
    lbMy=tk.Label(windowResults, text=str(round(cvResultTimeHSV,7))).grid(row = 2, column = 2)
    lbMy=tk.Label(windowResults, text=str(round(cvResultTimeBGR,6))).grid(row = 2, column = 4)
    
    #cv2.waitKey(0)  #Uncomment to wait key befor closing image
    #cv2.destroyAllWindows()  #Uncomment to close all the windows
    return 1

def brightnessRGB():
    ######################
    """Brightness value"""
    bright = 50
    ######################
    file = fileOpen()
    if (file == -1):
        return -1
    imageArr = cv2.imread(file)
    cv2.imshow('Original',imageArr)
    ###Loop for each pixel###
    for i in range(imageArr.shape[0]):
        for j in range(imageArr.shape[1]):
            (b, g, r) = imageArr[i, j]
            r = clamp((r + bright),255,0)
            g = clamp((g + bright),255,0)
            b = clamp((b + bright),255,0)
            imageArr[i, j] = (b, g, r)
    cv2.imshow('After bright-filter',imageArr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 1

def brightnessHSV():
    ######################
    """Brightness value"""
    bright = 50
    ######################
    file = fileOpen()
    if (file == -1):
        return -1
    imageArr = cv2.imread(file)
    cv2.imshow('Original',imageArr)
    imageArr = cv2.cvtColor(imageArr, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(imageArr)
    lim = 255 - bright
    v[v > lim] = 255
    v[v <= lim] += bright
    imageArr = cv2.merge((h, s, v))
    imageArr = cv2.cvtColor(imageArr, cv2.COLOR_HSV2BGR)
    cv2.imshow('After HSV+bright-filter',imageArr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 1

def compareBright():
    ######################
    """Brightness value"""
    bright = 75
    ######################
    ################################
    """Create window with results"""
    windowResults = tk.Toplevel(root)
    lbMy=tk.Label(windowResults, text="||\n||\n||\n||\n||").grid(row = 0, column = 1,rowspan = 5)
    lbMy=tk.Label(windowResults, text="Time").grid(row = 0, column = 2)
    lbMy=tk.Label(windowResults, text="Common brightness filter").grid(row = 1, column = 0)
    lbCV=tk.Label(windowResults, text="HSV brightness filter").grid(row = 2, column = 0)
    ################
    """Open image"""
    file = fileOpen()
    if (file == -1):
        return -1
    imageArr = cv2.imread(file)
    #cv2.imshow('Original',imageArr)  #Uncomment to output image 
    ###############################
    """Brightness filter for RGB"""
    startTime = time.time()
    ###Loop for each pixel###
    for i in range(imageArr.shape[0]):
        for j in range(imageArr.shape[1]):
            (b, g, r) = imageArr[i, j]
            r = clamp((r + bright),255,0)
            g = clamp((g + bright),255,0)
            b = clamp((b + bright),255,0)
            imageArr[i, j] = (b, g, r)
    rgbResultTime = time.time() - startTime
    #cv2.imshow('After bright-filter',imageArr)  #Uncomment to output image
    ###############################
    """Brightness filter for RGB"""
    imageArrHsv = cv2.imread(file)
    startTime = time.time()
    imageArrHsv = cv2.cvtColor(imageArrHsv, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(imageArrHsv)
    lim = 255 - bright
    v[v > lim] = 255
    v[v <= lim] += bright
    imageArrHsv = cv2.merge((h, s, v))
    imageArrHsv = cv2.cvtColor(imageArrHsv, cv2.COLOR_HSV2BGR)
    hsvResultTime = time.time() - startTime
    #cv2.imshow('After HSV+bright-filter',imageArrHsv)  #Uncomment to output image
    ################################
    """Change window with results"""
    lbMy=tk.Label(windowResults, text=str(round(rgbResultTime,4))).grid(row = 1, column = 2)
    lbMy=tk.Label(windowResults, text=str(round(hsvResultTime,6))).grid(row = 2, column = 2)

    #cv2.waitKey(0)  #Uncomment to wait key befor closing image
    #cv2.destroyAllWindows()  #Uncomment to close all the windows
    return 1

######################
"""Buttons and form"""
######################
root = tk.Tk()
hsvBut1 = tk.Button(root, text = 'From RGB to HSV', activebackground = "#555555", command = rgbToHsv).grid(row = 0, column = 0)
hsvBut2 = tk.Button(root, text = 'From HSV to RGB', activebackground = "#555555", command = hsvToBgr).grid(row = 0, column = 1)
hsvBut3 = tk.Button(root, text = 'OpenCV RGB to HSV', activebackground = "#555555", command = rgbToHsvCV).grid(row = 2, column = 0)
hsvBut4 = tk.Button(root, text = 'OpenCV HSV to RGB', activebackground = "#555555", command = hsvToBgrCV).grid(row = 2, column = 1)
hsvBut5 = tk.Button(root, text = 'Compare results of RGB <-> HSV', activebackground = "#555555", command = compareMyWithCv).grid(row = 4, column = 0, columnspan = 2)

lbFreeSpace = tk.Label(root, text = '||').grid(row = 0, column = 2)
lbFreeSpace = tk.Label(root, text = '||').grid(row = 1, column = 2)
lbFreeSpace = tk.Label(root, text = '||').grid(row = 2, column = 2)
lbFreeSpace = tk.Label(root, text = '=============================').grid(row = 1, column = 0, columnspan = 2)
lbFreeSpace = tk.Label(root, text = '=============================').grid(row = 1, column = 3, columnspan = 2)
lbFreeSpace = tk.Label(root, text = '||').grid(row = 3, column = 2)
lbFreeSpace = tk.Label(root, text = '=============================').grid(row = 3, column = 0, columnspan = 2)
lbFreeSpace = tk.Label(root, text = '=============================').grid(row = 3, column = 3, columnspan = 2)
lbFreeSpace = tk.Label(root, text = '||').grid(row = 4, column = 2)

hsvBut6 = tk.Button(root, text = 'RGB Brightness', activebackground = "#555555", command = brightnessRGB).grid(row = 0, column = 3)
hsvBut7 = tk.Button(root, text = 'HSV Brightness', activebackground = "#555555", command = brightnessHSV).grid(row = 0, column = 4)
hsvBut8 = tk.Button(root, text = 'Compare brightness func-s', activebackground = "#555555", command = compareBright).grid(row = 4, column = 3, columnspan = 2)
root.mainloop()
