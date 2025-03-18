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
    mainImage = models.ImageField(upload_to='used_cars_images/', blank=True, null=True)
    rightSideView = models.ImageField(upload_to='used_cars_images/', blank=True, null=True)
    leftSideView = models.ImageField(upload_to='used_cars_images/', blank=True, null=True)
    interiorView = models.ImageField(upload_to='used_cars_images/', blank=True, null=True)
    backSideImage = models.ImageField(upload_to='used_cars_images/', blank=True, null=True)
    extraImage = models.ImageField(upload_to='used_cars_images/', blank=True, null=True)
    image1 = models.ImageField(upload_to='used_cars_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='used_cars_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='used_cars_images/', blank=True, null=True)
    company = models.CharField(max_length=100, default="unknown")

    def __str__(self):
        return self.used_car_title


class SparePart(models.Model):
    spare_part_id = models.AutoField(primary_key=True)
    spare_part_title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    categories = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='spare_parts_images/', blank=True, null=True)
    company = models.CharField(max_length=100, default="unknown")
    related_spare_parts = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.spare_part_title
    

class RelatedSpareParts(models.Model):
    related_spare_part_id = models.AutoField(primary_key=True)
    spare_part = models.ForeignKey(SparePart, on_delete=models.CASCADE)

    @property
    def related_spare_part_id(self):
        return self.spare_part.spare_part_id

    @property
    def related_spare_part_title(self):
        return self.spare_part.spare_part_title
    
    @property
    def related_spare_part_image(self):
        return self.spare_part.image.url if self.spare_part.image else None

    def __str__(self):
        return self.related_spare_part_title
