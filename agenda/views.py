from django.shortcuts import render, redirect
from .models import Agenda
from .forms import AgendaForm

# Create your views here.
def list(resquest):
	form = AgendaForm(resquest.POST or None)
	agendas = Agenda.objects.all()
	return render(resquest, 'pages/list.html', {'agendas': agendas, 'form': form})

def delete(resquest, id):
    agenda = Agenda.objects.get(id=id)
    agenda.delete()
    return redirect('/agenda/list/')

def edit(resquest, id):
	agenda = Agenda.objects.get(id=id)
	form = AgendaForm(resquest.POST or None, instance=agenda)

	if form.is_valid():
		form.save()
		return redirect('/agenda/list/')


	return render(resquest, 'pages/edit.html', {'agenda': agenda, 'form': form })


def create(resquest):
	form = AgendaForm(resquest.POST or None)

	if form.is_valid():
		form.save()
		return redirect('/agenda/list/')

	return render(resquest, 'pages/create.html', {'form': form })