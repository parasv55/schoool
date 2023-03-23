from dataclasses import field
from django import forms
from .models import AuthUser, Demo

class UserloginForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ('email', 'password', 'image')
        #fields = "__all__"
        # exclude = ('demo', "demo1")
        
        # exclude = ('is_blogger', 'is_useradmin')

class DemoForm(forms.ModelForm):
    class Meta:
        model = Demo
        fields = '__all__'