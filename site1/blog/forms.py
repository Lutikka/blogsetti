from django.db import models
from django.forms import ModelForm, Textarea
from django.core.exceptions import NON_FIELD_ERRORS
from .models import Comment

class CommentForm(ModelForm):
	
	class Meta:
		
		model = Comment
		fields = ['commentee', 'comment_text']
		widgets = {
			'comment_text': Textarea(attrs={'cols': 40, 'rows': 4}),
		}
