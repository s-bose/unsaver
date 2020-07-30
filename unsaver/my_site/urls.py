from django.urls import path

from . import views

urlpatterns = [
    path('', views.default_view, name='default'),
    path('home', views.home_view, name="home"),
    path('login', views.login_view, name="login"),
    path('authenticated', views.authenticated, name="authenticated")
]