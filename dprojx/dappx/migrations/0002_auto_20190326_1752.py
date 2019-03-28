# Generated by Django 2.1.7 on 2019-03-26 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='date_answe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_value', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='options_selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_id', models.IntegerField()),
                ('option_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='qusetions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_name', models.CharField(max_length=60)),
                ('question_type', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='raw_text_answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='surveys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_answer', models.IntegerField()),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dappx.qusetions')),
            ],
        ),
        migrations.AddField(
            model_name='options_selection',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dappx.qusetions'),
        ),
    ]
