"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from posts.views import base_views

from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_views.post_list_view, name='list'),
    path('posts/', include('posts.urls', namespace='posts')),
    path('users/', include('users.urls', namespace='users')),
    
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # 추가
    path('reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # 추가

    # path('password-reset/',
    #     auth_views.PasswordResetView.as_View(
    #         template_name='users/password_reset.html'
    #     ),
    #     name = 'password_reset')
]
