from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from . models import *
from .forms import *

def index(request):
    if request.method=='GET':
        thread_list=Thread.objects.all()
        thread_form=ThreadForm()
        return render(request,'home.html',{'thread_list':thread_list,'thread_form':thread_form})
    elif request.method=='POST':
        title=request.POST['title']
        text=request.POST['text']
        file=request.FILES['image']
        thread=Thread.objects.create(title=title,text=text,image=file)
        thread.save()
        return redirect(reverse('home'))

def thread(request,pk):
    if request.method=='GET':
        thread = get_object_or_404(Thread, pk=pk)
        post_form = PostForm()
        return render(request, 'thread.html', {'thread': thread, 'post_form': post_form})
    elif request.method=='POST':
        text=request.POST['text']
        thread=get_object_or_404(Thread,pk=pk)
        file=request.FILES['post_image']
        post = Post.objects.create(text=text, thread=thread, post_image=file)
        post.save()
        return redirect(reverse('thread',args=[pk]))

