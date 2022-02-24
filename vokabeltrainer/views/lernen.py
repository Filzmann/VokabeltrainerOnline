from random import randrange

import json
from django.views.generic import TemplateView

from vokabeltrainer.models.vokabel_models import Vokabel, VokabelSet


class LernenView(TemplateView):
    template_name = "vokabeltrainer/lernen_template.html"
    model = Vokabel
    vokabel_set_id = None
    question = None
    vokabel = None
    right_wrong = True

    def get_context_data(self, **kwargs):
        context = super(LernenView, self).get_context_data(**kwargs)

        # Alle Set-ids ermitteln
        context['sets'] = VokabelSet.objects.all()

        # question_set ermitteln
        if 'set_id' in self.request.GET:
            context['act_set_id'] = self.request.GET['set_id']
            self.vokabel_set_id = self.request.GET['set_id']
            self.vokabel = Vokabel.get_random(vokabel_set=self.vokabel_set_id)
        else:
            self.vokabel = Vokabel.get_random()
        # neue Frage erstellen
        muenze = randrange(2)
        self.question = {
            'id': self.vokabel.id,
            'question': self.vokabel.german if muenze == 0 else self.vokabel.english,
            'hint': self.vokabel.english_description,
            'answer': self.vokabel.english if muenze==0 else self.vokabel.german,
            'lang_to_find': 'english' if muenze == 0 else 'german',
            'count_this': 1,
        }

        context['truefalse'] = False
        context['truefalse_text'] = ''

        context['question'] = self.question
        return context

