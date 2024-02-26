from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

menu = ['О сайте','Добавить статью','Обратная связь','Войти']

def index(request):
    data = {
        'title': "Главная станица",
        'menu': menu,
    }
    return render(request, "women/home.html", context=data)


def about(request):
    return render(request, 'women/about.html')


def category(request, cat_id):
    return HttpResponse(f"<h1>Категории</h1>"
                        f"<p>id: {cat_id}</p>")


def category_slug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f"<h1>Категории</h1>"
                        f"<p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        return redirect('home')
    return HttpResponse(f"<h1>Архив по годам</h1>"
                        f"<p>{year}</p>")


def page_not_fount(requestt,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')