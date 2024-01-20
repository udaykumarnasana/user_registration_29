from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *


def registration(request):
    ufo=userform()
    pfo=profileform()
    d={'user':ufo,'profile':pfo}
    return render(request,'registration.html',d)
