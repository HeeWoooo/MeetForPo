from contextlib import nullcontext
from operator import truediv
from django.db import models
import uuid

# python manage.py makemigrations Room
# python manage.py migrate

def create_code(string_length = 10):
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("=", "")



class Room(models.Model):
#    id = models.CharField(primary_key=True, default=create_code(8), editable=False, max_length=8)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=8)
    title = models.CharField(max_length = 50)
    max_people = models.PositiveIntegerField()
    password = models.CharField(max_length=50, null=True)
    password2 = models.CharField(max_length=50, null=True)
#    head = models.ForeignKey(User, on_delete=models.CASADE)

    #이렇게 하면 안되나 ?? => 접속 할때마다 추가되는지,, => 중복 허용 금지하는 게 있나
    #members = models.ManyToManyField(User, related_name='my_rooms')
 