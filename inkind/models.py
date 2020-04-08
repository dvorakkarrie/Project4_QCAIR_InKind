from django.db import models

# Create your models here.
class Volunteer(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email_address = models.CharField(default='@gmail.com', max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Service(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name='services')
    month = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    service_dates = models.CharField(max_length=100, null=True)
    hours_worked = models.IntegerField(null=True)
    description = models.TextField(default='provide description of services performed')
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    total_value_of_service = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self):
        return f"{self.year}-{self.month}: {self.volunteer}"