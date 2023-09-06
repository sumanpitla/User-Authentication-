from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages




def home(request):
    return render(request, 'home.html',{'name':'suman'})
def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2
    return render(request,'result.html',{'result':res})    
