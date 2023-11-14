from django.shortcuts import render

from frontEnd.Pick_image import Pick_image
from datetime import datetime
from PIL import Image
# Create your views here.

def index(request):
    """View function for home page of site."""

    p = Pick_image()
    with open('frontEnd/assets/Joeman.jpg', 'rb') as f:
        image = Image.open(f)

        context = {
            'keyword_resultIMageURLs': p.pick_images_with_keyword('woman'),
            'image_resultIMageURLs': p.pick_images_with_image(image),
        }

    return render(request, "index.html", context=context)
