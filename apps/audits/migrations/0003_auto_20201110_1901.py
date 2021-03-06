# Generated by Django 3.1.2 on 2020-11-10 19:01

from django.db import migrations
from sortedm2m.operations import AlterSortedManyToManyField
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('audits', '0002_auto_20201106_1733'),
    ]

    operations = [
        AlterSortedManyToManyField (
            model_name='template',
            name='questions',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='audits.Question'),
        ),
    ]
