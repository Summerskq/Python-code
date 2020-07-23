from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("图书管理系统")

# Create your views here.
