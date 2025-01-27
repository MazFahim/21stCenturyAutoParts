from django.db import models

class UsedSparePartsOptions(models.Model):
    option_id = models.AutoField(primary_key=True)
    option_title = models.CharField(max_length=255)
    option_url = models.URLField()

    def __str__(self):
        return self.option_title
    

class UsedCars(models.Model):
    used_cars_id = models.AutoField(primary_key=True)
    used_car_title = models.CharField(max_length=100)
    milage = models.IntegerField()
    description = models.TextField()


class SparePart(models.Model):
    spare_part_id = models.AutoField(primary_key=True)
    spare_part_title = models.CharField(max_length=100)
    milage = models.IntegerField()
    description = models.TextField()