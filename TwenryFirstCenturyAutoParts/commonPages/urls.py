from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('about/', views.about, name='about'),
    path('car_services/', views.car_services, name='car_services'),
    path('used_cars/', views.used_cars, name='used_cars'),
    path('spare_parts/', views.spare_parts, name='spare_parts'),

    #path for details page
    path('used_car_detail/<int:car_id>/', views.used_car_detail, name='used_car_detail'),
    path('spare_part_detail/<int:spare_part_id>/', views.spare_part_detail, name='spare_part_detail'),
    
    #paths for data fetching using ajax
    path('get-spare-parts-options/', views.get_spare_parts_options, name='get_spare_parts_options'),
]