
from .models import Blogpost, Comment
from django.utils import timezone

import datetime

#~ published in last x days
def recent_posts(request):
	
	x = 3
	
	now = timezone.now()
	
	recent_p = Blogpost.objects.filter( pub_date__gt = now - datetime.timedelta(days=x), pub_date__lt = now).order_by('-pub_date')[:3]
	
	return {
		'recent_posts': recent_p,
	}
