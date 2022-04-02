from django.shortcuts import render
from .models import Image, Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all()
    message ="Welcome to my Instagram clone"

    return render(request,'index.html',{'images':images, 'message': message})

