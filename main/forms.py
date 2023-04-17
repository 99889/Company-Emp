from django import forms
from main.models import Employee

class EmployeeForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())
