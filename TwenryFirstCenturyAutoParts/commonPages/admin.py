from django.contrib import admin
from .models import *
from django.utils.html import format_html


class UsedCarsAdmin(admin.ModelAdmin):
    list_display = ('used_car_title', 'milage', 'image_preview')
    def image_preview(self, obj):
        if obj.image1:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;"/>', obj.image1.url)
        return "(No Image)"

admin.site.register(UsedSparePartsOptions)
admin.site.register(UsedCars, UsedCarsAdmin)
admin.site.register(SparePart)
admin.site.register(RelatedSpareParts)