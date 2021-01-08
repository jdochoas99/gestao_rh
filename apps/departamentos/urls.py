from django.urls import path, include
from .views import DepartamentosList, DepartamentoCreate, DepartamentoEdit
urlpatterns = [

    path('list', DepartamentosList.as_view(), name='list_departamentos'),
    path('novo', DepartamentoCreate.as_view(), name='create_departamento'),
    path('editar/<int:pk>:', DepartamentoEdit.as_view(), name='update_departamento'),

]
