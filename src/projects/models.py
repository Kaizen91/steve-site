from django.db import models


class Project(models.Model):
    git_repo = models.URLField()
    jupyter_notebook = models.URLField(blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(default=None)

    def __str__(self):
        return self.title
