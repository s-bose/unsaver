from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader


import praw
import random


reddit = praw.Reddit("unsaver", user_agent="unsaver for reddit")
# Create your views here.
def default_view(request):
    # request.session['refresh_token'] = 'test'
    refresh_token = request.session.get('refresh_token')
    if (refresh_token is None):
        return redirect('login')
    else:
        return redirect('home')

def home_view(request):
    if (request.session.get('refresh_token') is None):
        return redirect('login')
    code = request.session.get('code')
    rf = request.session.get('refresh_token')
    print(f'code is {code}\nrefresh_token is {rf}')
    return HttpResponse("home page")

def login_view(request):
    if (request.session.get('refresh_token') is not None):
        return redirect('home')
    authentication_uri = reddit.auth.url(["identity", "read", "save", "history"], random.randint(1, 99999), "permanent")
    template = loader.get_template('my_site/login.html')
    return HttpResponse(template.render({'auth_url': authentication_uri}, request)) 

def authenticated(request):
    code = request.GET.get('code', '')
    refresh_token = reddit.auth.authorize(code)
    request.session['code'] = code
    request.session['refresh_token'] = refresh_token
    return redirect('home')

