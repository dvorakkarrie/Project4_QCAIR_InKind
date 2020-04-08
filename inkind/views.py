from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Volunteer, Service

from .forms import VolunteerForm, ServiceForm


# Create your views here.
def volunteer_list(request):
    volunteers = Volunteer.objects.order_by('last_name', 'first_name')
    return render(request, 'inkind/volunteer_list.html', {'volunteers': volunteers})

@login_required
def volunteer_detail(request, pk):
    volunteer = Volunteer.objects.get(id=pk)
    return render(request, 'inkind/volunteer_detail.html', {'volunteer': volunteer})

@login_required
def volunteer_create(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            volunteer = form.save()
            return redirect('volunteer_detail', pk=volunteer.pk)
    else:
        form = VolunteerForm()
    return render(request, 'inkind/volunteer_form.html', {'form': form})

@login_required
def volunteer_edit(request, pk):
    volunteer = Volunteer.objects.get(pk=pk)
    if request.method == "POST":
        form = VolunteerForm(request.POST, instance=volunteer)
        if form.is_valid():
            volunteer = form.save()
            return redirect('volunteer_detail', pk=volunteer.pk)
    else:
        form = VolunteerForm(instance=volunteer)
    return render(request, 'inkind/volunteer_form.html', {'form': form})

@login_required
def volunteer_delete(request, pk):
    Volunteer.objects.get(id=pk).delete()
    return redirect('volunteer_list')

def service_list(request):
    services = Service.objects.order_by('volunteer', 'year', 'month')
    return render(request, 'inkind/service_list.html', {'services': services})

@login_required
def service_detail(request, pk):
    service = Service.objects.get(id=pk)
    return render(request, 'inkind/service_detail.html', {'service': service})

@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save()
            return redirect('service_detail', pk=service.pk)
    else:
        form = ServiceForm()
    return render(request, 'inkind/service_form.html', {'form': form})

@login_required
def service_edit(request, pk):
    service = Service.objects.get(pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            service = form.save()
            return redirect('service_detail', pk=service.pk)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'inkind/service_form.html', {'form': form})

@login_required
def service_delete(request, pk):
    Service.objects.get(id=pk).delete()
    return redirect('service_list')