# Generated by Django 3.2.3 on 2021-05-28 07:12

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eunoia', '0002_alter_post_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('totalQuestions', models.IntegerField()),
                ('Questions', models.TextField()),
                ('added_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]