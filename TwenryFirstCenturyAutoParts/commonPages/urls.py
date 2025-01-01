from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('about/', views.about, name='about'),
    path('car_services/', views.car_services, name='car_services'),
    path('used_cars/', views.used_cars, name='used_cars'),
    
    #paths for data fetching using ajax
    path('get-spare-parts-options/', views.get_spare_parts_options, name='get_spare_parts_options'),
]