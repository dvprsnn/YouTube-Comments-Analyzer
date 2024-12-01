from django.db import models
from User.models import  Users
# Create your models here.
class BlogPost(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_description = models.TextField()
    blog_content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)

class Comment(models.Model):
    comment_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment_content = models.TextField()
    commented_date = models.DateTimeField(auto_now_add=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

class User(models.Model):
    user_name = models.CharField(max_length=50)
    comment_content = models.TextField()
    commented_date = models.DateTimeField(auto_now_add=True)
    commented_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)