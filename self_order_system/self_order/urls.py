from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # トップ画面
    path('menu/', views.MenuView.as_view(), name='menu'),  # メニュー画面
]
