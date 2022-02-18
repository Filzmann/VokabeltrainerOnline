from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from vokabeltrainer.models.vokabel_models import Vokabel


class VokabelListView(ListView):
    model = Vokabel
    context_object_name = 'words_to_learn'


class VokabelCreateView(CreateView):
    model = Vokabel
    fields = ['english', 'german', 'english_description', 'vokabel_sets']
    success_url = reverse_lazy('list_vokabel')


class VokabelUpdateView(UpdateView):
    model = Vokabel
    fields = ['english', 'german', 'english_description', 'vokabel_sets']
    success_url = reverse_lazy('list_vokabel_set')


class VokabelDeleteView(DeleteView):
    model = Vokabel
    success_url = reverse_lazy('list_vokabel')
