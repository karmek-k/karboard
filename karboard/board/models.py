from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title


class Reply(models.Model):
    content = models.TextField()
    parent = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
