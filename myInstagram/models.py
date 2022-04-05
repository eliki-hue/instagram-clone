
from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=20)
    useremail = models.EmailField(max_length=30)
    userage = models.CharField(max_length=2)
    bio = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to = 'images/')
    user_password = models.CharField(max_length=15)
    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self,username):
        to_delete= Profile.objects.filter(username=username).delete()
    
    def update_profile(self,old_user,new_user):
        Profile.objects.filter(username=old_user).update(name=new_user)
        self.save()

class Comment(models.Model):
    comments =models.CharField(max_length=100, blank=True, default='great')

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =60)
    image_caption= models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.CharField(blank=True,max_length=10 , default=0)
    comments = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self,image_reff):
        to_delete= Image.objects.filter(name=image_reff).delete()

    
    

    

    