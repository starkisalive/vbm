from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings


class UsersData(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='first name')
    last_name = models.CharField(
        max_length=100, verbose_name='last name', blank=True, null=True, default=None)
    date_of_birth = models.DateField(
        verbose_name='date of birth', blank=True, null=True, default=None)
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(
        auto_now=True, null=True, blank=True)
    credentials = models.ForeignKey(
        CredentialsData, on_delete=models.PROTECT)

    objects = models.Manager()

    def __str__(self):
        return str(self.first_name)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class PhoneNumbers(models.Model):
    phone_number = models.BigIntegerField(null=False, blank=False)
    user = models.ForeignKey(
        UsersData, related_name="phone_numbers", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    USERNAME_FIELD = "user"

    class Meta:
        verbose_name_plural = "Phone numbers"


class Emails(models.Model):
    email = models.EmailField(null=False, blank=False, unique=False)
    user = models.ForeignKey(
        UsersData, related_name="emails", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now=True, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Emails"

    def __str__(self):
        return self.email