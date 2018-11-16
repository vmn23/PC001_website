from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'landing/index.html', context)

def journey1(request):
    context = {'back':'', 'forward':'journey2', 'progress': '20'}
    return render(request, 'landing/journey1.html', context)

def journey2(request):
    context = {'back':'journey1', 'forward':'journey3', 'progress': '40'}
    return render(request, 'landing/journey2.html', context)

def journey3(request):
    context = {'back':'journey2', 'forward':'journey4', 'progress': '60'}
    return render(request, 'landing/journey3.html', context)

def journey4(request):
    context = {'back':'journey3', 'forward':'journey5', 'progress': '80'}
    return render(request, 'landing/journey4.html', context)

def journey5(request):
    context = {'back':'journey4', 'forward':'login', 'progress': '1000'}
    return render(request, 'landing/journey5.html', context)

def homepage(request):
    context = {}
    return render(request, 'landing/homepage.html', context)

def matches(request):
    context = {}
    return render(request, 'landing/matches.html', context)

def buildresume(request):
    context = {}
    return render(request, 'landing/buildResume.html', context)

def questionnaire(request):
    context = {}
    return render(request, 'landing/questionnaire.html', context)

def job1(request):
    context = {}
    return render(request, 'landing/job1.html', context)

def job2(request):
    context = {}
    return render(request, 'landing/job2.html', context)

def job3(request):
    context = {}
    return render(request, 'landing/job3.html', context)