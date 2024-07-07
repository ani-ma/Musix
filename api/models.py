from django.db import models
import string
import random 


def generate_unique_code():
    length = 6

    while True:
        code = "".join(random.choices(string.ascii_uppercase,k=length))


# Create your models here.
class Room(models.Model): # Always remember the models creates a unique ID column by default and it needs to mentioned in the serializer
    code = models.CharField(max_length=8,default="",unique=True)
    host = models.CharField(max_length=50,unique=True)
    guest_can_pause = models.BooleanField(null=False,default=False)
    votes_to_skip = models.IntegerField(null=False,default=2)
    created_at = models.DateTimeField(auto_now_add=True)