import random

from django.db.models import Model, CharField, ManyToManyField, TextField
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

    def __str__(self):
        return f'{self.english} - {self.german}'

    @classmethod
    def get_random(cls, vokabel_set=None):
        if vokabel_set:
            query = cls.objects.filter(vokabel_sets=vokabel_set)
        else:
            query = cls.objects.all()
        liste = list(query)

        return random.sample(liste, 1)[0]
