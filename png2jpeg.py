import os
from PIL import Image

os.chdir('/Users/eugependleton/Scripts')
path = os.getcwd()
ls = []
changes = 0
print("PNG file must also be in the 'Scripts' directory.")

# Scan for files and add to array
for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith(".png"):
            a = os.path.join(root,name)
            ls.append(a)
        else:
            pass

# Convert to JPEG and remove PNG
for image in ls:
    if image.endswith(".png"):
        im = Image.open(image)
        target_name = image[:-4] + ".jpeg"
        rgb_im = im.convert('RGB')
        rgb_im.save(target_name)
        changes+=1
        os.remove(image)
    else:
        pass
print("Process complete. {} files converted to JPEG.".format(changes))
