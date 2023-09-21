
from django import forms
from .models import Section_class  # Import the Section model from your app

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section_class
        fields = ['section_name', 'class_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['class_name'].widget.attrs['multiple'] = True
        # You can add any additional form customization here, if needed.
