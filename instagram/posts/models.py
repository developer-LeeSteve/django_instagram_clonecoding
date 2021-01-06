from django.db import models

from accounts.models import User
from accounts.custom_methods import customSlugify

# Class for Creating Posts
class Post(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(allow_unicode=True)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.png', blank=True)
	author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

	def snippet(self):
		if len(self.body) <= 50:
			return self.body[:50]
		else:
			return self.body[:50] + '...'

	def save(self, *args, **kwargs):
		self.slug = customSlugify(self.author, self.title)
		super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.title
