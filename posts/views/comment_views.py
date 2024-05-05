#comment_create, comment_modify, comment_delete

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.utils import timezone

from ..models import Comment, Post
from ..forms import CommentForm



@login_required(login_url='users:login')
def comment_create_view(request, post_id):
    '''댓글 등록'''
    post= get_object_or_404(Post, pk=post_id) 
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user #author 속성에 로그인 계정
            comment.created_at = timezone.now()
            comment.post = post
            comment.save()
            # return redirect('posts:detail', post_id=post.id)
            return redirect('{}#comment_{}'.format(
                resolve_url('posts:detail', post_id=comment.post.id), comment.id))
    else:
        form = CommentForm
    context = {'post':post, 'form':form}
    return render(request, 'posts/post_detail.html', context)

@login_required(login_url='users:login')
def comment_modify_view(request, comment_id):
    '''댓글 수정'''
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages(request, '수정권한이 없습니다')
        return redirect('posts:detail', comment_id=comment.id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modified_at= timezone.now()
            comment.save()
            # return redirect('posts:detail', post_id=comment.post.id) #주의!
            return redirect('{}#comment_{}'.format(
                resolve_url('posts:detail', post_id=comment.post.id), comment.id))
    else:
        form=CommentForm(instance=comment)
    context = {'form':form}
    return render(request, 'posts/comment_form.html', context)

@login_required(login_url='users:login')
def comment_delete_view(request, comment_id):
    comment = get_object_or_404(Comment, pk= comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        comment.delete()
    return redirect('posts:detail', post_id= comment.post.id)

@login_required(login_url='users:login')
def comment_like_view(request, comment_id):
    comment= get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        if request.user in comment.likes.all():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)
    # return redirect('posts:detail', post_id = comment.post.id)
    return redirect('{}#comment_{}'.format(
        resolve_url('posts:detail', post_id=comment.post.id), comment.id))