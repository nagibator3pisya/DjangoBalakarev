from django.urls import path
from . import views
urlpatterns = [
    path('', views.index), # http://127.0.0.1:8000 главная страница
    path('cat/', views.category),
]
