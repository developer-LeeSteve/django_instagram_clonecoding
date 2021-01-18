from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings

def custom_login_required(view_func):
	def wrap_func(request, *args, **kwargs):
		if not request.user.is_authenticated:
			messages.info(request, "로그인하지 않으면 이용하실 수 없습니다.")
			return redirect('accounts:login')
		else:
			return view_func(request, *args, **kwargs)
		return view_func(request, *args, **kwargs)
	return wrap_func

# def already_logged_in(view_func):
# 	if request.user.is_authenticated:
# 		return redirect('')

# def not_blocked_requried(view_func):
# 	def wrap_func(request, *args, **kwargs):
# 		if not request.user 