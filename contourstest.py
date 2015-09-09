import cv2
import numpy as np
# reading image in grayscale
image = cv2.imread('crop45.png',cv2.CV_LOAD_IMAGE_GRAYSCALE)
gray = cv2.GaussianBlur(image, (3, 3), 0)
edged = cv2.Canny(gray, 10, 250)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

# thresholding to get a binary one
#ret, image = cv2.threshold(image, 100,255,cv2.THRESH_BINARY_INV)
# finding the center of image
#image_center = (image.shape[0]/2, image.shape[1]/2)

#if image is None:
 #   print 'can not read the image data'
# finding image contours
contours, hier = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# finding distance of each contour from the center of image
d_min = 1000
for index,cnt in enumerate(contours):
    #mask = np.zeros(image.shape,np.uint8)
    [x, y, w, h] = cv2.boundingRect(cnt)
    crop_img = image[y:y+h, x:x+w] # Crop from x, y, w, h -> 100, 200, 300, 400
 #crop_img = img[y:y+100, x:x+200]
    cv2.imwrite('D:/imm1/crop'+str(index)+'.png', crop_img)
    #cv2.drawContours(image,[cnt],0,(0, 255, 0),-1)
    #mean = cv2.mean(im,mask = mask)
    # finding bounding rect
   # rect = cv2.boundingRect(cnt)
    #size = (w, h, channels) = (100, 100, 1)
    #drawing = np.zeros(size,np.uint8)
    #cv2.drawContours(drawing,cnt,0,(255,0,0),-1)
    #cv2.imwrite('D:/imm1/crop'+str(index)+'.png', cnt)
    #cv2.imwrite('crop1.png', contour)
    # skipping the outliers
    

#cv2.imwrite('crop1.png', contours[0])
#cv2.imshow("Output", image)
#cv2.waitKey(0)