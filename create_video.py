import cv2
import numpy as np
import glob
 
img_array = []
# for filename in glob.glob('C:/PERSO/raspberry/20200225/*.jpg'):
for filename in glob.glob('/home/raspberry/software/day/20200227/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter('20200227_48.avi',cv2.VideoWriter_fourcc(*'DIVX'), 48, size)
# out = cv2.VideoWriter('20200227_48.avi',cv2.cv.CV_FOURCC(*'DIVX'), 48, size)
# out = cv2.VideoWriter('20200225_48.mp4',cv2.cv.CV_FOURCC(*'MP4V'), 48, size)
# out = cv2.VideoWriter('20200225_48.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 48, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])

out.release()
