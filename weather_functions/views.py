from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def get_search_data(request):
    return JsonResponse({'status': '400'})
