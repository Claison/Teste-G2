from django.db import models

# Create your models here.

class Horario(models.Model):
    nome=models.CharField(max_length=100)
    horario=models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome=models.CharField(max_length=100)
    cargo=models.CharField(max_length=100)
    setor=models.CharField(max_length=100)
    adimisao=models.CharField(max_length=20)
    email=models.CharField(max_length=100)
    cpf=models.IntegerField(null=True, blank=False)
    salario=models.FloatField(max_length=20, blank=True)
    horario=models.ForeignKey(Horario, null=True, blank=False)
    chefe = models.BooleanField("Chefe?",default=False)
    def __str__(self):
        return self.nome

class TipoRegistro(models.Model):
    nome=models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Frequencia(models.Model):
    funcionario=models.ForeignKey(Pessoa,related_name='Funcionario', null=True, blank=False)
    chefe=models.ForeignKey(Pessoa,related_name='Chefe', null=True, blank=False)
    hora=models.DateTimeField(blank=True,null=True)
    ipMaquina=models.CharField(max_length=20)
    status=models.CharField(max_length=20,choices=(('valido','Consitente'),('invalido','Inconsistente')),default='Consistente')
    tipo=models.ForeignKey(TipoRegistro,null=True, blank=False)
    def __str__(self):
        return self.status
class Justificativa(models.Model):
    justificativa=models.TextField()
    frequencia = models.ForeignKey(Frequencia,related_name='justificativa')

    def __str__(self):
        return self.justificativa