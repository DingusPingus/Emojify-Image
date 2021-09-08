import os
import cv2
import numpy as np
from skimage import io

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

if __name__ == "__main__":
    dominant()