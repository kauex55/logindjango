from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

# DEfine um view baseada em função
def index(resquest):
    # return HttpResponse('Olá Django - index')

    return render(resquest, 'index.html', {'titulo': 'Ultimas enquetes'})

# DEfine um view baseada em função

@login_required
def ola(resquest):
    return HttpResponse('Olá Django')