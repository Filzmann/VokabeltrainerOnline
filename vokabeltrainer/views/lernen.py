from random import randrange

from django.views.generic import TemplateView

from vokabeltrainer.models.vokabel_models import Vokabel, VokabelSet


class LernenView(TemplateView):
    template_name = "vokabeltrainer/lernen_template.html"
    model = Vokabel
    vokabel_set_id = None

    def get_context_data(self, **kwargs):
        context = super(LernenView, self).get_context_data(**kwargs)

        # Alle Set-ids ermitteln
        context['sets'] = VokabelSet.objects.all()

        # question_set ermitteln
        question = None
        print(f' get: {self.request.GET}')
        if 'set_id' in self.request.GET:
            self.vokabel_set_id = self.request.GET['set_id']
            question_set = Vokabel.get_random(vokabel_set=self.vokabel_set_id)
        else:
            question_set = Vokabel.get_random()

            if randrange(2):
                # print('englisch')
                question = {
                    'id': question_set.id,
                    'question': question_set.german,
                    'hint': question_set.english_description,
                    'answer': question_set.english,
                }
            else:
                print('deutsch')
                question = {
                    'id': question_set.id,
                    'question': question_set.english,
                    'hint': question_set.english_description,
                    'answer': question_set.german,
                }

        context['question_set'] = question
        print(context)
        return context
