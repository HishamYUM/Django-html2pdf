from django.db import models

# Create your models here.

class dataModel(models.Model):
    s_no = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    amount = models.FloatField()
