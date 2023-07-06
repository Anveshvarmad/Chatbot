from django.shortcuts import render
from django.http import HttpResponse
from . models import Search

def index(request):
    data= request.POST.get('name')
    print(data)
    return render(request,'myapp/index.html', {'data': data})

def search(request):
    return render(request, "myapp/search.html", {})

def insertuser(request):
    vsearch = request.POST['tsearch'],
    us = Search(vs=vsearch),
    us.save(),
    return render(request, 'myapp/search.html', {})

def chat(request):
    return render(request, "myapp/chat.html", {})
