from django.shortcuts import render
from .models import Image, Profile

# Create your views here.

def welcome(request):
    images = Image.objects.all()
    message ="Welcome to my Instagram clone"

    return render(request,'index.html',{'images':images, 'message': message})

