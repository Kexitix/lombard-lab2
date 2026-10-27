from django.http import HttpResponse
from django.shortcuts import render
from django import template


def hello(request):
    # ответ с явным указанием типа: простой текст
    return HttpResponse(u'Привет, Мир! Это ломбард «Золотой залог».', content_type="text/plain")


def hello_default(request):
    # тип ответа не указан -> по умолчанию text/html; charset=utf-8
    return HttpResponse(u'Привет, Мир! Это ломбард «Золотой залог».')


def index(request):
    # исходный шаблон index.html (без стилей)
    return render(request, 'templates/index.html')


def home(request):
    # шаблон static_handler.html со стилями и картинкой
    return render(request, 'templates/static_handler.html')
