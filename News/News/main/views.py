from django.shortcuts import render, redirect
from .models import Rubric, Article, Hashtag
from .forms import ArticleForm, RubricForm, HashtagForm



def index(request):
    rubriks = Rubric.objects.all()
    news = Article.objects.all()
    news = reversed(news)
    return render(request, 'main/index.html', {'rubriks': rubriks, 'news': news})


def article(request):
    rubriks = Rubric.objects.all()
    return render(request, 'main/article.html', {'rubriks': rubriks})


def rubrika(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        parameter = form['rub'].value()
    parameter = request.GET.get('parameter')
    delete = request.GET.get('del')
    Article.objects.filter(title__exact=delete).delete()
    rubriks = Rubric.objects.all()
    lenta = Article.objects.filter(rub__name__exact=parameter)
    lenta = reversed(lenta)
    return render(request, 'main/rubrika.html', {'rubriks': rubriks, 'parameter': parameter, 'lenta': lenta})


def addState(request):
    error = ''
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'gbfgbgfbgfb'
    data = {
            'form': form,
            'error': error
        }
    return render(request, 'main/addState.html', data)


def addRubric(request):
    error = ''
    form = RubricForm()
    if request.method == 'POST':
        form = RubricForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'gbfgbgfbgfb'
    data = {
            'form': form,
            'error': error
        }
    return render(request, 'main/addRubric.html', data)


def addHash(request):
    error = ''
    form = HashtagForm()
    if request.method == 'POST':
        form = HashtagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'gbfgbgfbgfb'
    data = {
            'form': form,
            'error': error
        }
    return render(request, 'main/addHash.html', data)
