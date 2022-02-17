from django.db import models


# Create your models here.

class VokabelSet(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Vokabel(models.Model):
    english = models.CharField(max_length=255)
    german = models.CharField(max_length=255)
    english_description = models.TextField()
    vokabel_sets = models.ManyToManyField(to=VokabelSet, related_name='vokabeln')
    # ToDo  add later
    # synonyms = models.ManyToManyField(to='self', related_name='synonyms')

    def __str__(self):
        return f'{self.english} - {self.german}'
