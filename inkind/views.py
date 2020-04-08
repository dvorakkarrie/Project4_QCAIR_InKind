from django.shortcuts import render, redirect
from .models import Volunteer, Service
from .forms import VolunteerForm, ServiceForm

# Create your views here.
def volunteer_list(request):
    volunteers = Volunteer.objects.order_by('last_name', 'first_name')
    return render(request, 'inkind/volunteer_list.html', {'volunteers': volunteers})

def volunteer_detail(request, pk):
    volunteer = Volunteer.objects.get(id=pk)
    return render(request, 'inkind/volunteer_detail.html', {'volunteer': volunteer})

def volunteer_create(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            volunteer = form.save()
            return redirect('volunteer_detail', pk=volunteer.pk)
    else:
        form = VolunteerForm()
    return render(request, 'inkind/volunteer_form.html', {'form': form})

def service_list(request):
    services = Service.objects.order_by('volunteer', 'year', 'month')
    return render(request, 'inkind/service_list.html', {'services': services})

def service_detail(request, pk):
    service = Service.objects.get(id=pk)
    return render(request, 'inkind/service_detail.html', {'service': service})

def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save()
            return redirect('service_detail', pk=service.pk)
    else:
        form = ServiceForm()
    return render(request, 'inkind/service_form.html', {'form': form})