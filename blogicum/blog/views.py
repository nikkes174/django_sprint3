from django.shortcuts import get_object_or_404, render
from blog.models import Post, Category

from .constants import NUMBER_OF_POSTS


def index(request):
    post_list = Post.objects.published().published_category()[:NUMBER_OF_POSTS]
    context = {'post_list': post_list}
    template = 'blog/index.html'
    return render(request, template, context)


def post_detail(request, id):
    post = get_object_or_404(
        Post.objects.published().published_category(),
        id=id
    )
    context = {'post': post}
    template = 'blog/detail.html'
    return render(request, template, context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        is_published=True,
        slug=category_slug)
    post_list = (Post.objects.published()
                 .published_category()
                 .by_category(category_slug))
    context = {'category': category, 'post_list': post_list}
    template = 'blog/category.html'
    return render(request, template, context)
