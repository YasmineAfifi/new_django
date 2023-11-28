from django import forms
from .models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        widgets ={
            'name':forms.TextInput(attrs={"class":"registerInputs",'placeholder': 'Your Full Name'}),
            'email':forms.EmailInput(attrs={'class':'registerInputs','placeholder': 'Email'}),
            'password':forms.PasswordInput(attrs={'class':'registerInputs','placeholder': 'Password'})
        }
        
    # def __init__(self, *args, **kwargs):
    #     super(RegisterForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.required = False