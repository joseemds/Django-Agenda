from django.contrib import admin
from .models import Categoria,Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome','sobrenome','telefone','categoria','mostrar']
    list_editable = ('telefone','mostrar')


admin.site.register(Contato,ContatoAdmin)
admin.site.register(Categoria)
