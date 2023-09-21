from django import forms
from .models import SchoolClasses

class SchoolClassesForm(forms.ModelForm):
    class Meta:
        model = SchoolClasses
        fields = ['class_name']
    