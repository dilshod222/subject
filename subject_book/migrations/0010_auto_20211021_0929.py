# Generated by Django 3.2.8 on 2021-10-21 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject_book', '0009_auto_20211021_0210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='generated_name',
        ),
        migrations.AddField(
            model_name='book',
            name='code',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
