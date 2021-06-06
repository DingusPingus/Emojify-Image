import os
import cv2
import operator
import PixelMap
import numpy as np
from skimage import io
from math import sqrt
from PIL import Image

image1 = io.imread('1f0cf.png')[:,:,:-1]
image2 = io.imread('1f0cf.png')[:,:,:-1]

test = []
test.append(image1)
test.append(image2)
merged = np.concatenate(test, axis=1)
print(merged)
io.imshow(merged)
io.show()

input('we do a little testing')