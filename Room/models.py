from contextlib import nullcontext
from operator import truediv
from django.db import models
import uuid

# python manage.py makemigrations Room
# python manage.py migrate


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=8)
    title = models.CharField(max_length = 50)
    max_people = models.IntegerField()
