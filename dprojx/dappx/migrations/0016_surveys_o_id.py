# Generated by Django 2.1.7 on 2019-04-06 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0015_auto_20190406_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveys',
            name='o_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dappx.options_selection'),
        ),
    ]