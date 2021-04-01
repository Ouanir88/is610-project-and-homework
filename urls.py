from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('another', views.another, name='another'),
    #path('mysite', views.mysite, name='mysite'),
    path('Ouanir', views.Ouanir, name='Ouanir'),
]