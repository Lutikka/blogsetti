import datetime

from django.db import models
from django.utils import timezone

class Blogpost(models.Model):
    
    title = models.CharField(max_length=255)
    
    body_text = models.TextField()
    
    pub_date =  models.DateTimeField('date published')
    
    def __str__(self):
		
        return self.title
        
    def was_published_recently(self):
		
        now = timezone.now()
        
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Comment(models.Model):
    
    blogpost = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    
    commentee = models.CharField(max_length=100, default='')
    
    comment_text = models.TextField()
    
    pub_date =  models.DateTimeField('date published')
    
    votes = models.IntegerField(default=0)
    
    def __str__(self):
		
        return self.comment_text
        
    def was_published_recently(self):
		
        now = timezone.now()
        
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
