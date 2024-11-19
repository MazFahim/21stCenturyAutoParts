from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def contact_us(request):
    template = loader.get_template('contact_us.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())