# Generated by Django 2.1.7 on 2019-04-06 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0016_surveys_o_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveys',
            name='answer_sel_id',
        ),
    ]
