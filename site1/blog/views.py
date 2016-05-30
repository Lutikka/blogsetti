
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Blogpost, Comment
from .forms import CommentForm


def index(request):
	
	latest_blog_list = Blogpost.objects.order_by('-pub_date')[:6]
	
	context = {'latest_blog_list': latest_blog_list,}
	
	return render(request, 'blog/index.html', context)
	
def detail(request, blogpost_id): 
	
	blogpost = get_object_or_404(Blogpost, pk=blogpost_id)
	
	ordered_comment_list = Comment.objects.filter(blogpost__id=blogpost_id).order_by('-pub_date')
	
	if request.method == 'POST':
		
		f = CommentForm(request.POST)
		
		try:
			
			new_comment = f.save(commit=False)
			
		except (ValueError):
			
			#return to voting form with error message
			
			return render(request, 'blog/detail.html', {
			'blogpost': blogpost, 'ordered_comment_list': ordered_comment_list,})
			
		else:
			
			#save the comment
			
			new_comment.pub_date = timezone.now()
			new_comment.blogpost = blogpost
			new_comment.votes = 0
			new_comment.save()

			return HttpResponseRedirect(reverse('blog:detail',args=(blogpost_id,)))
			
	else:
		
		return render(request, 'blog/detail.html', {'blogpost': blogpost, 'form': CommentForm(), 'ordered_comment_list': ordered_comment_list,})
	
