# Generated by Django 2.1.7 on 2019-03-29 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0008_surveys_survey_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveys',
            old_name='question_answer',
            new_name='option_id',
        ),
    ]
