from django.shortcuts import render
from ponto.models import Pessoa,Horario,Frequencia,TipoRegistro,Justificativa
from rest_framework import viewsets
from ponto.serializers import PessoaSerializer,HorarioSerializer,FrequenciaSerializer,TipoRegistroSerializer,JustificativaSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset=Pessoa.objects.all()
    serializer_class=PessoaSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset=Horario.objects.all()
    serializer_class=HorarioSerializer

class FrequenciaViewSet(viewsets.ModelViewSet):
    queryset=Frequencia.objects.all()
    serializer_class=FrequenciaSerializer

class TipoRegistroViewSet(viewsets.ModelViewSet):
    queryset=TipoRegistro.objects.all()
    serializer_class=TipoRegistroSerializer

class JustificativaViewSet(viewsets.ModelViewSet):
    queryset=Justificativa.objects.all()
    serializer_class=JustificativaSerializer