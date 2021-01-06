from django.forms import ModelForm

from posts import models

class CreatePostForm(ModelForm):
	class Meta:
		model = models.Post
		fields = ['title', 'body', 'thumb']