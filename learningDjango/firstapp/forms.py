from django import forms
from .models import Firstapp


class FirstappForm(forms.Form):
    first_app = forms.ModelChoiceField(queryset=Firstapp.objects.all(),label='First App')
    # first_app = forms.CharField()
