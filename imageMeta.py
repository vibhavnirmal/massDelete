import glob
import os
import shutil

from PIL import Image
from PIL.ExifTags import TAGS

count = 0
fileNames = []
path = input("Enter the Folder Location where photos are.\n")
finalPath = input("Enter the Destination Path to copy photos.\n")
os.chdir(path)


for filename in glob.iglob(os.getcwd()+"//*.*", recursive=True):
    if ".jpg" in filename or ".png" in filename or ".jpeg" in filename:
        fileNames.append(filename)


def copyImages(onePic, finalDest):
	if not os.path.exists(finalDest):
		os.makedirs(finalDest)
	shutil.copy2(onePic,finalDest)

def get_date_taken(pathOfPhoto):
    image = Image.open(pathOfPhoto, "r")

    if image._getexif() is not None:
        return Image.open(pathOfPhoto)._getexif()[36867]
	return "No data found"

def cameraMaker(pathOfPhoto):
    image = Image.open(pathOfPhoto, "r")

    if image._getexif() is not None:
        for (tag, value) in image._getexif().items():
            if TAGS.get(tag) == "Make" and value == "Motorola": 
				# Copies all the photographs with maker name motorola to another folder
				copyImages(pathOfPhoto, finalPath)
				count+=1

for onePic in fileNames:
    # get_date_taken(onePic)
    cameraMaker(onePic)

print("Moved "+count+" Images")
