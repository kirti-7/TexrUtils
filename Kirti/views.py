# Created by Kirti
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # return HttpResponse('''<h1>Index</h1> <br> <a href="https://www.w3schools.com">Visit W3Schools</a>''')
    return render(request,'index.html')

def removepunc(request):
    return HttpResponse("Remove punc")

def capfirst(request):
    return HttpResponse("Capitalize first")

def newlineremove(request):
    return HttpResponse("NewLine remove")

def spaceremove(request):
    return HttpResponse("Space Remove")

def charcount(request):
    return HttpResponse('''<a href="/">back</a>''')