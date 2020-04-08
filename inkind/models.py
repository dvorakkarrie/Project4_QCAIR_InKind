from django.db import models

# Create your models here.
class Volunteer(models.Model):
    name = models.CharField(max_length=100, null=True)
    email_address = models.CharField(default='@gmail.com', max_length=100)

    def __str__(self):
        return self.name

class Service(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name='services')
    service_dates = models.CharField(max_length=100, null=True)
    hours_worked = models.IntegerField(null=True)
    description = models.TextField(default='provide description of services performed')
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    total_value_of_service = models.DecimalField(max_digits=7, decimal_places=2)

    