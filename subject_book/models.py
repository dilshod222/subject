from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from subject_book.utils import uploads_url_with_instance


class Subject(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'subject'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    generated_name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name


class Uploads(models.Model):
    media_url = models.FileField(upload_to=uploads_url_with_instance)
    original_name = models.CharField(max_length=255)
    generated_name = models.CharField(max_length=255)
    content_type = models.CharField(max_length=400)
    size = models.IntegerField(null=True)
    code = models.CharField(max_length=100)

    class Meta:
        db_table = 'uploads'
