import os
from PIL import Image
import numpy as np

rootDir = 'photos\\'
imageSize = (200,200)

def main():
    print("Number of Images: ",imageFinder(rootDir))
    print("Dimension of Array containing resized pictures.: ", imageProcess(rootDir, imageSize).ndim)
    print("Shape of Array containing resized pictures.: ", imageProcess(rootDir, imageSize).shape)
    print("Type of Array containing resized pictures.: ", type(imageProcess(rootDir, imageSize)))

#THIS FUNCTION WILL ONLY RETURN THE NUMBER OF IMAGES IN THE FOLDER
#This function first will check if the path exists or not
#Later it will walk through through the path
#Then it'll return with directories, sub-directoreis and files
#And then it'll save the number of files in fileList into a variable
#Which will be return after the execution of function
def imageFinder(path):
    try:
        if os.path.exists(path):
            for dirList, subDirList, fileList in os.walk(path):
                    numberOfImages = len(fileList)

        return numberOfImages
    except FileNotFoundError:
        print("File Not Found.")

#THIS FUNCTION WILL PROCESS THE IMAGE
#This function first will check if the path exists or not
#Later it will walk through through the path
#Then it'll return with directories, sub-directoreis and files
#Later we'd fetch filenames from the fileList
#After fetching, there will be a filter checking if the file is in JPG format to process futher
#And then it'll open the image, in next line it'll resize it and then it'll put each image into Numpy array after resizing it
def imageProcess(path,imageSize):
    try:
        if os.path.exists(path):
            for dirList, subDirList, fileList in os.walk(path):
                for pictures in fileList:
                    if pictures.endswith(".jpg"):
                        img = Image.open(path+pictures)
                        resized_img = img.resize(imageSize)
                        array_of_images = np.array(resized_img)

        return array_of_images

    except FileNotFoundError:
        print("File Not Found.")

if __name__ == "__main__":
    main()