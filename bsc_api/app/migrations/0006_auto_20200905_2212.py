# Generated by Django 3.1.1 on 2020-09-05 22:12

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200905_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(help_text='Máximo de 18 ou menos. Letras números e @ . + - _ caracteres', max_length=18, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Entre com um usuário válido', 'invalido')], verbose_name='username'),
        ),
        migrations.RemoveField(
            model_name='employee',
            name='work_for',
        ),
        migrations.AddField(
            model_name='employee',
            name='work_for',
            field=models.ManyToManyField(to='app.Company'),
        ),
    ]