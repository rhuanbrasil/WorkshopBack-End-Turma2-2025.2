
from django.urls import path
from . import views

app_name = 'ViaCep'

urlpatterns = [
   path('', views.ViaCepFormView.as_view(), name='form'),
   path('enderecos/', views.Listagem.as_view(), name='endereco-list'),
    
    # <int:pk> captura o ID do endereço da URL e o passa para a view
    path('enderecos/<int:pk>/', views.EnderecoDetail.as_view(), name='endereco-detail'),
        
    # D - Delete
    path('delete/<int:pk>', views.EnderecoDelete.as_view(), name='endereco-delete'),


]
