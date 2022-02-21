from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from vokabeltrainer.models.vokabel_models import LobUndAufmunterung


class LobUndAufmunterungListView(ListView):
    model = LobUndAufmunterung
    context_object_name = 'lob_list'


class LobUndAufmunterungCreateView(CreateView):
    model = LobUndAufmunterung
    fields = ['type', 'text']
    success_url = reverse_lazy('list_lob')


class LobUndAufmunterungUpdateView(UpdateView):
    model = LobUndAufmunterung
    fields = ['type', 'text']
    success_url = reverse_lazy('list_lob')


class LobUndAufmunterungDeleteView(DeleteView):
    model = LobUndAufmunterung
    success_url = reverse_lazy('list_lob')
