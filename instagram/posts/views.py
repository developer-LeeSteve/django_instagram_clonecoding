from django.shortcuts import render, redirect
from django.http import HttpResponse

from accounts.decorators import custom_login_required
from posts.forms import CreatePostForm
from posts.models import Post

@custom_login_required
def post_create(request):
	if request.method == "POST":
		form = CreatePostForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.nickname = request.user.username
			instance.save()
			return redirect("accounts:index")
	form = CreatePostForm()
	context = {"form":form}
	return render(request, 'posts/post_create.html', context)