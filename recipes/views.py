from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse('Bem vindo a Home')

def sobre(request):
    return HttpResponse('Sobre do User')

def contato(request):
    return HttpResponse('Contato do User')