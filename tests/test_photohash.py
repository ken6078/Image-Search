from src.photohash import average_hash
from PIL import Image

def test_average_hash():
    with open('assets/Joeman.jpg', 'rb') as f:
        image = Image.open(f).resize((8, 8), Image.Resampling.LANCZOS).convert('L')
        assert average_hash(image) == 'feffffffc3030323'