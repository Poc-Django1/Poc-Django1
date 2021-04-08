# \myclub_root\events\forms.py

from django import forms
from django.forms import ModelForm
from .models import Papers

class PaperForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Papers
        fields = '__all__'
