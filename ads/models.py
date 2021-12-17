from django.db import models
from django.conf import settings

from .utils import create_uuid4_hex


class BaseMixin:
    uuid = models.CharField(
        max_length=255,
        unique=True,
        db_index=True,
        default=create_uuid4_hex,
        verbose_name="UUID",
    )

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


class Profile(BaseMixin, models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )

    address = None

    first_name = models.CharField(max_length=150, blank=True)

    last_name = models.CharField(max_length=150, blank=True)

    date_of_birth = models.DateField(blank=True, null=True)

    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return f"Profile for user {self.user.email}"


class CategoryProposal:
    pass


class Customer:
    address = None


class Supplier:
    address = None


class Request:
    pass


class Proposal:
    pass


class Message:
    pass


class Deal:
    pass


class Rating:
    pass


class Comment:
    pass
