# Generated by Django 3.1.5 on 2021-01-30 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_question_question_text_fr'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_text_ar',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_text_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_text_fr',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_text_ar',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_text_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_text_fr',
            field=models.CharField(max_length=200, null=True),
        ),
    ]