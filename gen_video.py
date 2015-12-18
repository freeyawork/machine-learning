# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 20:54:34 2015

@author: freeya Wang
This function can merge images and video in given path where there are many jpg images and a video.
It is for first cv homework which is making your own video.
@ path: 
"""

def gen_video(path):
    import numpy as np
    import cv2
    import os
    alpha=np.arange(0,101)/float(100)    #path='F:/cv_video/'
    #print alpha
    frames=os.listdir(path)
    video=[i for i in frames if i.split('.')[1]!='jpg'and i.split('.')[1]!='avi'][0]
    #print video
    images=[i for i in frames if i.split('.')[1]=='JPG']
    capture=cv2.VideoCapture(path+video)
    # get properties of the given video
   
    Vwidth = np.uint(capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
    Vheight = np.uint(capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
    Vfps = capture.get(cv2.cv.CV_CAP_PROP_FPS)
    Fnum = int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    newvideoname='freeya.avi'
    newcapture=cv2.VideoWriter()
    newcapture.open(path+newvideoname,cv2.cv.CV_FOURCC('M','J','P','G'),np.uint(Vfps),(Vwidth,Vheight),1)
    for j in range(len(images)-1):
        image1=cv2.resize(cv2.imread(path+images[j]),(Vwidth,Vheight))
        image2=cv2.resize(cv2.imread(path+images[j+1]),(Vwidth,Vheight))
        #imageText=image.copy()
        # cv2.putText(image1, '21521202 Chenxi Wang', (100, Vheight-100), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 255 ,0), thickness = 4, lineType = 8)
        # newcapture.write(image1)
        for j in alpha:
            image=cv2.addWeighted(image1,1-j,image2,j,0.0)
            #print j
            cv2.putText(image, '21521202 Chenxi Wang', (100, Vheight-100), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 255 ,0), thickness = 4, lineType = 8)
            newcapture.write(image)
    print Fnum
    for i in range(Fnum):
        frame=capture.read()[1]
        cv2.putText(frame, '21521202 Chenxi Wang', (100, Vheight-100), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 255 ,0), thickness = 4, lineType = 8)  
        newcapture.write(frame)
    print 'new video has been generated successfully ! '
    newcapture.release()

if __name__ == '__main__':
    import sys
    path='f:/cv_video/'
    gen_video(sys.argv[1])
    #gen_video(path)
