from django.shortcuts import render, HttpResponse

from myapp.models import Message

# Create your views here.

def index(request):
    all_messages = Message.objects.all()	
    return render(request, 'index.html', {'messages': all_messages})
