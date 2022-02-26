from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from vokabeltrainer.models.vokabel_models import InFormal


class InFormalListView(ListView):
    model = InFormal
    context_object_name = 'in_formals_to_learn'
    # ordering = 'english'


class InFormalCreateView(CreateView):
    model = InFormal
    fields = ['formal', 'hint_formal', 'informal', 'hint_informal']
    success_url = reverse_lazy('list_in_formal')


class InFormalUpdateView(UpdateView):
    model = InFormal
    fields = ['formal', 'hint_formal', 'informal', 'hint_informal']
    success_url = reverse_lazy('list_in_formal')


class InFormalDeleteView(DeleteView):
    model = InFormal
    success_url = reverse_lazy('list_in_formal')
