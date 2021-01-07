from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from .models import Funcionario


# Create your views here.


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']