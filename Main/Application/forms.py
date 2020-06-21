from django.forms import ModelForm
from .models import Content

class Meme(ModelForm):
	class Meta:
		model = Content
		fields = [
			 "img", "caption" ,"type_meme"
		]