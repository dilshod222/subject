# Generated by Django 3.2.8 on 2021-10-20 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject_book', '0006_book_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='code',
        ),
    ]
