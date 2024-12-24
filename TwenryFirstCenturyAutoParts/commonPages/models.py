from django.db import models

class UsedSparePartsOptions(models.Model):
    option_id = models.AutoField(primary_key=True)
    option_title = models.CharField(max_length=255)
    option_url = models.URLField()

    def __str__(self):
        return self.option_title