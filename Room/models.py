from django.db import models

# python manage.py makemigrations Room
# python manage.py migrate

class Room(models.Model):
    room_code = models.CharField(max_length = 10, unique = True, primary_key = True)
    title = models.CharField(max_length = 50)
    max_people = models.IntegerField()
