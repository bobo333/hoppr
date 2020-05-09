from django.db import models
from django.contrib.auth.models import User

from .utils import calculate_rating_data


class Hops(models.Model):
    name = models.TextField('name', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Hops"

    def __str__(self):
        return self.name

    def rating_data(self):
        reviews = Review.objects.filter(beer__hops__id=self.id)
        return calculate_rating_data(reviews)

    def user_rating_data(self, user):
        if not user.is_authenticated:
            return None

        reviews = Review.objects.filter(beer__hops__id=self.id, user__id=user.id)
        return calculate_rating_data(reviews)


class Beer(models.Model):
    name = models.TextField('name', null=False, blank=False)
    abv = models.DecimalField('abv', decimal_places=2, max_digits=4, null=True, blank=True)
    ibu = models.IntegerField('ibu', null=True, blank=True)
    hops = models.ManyToManyField(Hops, related_name='beers', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def rating_data(self):
        reviews = self.reviews.all()
        return calculate_rating_data(reviews)

    def user_rating_data(self, user):
        if not user.is_authenticated:
            return None

        reviews = self.reviews.filter(user__id=user.id)
        return calculate_rating_data(reviews)


class Brewery(models.Model):
    name = models.TextField('name', null=False, blank=False)
    beers = models.ManyToManyField(Beer, related_name='breweries', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Breweries"

    def __str__(self):
        return self.name

    def rating_data(self):
        reviews = Review.objects.filter(beer__breweries__id=self.id)
        return calculate_rating_data(reviews)

    def user_rating_data(self, user):
        if not user.is_authenticated:
            return None

        reviews = Review.objects.filter(beer__breweries__id=self.id, user__id=user.id)
        return calculate_rating_data(reviews)


class Review(models.Model):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField('rating', null=False, blank=False)
    body = models.TextField('body', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
