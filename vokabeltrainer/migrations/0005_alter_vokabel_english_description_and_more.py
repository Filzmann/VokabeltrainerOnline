# Generated by Django 4.0.2 on 2022-02-22 10:14

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('vokabeltrainer', '0004_lobundaufmunterung'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vokabel',
            name='english_description',
            field=tinymce.models.HTMLField(default=''),
        ),
        migrations.AlterField(
            model_name='vokabel',
            name='example_sentences',
            field=tinymce.models.HTMLField(default=''),
        ),
    ]
