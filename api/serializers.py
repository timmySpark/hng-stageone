from rest_framework import serializers
from .models import *

class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields = ['slackUsername','backend','age','bio']


class ArithSerializer(serializers.ModelSerializer):
    class Meta:
        model = arit
        fields = '__all__'
