# Generated by Django 3.1.5 on 2021-01-30 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210130_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_text_tr',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_text_tr',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
