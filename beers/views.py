from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Beer, Brewery, Hops

# Create your views here.
def index(request):
    beers = Beer.objects.order_by('name')
    context = {'beer_list': beers}
    return render(request, 'beers/index.html', context)

def beer_detail(request, beer_id):
    beer = get_object_or_404(Beer, pk=beer_id)
    return render(request, 'beers/beer_detail.html', {'beer': beer, 'ratings': beer.rating_data()})

def hops_detail(request, hops_id):
    hops = get_object_or_404(Hops, pk=hops_id)
    return render(request, 'beers/hops_detail.html', {'hops': hops, 'ratings': hops.rating_data()})

def brewery_detail(request, brewery_id):
    brewery = get_object_or_404(Brewery, pk=brewery_id)
    return render(request, 'beers/brewery_detail.html', {'brewery': brewery, 'ratings': brewery.rating_data()})
