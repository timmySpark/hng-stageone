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
    return HttpResponse(result)



    # if request.method == 'GET':
    #     bios = Bio.objects.get()
    #     serializer= BioSerializer(bios)
    #     return Response(serializer.data)
    # if request.method == 'POST':
    #     serializer= ArithSerializer(data=request.data)
    #     if serializer.is_valid():
    #         res = 4
    #         serializer.save()
   
    #     return Response(serializer.data,status=status.HTTP_200_OK)

            # res = " "
    # opr = None
    # print(here)
    # # if request.GET:
    # data = request.data
    # print(data) 
    # raise ImportError
    # x=(int(data['x']))
    # opr = data['operation_type']
    # y = int(data['y'])
    # if opr == "+":
    #     res = x + y
    # elif opr == "-":
    #     res = x-y
    # elif opr == "/":
    #     res = x/y
    # else:
    #     result = "Invalid"
    # {
                # "slackUsername":"timmy-spark",
                # "result": res,
                # "operation_type":opr
                # }
            