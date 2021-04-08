from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy
from django_countries.fields import CountryField
from django_enumfield import enum


class Gender(enum.Enum):
    MALE = 0
    FEMALE = 1
    OTHERS = 2
    __labels__ = {
        MALE: ugettext_lazy("Male"),
        FEMALE: ugettext_lazy("Female"),
        OTHERS: ugettext_lazy("Others"),
    }


class CustomUser(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    id = models.AutoField(primary_key=True)
    email_id = models.CharField(max_length=50, blank=False)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    # phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=("Enter a valid international mobile phone number starting with +(country code)"))
    phone_number = models.IntegerField(blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # date_of_birth = models.DateField(blank=True, null=True)
    address1 = models.CharField(max_length=1024, blank=True, null=True)
    address2 = models.CharField(max_length=1024, blank=True, null=True)
    zip_code = models.CharField(max_length=12, blank=True, null=True)
    city = models.CharField(max_length=1024, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    additional_information = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"
