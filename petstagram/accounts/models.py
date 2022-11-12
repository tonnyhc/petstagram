from enum import Enum

from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models

class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class Gender(ChoicesEnumMixin, Enum):
    Male = "Male"
    Female = "Female"
    DoNotShow = "Do not show"


class PetstagramUser(auth_models.AbstractUser):
    MAX_LEN_FIST_NAME = 30
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_LAST_NAME = 30
    MIN_LEN_LAST_NAME = 2

    email = models.EmailField(
        unique=True
    )
    first_name = models.CharField(
        max_length=MAX_LEN_FIST_NAME,
        validators= [validators.MinLengthValidator(MIN_LEN_FIRST_NAME)]
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=[validators.MinLengthValidator(MIN_LEN_LAST_NAME)]
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    gender = models.CharField(
        choices = Gender.choices(),
        max_length= Gender.max_len()
    )
