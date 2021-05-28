from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView

from .data import anxeity_questions

from .forms import CreateUserForm

from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'eunoia/home.html', {})

def register(request):

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(home)
        
    else:
        form = CreateUserForm()
    
    content = {'form': form}

    return render(request, 'registration/registration.html', content)

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

def testgrid(request):
    return render(request, 'eunoia/testgrid.html', {})

def test(request, name = None):
    

    data = {
        'question': anxeity_questions,
    }
    return render(request, 'eunoia/test.html', data)
