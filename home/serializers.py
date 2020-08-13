from rest_framework import serializers
from .models import HomeSearch


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSearch
        fields = ('id', 'search_location', 'timestamp')
