from django import forms
from django.forms import ModelForm
from .models import Agenda

class AgendaForm(forms.ModelForm):
	name = forms.CharField(max_length=50, widget=forms.TextInput(
		attrs = {
			'class': 'form-control'
		}
	))
	firstname = forms.CharField(max_length=50, widget=forms.TextInput(
		attrs = {
			'class': 'form-control'
		}
	))
	telephone = forms.CharField(max_length=50, widget=forms.TextInput(
		attrs = {
			'class': 'form-control'
		}
	))

	class Meta:
		model = Agenda
		fields = ('name', 'firstname', 'telephone')
