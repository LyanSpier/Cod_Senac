from django.shortcuts import render
from django.http import HttpResponse

#CREATE YOUR VIEWS HERE.

def home(request):
    return (request,'home.html')

