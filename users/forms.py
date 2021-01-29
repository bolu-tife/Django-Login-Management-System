# users/forms.py

from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
	first_name = forms.CharField(max_length=100, help_text='First Name')
    
	class Meta(UserCreationForm.Meta):
		fields = UserCreationForm.Meta.fields + ("email","first_name",)