from .models import contact
from rest_framework import serializers


class contactserializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = contact
        fields = '__all__'
