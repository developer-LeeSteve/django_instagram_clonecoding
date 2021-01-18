from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, FormView
from django.core.mail import EmailMessage
from django.contrib.auth import login, authenticate, logout
from django.template.loader import render_to_string
# from django.contrib.messages import messages

from accounts.forms import CustomUserCreationForm, CustomLoginForm, EmailVerificationForm
from accounts.models import *
from accounts.custom_methods import email_verification_code, send_mail
from accounts.decorators import custom_login_required

from posts.models import Post


# 회원가입 View
class UserRegisterView(CreateView):
	model = User
	form_class = CustomUserCreationForm
	template_name = 'accounts/register.html'

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.is_active = False
		self.object.save()
		send_mail(
			subject=f'{self.object.code} is your Instagram code',
			recipient_list=[self.object.email],
			html=render_to_string('accounts/register_email.html', {
				'email':self.object.email,
				'code':self.object.code,
			})
		)
		return redirect('accounts:email_verification_code')


# 로그인 View
class LoginView(FormView):
	form_class = CustomLoginForm
	template_name = 'accounts/login.html'
	success_url = '/'

	def form_valid(self, form):
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		user = authenticate(self.request, username=email, password=password)

		if user is not None:
			login(self.request, user)
		return super().form_valid(form)


# 이메일 인증번호 입력 View
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

# 로그아웃
def logoutUser(request):
	logout(request)
	return redirect('accounts:login')

def RegisterEmail(request):
	return render(request, 'accounts/register_email.html')

@custom_login_required
def inbox(request):
	return HttpResponse('inbox')

@custom_login_required
def explore(request):
	return HttpResponse('explore')

@custom_login_required
def activity(request):
	return HttpResponse('activity')

@custom_login_required
def index(request):
	posts = Post.objects.all()
	context = {'posts': posts}
	return render(request, 'index.html', context)

@custom_login_required
def profile(request, username):
	objects = [user.username for user in User.objects.all()]
	if username not in objects:
		return redirect("accounts:index")
	context = {'username': username}
	return render(request, 'profile.html', context)