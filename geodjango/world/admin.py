from django.contrib.gis import admin
from .models import WorldBorder, Profile, Location

admin.site.register(WorldBorder, admin.ModelAdmin)
admin.site.register(Profile, admin.ModelAdmin)
admin.site.register(Location, admin.ModelAdmin)  