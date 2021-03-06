# Generated by Django 3.1.1 on 2020-09-05 21:57

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200905_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='created_at',
            new_name='joined_at',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.AddField(
            model_name='employee',
            name='first_name',
            field=models.CharField(default='', max_length=30, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default='', max_length=30, verbose_name='last_name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email_address'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(help_text='Máximo de 18 ou menos. Letras números e @/./+/-/_ caracteres', max_length=18, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Entre com um usuário válido', 'invalido')], verbose_name='username'),
        ),
    ]
