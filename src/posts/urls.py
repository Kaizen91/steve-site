from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path("", views.index, name="blog"),
    path("<int:post_id>/", views.post, name="post"),
    path("<str:category>/", views.index, name="category")
]
