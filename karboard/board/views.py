from django.shortcuts import render, redirect, get_object_or_404

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
    response_post = get_object_or_404(Post, pk=post_id)
    replies = response_post.reply_set.all()
    context = {
        'post': response_post,
        'replies': replies
    }
    return render(request, 'view_post.html', context)
