from django.shortcuts import render
from .models import Endereco
from .forms import EnderecoForm
from django.views.generic import FormView, ListView, DetailView, DeleteView
import requests
from django.urls import reverse_lazy

class ViaCepFormView(FormView):
    template_name = 'base.html'
    form_class = EnderecoForm
    success_url = reverse_lazy('ViaCep:endereco-list')
  

    def form_valid(self, form):
        cep = form.cleaned_data['cep']
        contexto = self.get_context_data(form=form) 

        try:
            url = f'https://viacep.com.br/ws/{cep}/json/'
            response = requests.get(url)
            response.raise_for_status()  
            data = response.json()

            if 'erro' in data:
                contexto['erro'] = f'CEP "{cep}" não foi encontrado.'
            else:
                endereco_obj = Endereco.objects.update_or_create(
                    cep=data.get('cep'),
                    rua=data.get('logradouro'),
                    bairro=data.get('bairro'),
                    cidade=data.get('localidade'),
                    estado=data.get('uf')
                )
                
                contexto['endereco'] = endereco_obj

        except requests.RequestException:
            contexto['erro'] = 'Falha ao se comunicar com a API do ViaCEP.'
            return self.form_invalid(form)

        return super().form_valid(form)
    
class Listagem(ListView):
    model = Endereco
    template_name = 'apiCepCRUD/list.html'
    context_object_name = 'enderecos'

class EnderecoDetail(DetailView):
    model = Endereco
    template_name = 'apiCepCRUD/detail.html'
    context_object_name = 'endereco'

class EnderecoDelete(DeleteView):
    model = Endereco
    template_name = 'apiCepCRUD/delete.html'
    success_url = reverse_lazy('ViaCep:endereco-list')
