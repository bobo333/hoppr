from django.contrib import admin

from .models import Hops, Beer, Brewery, Review

# Register your models here.
admin.site.register(Hops)
admin.site.register(Beer)
admin.site.register(Brewery)
admin.site.register(Review)
