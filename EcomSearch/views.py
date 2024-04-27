from django.http import HttpResponse
from django.shortcuts import render
import requests

def About_us(request):
    return render(request,"about_us.html")

def index(request):
   
    return render(request,"index.html")