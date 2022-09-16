from .models import UserProfile

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Django's UserCreationForm allows us to easily configure a form to handle sign-ups. 
class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Your first name'}))
    last_name = forms.CharField(max_length=30, required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Your last name'}))
    username = forms.EmailField(max_length=50, required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    password1 = forms.CharField(max_length=50, required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'password'}))
    username = forms.EmailField(max_length=50, required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    #ReCaptcha token
    token = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)


# Django's AuthenticationForm methods handle user authentication
class AuthForm(AuthenticationForm): 
    username = forms.EmailField(max_length=50, required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=50, required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'password'}))

    class Meta:
        models = User
        fields = ('username', 'password',)


class UserProfileForm(forms.ModelForm):
	address = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	town = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	county = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	post_code = forms.CharField(max_length=8, required=True, widget = forms.HiddenInput())
	country = forms.CharField(max_length=40, required=True, widget = forms.HiddenInput())

	longitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())
	latitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())

	class Meta:
		model = UserProfile
		fields = ('address', 'town', 'county', 'post_code',
		 'country', 'longitude', 'latitude')