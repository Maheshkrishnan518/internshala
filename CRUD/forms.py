
from django import forms
from .models import Crud
class CrudForm(forms.ModelForm):
    class Meta:
        model = Crud
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }