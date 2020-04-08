from django.db import models

# Create your models here.
class Volunteer(models.Model):
    name = models.CharField(max_length=100, null=True)
    email_address = models.CharField(default='@gmail.com', max_length=100)

    def __str__(self):
        return self.name

class Service(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name='services')
    dates = models.CharField(max_length=100, null=True)
    hours = models.IntegerField(null=True)
    description = models.TextField(default='provide description of services performed')
    rate = models.DecimalField(max_digits=3, decimal_places=2)
    total = models.DecimalField(max_digits=5, decimal_places=2)

    