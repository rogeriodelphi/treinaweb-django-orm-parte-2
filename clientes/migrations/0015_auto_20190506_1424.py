# Generated by Django 2.2 on 2019-05-06 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0014_auto_20190506_1423'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['-data_nascimento']},
        ),
    ]
