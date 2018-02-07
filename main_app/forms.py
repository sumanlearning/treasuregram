from django import forms
from django.forms import ModelForm
# inherit dari ModelForm
from .models import Treasure

class TreasureForm(forms.ModelForm):
	class Meta:
		model = Treasure
		fields = ['name','value','location','material','image']

class LoginForm(forms.Form):
	"""docstring for LoginForm"""
	username = forms.CharField(label='User Name', max_length=64)
	password = forms.CharField(widget=forms.PasswordInput())


"""
ini merupakan class yang lama, inherited dari form, 
# class TreasureForm(forms.Form):
# 	name = forms.CharField(label='Name',max_length=100)
# 	value = forms.DecimalField(label='Value',max_digits=10, decimal_places=2)
# 	material = forms.CharField(label='Material',max_length=100)
# 	location = forms.CharField(label='Location',max_length=100)
# 	img_url = forms.CharField(label='Image URL',max_length=100)
"""
"""
dibawah ini refactoring the form to inherit from ModelForm
"""