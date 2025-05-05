
from django.http import HttpResponse,JsonResponse
def home_page(request):
    print("Home page requested")
    friends = [
        'abhi',
        'poti'
    ]
    return JsonResponse(friends,safe = False)