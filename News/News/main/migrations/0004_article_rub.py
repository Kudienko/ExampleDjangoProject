# Generated by Django 4.1.3 on 2022-11-06 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='rub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.rubric'),
        ),
    ]
