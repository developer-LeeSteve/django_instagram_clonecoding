from django.http import HttpResponse
from django.shortcuts import render, redirect

def profile(request, username):
	context = {'username': username}
	return render(request, 'posts.html', context)