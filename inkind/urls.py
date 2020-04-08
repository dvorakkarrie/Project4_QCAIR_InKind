from django.urls import path
from . import views

urlpatterns = [
    path('',views.volunteer_list, name='volunteer_list'),
    path('volunteers/<int:pk>', views.volunteer_detail, name='volunteer_detail'),
    path('services/',views.service_list, name='service_list'),
    path('services/<int:pk>', views.service_detail, name='service_detail'),
]