from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

@login_required(login_url='login')
def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('home')
    return render(request, 'blog/add_post.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # کاربر پس از ثبت نام وارد می‌شود
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})