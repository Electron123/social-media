from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Content(models.Model):
	img = models.ImageField(upload_to='media')
	caption = models.CharField(max_length=200)
	type_meme = models.CharField(max_length=20)
	posted = models.DateField(auto_now=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.type_meme