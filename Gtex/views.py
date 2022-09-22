from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Gtex.models import GeneMedianTpm,SampleAttributesDs,SubjectPhenotypesDd, DiacoTissueAdiposeSubcutaneous, DiacoTissueAdiposeVisceralOm, DiacoTissueAdrenalGland, DiacoTissueArteryCoronary, DiacoTissueBladder, DiacoTissueBrainAmygdala, DiacoTissueBrainAnteriorCcBa24, DiacoTissueBrainCaudateBg, DiacoTissueBrainCerebellarHs, DiacoTissueLiver, ListaGeni, ListaTabelle
from Gtex.serializers import GeneMedianTpmSerializer,SampleAttributesDsSerializer,SubjectPhenotypesDdSerializer, DiacoTissueAdiposeSubcutaneousSerializer, DiacoTissueAdiposeVisceralOmSerializer, DiacoTissueAdrenalGlandSerializer, DiacoTissueArteryCoronarySerializer, DiacoTissueBladderSerializer, DiacoTissueBrainAmygdalaSerializer, DiacoTissueBrainAnteriorCcBa24Serializer, DiacoTissueBrainCaudateBgSerializer, DiacoTissueBrainCerebellarHsSerializer, DiacoTissueLiverSerializer, ListaGeniSerializer, ListaTabelleSerializer

# Tabelle generiche 
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

# Tabelle per singoli tessuti
@csrf_exempt
def diacoTissueAdiposeSubcutaneousApi(request,id=0):
    if request.method=='GET':
        diacoTissueAdiposeSubcutaneouss=DiacoTissueAdiposeSubcutaneous.objects.all()
        diacoTissueAdiposeSubcutaneous_serializer=DiacoTissueAdiposeSubcutaneousSerializer(diacoTissueAdiposeSubcutaneouss,many=True)
        return JsonResponse(diacoTissueAdiposeSubcutaneous_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueAdiposeSubcutaneous_data=JSONParser().parse(request)
        diacoTissueAdiposeSubcutaneous_serializer=DiacoTissueAdiposeSubcutaneousSerializer(data=diacoTissueAdiposeSubcutaneous_data)
        if (diacoTissueAdiposeSubcutaneous_serializer.is_valid()):
            diacoTissueAdiposeSubcutaneous_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueAdiposeSubcutaneous_data=JSONParser().parse(request)
        diacoTissueAdiposeSubcutaneous=DiacoTissueAdiposeSubcutaneous.objects.get(diacoTissueAdiposeSubcutaneousId=diacoTissueAdiposeSubcutaneous_data['subjid'])
        diacoTissueAdiposeSubcutaneous_serializer=DiacoTissueAdiposeSubcutaneousSerializer(diacoTissueAdiposeSubcutaneous,data=diacoTissueAdiposeSubcutaneous_data)
        if (diacoTissueAdiposeSubcutaneous_serializer.is_valid()):
            diacoTissueAdiposeSubcutaneous_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueAdiposeSubcutaneous=DiacoTissueAdiposeSubcutaneous.objects.get(diacoTissueAdiposeSubcutaneousId=id)
        diacoTissueAdiposeSubcutaneous.delete()
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
        diacoTissueAdiposeVisceralOm=DiacoTissueAdiposeVisceralOm.objects.get(diacoTissueAdiposeVisceralOmId=diacoTissueAdiposeVisceralOms_data['subjid'])
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
def diacoTissueArteryAortaApi(request,id=0):
    if request.method=='GET':
        diacoTissueArteryAortas=DiacoTissueArteryAorta.objects.all()
        diacoTissueArteryAorta_serializer=DiacoTissueArteryAortaSerializer(diacoTissueArteryAortas,many=True)
        return JsonResponse(diacoTissueArteryAorta_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueArteryAorta_data=JSONParser().parse(request)
        diacoTissueArteryAorta_serializer=DiacoTissueArteryAortaSerializer(data=diacoTissueArteryAorta_data)
        if (diacoTissueArteryAorta_serializer.is_valid()):
            diacoTissueArteryAorta_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueArteryAorta_data=JSONParser().parse(request)
        diacoTissueArteryAorta=DiacoTissueArteryAorta.objects.get(diacoTissueArteryAortaId=diacoTissueArteryAorta_data['subjid'])
        diacoTissueArteryAorta_serializer=DiacoTissueArteryAortaSerializer(diacoTissueArteryAorta,data=diacoTissueArteryAorta_data)
        if (diacoTissueArteryAorta_serializer.is_valid()):
            diacoTissueArteryAorta_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueArteryAorta=DiacoTissueArteryAorta.objects.get(diacoTissueAdiposeVisceralOmId=id)
        diacoTissueArteryAorta.delete()
        return JsonResponse ("Elimiato con suvvesso!",safe=False)

@csrf_exempt
def diacoTissueArteryCoronaryApi(request,id=0):
    if request.method=='GET':
        diacoTissueArteryCoronarys=DiacoTissueArteryCoronary.objects.all()
        diacoTissueArteryCoronary_serializer=DiacoTissueArteryCoronarySerializer(diacoTissueArteryCoronarys,many=True)
        return JsonResponse(diacoTissueArteryCoronary_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueArteryCoronary_data=JSONParser().parse(request)
        diacoTissueArteryCoronary_serializer=DiacoTissueArteryCoronarySerializer(data=diacoTissueArteryCoronary_data)
        if (diacoTissueArteryCoronary_serializer.is_valid()):
            diacoTissueArteryCoronary_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueArteryCoronary_data=JSONParser().parse(request)
        diacoTissueArteryCoronary=DiacoTissueArteryCoronary.objects.get(diacoTissueArteryCoronaryId=diacoTissueArteryCoronary_data['subjid'])
        diacoTissueArteryCoronary_serializer=DiacoTissueArteryCoronarySerializer(diacoTissueArteryCoronary,data=diacoTissueArteryCoronary_data)
        if (diacoTissueArteryCoronary_serializer.is_valid()):
            diacoTissueArteryCoronary_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueArteryCoronary=DiacoTissueArteryCoronary.objects.get(diacoTissueAdiposeVisceralOmId=id)
        diacoTissueArteryCoronary.delete()
        return JsonResponse ("Elimiato con suvvesso!",safe=False)

@csrf_exempt
def diacoTissueBladderApi(request,id=0):
    if request.method=='GET':
        diacoTissueBladders=DiacoTissueBladder.objects.all()
        diacoTissueBladder_serializer=DiacoTissueBladderSerializer(diacoTissueBladders,many=True)
        return JsonResponse(diacoTissueBladder_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueBladder_data=JSONParser().parse(request)
        diacoTissueBladder_serializer=DiacoTissueBladderSerializer(data=diacoTissueBladder_data)
        if (diacoTissueBladder_serializer.is_valid()):
            diacoTissueBladder_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueBladder_data=JSONParser().parse(request)
        diacoTissueBladder=DiacoTissueBladder.objects.get(diacoTissueBladderId=diacoTissueBladder_data['subjid'])
        diacoTissueBladder_serializer=DiacoTissueBladderSerializer(diacoTissueBladder,data=diacoTissueBladder_data)
        if (diacoTissueBladder_serializer.is_valid()):
            diacoTissueBladder_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueBladder=DiacoTissueBladder.objects.get(diacoTissueBladderId=id)
        diacoTissueBladder.delete()
        return JsonResponse ("Elimiato con suvvesso!",safe=False)

@csrf_exempt
def diacoTissueBrainAmygdalaApi(request,id=0):
    if request.method=='GET':
        diacoTissueBrainAmygdalas=DiacoTissueBrainAmygdala.objects.all()
        diacoTissueBrainAmygdala_serializer=DiacoTissueBrainAmygdalaSerializer(diacoTissueBrainAmygdalas,many=True)
        return JsonResponse(diacoTissueBrainAmygdala_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueBrainAmygdala_data=JSONParser().parse(request)
        diacoTissueBrainAmygdala_serializer=DiacoTissueBrainAmygdalaSerializer(data=diacoTissueBrainAmygdala_data)
        if (diacoTissueBrainAmygdala_serializer.is_valid()):
            diacoTissueBrainAmygdala_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueBrainAmygdala_data=JSONParser().parse(request)
        diacoTissueBrainAmygdala=DiacoTissueBrainAmygdala.objects.get(diacoTissueBrainAmygdalaId=diacoTissueBrainAmygdala_data['subjid'])
        diacoTissueBrainAmygdala_serializer=DiacoTissueBrainAmygdalaSerializer(diacoTissueBrainAmygdala,data=diacoTissueBrainAmygdala_data)
        if (diacoTissueBrainAmygdala_serializer.is_valid()):
            diacoTissueBrainAmygdala_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueBrainAmygdala=DiacoTissueBrainAmygdala.objects.get(diacoTissueBrainAmygdalaId=id)
        diacoTissueBrainAmygdala.delete()
        return JsonResponse ("Elimiato con suvvesso!",safe=False)

@csrf_exempt
def diacoTissueBrainAnteriorCcBa24Api(request,id=0):
    if request.method=='GET':
        diacoTissueBrainAnteriorCcBa24s=DiacoTissueBrainAnteriorCcBa24.objects.all()
        diacoTissueBrainAnteriorCcBa24_serializer=DiacoTissueBrainAnteriorCcBa24Serializer(diacoTissueBrainAnteriorCcBa24s,many=True)
        return JsonResponse(diacoTissueBrainAnteriorCcBa24_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueBrainAnteriorCcBa24_data=JSONParser().parse(request)
        diacoTissueBrainAnteriorCcBa24_serializer=DiacoTissueBrainAnteriorCcBa24Serializer(data=diacoTissueBrainAnteriorCcBa24_data)
        if (diacoTissueBrainAnteriorCcBa24_serializer.is_valid()):
            diacoTissueBrainAnteriorCcBa24_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueBrainAnteriorCcBa24_data=JSONParser().parse(request)
        diacoTissueBrainAnteriorCcBa24=DiacoTissueBrainAnteriorCcBa24.objects.get(diacoTissueBrainAnteriorCcBa24Id=diacoTissueBrainAnteriorCcBa24_data['subjid'])
        diacoTissueBrainAnteriorCcBa24_serializer=DiacoTissueBrainAnteriorCcBa24Serializer(diacoTissueBrainAnteriorCcBa24,data=diacoTissueBrainAnteriorCcBa24_data)
        if (diacoTissueBrainAnteriorCcBa24_serializer.is_valid()):
            diacoTissueBrainAnteriorCcBa24_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueBrainAnteriorCcBa24=DiacoTissueBrainAnteriorCcBa24.objects.get(diacoTissueBrainAnteriorCcBa24Id=id)
        diacoTissueBrainAnteriorCcBa24.delete()
        return JsonResponse ("Elimiato con suvvesso!",safe=False)

@csrf_exempt
def diacoTissueBrainCaudateBgApi(request,id=0):
    if request.method=='GET':
        diacoTissueBrainCaudateBgs=DiacoTissueBrainCaudateBg.objects.all()
        diacoTissueBrainCaudateBg_serializer=DiacoTissueBrainCaudateBgSerializer(diacoTissueBrainCaudateBgs,many=True)
        return JsonResponse(diacoTissueBrainCaudateBg_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueBrainCaudateBg_data=JSONParser().parse(request)
        diacoTissueBrainCaudateBg_serializer=DiacoTissueBrainCaudateBgSerializer(data=diacoTissueBrainCaudateBg_data)
        if (diacoTissueBrainCaudateBg_serializer.is_valid()):
            diacoTissueBrainCaudateBg_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueBrainCaudateBg_data=JSONParser().parse(request)
        diacoTissueBrainCaudateBg=DiacoTissueBrainCaudateBg.objects.get(diacoTissueBrainCaudateBgId=diacoTissueBrainCaudateBg_data['subjid'])
        diacoTissueBrainCaudateBg_serializer=DiacoTissueBrainCaudateBgSerializer(diacoTissueBrainCaudateBg,data=diacoTissueBrainCaudateBg_data)
        if (diacoTissueBrainCaudateBg_serializer.is_valid()):
            diacoTissueBrainCaudateBg_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueBrainCaudateBg=DiacoTissueBrainCaudateBg.objects.get(diacoTissueBrainCaudateBgId=id)
        diacoTissueBrainCaudateBg.delete()
        return JsonResponse ("Elimiato con suvvesso!",safe=False)

@csrf_exempt
def diacoTissueBrainCerebellarHsApi(request,id=0):
    if request.method=='GET':
        diacoTissueBrainCerebellarHss=DiacoTissueBrainCerebellarHs.objects.all()
        diacoTissueBrainCerebellarHs_serializer=DiacoTissueBrainCerebellarHsSerializer(diacoTissueBrainCerebellarHss,many=True)
        return JsonResponse(diacoTissueBrainCerebellarHs_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueBrainCerebellarHs_data=JSONParser().parse(request)
        diacoTissueBrainCerebellarHs_serializer=DiacoTissueBrainCerebellarHsSerializer(data=diacoTissueBrainCerebellarHs_data)
        if (diacoTissueBrainCerebellarHs_serializer.is_valid()):
            diacoTissueBrainCerebellarHs_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueBrainCerebellarHs_data=JSONParser().parse(request)
        diacoTissueBrainCerebellarHs=DiacoTissueBrainCerebellarHs.objects.get(diacoTissueBrainCerebellarHsId=diacoTissueBrainCerebellarHs_data['subjid'])
        diacoTissueBrainCerebellarHs_serializer=DiacoTissueBrainCerebellarHsSerializer(diacoTissueBrainCerebellarHs,data=diacoTissueBrainCerebellarHs_data)
        if (diacoTissueBrainCerebellarHs_serializer.is_valid()):
            diacoTissueBrainCerebellarHs_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueBrainCerebellarHs=DiacoTissueBrainCerebellarHs.objects.get(diacoTissueBrainCerebellarHsId=id)
        diacoTissueBrainCerebellarHs.delete()
        return JsonResponse ("Elimiato con suvvesso!",safe=False)

@csrf_exempt
def diacoTissueLiverApi(request,id=0):
    if request.method=='GET':
        diacoTissueLivers=DiacoTissueLiver.objects.all()
        diacoTissueLiver_serializer=DiacoTissueLiverSerializer(diacoTissueLivers,many=True)
        return JsonResponse(diacoTissueLiver_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueLiver_data=JSONParser().parse(request)
        diacoTissueLiver_serializer=DiacoTissueLiverSerializer(data=diacoTissueLiver_data)
        if (diacoTissueLiver_serializer.is_valid()):
            diacoTissueLiver_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueLiver_data=JSONParser().parse(request)
        diacoTissueLiver=DiacoTissueLiver.objects.get(diacoTissueLiverId=diacoTissueLiver_data['subjid'])
        diacoTissueLiver_serializer=DiacoTissueLiverSerializer(diacoTissueLiver,data=diacoTissueLiver_data)
        if (diacoTissueLiver_serializer.is_valid()):
            diacoTissueLiver_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueLiver=DiacoTissueLiver.objects.get(diacoTissueLiverId=id)
        diacoTissueLiver.delete()
        return JsonResponse ("Elimiato con suvvesso!",safe=False)

# Tabelle per uso lista
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

