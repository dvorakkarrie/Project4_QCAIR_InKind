from rest_framework import serializers
from .models import Volunteer, Service

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    volunteer = serializers.HyperlinkedRelatedField(
        view_name='volunteer_detail',
        read_only=True
    )

    service_url = serializers.ModelSerializer.serializer_url_field(
        view_name='service_detail',
    )

    class Meta:
        model = Service
        fields = ('id', 'service_url', 'month', 'year', 'service_dates', 'description', 'hours_worked', 'hourly_rate', 'total_value_of_service', 'volunteer')

class VolunteerSerializer(serializers.HyperlinkedModelSerializer):
    services = serializers.HyperlinkedRelatedField(
        view_name='service_detail',
        many=True,
        read_only=True
    )

    services = ServiceSerializer(many=True)

    def create(self, validated_data):
        services_data = validated_data.pop('services')
        volunteer = Volunteer.objects.create(**validated_data)
        for service_data in services_data:
            Service.objects.create(volunteer=volunteer, **service_data)
        return volunteer

    def update(self, instance, validated_data):
        services_data = validated_data.pop('services')
        Volunteer.objects.filter(id=instance.id).update(**validated_data)
        for service_data in services_data:
            Service.objects.get_or_create(volunteer__id=instance.id, defaults=service_data)
        return instance

    volunteer_url = serializers.ModelSerializer.serializer_url_field(
        view_name='volunteer_detail'
    )

    class Meta:
        model = Volunteer
        fields = ('id', 'volunteer_url', 'first_name', 'last_name', 'email_address', 'services')