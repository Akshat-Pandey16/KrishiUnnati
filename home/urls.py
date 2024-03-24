from django.urls import path
from . import views
from .views import index, home, register, login_user, logout_user, voice, GovtScheme

urlpatterns = [
    # path(' ', mainpage.as_view(), name="index"),
    path('home', index, name="index"),
    path('home', home, name="home"),
    path('map', views.map, name='map'),
    # path('login', views.login, name='login'),
    # path('detail', views.detail, name='detail'),
    path("register", register, name="register"),
    path("login_user", login_user, name="login_user"),
    path("logout_user", logout_user, name="logout_user"),
    path('vr', voice, name='voice'),
    path("GovtScheme", GovtScheme, name="GovtScheme"),
]

