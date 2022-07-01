from django.shortcuts import render


def home(request):
    return render(request, "recipes/pages/home.html")


def recipe(request, id_recipe):
    return render(request, "recipes/pages/recipe-view.html")
