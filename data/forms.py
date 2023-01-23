from django import forms
from .models import Employee
from django.forms import ModelForm

class employee_create(ModelForm):
    class Meta:
        model= Employee
        fields='__all__'