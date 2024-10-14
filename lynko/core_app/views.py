from django.shortcuts import render
from django.http import request


def index(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


def pricing(request):
    return render(request, 'core/pricing.html')
