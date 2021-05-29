from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView

from .data import anxeity_questions, getIndiaData, getGlobalCovidData

from .forms import CreateUserForm, FeedbackForm

from django.contrib.auth import authenticate, login

from cowin_api import CoWinAPI



# Create your views here.

def home(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        # If form is valid then it saves it.
        if form.is_valid():
            form.save()

    data = {}

    form = FeedbackForm()

    data['form'] = form

    return render(request, 'eunoia/home.html', data)

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

def covidDashboard(request):

    cowin = CoWinAPI()

    content = {}

    content["searched"] = '0'

    if request.method == 'POST':
        option = request.POST['option']
        date = request.POST["date"]
        age = request.POST["age"]
        parameter = request.POST['parameter']

        date = date.split("-")
        date = date[-1]+"-"+date[-2]+"-"+date[-3]

        age = 18
        print(parameter)
        if option == "pincode":
            data = cowin.get_availability_by_pincode(pin_code=parameter, date=date, min_age_limt=age)
        else:
            data = cowin.get_availability_by_district(district_id=parameter, date=date, min_age_limt=age)
        
        content = {
            "centers":data["centers"],
            "searched": '1',
        }


    return render(request, 'eunoia/covidDashboard.html', content)