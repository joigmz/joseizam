from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import os


# Create your views here.
def index(request):
    return render(request, "index.html")

def project(request):

    return render(request, "proyecto.html")