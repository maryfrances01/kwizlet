# Generated by Django 2.1.5 on 2019-12-10 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0016_auto_20191210_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='sentences',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
