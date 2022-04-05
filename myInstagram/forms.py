from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Profile,Image, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['username']
        fields ='__all__'

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        # exclude=['profile']
        fields ='__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields='__all__'