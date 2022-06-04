from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateTimeInput, ModelForm, Textarea, TextInput
from new_user.models import User

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'date']

        widgets = {
           "title": TextInput(attrs={
               'class': 'form-control',
               'placeholder': "Название поста"    
           }),
           "date": DateTimeInput(attrs={
               'class': 'form-control',
               'placeholder': "Дата: Месяц число, год"
           }),
           "text": Textarea(attrs={
               'class': 'form-control',
               'placeholder': "Текст"
           })
        }


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
