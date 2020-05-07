from django.urls import path

from . import views

app_name = 'beer'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:beer_id>/', views.beer_detail, name='beer_detail'),
]
