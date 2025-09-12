from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Filme



@api_view(['POST']) 
def sync_swapi_data(request):

    url = "https://swapi.py4e.com/api/films/"
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        
        filmes_criados = []
        filmes_atualizados = []

        for filme_data in data.get('results', []):
            
            filme_obj, created = Filme.objects.update_or_create(
                episode_id=filme_data['episode_id'],
                defaults={
                    'title': filme_data['title'],
                    'opening_crawl': filme_data['opening_crawl'],
                    'director': filme_data['director'],
                    'producer': filme_data['producer'],
                    'release_date': filme_data['release_date'],
                    'url': filme_data['url'],
                    'created': filme_data['created'],
                    'edited': filme_data['edited'],
                }
            )
            if created:
                filmes_criados.append(filme_obj.title)
            else:
                filmes_atualizados.append(filme_obj.title)
        return Response(
            {
                "status": "Sucesso",
                "message": "Dados da SWAPI foram sincronizados com o banco de dados.",
                "filmes_criados": filmes_criados,
                "filmes_atualizados": filmes_atualizados
            }, 
            status=status.HTTP_200_OK
        )
        
    except requests.exceptions.RequestException as e:
        return Response(
            {"error": f"Erro ao buscar dados: {e}"}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


