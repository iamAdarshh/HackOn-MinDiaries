from django.db import models
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextUploadingField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title + ' | ' + str(self.author)