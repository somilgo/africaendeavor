from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		exclude = []
	def clean(self):
		return self.cleaned_data

class LogIn(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput, label="Password")
	def clean(self):
		password = self.cleaned_data.get("password")
		if password=="african21connection":
			pass
		else:
			raise forms.ValidationError("WRONG PASSWORD")
		return self.cleaned_data
