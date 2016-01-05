from django import forms

class GoodieForm(forms.Form):
	matric = forms.CharField(max_length=256)
	matric.widget = forms.TextInput(attrs={'autofocus': 'autofocus',})