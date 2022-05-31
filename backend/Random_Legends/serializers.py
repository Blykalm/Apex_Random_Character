from rest_framework import serializers
from .models import Legend

class LegendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legend
        fields = ('name', 'legend_class')