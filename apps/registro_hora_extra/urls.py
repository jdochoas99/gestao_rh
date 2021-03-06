from django.urls import path, include
from .views import HoraExtraList, HoraExtraDelete, HoraExtraEdit, HoraExtraNovo, HoraExtraEditBase, UtilizouHoraExtra, NaoUtilizouHoraExtra
urlpatterns = [

    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('editar-funcionario/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('editar/<int:pk>/', HoraExtraEditBase.as_view(), name='update_hora_extra_base'),
    path('utilizou-hora-extra/<int:pk>/', UtilizouHoraExtra.as_view(), name='utilizou_hora_extra'),
    path('nao-utilizou-hora-extra/<int:pk>/', NaoUtilizouHoraExtra.as_view(), name='nao_utilizou_hora_extra'),
    path('delete/<int:pk>:', HoraExtraDelete.as_view(), name='delete_hora_extra'),
    path('novo/', HoraExtraNovo.as_view(), name='create_hora_extra'),
]
