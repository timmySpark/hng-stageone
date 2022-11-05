from rest_framework import serializers
from .models import *

class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields = ['slackUsername','backend','age','bio']



# create a serializer
class SolveSerializer(serializers.Serializer):
    operation_type = serializers.CharField(max_length = 200,required=True)
    x = serializers.IntegerField(required=True)
    y = serializers.IntegerField(required=True)
   
