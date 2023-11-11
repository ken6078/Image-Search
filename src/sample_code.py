from Pick_image import Pick_image

from datetime import datetime
from PIL import Image

start = datetime.now()
p = Pick_image()
init = datetime.now()
with open('assets/Joeman.jpg', 'rb') as f:
    image = Image.open(f)
    searchStart = datetime.now()
    p.pick_images_with_image(image)
searchImage = datetime.now()
p.pick_images_with_keyword('woman')
finish = datetime.now()

print(f"init Time: {init - start}")
print(f"search image Time: {searchImage - searchStart}")
print(f"search keyword Time: {finish - searchImage}")