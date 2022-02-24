import random
import django.db.models as models
from django.db.models import Model, CharField, ManyToManyField, TextField, IntegerField, F
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


class AbstractQuestion(Model):
    correct_answers = IntegerField(default=0)
    wrong_answers = IntegerField(default=0)

    class Meta:
        abstract = True

    @classmethod
    def get_random(cls, query=None):
        if not query:
            query = cls.objects.all()
        query = query.annotate(
            rank=F('wrong_answers') - F('correct_answers')
        ).order_by('-rank')[:10]

        # print(query)
        liste = list(query)
        for elem in liste:
            print(f'{elem.rank} - {elem}')
        return random.sample(liste, 1)[0]


class Vokabel(AbstractQuestion):
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
            query = None
        return super(Vokabel, cls).get_random(query=query)


class InFormal(AbstractQuestion):
    formal = CharField(max_length=255)
    informal = CharField(max_length=255)
    example_informal = HTMLField(default='')
    example_formal = HTMLField(default='')

    def __str__(self):
        return f'{self.formal} - {self.informal}'
