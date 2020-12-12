from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from accounts.forms import CustomUserCreationForm
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

def LoginView(request):
	return render(request, 'accounts/login.html')