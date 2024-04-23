from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Thread, Post, Like
from .forms import ThreadForm, PostForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'forum/category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    threads = Thread.objects.filter(category=category)
    return render(request, 'forum/category_detail.html', {'category': category, 'threads': threads})

def thread_detail(request, category_id, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    posts = Post.objects.filter(thread=thread)
    return render(request, 'forum/thread_detail.html', {'thread': thread, 'posts': posts})

def create_thread(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.category = category
            thread.created_by = request.user
            thread.save()
            return redirect('forum/thread_detail', category_id=category_id, thread_id=thread.id)
    else:
        form = ThreadForm()
    return render(request, 'forum/create_thread.html', {'form': form, 'category': category})

def create_post(request, category_id, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.created_by = request.user
            post.save()
            return redirect('forum/thread_detail', category_id=category_id, thread_id=thread_id)
    else:
        form = PostForm()
    return render(request, 'forum/create_post.html', {'form': form, 'thread': thread})

def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user

    existing_like = Like.objects.filter(user=user, post=post).first()
    if existing_like:
        # If the user has already liked the post, toggle the like
        existing_like.is_like = not existing_like.is_like
        existing_like.save()
    else:
        # If the user hasn't liked the post, create a new like
        like = Like.objects.create(user=user, post=post, is_like=True)
    return redirect('thread_detail', category_id=post.thread.category.id, thread_id=post.thread.id)
