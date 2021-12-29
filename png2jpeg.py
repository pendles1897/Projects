import os
from PIL import Image

os.chdir('/Users/eugependleton/Scripts/Conversion Station')
imageFile = ''
for files in os.listdir():
    imageFile = files

imagePath = os.getcwd() + '/' + imageFile
oldimagePath = imagePath

# Convert to JPEG and remove PNG
im = Image.open(imagePath)
target_name = imagePath[:-4] + ".jpeg"
rgb_im = im.convert('RGB')
rgb_im.save(target_name)
os.remove(oldimagePath)

print("Process complete.")
