from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.core.exceptions import ValidationError
# from django.http import HttpResponseRedirect
# from django.urls import reverse
import django.contrib.auth.forms as auth_forms

# import django.contrib.auth.forms as auth_forms


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

class PasswordResetForm(PasswordResetForm):

    username = auth_forms.UsernameField(label="사용자ID")  

    # STEP 1. username과 일치하는 User 존재하는지
    def clean_username(self):
        data= self.cleaned_data['username']
        if not User.objects.filter(username=data).exists():
            raise ValidationError("해당 사용자 ID가 존재하지 않습니다.")
        return data

    # STEP 2. usenrname과 일치하는 User의 email과 입력받은 email 동일한지
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if username and email:
            if User.objects.get(username=username).email != email:
                raise ValidationError("사용자의 이메일 주소가 일치하지 않습니다")


    def get_users(self, email=''):
        active_users = User.objects.filter(**{
            'username__iexact': self.cleaned_data["username"],
            'is_active': True,
        })
        return (
            u for u in active_users
            if u.has_usable_password()
        )