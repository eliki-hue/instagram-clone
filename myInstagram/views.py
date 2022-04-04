from email import message
from django.shortcuts import redirect, render
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# Create your views here.


def first_page(request):
    
    return redirect('/accounts/login/')

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
    message ="Welcome to my Instagram clone"

    return render(request,'index.html',{'images':images, 'message': message})
def profile_update(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile= Profile.objects.filter(username=current_user)
            print(profile)
            if profile:
                print('profile exist')
                username = current_user
                useremail=form.cleaned_data['useremail']
               
                userage=form.cleaned_data['userage']
                profile_image=form.cleaned_data['profile_image']
                user_password=form.cleaned_data['user_password']
                Profile.objects.filter(username=current_user).update(useremail=useremail, userage=userage,profile_image=profile_image,user_password=user_password)
            else:
                print('profile does not exist')
                profile=form.save(commit=False)
                profile.username= current_user
                profile.create()

            message='saved successfuly'
            # profile_display(request)
            return redirect(profile_display)
    
            
    else:
        form = ProfileForm()
        
    return render(request, 'profiledisplay.html',{'form':form})
       
       

def profile_display(request):

    current_user = request.user
    profile= Profile.objects.filter(username=current_user)
   

    return render(request, 'profile.html',{'profile':profile})


    

