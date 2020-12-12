from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import *

class CustomUserCreationForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CustomUserCreationForm, self).__init__(*args, **kwargs)

		self.fields['email'].label = 'email'
		self.fields['email'].widget.attrs.update({
			'class': 'form-control',
			'placeholder': '이메일 주소',
			})

		self.fields['name'].label = 'name'
		self.fields['name'].widget.attrs.update({
			'class': 'form-control',
			'placeholder': '성명',
			})

		self.fields['username'].label = 'username'
		self.fields['username'].widget.attrs.update({
			'class': 'form-control',
			'placeholder': '사용자 이름',
			})

		self.fields['password'].label = 'password'
		self.fields['password'].widget.attrs.update({
			'class': 'form-control',
			'placeholder': '비밀번호',
			})

		self.fields['date_of_birth'].label = 'date_of_birth'
		self.fields['date_of_birth'].widget.attrs.update({
			'class': 'form-control',
			})

	class Meta:
		model = User
		fields = ['email', 'name', 'username', 'password', 'date_of_birth']

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password"])
		user.save()
		return user