from django.shortcuts import render

# Create your views here.

def get_home_page(request):
    
    return render(request ,'cars/home.html')