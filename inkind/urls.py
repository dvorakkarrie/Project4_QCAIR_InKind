from django.urls import path
from . import views

urlpatterns = [
    path('',views.volunteer_list, name='volunteer_list'),
    path('',views.service_list, name='service_list'),
]