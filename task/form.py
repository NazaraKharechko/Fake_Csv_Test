from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)


class Save_Schemas_Form(forms.Form):
    ful_name = forms.CharField(widget=forms.TextInput)
    job = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.EmailInput)
    phone = forms.CharField(widget=forms.NumberInput)
    description = forms.CharField(widget=forms.TextInput)
    date = forms.CharField(widget=forms.DateInput)
