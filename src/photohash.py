from PIL import Image

def average_hash(image: Image, hash_size=8):
    """ Compute the average hash of the given image. """
    pixels = list(image.getdata())
    print(type(image))
    avg = sum(pixels) / len(pixels)
    bits = "".join(map(lambda pixel: '1' if pixel > avg else '0', pixels))
    hashformat = "0{hashlength}x".format(hashlength=hash_size ** 2 // 4)
    return int(bits, 2).__format__(hashformat)