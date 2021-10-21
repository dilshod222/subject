# Generated by Django 3.2.8 on 2021-10-21 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject_book', '0010_auto_20211021_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='code',
        ),
        migrations.AddField(
            model_name='book',
            name='generated_name',
            field=models.CharField(default=11, max_length=255),
            preserve_default=False,
        ),
    ]