# # map/views.py
# from django.shortcuts import render

# def map_view(request):
#     # You can replace this with actual data fetching logic
#     locations = [{'name': 'Location 1', 'address': 'Address 1'}, {'name': 'Location 2', 'address': 'Address 2'}]
#     return render(request, 'map.html', {'locations': locations})


# def home_view(request):
#     # This will render a different template for the home page
#     return render(request, 'home.html')

from django.shortcuts import render
from .models import Location

# Create your views here.
def map_view(request):

    locations = Location.objects.all()
    return render(request, 'map.html', {'locations': locations})