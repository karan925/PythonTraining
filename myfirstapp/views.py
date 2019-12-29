from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("This is first page")


def random(request):
    return HttpResponse("This is second page")
