import random

from django.db import models


# Create your models here.

class VokabelSet(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Vokabel(models.Model):
    english = models.CharField(max_length=255)
    german = models.CharField(max_length=255)
    english_description = models.TextField(default='')
    example_sentences = models.TextField(default='')
    vokabel_sets = models.ManyToManyField(to=VokabelSet, related_name='vokabeln', null=True, blank=True)

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


