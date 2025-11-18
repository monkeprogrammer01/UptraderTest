from django.urls import path
from django_menu.views import menu

urlpatterns = [
    path('', menu, name="menu"),
]