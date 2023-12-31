import datetime
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField("date published")
    text = RichTextField(blank=True, null=True)
    #text = models.TextField()
    topics = models.ManyToManyField(Topic, related_name="posts")

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
    text = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text



