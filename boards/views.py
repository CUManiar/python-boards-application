from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home Page')


def index(request):
    return HttpResponse('index.html Page')
