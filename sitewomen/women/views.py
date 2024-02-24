from django.http import HttpResponse
from django.shortcuts import render


def index(requrest):
    return HttpResponse("Страница приложения women")


def category(requrest, cat_id):
    return HttpResponse(f"<h1>Категории</h1>"
                        f"<p>id: {cat_id}</p>")


def category_slug(requrest, cat_slug):
    return HttpResponse(f"<h1>Категории</h1>"
                        f"<p>slug: {cat_slug}</p>")


def archive(requrest, year):
    return HttpResponse(f"<h1>Архив по годам</h1>"
                        f"<p>{year}</p>")