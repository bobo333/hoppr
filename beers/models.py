from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hops(models.Model):
    name = models.TextField('name', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Hops"

    def __str__(self):
        return self.name

class Beer(models.Model):
    name = models.TextField('name', null=False, blank=False)
    abv = models.IntegerField('abv', null=True, blank=True)
    ibu = models.IntegerField('ibu', null=True, blank=True)
    hops = models.ManyToManyField(Hops, related_name='beers', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Brewery(models.Model):
    name = models.TextField('name', null=False, blank=False)
    beers = models.ManyToManyField(Beer, related_name='breweries', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Breweries"

    def __str__(self):
        return self.name

class Review(models.Model):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField('rating', null=False, blank=False)
    body = models.TextField('body', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
