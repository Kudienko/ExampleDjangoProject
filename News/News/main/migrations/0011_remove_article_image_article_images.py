# Generated by Django 4.1.3 on 2022-11-17 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.AddField(
            model_name='article',
            name='images',
            field=models.CharField(default=1, max_length=255, verbose_name='images'),
            preserve_default=False,
        ),
    ]
