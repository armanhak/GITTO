# Generated by Django 2.1.7 on 2019-04-06 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0011_auto_20190405_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='date_answers',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dappx.questions'),
            preserve_default=False,
        ),
    ]
