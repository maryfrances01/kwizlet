# Generated by Django 4.2.1 on 2023-05-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0019_alter_card_id_alter_card_set_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='definition',
        ),
        migrations.RemoveField(
            model_name='card',
            name='sentences',
        ),
        migrations.RemoveField(
            model_name='card',
            name='word',
        ),
        migrations.AlterField(
            model_name='card',
            name='answer',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='card',
            name='question',
            field=models.CharField(max_length=50),
        ),
    ]