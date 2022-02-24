import random
import django.db.models as models
from django.db.models import Model, CharField, ManyToManyField, TextField, IntegerField
from tinymce.models import HTMLField


# Create your models here.

class VokabelSet(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class LobUndAufmunterung(Model):
    LOB = 'LO'
    AUF = 'AU'
    CHOICES = [
        (LOB, 'Lob für richtiges Ergebnis'),
        (AUF, 'Aufmunterung bei falschem Ergebnis'),
    ]
    type = CharField(
        max_length=2,
        choices=CHOICES,
        default=LOB,
    )
    text = HTMLField(default='')

    @classmethod
    def get_random(cls, l_type):
        query = cls.objects.filter(type=l_type)
        liste = list(query)

        return random.sample(liste, 1)[0]


class Vokabel(Model):
    english = CharField(max_length=255)
    german = CharField(max_length=255)
    english_description = HTMLField(default='')
    example_sentences = HTMLField(default='')
    vokabel_sets = ManyToManyField(to=VokabelSet, related_name='vokabeln', null=True, blank=True)
    correct_answers = IntegerField(default=0)
    wrong_answers = IntegerField(default=0)

    def __str__(self):
        return f'{self.english} - {self.german}'

    @classmethod
    def get_random(cls, vokabel_set=None):
        if vokabel_set:
            query = cls.objects.filter(vokabel_sets=vokabel_set)
        else:
            query = cls.objects.all()
        liste = list(query)
        random_liste = random.sample(liste, 10)

        # größtes falsch - richtig ermitteln
        max_delta = 0
        act_vok = None
        while len(random_liste) > 0:
            vok = random_liste.pop(0)
            print(vok)
            if vok.get_diff() > max_delta:
                max_delta = vok.get_diff()
                act_vok = vok

        return act_vok

    def add_correct(self):
        self.correct_answers += 1
        self.save()

    def add_wrong(self):
        self.wrong_answers += 1
        self.save()

    def get_diff(self):
        return self.wrong_answers - self.correct_answers
