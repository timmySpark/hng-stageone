from django.shortcuts import render
from .serializers import BioSerializer
from .models import Bio
from django.http import JsonResponse,HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def bio_list(request):
    bios = Bio.objects.get()
    serializer= BioSerializer(bios)
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def Arith(request):
    res = " "
    opr = None
    if request.method == "POST":
        data = request.POST
        x=(int(data['x']))
        opr = data['operation_type']
        y = int(data['y'])
        if opr == "+":
            res = x + y
        elif opr == "-":
            res = x-y
        elif opr == "/":
            res = x/y
        else:
            result = "Invalid"
               
    return JsonResponse( {
            "slackUsername":"timmy-spark",
            "result": res,
            "operation_type":opr
            },
        status=status.HTTP_200_OK)

           