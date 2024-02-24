from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render,redirect


def index(requrest):
    return HttpResponse("Страница приложения women")


def category(requrest, cat_id):
    return HttpResponse(f"<h1>Категории</h1>"
                        f"<p>id: {cat_id}</p>")


def category_slug(requrest, cat_slug):
    print(requrest.GET)
    return HttpResponse(f"<h1>Категории</h1>"
                        f"<p>slug: {cat_slug}</p>")


def archive(requrest, year):
    if year > 2023:
        return redirect('home')
    return HttpResponse(f"<h1>Архив по годам</h1>"
                        f"<p>{year}</p>")


def page_not_fount(requrest,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')