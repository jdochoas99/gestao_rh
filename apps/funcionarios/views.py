from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Funcionario


# Create your views here.


class FuncionariosList(ListView):
    model = Funcionario
