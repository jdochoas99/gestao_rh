from django.views.generic import CreateView
from apps.documentos.models import Documento


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']