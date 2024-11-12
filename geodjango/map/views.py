from django.shortcuts import render, redirect
from .models import Location
from django.db.models import Q  # For search functionality

# Map view to display locations
def map_view(request):
    query = request.GET.get('query')  # Get the search query from the form
    if query:
        locations = Location.objects.filter(
            Q(name__icontains=query) | Q(address__icontains=query)
        )
    else:
        locations = Location.objects.all()

    return render(request, 'map.html', {'locations': locations})

# View to add a new location
def add_location(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']

        # Create and save new location
        Location.objects.create(
            name=name,
            address=address,
            latitude=latitude,
            longitude=longitude
        )
        return redirect('map:map')  # Redirect to map view after saving

    return render(request, 'add_location.html')
