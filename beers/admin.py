from django.contrib import admin

from .models import Hops, BeerStyle, Beer, Brewery, Review

# Hops
class HopsBeerInline(admin.TabularInline):
	model = Beer.hops.through
	extra = 1


class HopsAdmin(admin.ModelAdmin):
	ordering = ('name',)

	inlines = [
		HopsBeerInline,
	]


# Beer Style
class BeerStyleAdmin(admin.ModelAdmin):
	ordering = ('name',)


# Beer
class BeerBreweryInline(admin.TabularInline):
	model = Brewery.beers.through
	extra = 1


class BeerAdmin(admin.ModelAdmin):
	ordering = ('name',)

	inlines = [
		BeerBreweryInline,
	]

# Review
class ReviewAdmin(admin.ModelAdmin):
	ordering = ('beer__name',)


# Register your models here.
admin.site.register(Hops, HopsAdmin)
admin.site.register(BeerStyle, BeerStyleAdmin)
admin.site.register(Beer, BeerAdmin)
admin.site.register(Brewery)
admin.site.register(Review, ReviewAdmin)
