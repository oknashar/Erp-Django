from django import forms
from .models import Employe,Absense
class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields= '__all__'
