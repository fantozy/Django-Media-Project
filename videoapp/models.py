import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    file = models.FileField(
    upload_to='video/',
    validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title    

class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField(max_length=200)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name


class Like(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Dislike(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='dislikes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    
