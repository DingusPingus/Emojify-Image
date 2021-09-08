import numpy as np

#thanks https://stackoverflow.com/a/54244301/16065633
def closestEmoji(userImagePixelColor, emojiColors, filelist):
    distances = np.sqrt(np.sum((emojiColors - userImagePixelColor)**2, axis=1))
    index_of_smallest = np.where(distances==np.amin((distances)))[0]
    smallest_distance = emojiColors[index_of_smallest]
    return smallest_distance, index_of_smallest[0].item()


if __name__ == "__main__":
    closestEmoji(userImagePixelColor, emojiColors, filelist)