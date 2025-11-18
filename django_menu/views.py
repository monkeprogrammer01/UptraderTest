from django.shortcuts import render

def menu(request):
    return render(request, "django_menu/menu_page.html")
