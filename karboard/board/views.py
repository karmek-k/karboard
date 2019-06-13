from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.order_by('-id')[:10]
    return render(request, 'home.html', {'posts': posts})


def post(request):
    return render(request, 'post.html')


def submit_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('home')
