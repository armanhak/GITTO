# Generated by Django 2.1.7 on 2019-04-05 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0010_auto_20190405_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveys',
            name='option_id',
        ),
        migrations.AddField(
            model_name='surveys',
            name='answer_date_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dappx.date_answers'),
        ),
        migrations.AddField(
            model_name='surveys',
            name='answer_sel_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dappx.options_selection'),
        ),
        migrations.AlterModelTable(
            name='surveys',
            table='survey',
        ),
    ]
