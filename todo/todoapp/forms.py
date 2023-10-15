from django.forms import ModelForm
from .models import Todo, Priority
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from bootstrap_datepicker_plus.widgets import DatePickerInput, DateTimePickerInput


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "task_description", "start_date", "due_date"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter task title"}),
            "task_description": forms.Textarea(
                attrs={"class": "form-control", "rows": "4", "placeholder": "Enter task description", }),
            "start_date": DateTimePickerInput(options={"showTodayButton": True, "showClear": True, "showClose": True}, attrs={"class": "form-control dbdp", "placeholder": "Start Date"}),
            "due_date": DatePickerInput(options={ "showTodayButton": True, "showClear": True, "showClose": True}, attrs={"class": "form-control dbdp" ,"placeholder": "Task Due Date" }),

        }


class PriorityForm(ModelForm):
    class Meta:
        model = Priority
        fields = ["priority"]


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Username"}))
    # email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": "Password"}))
