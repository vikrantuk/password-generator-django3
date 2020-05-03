from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))
    thepd = ""

    if(request.GET.get('uppercase')):
        li = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        thepd+= random.choice(li)
        length -= 1
        characters.extend(li)


    if(request.GET.get('special')):
        li = list('!@#$%^&*()')
        thepd+= random.choice(li)
        length -= 1
        characters.extend(li)

    if(request.GET.get('numbers')):
        li = list('0123456789')
        thepd+= random.choice(li)
        length -= 1
        characters.extend(li)



    for _ in range(length):
        thepd += random.choice(characters)


    return render(request, 'generator/password.html', {'password':thepd})

def about(request):
    return render(request, 'generator/about.html')
