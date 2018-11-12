from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    #return HttpResponse("You are at the index.")
    #template = loader.get_template('landing/index.html')
    context = {}
    #return HttpResponse(template.render(context,request))
    return render(request, 'landing/index.html', context)

def tutorial(request):
    return HttpResponse("You are at the tutorial page.")

def homepage(request):
    return HttpResponse("You are at the homepage page.")