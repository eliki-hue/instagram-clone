from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=20)
    useremail = models.EmailField(max_length=20)
    userage = models.CharField(max_length=2)
    profile_image = models.ImageField(upload_to = 'images/')
    user_password = models.CharField(max_length=15)

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =60)
    image_caption= models.CharField(max_length=100)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.CharField(max_length=10)
    comments = models.CharField(max_length=50)

    def __str__(self):
        return self.image_name