from django.shortcuts import render
from .forms import CarForm

# Create your views here.

# display home page html 
def get_home_page(request):
    
    return render(request ,'cars/home.html')

# add car function  
def add_car(request):
    if request.method == 'POST':
        car_data = CarForm(request.POST, request.FILES)
        print(car_data.errors)
        if car_data.is_valid():
            car_data.save()
    else:
        car_data = CarForm()
        
    return render(request,'cars/addcar.html',{'carForm':car_data})