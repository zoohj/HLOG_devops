from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Hashtag(models.Model):
    category = models.TextField(unique=True)

    def __str__(self):
        return self.content

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_post')
    title = models.CharField(max_length=50, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='likes_post') #추천인 추가

    def __str__(self):
        return self.title
    
    hashtags = models.ManyToManyField(Hashtag, blank=True, related_name='hash_post')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='') #외래키 설정
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='likes_comment') #추천인 추가


# class Reply(models.Model):
#     comment= models.ForeignKey(to='Comment', on_delete=models.CASCADE, default='') #외래키 설정
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)