from django.shortcuts import redirect, render
from .models import Image, Profile
from django.contrib.auth.decorators import login_required

# Create your views here.


def first_page(request):
    
    return redirect('/accounts/login/')

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
    message ="Welcome to my Instagram clone"

    return render(request,'index.html',{'images':images, 'message': message})

