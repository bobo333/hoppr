from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from .models import Beer, BeerStyle, Brewery, Hops


def index(request):
    beers = Beer.objects.order_by('name')
    breweries = Brewery.objects.order_by('name')
    hops = Hops.objects.order_by('name')
    styles = BeerStyle.objects.order_by('name')
    context = {
        'beer_list': beers,
        'brewery_list': breweries,
        'hops_list': hops,
        'styles_list': styles,
    }
    return render(request, 'beers/index.html', context)


def beer_detail(request, beer_id):
    beer = get_object_or_404(Beer, pk=beer_id)
    return render(request, 'beers/beer_detail.html',
        {
            'beer': beer,
            'ratings': beer.rating_data(),
            'user_rating': beer.user_rating_data(request.user),
            'predictions': {
                'all': {
                    'categories': {
                        'Brewery': [{
                                'name': b.name,
                                'rating': b.rating_data()}
                            for b in beer.breweries.all()
                        ],
                        'Hops': [{
                                'name': h.name,
                                'rating': h.rating_data()}
                            for h in beer.hops.all()
                        ],
                        'Style': [{
                                'name': s.name,
                                'rating': s.rating_data()}
                            for s in beer.styles.all()
                        ],
                    }
                },
                'user': {
                    'categories': {
                        'Brewery': [{
                                'name': b.name,
                                'rating': b.user_rating_data(request.user)}
                            for b in beer.breweries.all()
                        ],
                        'Hops': [{
                                'name': h.name,
                                'rating': h.user_rating_data(request.user)}
                            for h in beer.hops.all()
                        ],
                        'Style': [{
                                'name': s.name,
                                'rating': s.user_rating_data(request.user)}
                            for s in beer.styles.all()
                        ],
                    }
                }
            },
        }
    )


def hops_detail(request, hops_id):
    hops = get_object_or_404(Hops, pk=hops_id)
    return render(request, 'beers/hops_detail.html',
        {
            'hops': hops,
            'ratings': hops.rating_data(),
            'user_rating': hops.user_rating_data(request.user)
        }
    )


def brewery_detail(request, brewery_id):
    brewery = get_object_or_404(Brewery, pk=brewery_id)
    return render(request, 'beers/brewery_detail.html',
        {
            'brewery': brewery,
            'ratings': brewery.rating_data(),
            'user_rating': brewery.user_rating_data(request.user)
        }
    )


def style_detail(request, style_id):
    style = get_object_or_404(BeerStyle, pk=style_id)
    return render(request, 'beers/style_detail.html',
        {
            'style': style,
            'ratings': style.rating_data(),
            'user_rating': style.user_rating_data(request.user)
        }
    )


def signup(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})
