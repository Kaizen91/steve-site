from django.shortcuts import render
from posts.models import Post


def index(request):
    latest_post_list = Post.objects.order_by("-date")[:5]
    context = {
            "latest_post_list": latest_post_list,
            }
    return render(request, "index.html", context)


def contact(request):
    context = {}
    return render(request, "contact.html", context)


def resume(request):
    context = {}
    return render(request, "resume.html", context)
