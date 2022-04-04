from email import message
from django.shortcuts import redirect, render
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from .form import ProfileForm

# Create your views here.


def first_page(request):
    
    return redirect('/accounts/login/')

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
    message ="Welcome to my Instagram clone"

    return render(request,'index.html',{'images':images, 'message': message})
def profile_update(request):
    form =ProfileForm(request.POST)
    if form.is_valid():
        form.save()
        profile= Profile.objects.get().all()
        return render(request, 'profile.html',{'profile':profile})

def profile_display(request):

    try:
        profile= Profile.objects.get().all()
    except:
        message= "no profile information"
        return render(request, 'profile.html',{'profile':'none', 'message':message})

    return render(request, 'profile.html',{'profile':profile})


    

