from random import randrange

import json
from django.views.generic import TemplateView

from vokabeltrainer.models.vokabel_models import Vokabel, VokabelSet


class LernenErgebnisView(TemplateView):
    template_name = "vokabeltrainer/lernen_ergebnis_template.html"
    model = Vokabel
    vokabel_set_id = None
    question = None
    question_set = None
    right_wrong = True

    def get_context_data(self, **kwargs):
        context = super(LernenErgebnisView, self).get_context_data(**kwargs)

        # Alle Set-ids ermitteln
        context['sets'] = VokabelSet.objects.all()

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # korrekte Antwort ermitteln
        vokabel = Vokabel.objects.get(pk=request.POST['question_id'])
        lang_to_find = request.POST['lang_to_find']
        correct_answer = vokabel.english if lang_to_find == 'english' else vokabel.german
        correct_answers = correct_answer.replace(' ', '').split(',')
        if self.request.POST['answer'].replace(' ', '') in correct_answers:
            print('korrekt')
            context['solution_correct'] = True
            context['message_text'] = "RICHTIGE Antwort! Du bist super!"
        else:
            print('wrong')
            context['solution_correct'] = False
            context['message_text'] = "Leider ist das die FALSCHE Antwort! Nochmal versuchen!"

        context['question'] = {
            'id': vokabel.id,
            'question': vokabel.german if lang_to_find == 'english' else vokabel.english,
            'hint': vokabel.english_description,
            'answer': vokabel.english if lang_to_find == 'english' else vokabel.german,
            'lang_to_find': lang_to_find,
            'examples': vokabel.example_sentences,
        }
        print(context)
        return self.render_to_response(context)
