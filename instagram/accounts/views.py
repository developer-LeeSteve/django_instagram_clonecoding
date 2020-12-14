from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, FormView
from django.core.mail import EmailMessage
from django.contrib.auth import login, authenticate, logout

from accounts.forms import CustomUserCreationForm, CustomLoginForm
from accounts.models import *

class UserRegisterView(CreateView):
	model = User
	form_class = CustomUserCreationForm
	template_name = 'accounts/register.html'

	# def get_success_url(self):
	# 	return redirect('accounts:login')

	def form_valid(self, form):
		self.object = form.save()
		return redirect('accounts:login')

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

def logoutUser(request):
	logout(request)
	return redirect('accounts:login')

def index(request):
	return render(request, 'accounts/index.html')