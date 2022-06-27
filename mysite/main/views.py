from django.shortcuts import render
from .models import Shoes
from django.http import HttpResponse


def index(request):
    shoes = Shoes.objects.order_by('-price')
    title = 'Список обуви'
    desc = 'Список обуви в базе данных '
    return render(request, 'main.html', {'title': title, 'desc': desc, 'shoes': shoes})


def about(request):
    render(request, 'about.html')


def contacts(request):
    render(request, 'contacts.html')


def new_shoes(request):
    render(request, 'new_shoes.html')


def most_popular(request):
    render(request, 'most_popular')

# Create your views here.
