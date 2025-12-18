from django.http import JsonResponse

def send_fruits(request):
    fruits = [
        {"name": "Apple", "weight": 150, "color": "red"},
        {"name": "Banana", "weight": 120, "color": "yellow"},
        {"name": "Orange", "weight": 180, "color": "orange"},
        {"name": "Grape", "weight": 5, "color": "purple"},
        {"name": "Kiwi", "weight": 90, "color": "green"},
    ]
    return JsonResponse(fruits, safe=False)
