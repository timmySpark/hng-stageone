import os
from django.shortcuts import render
from .serializers import *
from .models import Bio
from django.http import JsonResponse,HttpRequest, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import openai
import json

# API KEY
OPENAI_API_KEY= "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"

openai.api_key=OPENAI_API_KEY  
# openai.api_key = os.environ.get("OPENAI_API_KEY")

# Create your views here.

def bio_list(request):
    bios = Bio.objects.get()
    serializer= BioSerializer(bios)
    return Response(serializer.data)

#  Api view 1
@api_view(['GET','POST'])
def solve_list(request):

    if request.method == 'POST':
        serializer = SolveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


# Apu view 2
class SolveApiView(APIView):

        def post(self,request,*args,**kwargs):
           
            operations = {
                'addition': '+',
                'subtraction': '-',
                'multiplication': '*',
                'division':'/'
            }

            data = {
                "operation_type":request.data.get('operation_type'),
                "x":request.data.get('x'),
                "y":request.data.get('y'),
            }
            opr = data['operation_type'].lower()
            x = int(data['x'])
            y = int(data['y'])
            if opr in operations:
                print(opr)
                real_opr = operations[opr]
                result = eval(f'{x}{real_opr}{y}')
                print(result)
            else:
                print('something else')
            serializer = SolveSerializer(data=data)
           
            if serializer.is_valid():
                serializer.save() 
                return Response({
                "slackUsername":"timmy-spark",
                "result": result,
                "operation_type":real_opr
                })
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)




def toString(s):  
    # initialize an empty string
    str1 = " "
    # return string 
    return (str1.join(s))
       

# Function()
def solve(request):
    operations = {
                'addition': '+',
                'subtraction': '-',
                'multiplication': '*',
                'division':'/'
            }
   
    if request.GET:
        data = request.GET
    else:
        data = request.data
    # load = json.dumps(data, indent=4)
    # print(load)
    print(data)
        
    opr = data['operation_type'].strip().lower()
    x = int(data['x'])
    y = int(data['y'])

    real_opr = ""
    result = ""

    if opr in operations:
        real_opr = operations[opr]
        result = eval(f'{x}{real_opr}{y}')
    else:

        # varieties = "Find Synonyms:\n\n Subtraction | addition |multiplication"
        varieties = f'Find Math Operator: \n \n {opr} '

        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=varieties,
        temperature=0.2,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
        responses = toString(response['choices'][0]['text'].split(','))
        for special_op in responses:
            for op in operations:
                if operations[op] == special_op:
                    result = eval(f'{x}{operations[op]}{y}')  
                    real_opr = operations[op]

    return  JsonResponse({
                "slackUsername":"timmy-spark",
                "result": result,
                "operation_type":real_opr
                })



   
