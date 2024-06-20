from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<h1> My first webpage with python Django </h1>")