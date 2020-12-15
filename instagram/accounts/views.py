from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, FormView
from django.core.mail import EmailMessage
from django.contrib.auth import login, authenticate, logout

from accounts.forms import CustomUserCreationForm, CustomLoginForm, EmailVerificationForm
from accounts.models import *
from accounts.custom_methods import email_verification_code
# from accounts.custom_methods import 

# 회원가입
class UserRegisterView(CreateView):
	model = User
	form_class = CustomUserCreationForm
	template_name = 'accounts/register.html'

	# def get_success_url(self):
	# 	return redirect('accounts:login')

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.is_active = False
		self.object.save()
		return redirect('accounts:login')

# 로그인
class LoginView(FormView):
	form_class = CustomLoginForm
	template_name = 'accounts/login.html'
	success_url = '/accounts/index/'

	def form_valid(self, form):
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		user = authenticate(self.request, username=email, password=password)

		if user is not None:
			login(self.request, user)
		return super().form_valid(form)

class EmailVerificationView(FormView):
	form_class = EmailVerificationForm
	template_name = 'accounts/email_verification_code.html'
	success_url = '/accounts/login/'

	def form_valid(self, form):
		email = form.cleaned_data.get('email')
		code = form.cleaned_data.get('code')
		user = User.objects.get(email=email)
		if user.code == code:
			user.is_active = True
			user.save()
		return super().form_valid(form)

def logoutUser(request):
	logout(request)
	return redirect('accounts:login')

def index(request):
	return render(request, 'accounts/index.html')