
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context, RequestContext
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views.decorators.http import require_http_methods

from .models import Blogpost, Comment
from .forms import CommentForm

@require_http_methods(["GET"])
def index(request):
	
	latest_blog_list = Blogpost.objects.order_by('-pub_date')[:6]
	
	
	return render(request, 'blog/index.html',
	{'latest_blog_list': latest_blog_list,}, RequestContext(request))
	
@require_http_methods(["GET", "POST" ])
def detail(request, blogpost_id): 
	
	blogpost = get_object_or_404(Blogpost, pk=blogpost_id)
	#quick solution, probably not the best
	ordered_comment_list = Comment.objects.filter(blogpost__id=blogpost_id).order_by('-pub_date')
	
	c = Context({
			
			'blogpost': blogpost,
			'form': CommentForm(),
			'ordered_comment_list': ordered_comment_list,
			
			})
	
	if request.method == 'POST':
		
		f = CommentForm(request.POST)
		
		try:
			
			new_comment = f.save(commit=False)
			
		except (ValueError):
			
			#return to commenting form with error message
			
			return render(request, 'blog/detail.html', c)
			
		else:
			
			#save the comment
			
			new_comment.pub_date = timezone.now()
			new_comment.blogpost = blogpost
			new_comment.votes = 0
			new_comment.save()

			return HttpResponseRedirect(reverse('blog:detail',args=(blogpost_id,)))
			
	else: #reques.method == 'GET'
		
											 # , ,specific context, global context
		return render(request, 'blog/detail.html', c,RequestContext(request))
	
	
	
	
	
