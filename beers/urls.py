from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('beer/<int:beer_id>/', views.beer_detail, name='beer_detail'),
	path('hops/<int:hops_id>/', views.hops_detail, name='hops_detail'),
	path('brewery/<int:brewery_id>/', views.brewery_detail, name='brewery_detail'),
	path('account/create', views.register, name="register"),
]
