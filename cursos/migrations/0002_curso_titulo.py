# Generated by Django 2.2.9 on 2020-09-22 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='titulo',
            field=models.CharField(default='', max_length=255),
        ),
    ]
