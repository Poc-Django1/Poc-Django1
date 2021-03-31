from django import forms
from django_enumfield import enum
from django_enumfield.forms.fields import EnumChoiceField
from django_countries.fields import CountryField
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class GenderEnum(enum.Enum):
    MALE = 0
    FEMALE = 1
    OTHERS = 2


class CustomRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50, required=True)
    phone_number = forms.IntegerField(required=True)
    gender = forms.CharField(max_length=1)
    address1 = forms.CharField(max_length=1024)
    address2 = forms.CharField(max_length=1024)
    zip_code = forms.CharField(max_length=12)
    city = forms.CharField(max_length=100)
    country = CountryField()
    additional_information = forms.CharField(max_length=1024)


    class Meta:
        model = CustomUser

        fields = ('username', 'first_name', 'last_name',
                  'email', 'phone_number', 'gender', 'password1', 'password2', 'address1',
                  'address2', 'zip_code', 'city', 'country', 'additional_information')

