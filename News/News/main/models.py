from django.db import models


class Rubric(models.Model):
    name = models.CharField('name', max_length=255)

    def __str__(self):
        return self.name


class Hashtag(models.Model):
    name = models.CharField('name', max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('title', max_length=255)
    keywords = models.CharField('keywords', max_length=255)
    annotation = models.CharField('annotation',max_length=1100)
    rub = models.ForeignKey('Rubric', on_delete=models.PROTECT, null=True)
    hash = models.ManyToManyField(Hashtag)
    images = models.CharField('images', max_length=255)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'