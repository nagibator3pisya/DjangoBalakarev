from django.urls import path, register_converter
from . import views
from . import convertors
register_converter(convertors.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'), # http://127.0.0.1:8000 главная страница
    path('about/', views.about, name='about'),
    path('cat/<int:cat_id>/', views.category, name='cat_id'), #http://127.0.0.1:8000/cat/1/
    path('cat/<slug:cat_slug>/', views.category_slug, name='cat_slug'),  #http://127.0.0.1:8000/cat/dd+d/
    path("archive/<year4:year>/", views.archive, name='archive')
]
