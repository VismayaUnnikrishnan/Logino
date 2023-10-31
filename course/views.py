from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
@login_required
def frontpage(request):
    all=Course.objects.all()
    return render(request,'accounts/index.html',{'data':all})

def Short(request):
    all=Course.objects.filter(category="Short")
    return render(request,'accounts/short.html',{'data':all})