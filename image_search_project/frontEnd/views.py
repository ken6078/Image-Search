from django.shortcuts import render
from .forms import KeywordForm, ImageUploadForm
from frontEnd.Pick_image import Pick_image
from PIL import Image
from django.core.files.storage import default_storage

# Create your views here.
def index(request):
    """View function for home page of site."""
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        keyword_form = KeywordForm(request.POST)
        image_form = ImageUploadForm(request.POST, request.FILES)
        # Default context values
        context = {
            'keyword_resultIMageURLs': [],
            'image_resultIMageURLs': [],
        }
        p = Pick_image()
        # check whether it's valid:
        if keyword_form.is_valid():
            keyword = request.POST.get('keyword', 'car')
            seed = request.POST.get('seed', '')

            # Handle seed
            # If seed is empty, set it to None
            if not seed:
                seed = None
            elif seed.isdigit():  # If seed consists of digits, convert it to int
                seed = int(seed)  
            else:
                seed = None  # If seed is not a number, set it to None  
            keyword_result = p.pick_images_with_keyword(keyword, seed)
            if keyword_result not in ["關鍵字不存在!", "Keyword does not exist."]: #這邊邏輯還是會error，需要從pick_images修
                context['keyword_resultIMageURLs'] = keyword_result
                
            return render(request, "index.html", context=context)
        
        elif image_form.is_valid():
            print("image_form")
            image = image_form.cleaned_data['image']

            if image:
                file_path = default_storage.save('frontEnd/assets/uploaded_image.jpg', image)
                with default_storage.open(file_path, 'rb') as f:
                    image_result = p.pick_images_with_image(Image.open(f))
                    context['image_resultIMageURLs'] = image_result
            print(image_result)
            return render(request, "index.html", context=context)
    # if a GET (or any other method) we'll create a blank form
    else:
        keyword_form = KeywordForm()
        image_form = ImageUploadForm()

    return render(request, "index.html", {'keyword_form': keyword_form, 'image_form': image_form})