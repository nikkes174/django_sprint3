from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Category, Post


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('pub_date')[:5]
    context = {'posts': post_list}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category, is_published=True,
                                 slug=category_slug)
    posts_list = category.posts.filter(
        is_published=True,
        pub_date__lte=timezone.now
    ).order.by('pub_date')
    context = {
        'category': category,
        'posts': posts_list
    }
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        pub_date__lte=timezone.now(),
        category__is_published=True,
        id=id
    )
    context = {'post': post}
    return render(request, template, context)
