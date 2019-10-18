from django.shortcuts import render
from .models import Agenda

# Create your views here.
def list(resquest):
    agendas = Agenda.all()
    render(resquest, 'pages.list.html', {'agendas': agendas})