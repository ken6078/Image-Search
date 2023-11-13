from django.shortcuts import render

# Create your views here.


def index(request):
    """View function for home page of site."""
    context = {
        'keyword_resultIMageURLs': ['pick_images_with_keyword WORK!','pick_images_with_keyword WORK2!'],
        'image_resultIMageURLs': ['pick_images_with_image_resultIMageURLs WORK!', 'pick_images_with_image_resultIMageURLs WORK2!'],
    }
    
    return render(request, "index.html", context=context)