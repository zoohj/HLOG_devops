
from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields= ['title', 'content'] #PostBaseForm에서 사용할 Post 모델의 속성
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['content']
        labels = {
            'content' : '댓글내용',
        }