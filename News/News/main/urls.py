from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('article', views.article, name='article'),
    path('rubrika', views.rubrika, name='rubrika'),
    path('addState', views.addState, name='addState'),
    path('addRubric', views.addRubric, name='addRubric'),
    path('addHash', views.addHash, name='addHash'),
]
