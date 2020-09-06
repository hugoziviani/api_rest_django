from django.db import models as models
from django.core import validators
from django.utils.translation import ugettext_lazy as _
import re

from django.core.exceptions import ValidationError

class Company(models.Model):
    name = models.CharField(max_length=120)
    institutional_registry = models.CharField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Employee(models.Model):
    first_name = models.CharField(_('first_name'), max_length=30, default='')
    last_name = models.CharField(_('last_name'), max_length=30, default='')
    email = models.EmailField(_('email_address'), max_length=255, unique=True)
    username = models.CharField(_('username'), max_length=18, unique=True, help_text=_('Máximo de 18 caracteres ou menos. Letras números e @ . + - _ caracteres'), validators=[ validators.RegexValidator(re.compile(r'^[\w.@+-]+$'), _('Entre com um usuário válido'), _('invalido'))])
    work_for = models.ManyToManyField(Company)
    joined_at = models.DateTimeField(auto_now_add=True)