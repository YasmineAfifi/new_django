from django.urls import path
from . import views

urlpatterns = [
    path('home',views.get_home_page,name='home')
]
