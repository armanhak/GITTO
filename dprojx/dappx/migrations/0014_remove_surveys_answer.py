# Generated by Django 2.1.7 on 2019-04-06 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0013_surveys_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveys',
            name='answer',
        ),
    ]