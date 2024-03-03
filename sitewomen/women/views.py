from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


menu = [
    {'title': "О сайте",  'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'},

]
data_bd = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Всемирно известная актриса и гуманитарий.', 'is_published': True},
    {'id': 2, 'title': 'Джонни Депп', 'content': 'Талантливый актер и кинозвезда.', 'is_published': False},
    {'id': 3, 'title': 'Мэрилин Монро', 'content': 'Легендарная голливудская актриса и киноикона.', 'is_published': True}
]
# Главная страница
def index(request):
    data = {
        'title': "Главная станица",
        'menu': menu,
        'post': data_bd
    }
    return render(request, "women/home.html", context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})


def addpage(request):
    return HttpResponse(f"Добавление статьи")


def contact(request):
    return HttpResponse(f"Обратная связь")


def login(request):
    return HttpResponse(f"Авторизация")




def how_post(request,post_id):
    return HttpResponse(f"Отображение статьи с id: {post_id}")



def page_not_fount(requestt,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')