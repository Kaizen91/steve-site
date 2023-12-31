from django.shortcuts import render
from django.views import generic
from django.urls import reverse

from .models import Project


class IndexView(generic.ListView):
    template_name = "projects/index.html"
    # context_object_name = "projects_list"

    def get_queryset(self):
        """Returns the list of all current projects"""
        return Project.objects.all()
