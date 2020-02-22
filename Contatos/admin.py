from django.contrib import admin
from .models import Contato
class contato_admin(admin.ModelAdmin):
    list_display = ['nome','sobrenome']
    admin.site.register(Contato)
