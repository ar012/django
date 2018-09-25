from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Hello World! Welcome to selftics-world")

def index(request):
    my_dict = {'insert_content':"Hello I'm from firstapp!"}
    return render(request, 'first_app/index.html',context=my_dict)
