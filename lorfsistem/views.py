from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context = {"item": {"name": 'blanco', 'price': 344}}
    return render(request, 'lorfsistem/index.html', context)
