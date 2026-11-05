from django.db import models

# Create your models here.

class Item(models.Model):
    item_name= models.CharField(max_length=200)
    item_desc = models.CharField(max_length=500)
    item_price = models.FloatField()
    item_image = models.CharField(max_length=500, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXWerla0KNr2Vu-IMXfvB5icPVK55T-eBWfJ-iR0FNOQ-2rKyhS5AadUY&s")

    def __str__(self):
        return self.item_name
