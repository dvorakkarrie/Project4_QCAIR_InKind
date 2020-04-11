from rest_framework import serializers
from .models import Volunteer, Service

class VolunteerSerializer(serializers.HyperlinkedModelSerializer):
    services = serializers.HyperlinkedRelatedField(
        view_name='service_detail',
        many=True,
        read_only=True
    )

    volunteer_url = serializers.ModelSerializer.serializer_url_field(
        view_name='volunteer_detail'
    )

    class Meta:
        model = Volunteer
        fields = ('id', 'volunteer_url', 'first_name', 'last_name', 'email_address', 'services')

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    volunteer = serializers.HyperlinkedRelatedField(
        view_name='volunteer_detail',
        read_only=True
    )

    service_url = serializers.ModelSerializer.serializer_url_field(
        view_name='service_detail'
    )

    class Meta:
        model = Service
        fields = ('id', 'service_url', 'month', 'year', 'service_dates', 'description', 'hours_worked', 'hourly_rate', 'total_value_of_service', 'volunteer')

