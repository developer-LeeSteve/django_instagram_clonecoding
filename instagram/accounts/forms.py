from django import forms
from django.contrib.auth.hashers import check_password

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

class CustomLoginForm(forms.Form):
	email = forms.CharField(
		widget=forms.EmailInput(attrs={'class':'form-control'}),
		error_messages={'required':'이메일을 입력해주세요.'},
		label='email')
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={'class':'form-control'}),
		error_messages={'required':'비밀번호를 입력해주세요.'},
		label='password')

	def clean(self):
		cleaned_data = super().clean()
		email = cleaned_data.get('email')
		password = cleaned_data.get('password')

		if email and password:
			try:
				user = User.objects.get(email=email)
			except User.DoesNotExist:
				self.add_error('사용자가 존재하지 않습니다.')
			if not check_password(password, user.password):
				self.add_error('비밀번호가 틀렸습니다.')