from django.urls import path
from . import views

urlpatterns = [
    path('',views.volunteer_list, name='volunteer_list'),
    path('volunteers/<int:pk>', views.volunteer_detail, name='volunteer_detail'),
    path('volunteer/new', views.volunteer_create, name='volunteer_create'),
    path('volunteers/<int:pk>/edit', views.volunteer_edit, name='volunteer_edit'),
    path('volunteers/<int:pk>/delete', views.volunteer_delete, name='volunteer_delete'),
    path('services/',views.service_list, name='service_list'),
    path('services/<int:pk>', views.service_detail, name='service_detail'),
    path('service/new', views.service_create, name='service_create'),
    path('services/<int:pk>/edit', views.service_edit, name='service_edit'),
    path('services/<int:pk>/delete', views.service_delete, name='service_delete'),
]