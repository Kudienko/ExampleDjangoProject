# Generated by Django 4.1.3 on 2022-11-16 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_article_rubnum_alter_article_annotation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
    ]
