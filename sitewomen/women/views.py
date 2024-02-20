from django.http import HttpResponse
from django.shortcuts import render


def index(requrest):
    return HttpResponse("Страница приложения women")


def category(requrest):
    return HttpResponse("<h1>Категории</h1>")