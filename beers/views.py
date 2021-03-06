from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from .models import Beer, BeerStyle, Brewery, Hops, Review


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
            'predictions': beer.prediction_data(request.user),
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


@login_required
def review_create(request):
    if request.method == 'GET':
        max_rating = 5
        return render(request, 'beers/review_create.html', {
            'rating_range': range(1, max_rating + 1),
            'beers': Beer.objects.all(),
        })

    beer = get_object_or_404(Beer, pk=request.POST['beer'])
    try:
        rating_val = request.POST['rating']
    except (KeyError):
        return render(request, 'beers/review_create.html', {
            'error_message': 'you must select a rating!',
        })
    else:
        review = Review(beer=beer, user=request.user, rating=rating_val)
        review.save()
        return redirect('beer_detail', beer.id)



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
