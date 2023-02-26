#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 


# In[2]:


#Break down the video into frames
video = cv2.VideoCapture("Lots of Butterfly Flying in Flowers Garden _ How Butterflies Pollinate Flowers.mp4")
frameNr = 0
while (True):
    success, frame = video.read()
    if success:
        cv2.imwrite(f'/Users/admin/Documents/eaiQ1/frame_{frameNr}.jpg', frame)
    else:
        break
    frameNr = frameNr+1
video.release()


# In[1]:


from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
from skimage import filters
from skimage import io, color, filters as filters
from scipy import ndimage

from skimage.feature import peak_local_max
from skimage.measure import regionprops, label

# Count the no. of butterflies in each frame
for x in range(0, 2127):
    image = color.rgb2gray(io.imread(f'frame_{x}.jpg'))
    image = image < filters.threshold_otsu(image)
    distance = ndimage.distance_transform_edt(image)
    butterfly_centres = (distance > 0.8 * distance.max())
    print(f'Number of butterflies of frame_{x}:', np.max(label(butterfly_centres)))


# In[ ]:




