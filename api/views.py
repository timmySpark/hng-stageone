import os
from django.shortcuts import render
from .serializers import *
from .models import Bio
from django.http import JsonResponse,HttpRequest, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import openai

# API KEY

openai.api_key = os.environ.get("OPENAI_API_KEY")

# Create your views here.

def bio_list(request):
    bios = Bio.objects.get()
    serializer= BioSerializer(bios)
    return Response(serializer.data)
 
def listToString(s):
   
    # initialize an empty string
    str1 = " "
   
    # return string 
    return (str1.join(s))
       


@api_view(['GET','POST'])
def solve(request):

    operations = {
        'addition': '+',
        'subtraction': '-',
        'multiplication': '*'
    }

    data = request.GET
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
        responses = listToString(response['choices'][0]['text'].split(','))
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



   
