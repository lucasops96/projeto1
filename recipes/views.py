from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'recipes/home.html', context={
        'name':'Miguel Santos'
    })

def sobre(request):
    return HttpResponse('Sobre do User')

def contato(request):
    return HttpResponse('Contato do User')