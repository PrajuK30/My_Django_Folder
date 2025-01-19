from django.shortcuts import render,HttpResponse

# Create your views here.
def home (request):
    return HttpResponse("this is my home page")

def home1 (request):
    return HttpResponse("this is my home1 page")


def home2 (request):
    return HttpResponse("this is my home2 page")


def home3 (request):
    return HttpResponse("this is my home3 page")

