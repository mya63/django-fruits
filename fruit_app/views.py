from django.http import JsonResponse

def send_fruits(request):
    fruits = {
        "f1": {"name": "Apple", "weight": 150, "color": "red"},
        "f2": {"name": "Banana", "weight": 120, "color": "yellow"},
        "f3": {"name": "Orange", "weight": 180, "color": "orange"},
        "f4": {"name": "Grape", "weight": 5, "color": "purple"},
        "f5": {"name": "Kiwi", "weight": 90, "color": "green"}
    }
    return JsonResponse(fruits)
