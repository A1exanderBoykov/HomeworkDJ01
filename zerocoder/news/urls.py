
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='news_home')
    ]