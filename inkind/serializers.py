from rest_framework import serializers
from .models import Volunteer, Service

class VolunteerSerializer(serializers.HyperlinkedModelSerializer):
    services = serializers.HyperlinkedRelatedField(
        view_name='service_detail',
        many=True,
        read_only=True
    )

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    volunteer = serializers.HyperlinkedRelatedField(
        view_name='volunteer_detail',
        read_only=True
    )