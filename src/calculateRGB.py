import os
import cv2
import numpy as np
from skimage import io
from PIL import Image
#see below page for much of the code this program is based upon
#https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv/43111221

#looks at the assets/72x72 directory, calculates the dominant color in each .png image in that folder, and returns a dictionary where the key refers to the image file name, and the value is a tuple of RGB values
def dominant():
    dominant_colors ={}
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
            dominant = palette[np.argmax(counts)]
            dominant_colors.update({f'{filename}': dominant})
    
    return dominant_colors

if __name__ == "__main__":
    main()