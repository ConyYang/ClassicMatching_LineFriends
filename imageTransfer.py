
import os
import glob
from PIL import Image

img_path = glob.glob("OriginalImage/*.png")
print(img_path)
path_save = "transferedImage"

for file in img_path:
  name = os.path.join(path_save, file)
  im = Image.open(file)
  im.thumbnail((130,130))
  print(im.format, im.size, im.mode)
  im.save(name,'png')