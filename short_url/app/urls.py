from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.creatShortURL, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('<str:url>', views.direct, name="direct"),
    path('my-urls/', views.myUrls, name="my-urls"),
]