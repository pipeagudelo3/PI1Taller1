from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html", {"name": "Felipe Agudelo"})

def about(request):
    return HttpResponse("<h1>About</h1><p>About page content</p>")
