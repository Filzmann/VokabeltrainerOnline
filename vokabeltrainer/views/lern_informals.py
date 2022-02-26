from random import randrange
from django.views.generic import TemplateView
from vokabeltrainer.models.vokabel_models import Vokabel, VokabelSet, LobUndAufmunterung, InFormal


class LernInformalView(TemplateView):
    template_name = "vokabeltrainer/lern_informals_template.html"
    model = InFormal
    question = None
    informal = None
    right_wrong = True

    def get_context_data(self, **kwargs):
        context = super(LernInformalView, self).get_context_data(**kwargs)

        self.informal = InFormal.get_random()
        # neue Frage erstellen
        muenze = randrange(2)
        self.question = {
            'id': self.informal.id,
            'question': self.informal.formal if muenze == 0 else self.informal.informal,
            'hint': self.informal.hint_informal,
            'answer': self.informal.informal if muenze == 0 else self.informal.formal,
            'to_find': 'informal' if muenze == 0 else 'informal',
            'count_this': 1,
        }

        context['truefalse'] = False
        context['truefalse_text'] = ''
        context['question'] = self.question
        return context


class LernInformalErgebnisView(TemplateView):
    template_name = "vokabeltrainer/lern_informal_ergebnis_template.html"
    model = InFormal
    question = None
    informal = None
    right_wrong = True

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # korrekte Antwort ermitteln
        informal = InFormal.objects.get(pk=request.POST['question_id'])
        to_find = request.POST['to_find']
        correct_answer = informal.formal if to_find == 'formal' else informal.informal
        correct_answers = correct_answer.replace(' ', '').split(',')
        if self.request.POST['answer'].replace(' ', '') in correct_answers:
            # print('korrekt')
            context['solution_correct'] = True
            message = LobUndAufmunterung.get_random(l_type='LO')
            context['message_text'] = message.text
            if self.request.POST['count_this'] == '1':
                informal.add_correct()
        else:
            # print('wrong')
            context['solution_correct'] = False
            message = LobUndAufmunterung.get_random(l_type='AU')
            context['message_text'] = message.text
            if self.request.POST['count_this'] == '1':
                informal.add_wrong()

        if to_find == 'informal':
            context['question'] = {
                'id': informal.id,
                'question': informal.formal,
                'hint': informal.hint_informal,
                'answer': informal.informal,
                'to_find': to_find,
                'count_this': self.request.POST['count_this'],
            }
        else:
            context['question'] = {
                'id': informal.id,
                'question': informal.informal,
                'hint': informal.hint_formal,
                'answer': informal.formal,
                'to_find': to_find,
                'count_this': self.request.POST['count_this'],
            }

        # print(context)
        return self.render_to_response(context)
