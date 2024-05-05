#post_create, post_modify, post_delete

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from ..models import Hashtag, Post
from ..forms import PostForm



@login_required(login_url='users:login')
def post_create_view(request):
    '''게시글 등록'''
    if request.method == 'POST':
        form = PostForm(request.POST) #request.POST의미:화면에서 사용자가 입력한 니용
        if form.is_valid():
            post = form.save(commit=False) #임시 저장(commit=False)하여 post 객체를 리턴 받음
            post.author = request.user #author 속성에 로그인 계정 저장
            post.created_at = timezone.now() #실제 저장을 위해 작성일시 설정/ 저장시점에 생성해야하므로 form으로 등록하지 않음
            post.save() #데이터 실제로 저장
            return redirect('posts:list')
    else:
        form = PostForm()
    context ={'form':form}
    return render(request, 'posts/post_form.html', context)

@login_required(login_url='users:login')
def post_modify_view(request, post_id):
    '''게시글 수정'''
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect ('posts:detail', post_id=post.id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.modified_at = timezone.now()
            post.save()
            return redirect('posts: detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    context = {'form':form}
    return render(request, 'posts/post_form.html', context)

@login_required(login_url='users/login')
def post_delete_view(request, post_id):
    post= get_object_or_404(Post, pk= post_id)
    if request.user != post.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('posts:detail', post_id=post.id)
    post.delete()
    return redirect('posts:list')

@login_required(login_url='users:login')
def post_like_view(request, post_id):
    post= get_object_or_404(Post, pk=post_id)
    if request.user == post.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        if request.user in post.likes.all():
            post.likes.remove(request.user) #취소 기능 구현 필요(중복 추천은 막아줌)
        else:
            post.likes.add(request.user) 
    return redirect('posts:detail', post_id=post.id)

@login_required
def hashtag(request, hash_id):
    hashtag = get_object_or_404(Hashtag, pk=hash_id)
    posts = hashtag.post.order_by('-pk')
    context = {
        'hashtag': hashtag, 
        'posts': posts,
    }
    return render(request, 'movies/hashtag.html', context)