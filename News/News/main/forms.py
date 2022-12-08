from django.forms import ModelForm, TextInput, Textarea, Select
from .models import Article, Rubric, Hashtag


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'keywords', 'annotation', 'rub', 'hash', 'images']
        widgets = {
            "title": TextInput(attrs={
                'class': 'intut',
                'placeholder': 'Название статьи'
            }),
            "keywords": TextInput(attrs={
                'class': 'intut',
                'placeholder': 'Ключевое слово'
            }),
            "annotation": Textarea(attrs={
                'class': 'intut',
                'placeholder': 'Текст статьи'
            }),
            "rub": Select(attrs={
                'name': 'rub',
                'class': 'intut',
                'placeholder': 'Рубрика'
            }),
            # "hash": Select(attrs={
            #     'multiple': 'multiple',
            #     'class': 'intut',
            # }),
            "images": TextInput(attrs={
                'class': 'intut',
                'placeholder': 'Название фотографии'
            }),
        }


class RubricForm(ModelForm):
    class Meta:
        model = Rubric
        fields = ['name']
        widgets = {
            "name": TextInput(attrs={
                'name': 'name',
                'class': 'intut',
                'placeholder': 'Рубрика'
            })
        }


class HashtagForm(ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']
        widgets = {
            "name": TextInput(attrs={
                'name': 'name',
                'class': 'intut',
                'placeholder': 'Хештег'
            })
        }
