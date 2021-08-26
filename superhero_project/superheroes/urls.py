from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name = 'detail'),
    path('new/', views.create, name='create'),
    path('edit/<int:hero_id>/', views.edit, name='edit'),
    path('remove/<int:hero_id>/', views.remove, name='remove')

]