from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello')
def index2(request):
    return render(request,'index2.html')
def index3(r):
    return render(r,'facebook.html') 
def index4(m):
    return render(m,'artofsoul.html')  