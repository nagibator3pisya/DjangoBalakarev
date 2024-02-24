from django.urls import path, register_converter
from . import views
from . import convertors
register_converter(convertors.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index), # http://127.0.0.1:8000 главная страница
    path('cat/<int:cat_id>/', views.category), #http://127.0.0.1:8000/cat/1/
    path('cat/<slug:cat_slug>/', views.category_slug),  #http://127.0.0.1:8000/cat/dd+d/
    path("archive/<year4:year>/", views.archive)
]
