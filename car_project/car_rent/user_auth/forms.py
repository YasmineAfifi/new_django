from django import forms
from .models import Login



class LoginForm(forms.Form):
    class Meta:
        model = Login
        field = '__all__'