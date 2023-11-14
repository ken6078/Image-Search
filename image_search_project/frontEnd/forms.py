from django import forms


class KeywordForm(forms.Form):
    keyword = forms.CharField(label="keyword", max_length=100)
    
class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Upload Image')