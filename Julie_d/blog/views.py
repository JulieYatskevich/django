from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import PostForm, RegisterUserForm
from .models import Post


def blog_home(request):
    post = Post.objects.all()
    return render(request, 'blog/blog_home.html', {'post': post})


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    form = PostForm()
    data = {
        'form':
        form
    }
    return render(request, 'blog/create.html', data)


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.success(request, ('Пользователь не найден'))
            return redirect('login_user')
    else:
        return render(request, 'blog/login_user.html')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, ('Вы зарегистрировались'))
            return redirect('main')
    else:
        form = RegisterUserForm()
    return render(request, 'blog/register_user.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.warning(request, 'Logout')
    return redirect('main')
