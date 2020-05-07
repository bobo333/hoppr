from django.contrib import admin

from .models import Hops, Beer, Brewery, Review

# Hops
class HopsBeerInline(admin.TabularInline):
	model = Beer.hops.through
	extra = 1

class HopsAdmin(admin.ModelAdmin):
	inlines = [
		HopsBeerInline,
	]

# Beer
class BeerBreweryInline(admin.TabularInline):
	model = Brewery.beers.through
	extra = 1

class BeerAdmin(admin.ModelAdmin):
	inlines = [
		BeerBreweryInline,
	]

# Register your models here.
admin.site.register(Hops, HopsAdmin)
admin.site.register(Beer, BeerAdmin)
admin.site.register(Brewery)
admin.site.register(Review)
