# Generated by Django 2.1.7 on 2019-03-27 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0006_auto_20190326_1955'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='qusetions',
            new_name='questions',
        ),
        migrations.AlterModelOptions(
            name='questions',
            options={'verbose_name': 'Вопросы'},
        ),
        migrations.AlterModelTable(
            name='questions',
            table='questions',
        ),
    ]
