from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import  AuthenticationForm

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
        labels = {
            'username': 'Имя',
            'password': 'Пароль',
        }

class RefisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={}))
    exclude = ['username']

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
        labels = {
            'username':'',
        'email':'Почта',
        'first_name':'Имя',
        'last_name':'Фамилия',
        'password':'Пароль',
        'password2':'Повторите пароль',
        }
        # placeholders = {
        #     'username': 'Логин',
        #     'email': 'Электронная почта',
        #     'first_name': 'Имя',
        #     'last_name': 'Фамилия',
        #     'password': 'Пароль',
        #     'password2': 'Повтор пароля',
        # }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd['password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такоей E-mail уже сущеествует!")
        return email


