# Generated by Django 3.2.3 on 2021-05-28 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eunoia', '0003_auto_20210528_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessmenttest',
            name='added_date',
        ),
        migrations.RemoveField(
            model_name='assessmenttest',
            name='totalQuestions',
        ),
        migrations.AlterField(
            model_name='assessmenttest',
            name='Questions',
            field=models.JSONField(),
        ),
    ]
