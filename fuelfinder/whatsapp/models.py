from django.db import models
from django.contrib.auth.models import User 

class BuyerProfile(models.Model):
    id = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='file')
    phone_number = models.CharField(max_length=20)
    stage = models.CharField(max_length=20)
    position = models.IntegerField()
    

    