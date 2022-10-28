from rest_framework import serializers
from .models import Bio

class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields = ['slackUsername','backend','age','bio']