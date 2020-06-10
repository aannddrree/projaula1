from django import forms
from agenda.models import Agenda


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['descricao', 'data', 'tipo']
