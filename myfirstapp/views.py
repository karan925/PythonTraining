from django.shortcuts import render
from django.http import HttpResponse
from . import forms


# Create your views here.

def home(request):
    return HttpResponse("This is first page")


def random(request):
    return HttpResponse("This is second page")


def index(request):
    return render(request, "myfirstapp/index.html", context={"context_var": "context_value"})
    # request, template directory, context


def form_view(request):
    form = forms.Login()
    if request.method == "POST":
        form = forms.Login(request.POST)
    if form.is_valid():
        print("Validation worked")
        print("Name: " + form.cleaned_data['name'])
        print("Email: " + form.cleaned_data['email'])
        print("Text: " + form.cleaned_data['text'])
        print("Password: " + form.cleaned_data['password'])
    return render(request, "myfirstapp/forms.html", {'form': form})
