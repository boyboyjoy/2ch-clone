from PIL import Image
from django.db import models
from django.forms import ModelForm
from django_resized import ResizedImageField

from .forms import UploadForm

class Thread(models.Model):
    image=ResizedImageField(size=[400, 250], upload_to='media/')
    title=models.CharField(max_length=50,blank=False)
    text=models.TextField(max_length=500,blank=False)


class Post(models.Model):
    post_image=ResizedImageField(size=[400, 250], upload_to='media/',default=None,null=True)
    text=models.TextField(max_length=100,blank=False)
    thread=models.ForeignKey(Thread,on_delete=models.CASCADE,blank=False)


class ThreadForm(ModelForm):
    class Meta:
        model=Thread
        fields=['image','title','text']

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields = ['post_image', 'text',]
