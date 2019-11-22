from django.db import models
from django.contrib.auth.models import User 
from ..supplier.models import FuelRequest

class BuyerProfile(models.Model):
    id = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='file')
    fuel_request = models.OneToOneField(FuelRequest,on_delete=models.CASCADE,primary_key=True, )
    phone_number = models.CharField(max_length=20)
    stage = models.CharField(max_length=20)
    position = models.IntegerField()
    

    