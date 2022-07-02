from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=32, widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': '用户名/邮箱'
    }))
    password = forms.CharField(label='密码', max_length=18, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': '密码'
    }))


    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username == password:
            raise forms.ValidationError('密码不能与用户名一样！')
        return password


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='邮箱', min_length=6, widget=forms.EmailInput(attrs={
        'class': 'input', 'placeholder': '用户名/邮箱'}))
    password = forms.CharField(label='密码', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': '密码'}))
    password1 = forms.CharField(label='再次输入密码', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': '再次输入密码'}))

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean_email(self):
        """验证用户是否存在"""
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(username=email).exists()
        if exists:
            raise forms.ValidationError("用户名已经存在！")
        return email

    def clean_password1(self):
        """验证两次密码是否一致"""
        data = self.cleaned_data
        password = data['password']
        password1 = data['password1']
        if password != password1:
            raise forms.ValidationError('两次输入的密码不一致，请修改!')
        return password


class ForgetPwdForm(forms.Form):
    """ 填写邮箱地址表单 """
    email = forms.EmailField(label='请输入注册邮箱地址', min_length=4, widget=forms.EmailInput(attrs={
        'class': 'input', 'placeholder': '用户名/邮箱'
    }))

class ModifyPwdForm(forms.Form):
	"""Form definition for UserProfile."""
	password = forms.CharField(label='输入新密码', min_length=6, 
		widget=forms.PasswordInput(attrs={'class':'input', 'placeholder':'输入新密码'}))


class UserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input',        #    'disabled':'disabled'
    }))

    class Meta:
        model = User
        fields = ('email',)


class UserProfileForm(forms.ModelForm):
    """Form definition for UserInfo."""
 
    class Meta:
        """Meta definition for UserInfoform."""

        model = UserProfile
        fields = ('nike_name','desc', 'gexing', 'birthday',  'gender', 'address', 'image')

