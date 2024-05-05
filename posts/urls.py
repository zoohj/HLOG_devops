from .views import base_views, post_views, comment_views

from django.urls import path

app_name= 'posts'

urlpatterns =[
    #base_views.py
    path('', base_views.home_view, name= 'home'),
    path('list/', base_views.post_list_view, name ='list'),
    path('<int:post_id>/', base_views.post_detail_view, name='detail'),

    #post_views.py
    path('post/create/', post_views.post_create_view, name='post_create'),
    path('post/modify/<int:post_id>/',post_views.post_modify_view ,name='post_modify'),
    path('post/delete/<int:post_id>/', post_views.post_delete_view, name='post_delete'),
    path('post/like/<int:post_id>/', post_views.post_like_view, name='post_like'),
    path('post/<int:hash_id>/hashtag/', post_views.hashtag, name='hashtag'),

    #comment_views.py
    path('comment/create/<int:post_id>/', comment_views.comment_create_view, name='comment_create'),
    path('comment/modify/<int:comment_id>/', comment_views.comment_modify_view, name='comment_modify'),
    path('comment/delete/<int:comment_id>/', comment_views.comment_delete_view, name='comment_delete'),
    path('comment/like/<int:comment_id>/', comment_views.comment_like_view, name='comment_like'),
]