from rest_framework import  serializers, viewsets
from ponto.models import Pessoa,Horario,Frequencia,TipoRegistro,Justificativa

class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Horario
        fields=('nome','horario')

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    #horario=HorarioSerializer(many=False)
    class Meta:
        model=Pessoa
        fields=('nome','cargo','setor','adimisao','email','cpf','salario','horario','chefe')

class TipoRegistroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=TipoRegistro
        fields=('nome',)

class FrequenciaSerializer(serializers.HyperlinkedModelSerializer):
    #hora=serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S')
    #funcionario=PessoaSerializer(many=False)
    #chefe=PessoaSerializer(many=False)
    class Meta:
        model=Frequencia
        fields=('tipo','funcionario','chefe','hora','ipMaquina','status')

class JustificativaSerializer(serializers.HyperlinkedModelSerializer):
    #frequencia=FrequenciaSerializer(many=False)
    class Meta:
        model=Justificativa
        fields=('justificativa','frequencia')
        
class TipoRegistroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=TipoRegistro
        fields=('nome',)
    
    