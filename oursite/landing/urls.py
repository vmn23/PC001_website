from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('homepage/', views.homepage, name='homepage'),
]