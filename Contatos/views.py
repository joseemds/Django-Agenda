from django.shortcuts import render
from .models import Contato
def listar_contatos(request):
    contatos = Contato.objects.all()
    return render(request,'Agenda/agenda.html',{'contatos':contatos})
