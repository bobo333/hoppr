from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Beer

# Create your views here.
def index(request):
    beers = Beer.objects.order_by('name')
    context = {'beer_list': beers}
    return render(request, 'beers/index.html', context)

def beer_detail(request, beer_id):
    beer = get_object_or_404(Beer, pk=beer_id)
    return render(request, 'beers/beer_detail.html', {'beer': beer})
