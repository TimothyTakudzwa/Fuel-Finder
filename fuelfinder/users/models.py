from django.db import models
from django.dispatch import receiver

from supplier.models import *

from django.db import models
from django.contrib.auth.models import User

class SupplierContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    supplier_profile = models.ForeignKey(SupplierProfile,on_delete=models.CASCADE)

