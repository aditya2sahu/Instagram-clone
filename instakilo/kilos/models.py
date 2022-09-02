from django.db import models
from  django.contrib.auth.models import User
# Create your models here.
from PIL import Image

class userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    followers=models.ManyToManyField(User,related_name="followrs",blank=True)
    following = models.ManyToManyField(User, related_name="following", blank=True)
    profileimage=models.ImageField(upload_to="image",blank=True)
    bio=models.CharField(max_length=200,blank=True)
    accountcreated=models.DateTimeField(auto_now_add=True)


class profilepost(models.Model):
    profile=models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="image",blank=True)
    like=models.ManyToManyField(User,related_name="likes",blank=True)
    caption=models.CharField(max_length=500,blank=True)
    profile_for_unlike_post=models.ForeignKey(userprofile,on_delete=models.CASCADE)
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.image.path)


        if img.height >450 or img.weight >450:
            output_size=(450,450)
            img.thumbnail(output_size)
            img.save(self.image.path)


class comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile=models.ForeignKey(userprofile,on_delete=models.CASCADE)
    comment=models.CharField(max_length=500)
    reply=models.CharField(max_length=500)
    post=models.ForeignKey(profilepost,on_delete=models.CASCADE)















