from django.shortcuts import render, redirect

from agenda.forms import AgendaForm
from agenda.models import Agenda


def list_agenda(request):
    agendas = Agenda.objects.all()
    return render(request, 'agenda.html', {'agendas': agendas})


def create_agenda(request):
    form = AgendaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_agenda')

    return render(request, 'agenda-form.html', {'form': form})


def update_agenda(request, id):
    agenda = Agenda.objects.get(id=id)
    form = AgendaForm(request.POST or None, instance=agenda)

    if form.is_valid():
        form.save()
        return redirect('list_agenda')

    return render(request, 'agenda-form.html', {'form': form, 'agenda': agenda})


def delete_agenda(request, id):
    agenda = Agenda.objects.get(id=id)

    if request.method == 'POST':
        agenda.delete()
        return redirect('list_agenda')

    return render(request, 'agenda-delete-confirm.html', {'agenda': agenda})
