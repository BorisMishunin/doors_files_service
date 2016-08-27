from django import forms
from models import DoorsImages


class DoorsImagesForm(forms.ModelForm):
    
    class Meta:
        model = DoorsImages
        fields = "__all__"
