from django.shortcuts import render, redirect
from django.http import Http404
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


def view_post(request, post_id):
    try:
        response_post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404('No such post')
    return render(request, 'view_post.html', {'post': response_post})
