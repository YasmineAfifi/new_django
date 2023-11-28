from django.shortcuts import render
from .forms import RegisterForm
from .models import Register
from django.shortcuts import redirect
# Create your views here.

def register(request):
    if request.method == 'POST':
        user = RegisterForm(request.POST)
        if user.is_valid():
            user.save()
    else:
        user=RegisterForm()
        
    return render(request,'user_auth/register.html',{'rf':user})
            
    

def get_login(request):
    if request.method == 'POST':
        user_email   = request.POST.get('email')
        user_password= request.POST.get('password')
        data = Register.objects.filter(email=user_email,password=user_password)
        if data.exists() :
            return redirect('home')           
             
    return render(request,'user_auth/login.html')
