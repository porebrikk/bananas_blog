from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='blog/images/')
    created_at = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = TaggableManager(blank=True)

    def __str__(self):
        return self.title