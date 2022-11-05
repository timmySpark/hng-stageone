from django import forms
from api.models import *

class AritForm(forms.ModelForm):
    class Meta:
        model = arit
        fields = '__all__'
