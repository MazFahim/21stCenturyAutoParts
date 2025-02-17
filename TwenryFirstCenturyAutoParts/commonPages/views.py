from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import *


#Stand Alone Pages
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def contact_us(request):
    template = loader.get_template('contact_us.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def car_services(request):
    template = loader.get_template('car_services.html')
    return HttpResponse(template.render())

#Used Cars function
def used_cars(request):
    cars = UsedCars.objects.all()
    context = {
        'cars': cars
    }
    template = loader.get_template('used_cars.html')
    return HttpResponse(template.render(context, request))

def used_car_detail(request, car_id):
    car = get_object_or_404(UsedCars, pk=car_id)
    return render(request, 'used_car_detail.html', {'car': car})

#Used Spare Parts function
def get_spare_parts_options(request):
    options = UsedSparePartsOptions.objects.all().values('option_title', 'option_url')
    return JsonResponse(list(options), safe=False)

def spare_parts(request):
    spareParts = SparePart.objects.all()
    context = {
        'spareParts': spareParts
    }
    template = loader.get_template('spare_parts.html')
    return HttpResponse(template.render(context, request))

def spare_part_detail(request, spare_part_id):
    spare_part = get_object_or_404(SparePart, pk=spare_part_id)
    return render(request, 'spare_part_detail.html', {'spare_part': spare_part})

def spare_parts_by_company(request, company_name):
    spare_parts = SparePart.objects.filter(spare_part_title__icontains=company_name)
    context = {
        'spareParts': spare_parts,
        'company_name': company_name
    }
    template = loader.get_template('spare_parts_by_company.html')
    return HttpResponse(template.render(context, request))


#search related functions
def search_results(request):
    query = request.GET.get('q', '')
    usedCars = UsedCars.objects.filter(used_car_title__icontains=query)
    spareParts = SparePart.objects.filter(spare_part_title__icontains=query)
    context = {
        'query': query,
        'usedCars': usedCars,
        'spareParts': spareParts
    }
    template = loader.get_template('search_results.html')
    return HttpResponse(template.render(context, request))