from .models import Videos
from django.forms import ModelForm, TextInput

class VideoForm(ModelForm):
    class Meta:
        model = Videos
        fields = ["word"]
        widgets = {
            "word": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter text"               
            }),
            }