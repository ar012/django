from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1> Hello Viewer!<h1><em> Welcome to My Second Project</em>")

# def home(request):
#     return HttpResponse("<h2>We are always ready to help you</h2>")

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request, 'appTwo/help.html', context=helpdict)
