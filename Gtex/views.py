#Import necessari per far funzionare il file views.py
from ast import Delete
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

#Import dei modelli da utilizzares
#from Gtex.models import ...
#from Gtex.serializer import ...

# Create your views here.

"""
@csrf_exempt
def nomedelmodelloApi(request, id=0):
    if request.method=='GET':
        nomedelmodello=modello.object.all()
        nomedelmodello_serializer=nomedelmodelloSerializer(nomedelmodello, many=True)
        return JsonResponse(nomedelmodello_serializer, data, safe=False)
    elif request.method=='POST':
        modello_data=JSONParser().parse(request)
        nomedelmodello_serializer=nomedelmodelloSerializer(data=modello_data)
        if nomedelmodello_serializer.is_valid():
            nomedelmodello_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Fail to Add", safe=False)
    elif request.method=='PUT':
        modello_data=JSONParser().parse(request)
        nomedelmodello=Nomedelmodello.object.get(ModelloId=modello_data['ModelloId'])
        nomedelmodello_serializer=nomedelmodelloSerializer(nomedelmodello, data=modello_data)
        if nomedelmodello_serializer.is_valid():
            nomedelmodello_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Fail to Update")
    elif request.method=='DELETE':
        nomedelmodello=Nomedelmodello.objects.get(NomedelModelloId=nomedelmodello_data['NomedelModelloId'])
        nomedelmodello.delete()
        return JsonResponse("Deleted Successfully", safe=False)
"""

