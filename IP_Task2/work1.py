import cv2
import time
def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image = cv2.imread('sobachki.jpg')
viewImage(image, "Image")

startTime = time.time()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
endTime = time.time()
print("Time OpenCV: ",endTime - startTime)
viewImage(gray_image, "Gray Image CV")
TimeCV = endTime - startTime


startTime = time.time()
new_image = image
Red = new_image[:,:,0]
Green = new_image[:,:,1]
Blue= new_image[:,:,2]
average = (Blue*0.148 + Green*0.5547 + Red*0.2952) 
new_image[:,:,0] = average
new_image[:,:,1] = average
new_image[:,:,2] = average
endTime = time.time()
print("Time Average: ",endTime - startTime)
TimeAverage = endTime - startTime
viewImage(new_image, "Gray Image")  
