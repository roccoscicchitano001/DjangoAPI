from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Gtex.models import GeneMedianTpm,SampleAttributesDs,SubjectPhenotypesDd,DiacoTissueAdiposeVisceralOm, ListaGeni, ListaTabelle
from Gtex.serializers import GeneMedianTpmSerializer,SampleAttributesDsSerializer,SubjectPhenotypesDdSerializer,DiacoTissueAdiposeVisceralOmSerializer, ListaGeniSerializer, ListaTabelleSerializer

@csrf_exempt
def geneMedianTpmApi(request,id=0):
    if request.method=='GET':
        geneMedianTpms=GeneMedianTpm.objects.all()
        geneMedianTpm_serializer=GeneMedianTpmSerializer(geneMedianTpms,many=True)
        return JsonResponse(geneMedianTpm_serializer.data,safe=False)
    elif request.method=='POST':
        geneMedianTpm_data=JSONParser().parse(request)
        geneMedianTpm_serializer=GeneMedianTpmSerializer(data=geneMedianTpm_data)
        if (geneMedianTpm_serializer.is_valid()):
            geneMedianTpm_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        geneMedianTpm_data=JSONParser().parse(request)
        geneMedianTpm=GeneMedianTpm.objects.get(geneMedianTpmId=geneMedianTpm_data['id'])
        geneMedianTpm_serializer=GeneMedianTpmSerializer(geneMedianTpm,data=geneMedianTpm_data)
        if (geneMedianTpm_serializer.is_valid()):
            geneMedianTpm_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        geneMedianTpm=GeneMedianTpm.objects.get(geneMedianTpmId=id)
        geneMedianTpm.delete()
        return JsonResponse ("Elimiato con suvvesso!",safe=False)

@csrf_exempt
def subjectPhenotypesDdApi(request,id=0):
    if request.method=='GET':
        subjectPhenotypesDds=SubjectPhenotypesDd.objects.all()
        subjectPhenotypesDd_serializer=SubjectPhenotypesDdSerializer(subjectPhenotypesDds,many=True)
        return JsonResponse(subjectPhenotypesDd_serializer.data,safe=False)
    elif request.method=='POST':
        subjectPhenotypesDd_data=JSONParser().parse(request)
        subjectPhenotypesDd_serializer=SubjectPhenotypesDdSerializer(data=subjectPhenotypesDd_data)
        if (subjectPhenotypesDd_serializer.is_valid()):
            subjectPhenotypesDd_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        subjectPhenotypesDd_data=JSONParser().parse(request)
        subjectPhenotypesDd=SubjectPhenotypesDd.objects.get(subjectPhenotypesDdId=subjectPhenotypesDd_data['id'])
        subjectPhenotypesDd_serializer=SubjectPhenotypesDdSerializer(subjectPhenotypesDd,data=subjectPhenotypesDd_data)
        if (subjectPhenotypesDd_serializer.is_valid()):
            subjectPhenotypesDd_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        subjectPhenotypesDd=SubjectPhenotypesDd.objects.get(subjectPhenotypesDdId=id)
        subjectPhenotypesDd.delete()
        return JsonResponse ("Elimiato con suvvesso!",safe=False)

@csrf_exempt
def sampleAttributesDsApi(request,id=0):
    if request.method=='GET':
        sampleAttributesDss=SampleAttributesDs.objects.all()
        sampleAttributesDs_serializer=SampleAttributesDsSerializer(sampleAttributesDss,many=True)
        return JsonResponse(sampleAttributesDs_serializer.data,safe=False)
    elif request.method=='POST':
        sampleAttributesDs_data=JSONParser().parse(request)
        sampleAttributesDs_serializer=SampleAttributesDsSerializer(data=sampleAttributesDs_data)
        if (sampleAttributesDs_serializer.is_valid()):
            sampleAttributesDs_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        sampleAttributesDs_data=JSONParser().parse(request)
        sampleAttributesDs=SampleAttributesDs.objects.get(sampleAttributesDsId=sampleAttributesDs_data['id'])
        sampleAttributesDs_serializer=SampleAttributesDsSerializer(sampleAttributesDs,data=sampleAttributesDs_data)
        if (sampleAttributesDs_serializer.is_valid()):
            sampleAttributesDs_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        sampleAttributesDs=SampleAttributesDs.objects.get(sampleAttributesDsId=id)
        sampleAttributesDs.delete()
        return JsonResponse ("Elimiato con suvvesso!",safe=False)

@csrf_exempt
def diacoTissueAdiposeVisceralOmApi(request,id=0):
    if request.method=='GET':
        diacoTissueAdiposeVisceralOms=DiacoTissueAdiposeVisceralOm.objects.all()
        diacoTissueAdiposeVisceralOm_serializer=DiacoTissueAdiposeVisceralOmSerializer(diacoTissueAdiposeVisceralOms,many=True)
        return JsonResponse(diacoTissueAdiposeVisceralOm_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueAdiposeVisceralOms_data=JSONParser().parse(request)
        diacoTissueAdiposeVisceralOm_serializer=DiacoTissueAdiposeVisceralOmSerializer(data=diacoTissueAdiposeVisceralOms_data)
        if (diacoTissueAdiposeVisceralOm_serializer.is_valid()):
            diacoTissueAdiposeVisceralOm_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueAdiposeVisceralOms_data=JSONParser().parse(request)
        diacoTissueAdiposeVisceralOm=DiacoTissueAdiposeVisceralOm.objects.get(diacoTissueAdiposeVisceralOmId=diacoTissueAdiposeVisceralOms_data['id'])
        diacoTissueAdiposeVisceralOm_serializer=DiacoTissueAdiposeVisceralOmSerializer(diacoTissueAdiposeVisceralOm,data=diacoTissueAdiposeVisceralOms_data)
        if (diacoTissueAdiposeVisceralOm_serializer.is_valid()):
            diacoTissueAdiposeVisceralOm_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueAdiposeVisceralOm=DiacoTissueAdiposeVisceralOm.objects.get(diacoTissueAdiposeVisceralOmId=id)
        diacoTissueAdiposeVisceralOm.delete()
        return JsonResponse ("Elimiato con suvvesso!",safe=False)

@csrf_exempt
def listaGeniApi(request,id=0):
    if request.method=='GET':
        listaGenis=ListaGeni.objects.all()
        listaGeni_serializer=ListaGeniSerializer(listaGenis,many=True)
        return JsonResponse(listaGeni_serializer.data,safe=False)
    elif request.method=='POST':
        listaGeni_data=JSONParser().parse(request)
        listaGeni_serializer=ListaGeniSerializer(data=listaGeni_data)
        if (listaGeni_serializer.is_valid()):
            listaGeni_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        listaGeni_data=JSONParser().parse(request)
        listaGeni=ListaGeni.objects.get(listaGeniId=listaGeni_data['id'])
        listaGeni_serializer=ListaGeniSerializer(listaGeni,data=listaGeni_data)
        if (listaGeni_serializer.is_valid()):
            listaGeni_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        listaGeni=ListaGeni.objects.get(listaGeniId=id)
        listaGeni.delete()
        return JsonResponse ("Elimiato con suvvesso!",safe=False)

@csrf_exempt
def listaTabelleApi(request,id=0):
    if request.method=='GET':
        listaTabelles=ListaTabelle.objects.all()
        listaTabelle_serializer=ListaTabelleSerializer(listaTabelles,many=True)
        return JsonResponse(listaTabelle_serializer.data,safe=False)
    elif request.method=='POST':
        listaTabelle_data=JSONParser().parse(request)
        listaTabelle_serializer=ListaTabelleSerializer(data=listaTabelle_data)
        if (listaTabelle_serializer.is_valid()):
            listaTabelle_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        listaTabelle_data=JSONParser().parse(request)
        listaTabelle=ListaTabelle.objects.get(listaTabelleId=listaTabelle_data['tabella'])
        listaTabelle_serializer=ListaTabelleSerializer(listaTabelle,data=listaTabelle_data)
        if (listaTabelle_serializer.is_valid()):
            listaTabelle_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        listaTabelle=ListaTabelle.objects.get(listaTabelleId=id)
        listaTabelle.delete()
        return JsonResponse ("Elimiato con suvvesso!",safe=False)

