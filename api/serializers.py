from rest_framework import serializers
from .models import *

class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields = ['slackUsername','backend','age','bio']


class SolveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solve
        fields = '__all__'
