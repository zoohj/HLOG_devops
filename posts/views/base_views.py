#list, detail, home

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from ..models import Post

from django.db.models import Q


def home_view(request):
    return render(request, 'home.html')

def post_list_view(request):
    '''게시글 list'''
    page = request.GET.get('page','1') #페이지
    kw= request.GET.get('kw', '') #검색어
    post_list = Post.objects.order_by('-created_at')
    
    if kw:
        post_list = post_list.filter(
            Q(title__icontains=kw) |
            Q(content__icontains=kw) |
            Q(comment__content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(comment__author__username__contains=kw)
        ).distinct()
    
    paginator= Paginator(post_list, 10) #페이지당 10개씩 보여주기
    page_obj= paginator.get_page(page)

    context = {'post_list': page_obj, 'page':page, 'kw':kw}
    return render(request, 'posts/post_list.html', context)

def post_detail_view(request, post_id):
    '''게시글 detail'''
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, pk=post_id)
    context = {'post':post }
    return render(request, 'posts/post_detail.html', context)
