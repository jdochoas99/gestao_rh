from django.urls import path, include
from .views import DocumentoCreate
urlpatterns = [

    path('novo', DocumentoCreate.as_view(), name='create_documento'),
]
