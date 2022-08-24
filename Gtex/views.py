#Import necessari per far funzionare il file views.py
from ast import Delete
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


