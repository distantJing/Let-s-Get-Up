from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200) #   to do : use md5 to encrypt
#     # basic info
#     age = models.IntegerField(default=18)
#     avatar = models.ImageField(upload_to='img')
#     weight = models.IntegerField(default=50)
#     height = models.FloatField(default=150.0)
#     def __str__(self):
#         return self.username 

class UserProfile(models.Model):
    # Link to a user model instance.
    user = models.OneToOneField(User,null=True,blank=True)

    # Some additional attributes we wish to be included.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='img',blank=True)
    age = models.IntegerField(default=18)
    weight = models.FloatField(default=50.0)
    height = models.FloatField(default=165.0)
    

    # overide the __unicode__() to return something meanigful
    def __unicode__(self):
        return self.user.username


