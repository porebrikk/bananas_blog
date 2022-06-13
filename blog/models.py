from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(blank=True)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='blog/images/')
    created_at = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title