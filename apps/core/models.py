from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Services(models.Model):
    name = models.CharField(_('Nome do Serviço'), max_length=150)
    value = models.DecimalField(_('Valor do Serviço'), max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = _('Serviço')
        verbose_name_plural = _('Serviços')

    def __str__(self):
        return self.name


class Office(models.Model):
    office = models.CharField(_('Cargo'), max_length=150)
    
    class Meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargos')
        ordering = ['office']

    def __str__(self):
        return self.office


class Employees(models.Model):

    users = models.ForeignKey(User, verbose_name=_('Usuário'), on_delete=models.CASCADE)
    office = models.ManyToManyField(Office, verbose_name=_("Cargo"))

    class Meta:
        verbose_name = _('Funcionário')
        verbose_name_plural = _('Funcionários')
        ordering = ['users']
    
    def __str__(self):
        return self.users.name


class Attendance(models.Model):

    STATUS_ATTENDANCE = (
        ('PE', _('Pendente')),
        ('RE', _('Realizado')),
        ('CA', _('Cancelado')),
    )

    services = models.ForeignKey(Services, verbose_name=_('Serviço Contratado'), on_delete=models.CASCADE)
    users = models.ForeignKey(User, verbose_name=_('Atendente'), on_delete=models.CASCADE)
    discount = models.PositiveSmallIntegerField(_('Desconto'), null=True, blank=True)
    total_value = models.DecimalField(_('Valor Total'), max_digits=8, decimal_places=2)
    date_attendance = models.DateField(_('Data do Atendimento'), auto_now=False, auto_now_add=True)
    date_service = models.DateField(_('Data da Limpeza'), auto_now=False, auto_now_add=False)
    status_attendance = models.CharField(_('Status do Atendimento'), max_length=50, choices=STATUS_ATTENDANCE)
    client_name = models.CharField(_('Nome do Cliente'), max_length=150)
    client_phone = models.CharField(_('Telefone do Cliente'), max_length=14)
    client_address = models.CharField(_('Endereço do Cliente'), max_length=250)

    class Meta():
        verbose_name = _('Atendimento')
        verbose_name_plural = _('Atendimentos')
        ordering = ['services']
    
    def __str__(self):
        return self.services
    