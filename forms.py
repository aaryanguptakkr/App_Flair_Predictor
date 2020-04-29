from django import forms
from django.contrib.auth.models import User
from .models import Upload


class uploadForm(forms.ModelForm):
    # files = forms.FileField(upload_to='documents/')
    class Meta:
        model = Upload
        fields = '__all__'
