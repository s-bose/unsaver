from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.http import JsonResponse

import praw
import random


# Create your views here.
def default_view(request):
    # request.session['refresh_token'] = 'test'
    if (request.session.get('refresh_token')):
        return redirect('home')
    else:
        return redirect('login')

def home_view(request):
    if (request.session.get('refresh_token')):
        code = request.session.get('code')
        rf = request.session.get('refresh_token')
        print(f'code is {code}\nrefresh_token is {rf}')
        reddit_authenticated = praw.Reddit("unsaver", refresh_token=rf, user_agent="unsaver for reddit")
        user_name = reddit_authenticated.user.me()
        for saved_posts in reddit_authenticated.user.me().saved(limit=5, params={"after": "t3_i0ut1t"}):
            print(saved_posts.id)
        return HttpResponse(user_name)
    else:
        return redirect('login')


def login_view(request):
    if (request.session.get('refresh_token')):
        return redirect('home')
    reddit = praw.Reddit("unsaver", user_agent="unsaver for reddit")
    authentication_uri = reddit.auth.url(["identity", "read", "save", "history"], random.randint(1, 99999), "permanent")
    # template = loader.get_template('my_site/login.html')
    # return HttpResponse(template.render({'auth_url': authentication_uri}, request))  
    return JsonResponse({"auth_uri": authentication_uri})
    
def authenticated(request):
    reddit = praw.Reddit("unsaver", user_agent="unsaver for reddit")
    code = request.GET.get('code', '')
    refresh_token = reddit.auth.authorize(code)
    request.session['code'] = code
    request.session['refresh_token'] = refresh_token
    return redirect('home')

