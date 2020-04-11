from django import forms
from .models import Volunteer, Service

class VolunteerForm(forms.ModelForm):

    class Meta:
        model = Volunteer
        fields = (
            'first_name', 'last_name', 'email_address', 
            'photo_url'
        )

class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = (
            'volunteer', 'month', 'year', 
            'service_dates', 'description', 
            'hours_worked', 'hourly_rate', 
            'total_value_of_service', 
            'preview_url'
        )
