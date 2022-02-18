from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from vokabeltrainer.models.vokabel_models import VokabelSet


class VokabelSetListView(ListView):
    model = VokabelSet
    context_object_name = 'vokabel_set_list'


class VokabelSetCreateView(CreateView):
    model = VokabelSet
    fields = ['name']
    success_url = reverse_lazy('list_vokabel_set')


class VokabelSetUpdateView(UpdateView):
    model = VokabelSet
    fields = ['name']
    success_url = reverse_lazy('list_vokabel_set')


class VokabelSetDeleteView(DeleteView):
    model = VokabelSet
    success_url = reverse_lazy('list_vokabel_set')
