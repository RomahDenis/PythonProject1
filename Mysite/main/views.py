from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>Перевірки роботи</h4>")

def about(request):
    return HttpResponse("<h4>Pro Nas</h4>")

