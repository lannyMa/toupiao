# Generated by Django 2.0.6 on 2018-07-20 11:31

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=50)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name=datetime.datetime(2018, 7, 20, 11, 31, 52, 522810, tzinfo=utc))),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question_text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app02.Question'),
        ),
    ]