from django.urls import path
from . import views

app_name = 'map'

urlpatterns = [
    path('map/', views.map_view, name='map'),
    path('add_location/', views.add_location, name='add_location'),
]
