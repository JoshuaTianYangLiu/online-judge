# Generated by Django 2.2.19 on 2021-04-05 03:37

from django.db import migrations, models


def hide_scoreboard_eq_true(apps, schema_editor):
    Contest = apps.get_model('judge', 'Contest')
    Contest.objects.filter(hide_scoreboard=True).update(scoreboard_visibility='Contest')


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0114_contest_partially_hide_scoreboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='scoreboard_visibility',
            field=models.CharField(choices=[('Visible', 'Visible'), ('Hidden_for_duration_of_contest', 'Hidden for duration of contest'), ('Hidden_for_duration_of_participation', 'Hidden for duration of participation')], default='Visible', help_text='Scoreboard visibility through the duration of the contest', max_length=64, verbose_name='scoreboard visibility'),
        ),
        migrations.RunPython(hide_scoreboard_eq_true, atomic=True),
    ]
