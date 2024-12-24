from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import *


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def contact_us(request):
    template = loader.get_template('contact_us.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('car_services.html')
    return HttpResponse(template.render())

#Used Spare Parts function
def get_spare_parts_options(request):
    options = UsedSparePartsOptions.objects.all().values('option_title', 'option_url')
    return JsonResponse(list(options), safe=False)