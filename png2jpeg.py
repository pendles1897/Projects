import os
from PIL import Image

os.chdir('/Users/eugependleton/Scripts')
oldImage = ''
newImage = ''
for files in os.getcwd():
    if files.endswith('.png') or files.endswith('.png'):
        newImage = files
        oldImage = files
    else:
        pass

# Convert to JPEG and remove PNG
im = Image.open(newImage)
target_name = newImage[:-4] + ".jpeg"
rgb_im = im.convert('RGB')
rgb_im.save(target_name)
os.remove(oldImage)

print("Process complete.")
