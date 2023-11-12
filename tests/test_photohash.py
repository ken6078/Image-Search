from src.photohash import average_hash, hash_distance
from PIL import Image
import pytest

def test_average_hash():
    with open('assets/Joeman.jpg', 'rb') as f:
        image = Image.open(f).resize((8, 8), Image.Resampling.LANCZOS).convert('L')
        assert average_hash(image) == 'feffffffc3030323'
    
    with open('assets/Lyla.jpeg', 'rb') as f:
        image = Image.open(f).resize((8, 8), Image.Resampling.LANCZOS).convert('L')
        assert average_hash(image) == '36221a096fe3f1fc'

def test_hash_distance():
    assert hash_distance('feffffffc3030323','feffffffc3030323') == 0
    assert hash_distance('feffffffc3030323','36221a096fe3f1fc') == 15

    with pytest.raises(ValueError) as excinfo:
        hash_distance('','0')
    assert str(excinfo.value) == "Hamming distance requires two strings of equal length"