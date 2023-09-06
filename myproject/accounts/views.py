from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
#from django.contrib import mesaages


# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        #print("username:",username)
        #print("possword:",password)
        user=auth.authenticate(username=username,password=password)
        #print("user:",user)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return HttpResponse("Invalid credentials") 

        
    else:
        return render(request,'login.html')
    


def register(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        email=request.POST["email"]
        password_1=request.POST["password_1"]
        password_2=request.POST["password_2"]

        if password_1==password_2:
            if User.objects.filter(username=username).exists():
                return HttpResponse("username already existed in the database")

            elif User.objects.filter(email=email).exists():
                return HttpResponse("email already exists in tha database")  
            else: 
                user=User.objects.create_user(username=username,email=email,password=password_1,first_name=first_name,last_name=last_name)
                user.save()
                print("user is created")  
                return redirect("login")
                #return HttpResponse("successfully created acoount")   
        else:
            return HttpResponse("passwords not matching")                   

    else:    
        return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
    

