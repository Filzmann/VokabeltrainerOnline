from random import randrange
from django.views.generic import TemplateView
from vokabeltrainer.models.vokabel_models import Vokabel, VokabelSet, LobUndAufmunterung


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
            'answer': self.vokabel.english if muenze == 0 else self.vokabel.german,
            'lang_to_find': 'english' if muenze == 0 else 'german',
            'count_this': 1,
        }

        context['truefalse'] = False
        context['truefalse_text'] = ''

        context['question'] = self.question
        return context


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
        print(self.request.POST)
        # korrekte Antwort ermitteln
        vokabel = Vokabel.objects.get(pk=request.POST['question_id'])
        lang_to_find = request.POST['lang_to_find']
        correct_answer = vokabel.english if lang_to_find == 'english' else vokabel.german
        correct_answers = correct_answer.replace(' ', '').split(',')
        if self.request.POST['answer'].replace(' ', '') in correct_answers:
            # print('korrekt')
            context['solution_correct'] = True
            message = LobUndAufmunterung.get_random(l_type='LO')
            context['message_text'] = message.text
            if self.request.POST['count_this'] == '1':
                vokabel.add_correct()
        else:
            # print('wrong')
            context['solution_correct'] = False
            message = LobUndAufmunterung.get_random(l_type='AU')
            context['message_text'] = message.text
            if self.request.POST['count_this'] == '1':
                vokabel.add_wrong()

        context['question'] = {
            'id': vokabel.id,
            'question': vokabel.german if lang_to_find == 'english' else vokabel.english,
            'hint': vokabel.english_description,
            'answer': vokabel.english if lang_to_find == 'english' else vokabel.german,
            'lang_to_find': lang_to_find,
            'examples': vokabel.example_sentences,
            'count_this': self.request.POST['count_this'],
        }
        # print(context)
        return self.render_to_response(context)
