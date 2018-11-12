from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'landing/index.html', context)

def journey1(request):
    context = {}
    return render(request, 'landing/journey1.html', context)

def journey2(request):
    context = {}
    return render(request, 'landing/journey2.html', context)

def journey3(request):
    context = {}
    return render(request, 'landing/journey3.html', context)

def journey4(request):
    context = {}
    return render(request, 'landing/journey4.html', context)

def journey5(request):
    context = {}
    return render(request, 'landing/journey5.html', context)

def homepage(request):
    context = {}
    return render(request, 'landing/homepage.html', context)

def matches(request):
    context = {}
    return render(request, 'landing/matches.html', context)

def buildresume(request):
    context = {}
    return render(request, 'landing/buildresume.html', context)

def questionnaire(request):
    context = {}
    return render(request, 'landing/questionnaire.html', context)