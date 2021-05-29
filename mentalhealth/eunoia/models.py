from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
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

class AssessmentTest(models.Model):
    title = models.CharField(max_length=255)
    totalQuestions = models.IntegerField()
    Questions = TextField()
    totalOptions = models.IntegerField()
    Options = TextField()
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name