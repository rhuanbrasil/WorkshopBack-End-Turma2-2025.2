from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.api import viewSets
from app import views

app_name = 'api'

router = DefaultRouter()

router.register(r'movies', viewSets.FilmeViewSet, basename='filmes')

urlpatterns = [
    path('movie/', views.sync_swapi_data, name='sync-api'),
    path('', include(router.urls)),
]