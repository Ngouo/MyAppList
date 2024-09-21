from django import forms
from .models import Task


class FormTask(forms.ModelForm):
  tache = forms.CharField(max_length=2000, widget=forms.TextInput(attrs={
    'placeholder': 'Entrez votre tache',
    'class': 'form-control-lg', 
  }))
  
  class Meta:
    model = Task
    fields = [
      'tache',
    ]