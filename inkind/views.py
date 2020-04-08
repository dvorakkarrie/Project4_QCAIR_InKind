from django.shortcuts import render
from .models import Volunteer, Service

# Create your views here.
def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'inkind/volunteer_list.html', {'volunteers': volunteers})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'inkind/service_list.html', {'services': services})
    