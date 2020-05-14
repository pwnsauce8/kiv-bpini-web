from django import forms

from .models import *


class TaskForm(forms.ModelForm):
	first_word = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'input'}))

	class Meta:
		model = Subtitle
		fields = 'select_model', 'first_word', 'select_genre'
		# fields = '__all__'
