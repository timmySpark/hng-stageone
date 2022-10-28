from django.shortcuts import render
from .serializers import BioSerializer
from .models import Bio
from django.http import JsonResponse


# Create your views here.

def bio_list(request):
    bios = Bio.objects.get()
    serializer= BioSerializer(bios)
    return JsonResponse(serializer.data,safe=False)

