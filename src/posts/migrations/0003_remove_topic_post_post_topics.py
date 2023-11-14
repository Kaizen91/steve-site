# Generated by Django 4.2.6 on 2023-10-28 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='topics',
            field=models.ManyToManyField(related_name='posts', to='posts.topic'),
        ),
    ]
