# Generated by Django 2.1.7 on 2019-03-26 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0002_auto_20190326_1752'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='date_answe',
            new_name='date_answers',
        ),
        migrations.AlterModelTable(
            name='date_answers',
            table='date_answers',
        ),
        migrations.AlterModelTable(
            name='options_selection',
            table='options_selection',
        ),
        migrations.AlterModelTable(
            name='qusetions',
            table='qusetions',
        ),
        migrations.AlterModelTable(
            name='raw_text_answer',
            table='raw_text_answer',
        ),
        migrations.AlterModelTable(
            name='surveys',
            table='surveys',
        ),
    ]
