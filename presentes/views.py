from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Presente


class PresenteList(ListView):
    model = Presente


class PresenteCreate(CreateView):
    model = Presente
    fields = ['nome', 'descricao']
    success_url = reverse_lazy('presente_list')

class PresenteUpdate(UpdateView):
    model = Presente
    fields = ['nome', 'descricao']
    success_url = reverse_lazy('presente_list')


class PresenteDelete(DeleteView):
    model = Presente
    success_url = reverse_lazy('presente_list')
