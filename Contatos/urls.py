from django.contrib import admin
from django.urls import path, include
from Contatos import views
urlpatterns = [
    path('Agenda/agenda.html', views.listar_contatos , name = 'agenda')
]
