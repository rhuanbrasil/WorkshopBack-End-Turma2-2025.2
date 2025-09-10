
from django.urls import path
from .migrations import views as view

urlpatterns = [
   path('', view.home, name='home'),
   path('consulta/', view.consulta_cep, name='consulta_cep')
]