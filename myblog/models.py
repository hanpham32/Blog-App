from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.ForeignKey(Tag, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    preview = models.CharField(max_length=255, default='')
    body = RichTextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')