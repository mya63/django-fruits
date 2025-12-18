from django.shortcuts import render
from django.templatetags.static import static

def fruitlist(request):
    fruits = [
        {"name": "Apfel", "weight": 150, "color": "Rot", "img": static("fruit_app/img/apfel.jpg"), "is_ordered": True},
        {"name": "Banane", "weight": 120, "color": "Gelb", "img": static("fruit_app/img/banane.jpg"), "is_ordered": False},
        {"name": "Orange", "weight": 180, "color": "Orange", "img": static("fruit_app/img/orange.jpg"), "is_ordered": True},
        {"name": "Kirsche", "weight": 10, "color": "Rot", "img": static("fruit_app/img/kirsche.jpg"), "is_ordered": False},
        {"name": "Birne", "weight": 90, "color": "Grün", "img": static("fruit_app/img/birne.jpg"), "is_ordered": False},
    ]
    return render(request, "fruit_app/fruitlist.html", {"fruits": fruits})

def info(request):
    return render(request, "fruit_app/info.html")
