# Generated by Django 3.2.8 on 2021-10-20 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject_book', '0008_book_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='code',
        ),
        migrations.AddField(
            model_name='book',
            name='generated_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
