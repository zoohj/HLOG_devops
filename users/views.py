from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from users.forms import PasswordResetForm, UserForm


def logout_view(request):
    logout(request)
    return redirect('list')

def signup_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid(): 
            form.save() # User생성?
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) #사용자 인증
            login(request, user) #로그인
            return redirect('list')
    else: #GET인 경우
        form = UserForm()
    return render(request, 'users/signup.html', {'form':form})

class PasswordResetView(auth_views.PasswordResetView):
    """
    비밀번호 초기화 - 사용자ID, email 입력 
    Form 유효한지 확인하는 듯 -> overiding
    """
    template_name= 'users/password_reset.html'
    form_class= PasswordResetForm

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    """
    비밀번호 초기화 - 메일 전송 완료
    """
    template_name='users/password_reset_done.html'

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    """
    비밀번호 초기화 - 새로운 비밀번호 입력
    """
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:  login')