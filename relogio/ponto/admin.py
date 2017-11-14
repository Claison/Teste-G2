from django.contrib import admin
from ponto.models import Pessoa,Horario,Frequencia,TipoRegistro,Justificativa
# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Horario)
admin.site.register(Frequencia)
admin.site.register(TipoRegistro)
admin.site.register(Justificativa)