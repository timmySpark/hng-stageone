from django.shortcuts import render
from .serializers import *
from .models import Bio
from django.http import JsonResponse,HttpRequest, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def bio_list(request):
    bios = Bio.objects.get()
    serializer= BioSerializer(bios)
    return Response(serializer.data)


@api_view(['GET','POST'])
def Arith(request):

    operations = {
        'addition': '+',
        'subtraction': '-',
        'multiplication': '*'
    }

    data = request.GET
    opr = data['operation_type'].lower()

    real_opr = operations[opr]
    x = int(data['x'])
    y = int(data['y'])
    result = eval(f'{x}{real_opr}{y}')
    return  JsonResponse({
                "slackUsername":"timmy-spark",
                "result": result,
                "operation_type":real_opr
                })



   