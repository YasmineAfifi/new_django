from django.shortcuts import render

# Create your views here.

def register(request):
    
    return render(request,'user_auth/register.html')

def get_login(request):
    
    return render(request,'user_auth/login.html')
