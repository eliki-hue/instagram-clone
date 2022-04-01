from django.shortcuts import render
from .models import Image, Profile

# Create your views here.

def welcome(request):
    images = Image.objects.all()

    return render('index.html',{'images':images})

