from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('posts/', include("posts.urls")),
    path('projects/', include("projects.urls")),
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('resume/', views.resume, name="resume"),
    path('admin/', admin.site.urls),
]
