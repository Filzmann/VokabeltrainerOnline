from random import randrange

import json
from django.views.generic import TemplateView

from vokabeltrainer.models.vokabel_models import Vokabel, VokabelSet


class LernenView(TemplateView):
    template_name = "vokabeltrainer/lernen_template.html"
    model = Vokabel
    vokabel_set_id = None
    question = None
    question_set = None
    right_wrong = True

    def get_context_data(self, **kwargs):
        context = super(LernenView, self).get_context_data(**kwargs)

        # Alle Set-ids ermitteln
        context['sets'] = VokabelSet.objects.all()

        # question_set ermitteln
        if not self.right_wrong:
            self.question = self.question_set
        else:
            if 'set_id' in self.request.GET:
                context['act_set_id'] = self.request.GET['set_id']
                self.vokabel_set_id = self.request.GET['set_id']
                self.question_set = Vokabel.get_random(vokabel_set=self.vokabel_set_id)
            else:
                self.question_set = Vokabel.get_random()
            # neue Frage erstellen
            if randrange(2):
                #  englisch
                self.question = {
                    'question': self.question_set.german,
                    'hint': self.question_set.english_description,
                    'answer': self.question_set.english,
                    'lang_to_find': 'english',
                }
            else:
                # deutsch
                self.question = {
                    "question": self.question_set.english,
                    "hint": self.question_set.english_description,
                    "answer": self.question_set.german,
                    "lang_to_find": "german",
                }

        if self.request.POST and not self.right_wrong:
            context['truefalse'] = False
            context['truefalse_text'] = "FALSCHE Antwort! Nochmal versuchen!"
        elif self.request.POST and self.right_wrong:
            context['truefalse'] = True
            context['truefalse_text'] = "RICHTIGE Antwort! Du bist super!"
        else:
            context['truefalse'] = False
            context['truefalse_text'] = ''

        context['question_set'] = self.question
        return context

    def post(self, request, *args, **kwargs):
        # Your code here
        # Here request.POST is the same as self.request.POST
        # You can also access all possible self variables
        # like changing the template name for instance

        # single_quotes to double to make a json string from input
        question_set = self.request.POST['question_set'].replace("'", '"')
        print(question_set)
        question_set = json.loads(question_set)

        correct_answers = question_set['answer'].replace(' ', '').split(',')
        if self.request.POST['answer'].replace(' ', '') in correct_answers:
            self.right_wrong = True
            print('right')
        else:
            self.right_wrong = False
            self.question_set = question_set
            print('wrong')

        context = self.get_context_data(**kwargs)

        # context['new_variable'] = 'new_variable' + ' updated'

        return self.render_to_response(context)
