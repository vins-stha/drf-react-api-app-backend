from django.shortcuts import render
from .models import Category,Product
from django.http import HttpResponse,HttpResponseBadRequest, request

def index(request):
    return HttpResponse('it works!!')



# Create your views here.
