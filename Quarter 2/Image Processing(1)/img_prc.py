import numpy as np
from PIL import Image
import os

image_size = (512, 512)

rootDir = 'photos\\'
for dirName,subDirList,fileList in os.walk(rootDir):
    for pictures in fileList:
        if pictures.endswith(".jpg"):
            img = Image.open(rootDir+pictures)
            resized = img.resize((image_size))
            array_of_images = np.array(resized)
#             display(pictures,": ",array_of_images)