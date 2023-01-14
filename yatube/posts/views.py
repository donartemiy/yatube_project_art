from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Group, User, Comment
from .forms import PostForm, CommentForm

COUNT_POSTS = 10


def paginator(request, query_set):
    paginator = Paginator(query_set, COUNT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def index(request):
    posts = Post.objects.all()

    page_obj = paginator(request, posts)
    context = {'page_obj': page_obj, 'post': posts}
    template = 'posts/index.html'
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts_rname.all()

    page_obj = paginator(request, posts)
    context = {'group': group, 'page_obj': page_obj}
    template = 'posts/group_list.html'
    return render(request, template, context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts_user = author.posts_rname.all()

    page_obj = paginator(request, posts_user)
    context = {
        'author': author,
        'page_obj': page_obj,
        'paginator': paginator
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST or None, files=request.FILES or None)
    comments = Comment.objects.filter(post=post)
    # print(f'{request.user} request.user.is_authenticated: {request.user.is_authenticated}')
    if request.user.is_authenticated:
        context = {
            'post': post,
            'post_id': post_id,
            'form': form,
            'comments': comments,
            'user': request.user
        }
    else:
        context = {
            'post': post,
            'post_id': post_id,
            'comments': comments,
            'user': request.user
        }
    return render(request, 'posts/post_detail.html', context)

@login_required
def post_create(request):
    form = PostForm(request.POST or None, files=request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts:profile', new_post.author)
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(request.POST or None, files=request.FILES or None, instance=post)
    if request.user != post.author:
        return redirect('posts:post_detail', post_id=post_id)
    if request.method == 'POST' and form.is_valid():
        post.author = request.user
        form.save()
        return redirect('posts:post_detail', post_id=post_id)
    is_edit = True
    context = {
        'form': form,
        'is_edit': is_edit,
        'post_id': post_id
    }
    return render(request, 'posts/create_post.html', context)

@login_required
def add_comment(request, post_id):
    """Функция вызывается из шаблона comment.html"""
    post = get_object_or_404(Post, pk=post_id)
    # Получите пост и сохраните его в переменную post.
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('posts:post_detail', post_id=post_id)
