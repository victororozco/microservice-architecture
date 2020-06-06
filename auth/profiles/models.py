from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    first_name = models.CharField(_("Nombre"), max_length=25)
    last_name = models.CharField(_("Apellido"), max_length=25)
    dni = models.CharField(_("Cedula"), max_length=25, blank=True)
    role = models.IntegerField(_("Rol de Usuario"), null=True, blank=True, default=0)
    email = models.EmailField(_("Email de usuario"), max_length=100)

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.username
