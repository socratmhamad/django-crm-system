from django import forms
from .models import Record
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput,TextInput
#register user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2']
        
        
        

#login

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)        
    
    
#Record form

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record 
        fields  = ['first_name','last_name','phone','Category','tall','wedight','address']
        
        
  