from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from accounts.decorators import custom_login_required
from accounts.models import User

@custom_login_required
def index(request):
	return render(request, 'index.html')

@custom_login_required
def profile(request, username):
	objects = [user.username for user in User.objects.all()]
	if username not in objects:
		raise Http404("No Page Found")
	context = {'username': username}
	return render(request, 'profile.html', context)