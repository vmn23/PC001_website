from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('journey1/', views.journey1, name='journey1'),
    path('journey2/', views.journey2, name='journey2'),
    path('journey3/', views.journey3, name='journey3'),
    path('journey4/', views.journey4, name='journey4'),
    path('journey5/', views.journey5, name='journey5'),
    path('homepage/', views.homepage, name='homepage'),
    path('matches/', views.matches, name='matches'),
    path('buildresume/', views.buildresume, name='buildresume'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    path('job1/', views.job1, name='job1'),
    path('job2/', views.job2, name='job2'),
    path('job3/', views.job3, name='job3'),
]