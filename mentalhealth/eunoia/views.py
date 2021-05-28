from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

def home(request):
    return render(request, 'eunoia/home.html', {})

def detailBlog(request, blog_id):
    data = {}

    blog_id = int(blog_id)

    post = Post.objects.get(id = blog_id)

    data = {
        'post': post
    }

    return render(request, 'eunoia/detailedblog.html', data)


def blogGrid(request):

    posts = Post.objects.all()

    data = {'posts': posts}

    return render(request, 'eunoia/bloggrid.html', data)