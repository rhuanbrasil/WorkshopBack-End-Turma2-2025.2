from django.db import models

class Filme(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    episode_id = models.PositiveIntegerField(verbose_name="ID do Episódio")
    opening_crawl = models.TextField(verbose_name="Texto de Abertura")
    director = models.CharField(max_length=100, verbose_name="Diretor")
    producer = models.CharField(max_length=200, verbose_name="Produtor")
    
    release_date = models.DateField(verbose_name="Data de Lançamento")

    created = models.DateTimeField(verbose_name="Criado em")
    edited = models.DateTimeField(verbose_name="Editado em")
    url = models.URLField(unique=True, max_length=255, verbose_name="URL da API")

    def __str__(self):
        return f"Episódio {self.episode_id}: {self.title}"

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"
        ordering = ['episode_id']
