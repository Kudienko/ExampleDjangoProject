# Generated by Django 4.1.3 on 2022-11-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
    ]