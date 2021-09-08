import os
import sys
import cv2
import operator
import numpy as np
from skimage import io
from math import sqrt
import matplotlib.pyplot as plt
from PIL import Image
import findDominant
import closestEmoji
#see below page for much of the code this program is based upon
#https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv/43111221

<<<<<<< Updated upstream:src/calculateRGB.py
#looks at the assets/72x72 directory, calculates the dominant color in each .png image in that folder, and returns a dictionary where the key refers to the image file name, and the value is a tuple of RGB values

#possible improvments to function involve having a check in place for ignore pixels under a certain alpha value
def dominant():
    dominant_colors = []
    filelist = []
    cur_path = os.path.dirname(__file__)
    assets = os.path.relpath('../assets/72x72', cur_path)
    for filename in os.listdir(assets):
        if filename.endswith('.png'):
            image = io.imread(assets +"/"+str(filename))[:, :, :-1]
            pixels = np.float32(image.reshape(-1, 3))
            n_colors = 1
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
            flags = cv2.KMEANS_RANDOM_CENTERS

            _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
            _, counts = np.unique(labels, return_counts=True)
            dominant_color = palette[np.argmax(counts)]
            dominant_colors.append(dominant_color)
            filelist.append(filename)
            
    dominant_colors = np.array(dominant_colors)
    return dominant_colors, filelist
    
#thanks https://stackoverflow.com/a/54244301/16065633
def closestEmoji(userImagePixelColor, emojiColors, filelist):
    distances = np.sqrt(np.sum((emojiColors - userImagePixelColor)**2, axis=1))
    index_of_smallest = np.where(distances==np.amin((distances)))
    smallest_distance = emojiColors[index_of_smallest]
    return smallest_distance, index_of_smallest[0].item()




if __name__ == "__main__":
    
    userImage = io.imread('pepelaugh.png')[:,:,:-1]
    userImageHeight = userImage.shape[0]
    userImageWidth = userImage.shape[1]
    userPixels = np.float32(userImage.reshape(-1, 3))
    emojiList,filelist = dominant()
    finalImage = np.zeros((userImageHeight*72, userImageWidth*72, 4))
=======

if __name__ == "__main__":
    
    #change string to path of image name
    userImage = io.imread('osrsIcon.png')[:,:,:-1]
    userImageHeight, userImageWidth = userImage.shape[0], userImage.shape[1]
    userPixels = np.float32(userImage.reshape(-1, 3))
    emojiList,filelist = findDominant.dominant()
    finalImage = np.zeros((userImageHeight*72, userImageWidth*72, 4,), dtype=np.uint8)
>>>>>>> Stashed changes:src/ConvertPNG.py
    finalImageX = 0
    finalImageY = 0

    #these offsets are set to the size of an emoji
    emojiImageXOffset = 72
    emojiImageYOffset = 72
    cur_path = os.path.dirname(__file__)
    assets = os.path.relpath('../assets/72x72/', cur_path)
    for i in userPixels:
        userClosestEmoji, filename = closestEmoji.closestEmoji(i, emojiList, filelist)
        emoji = io.imread(assets +"/"+ filelist[filename])
        finalImage[finalImageY:(finalImageY+emojiImageYOffset),finalImageX:(finalImageX+emojiImageXOffset)] = emoji

        finalImageX += emojiImageXOffset
        if(finalImageX == finalImage.shape[0]):
            finalImageX = 0
            finalImageY += emojiImageYOffset
    print('done') 
    
<<<<<<< Updated upstream:src/calculateRGB.py
    finalImageInt = finalImage.astype(int)
=======

    io.imsave('emojiVersionImage.png', finalImage)
>>>>>>> Stashed changes:src/ConvertPNG.py
    
    io.imshow(finalImageInt)
    io.imsave('poopy.png', finalImageInt)
    plt.show()

   

   
   