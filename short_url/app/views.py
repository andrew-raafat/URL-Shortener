from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def shorten_url(original):
    idList = Count.objects.all()
    id = idList[0]
    short = encode(id.counter)
    id.counter += 1
    id.save()
    # if len(ShortURL.objects.filter(original_url = original)) != 0:
    #     list = ShortURL.objects.filter(original_url = original)
    #     short = list[0].short_url
    # else:
    #     short = encode(id.counter)
    #     id.counter += 1
    #     id.save()

    return str(short)

def encode(id):
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(characters)

    ret = []

    while id > 0:
        val = id % base
        ret.append(characters[val])
        id = id // base

    return "".join(ret[::-1])

# @login_required(login_url='login')
def creatShortURL(request):
    form = CreateShortURL()
    obj = request.user
    if request.method == 'POST':
        form = CreateShortURL(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_url']
            short = shorten_url(original_website)
            if len(ShortURL.objects.filter(short_url = short)) == 0:
                d = datetime.now()
                if obj in User.objects.all():
                    s = ShortURL(original_url = original_website,
                                short_url = short, user = obj, time_date_created = d)
                else:
                    s = ShortURL(original_url = original_website,
                                short_url = short, time_date_created = d)
                s.save()
            context = {'form' : short}
            return render(request, 'app/shortURL.html', context)
    context = {'form' : form}
    return render(request, 'app/home.html', context)

def register(request):
    if request.user in User.objects.all():
        return redirect('home')
    form = registerForm()

    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # messages.success(request, f'Hi {username}, your account was created successfully')

            user = authenticate(request, username=username, password=request.POST['password1'])

            if user is not None:
                login(request, user)
                return redirect('home')
            

    context = {'form' : form}
    return render(request, 'app/signup.html', context)

def loginUser(request):
    if request.user in User.objects.all():
        return redirect('home')
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
    return render(request, 'app/signin.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def direct(request, url):
    obj = ShortURL.objects.filter(short_url = url)
    if len(obj) == 0:
        return HttpResponse("ERROR 404 Page not found")
    link = obj[0].original_url
    return redirect(link)

@login_required(login_url='login')
def myUrls(request):
    obj = request.user
    list = ShortURL.objects.filter(user = obj)
    context = {'list' : list}
    return render(request, 'app/myURLs.html', context)