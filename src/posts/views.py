from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Post, Topic


def index(request, category=None):
    if category:
        post_list = Post.objects.filter(topics__name=category)
    else:
        post_list = Post.objects.all().order_by("date")
    topic_list = Topic.objects.all()
    context = {
            "post_list": post_list,
            "topic_list": topic_list,
            }
    return render(request, "posts/blog.html", context)


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
            "post": post
            }
    return render(request, "posts/post.html", context)


def category(request, category):
    query_set = Post.objects.filter(topics__name=category)
    context = {
            "query_set": query_set,
            }
    return render(request, "posts/category.html", context)
