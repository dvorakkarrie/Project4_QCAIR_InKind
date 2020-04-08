from django.shortcuts import render
from .models import Volunteer, Service

# Create your views here.
def volunteer_list(request):
    volunteers = Volunteer.objects.order_by('last_name', 'first_name')
    return render(request, 'inkind/volunteer_list.html', {'volunteers': volunteers})

def volunteer_detail(request, pk):
    volunteer = Volunteer.objects.get(id=pk)
    return render(request, 'inkind/volunteer_detail.html', {'volunteer': volunteer})

def service_list(request):
    services = Service.objects.order_by('volunteer', 'year', 'month')
    return render(request, 'inkind/service_list.html', {'services': services})

def service_detail(request, pk):
    service = Service.objects.get(id=pk)
    return render(request, 'inkind/service_detail.html', {'service': service})