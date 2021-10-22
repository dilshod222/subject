from django.contrib import admin

# Register your models here.
from subject_book.models import Subject, Book

admin.site.register(Subject)
admin.site.register(Book)
