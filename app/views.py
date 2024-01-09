from django.shortcuts import render

# Create your views here.

from app.forms import *
from django.http import HttpResponse
from app.models import *

def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO' : ETFO}

    if request.method=='POST':
        TFDO = TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse ('Data is Inserted')
    return render(request,'insert_topic.html',d)

def insert_webpage (request):
    EWFO=WebForm()
    d={'EWFO' : EWFO }

    if request.method=='POST':
        WFDO=WebForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse ('Web data is Inserted!!!')
    return render (request,'insert_webpage.html',d)

def insert_accessrecord (request):
    EAFO=AccessForm()
    d={'EAFO' : EAFO}

    if request.method=='POST':
        WAFO=AccessForm(request.POST)

        if WAFO.is_valid():
            WAFO.save()
            return HttpResponse ('AccessRecord data is Inserted!!!')

    return render(request,'insert_accessrecord.html',d)