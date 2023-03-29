from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models

dni_validator = RegexValidator(
    r'^\d{8}[A-Z]$', 'El DNI debe tener 8 dígitos y una letra mayúscula al final.')


class UserManager(BaseUserManager):
    def create_user(self, dni, email, password=None):
        if not dni:
            raise ValueError('El usuario debe tener un DNI')
        if not email:
            raise ValueError('El usuario debe tener un email')
        user = self.model(dni=dni.upper(), email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, dni, email, password):
        user = self.create_user(dni, email, password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    dni = models.CharField(max_length=9, unique=True,
                           validators=[dni_validator])
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'dni'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.dni

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
