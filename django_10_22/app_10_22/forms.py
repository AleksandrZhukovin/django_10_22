from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Task


class Form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.IntegerField()
    adress = forms.CharField()
    photo = forms.FileField()
    date = forms.DateField(widget=forms.SelectDateWidget())


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ProjectForm(forms.Form):
    name = forms.CharField()


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'status', 'deadline', 'number']
        widgets = {'text': forms.TextInput(attrs={'id': 'text'}),
                   'status': forms.ChecboxInput(attrs={'id': 'status'}),
                   'deadline': forms.DateInput(attrs={'id': 'deadline'}),
                   'number': forms.NumberInput(attrs={'id': 'number'})}


class TestForm(forms.Form):
    name = forms.CharField()

