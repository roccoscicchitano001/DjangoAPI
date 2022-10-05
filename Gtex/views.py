from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Gtex.models import GeneMedianTpm,SampleAttributesDs,SubjectPhenotypesDd, DiacoTissueAdiposeSubcutaneous, DiacoTissueAdiposeVisceralOm, DiacoTissueAdrenalGland, DiacoTissueArteryAorta, DiacoTissueArteryCoronary, DiacoTissueArteryTibial,DiacoTissueBladder, DiacoTissueBrainAmygdala, DiacoTissueBrainAnteriorCcBa24, DiacoTissueBrainCaudateBg, DiacoTissueBrainCerebellarHs, DiacoTissueBrainCerebellum, DiacoTissueBrainCortex, DiacoTissueBrainFrontalCortexBa9, DiacoTissueBrainHippocampus, DiacoTissueBrainHypothalamus, DiacoTissueBrainNucleusAccumbensBg, DiacoTissueBrainSpinalCordCervicalC1, DiacoTissueBrainPutamenBasalGanglia, DiacoTissueBrainSubstantiaNigra, DiacoTissueBreastMammary, DiacoTissueCellsCulturedFibroblasts, DiacoTissueCellsEbvTransformedLymphocytes, DiacoTissueEsophagusMuscularis, DiacoTissueEsophagusMucosa, DiacoTissueCervixEctocervix, DiacoTissueCervixEndocervix, DiacoTissueColonSigmoid, DiacoTissueColonTransverse, DiacoTissueEsophagusGastroesophagealJunction, DiacoTissueLiver, DiacoTissueStomach, ListaGeni, ListaTabelle
from Gtex.serializers import GeneMedianTpmSerializer,SampleAttributesDsSerializer,SubjectPhenotypesDdSerializer, DiacoTissueAdiposeSubcutaneousSerializer, DiacoTissueAdiposeVisceralOmSerializer, DiacoTissueAdrenalGlandSerializer, DiacoTissueArteryAortaSerializer, DiacoTissueArteryCoronarySerializer, DiacoTissueArteryTibialSerializer, DiacoTissueBladderSerializer, DiacoTissueBrainAmygdalaSerializer, DiacoTissueBrainAnteriorCcBa24Serializer, DiacoTissueBrainCaudateBgSerializer, DiacoTissueBrainCerebellarHsSerializer, DiacoTissueBrainCerebellumSerializer, DiacoTissueBrainCortexSerializer, DiacoTissueBrainFrontalCortexBa9Serializer, DiacoTissueBrainHippocampusSerializer, DiacoTissueBrainHypothalamusSerializer, DiacoTissueBrainSpinalCordCervicalC1Serializer, DiacoTissueBrainSubstantiaNigraSerializer , DiacoTissueBrainNucleusAccumbensBgSerializer, DiacoTissueBrainPutamenBasalGangliaSerializer, DiacoTissueBreastMammarySerializer, DiacoTissueCellsCulturedFibroblastsSerializer, DiacoTissueCellsEbvTransformedLymphocytesSerializer, DiacoTissueColonSigmoidSerializer, DiacoTissueColonTransverseSerializer, DiacoTissueEsophagusMucosaSerializer, DiacoTissueCervixEctocervixSerializer, DiacoTissueCervixEndocervixSerializer, DiacoTissueEsophagusMuscularisSerializer, DiacoTissueEsophagusGastroesophagealJunctionSerializer, DiacoTissueLiverSerializer, DiacoTissueStomachSerializer,ListaGeniSerializer, ListaTabelleSerializer

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
        return JsonResponse ("Elimiato con successo!",safe=False)

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
        return JsonResponse ("Elimiato con successo!",safe=False)

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
        return JsonResponse ("Elimiato con successo!",safe=False)

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
        return JsonResponse ("Elimiato con successo!",safe=False)

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
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueAdrenalGlandApi(request,id=0):
    if request.method=='GET':
        diacoTissueAdrenalGlands=DiacoTissueAdrenalGland.objects.all()
        diacoTissueAdrenalGland_serializer=DiacoTissueAdrenalGlandSerializer(diacoTissueAdrenalGlands,many=True)
        return JsonResponse(diacoTissueAdrenalGland_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueAdrenalGland_data=JSONParser().parse(request)
        diacoTissueAdrenalGland_serializer=DiacoTissueAdrenalGlandSerializer(data=diacoTissueAdrenalGland_data)
        if (diacoTissueAdrenalGland_serializer.is_valid()):
            diacoTissueAdrenalGland_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueAdrenalGland_data=JSONParser().parse(request)
        diacoTissueAdrenalGland=DiacoTissueAdrenalGland.objects.get(diacoTissueAdrenalGlandId=diacoTissueAdrenalGland_data['subjid'])
        diacoTissueAdrenalGland_serializer=DiacoTissueAdiposeVisceralOmSerializer(diacoTissueAdrenalGland,data=diacoTissueAdrenalGland_data)
        if (diacoTissueAdrenalGland_serializer.is_valid()):
            diacoTissueAdrenalGland_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueAdrenalGland=DiacoTissueAdiposeVisceralOm.objects.get(diacoTissueAdrenalGlandId=id)
        diacoTissueAdrenalGland.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

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
        return JsonResponse ("Elimiato con successo!",safe=False)

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
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueArteryTibialApi(request,id=0):
    if request.method=='GET':
        diacoTissueArteryTibials=DiacoTissueArteryTibial.objects.all()
        diacoTissueArteryTibial_serializer=DiacoTissueArteryTibialSerializer(diacoTissueArteryTibials,many=True)
        return JsonResponse(diacoTissueArteryTibial_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueArteryTibial_data=JSONParser().parse(request)
        diacoTissueArteryTibial_serializer=DiacoTissueArteryTibialSerializer(data=diacoTissueArteryTibial_data)
        if (diacoTissueArteryTibial_serializer.is_valid()):
            diacoTissueArteryTibial_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueArteryTibial_data=JSONParser().parse(request)
        diacoTissueArteryTibial=DiacoTissueArteryTibial.objects.get(diacoTissueArteryTibialId=diacoTissueArteryTibial_data['subjid'])
        diacoTissueArteryTibial_serializer=DiacoTissueArteryTibialSerializer(diacoTissueArteryTibial,data=diacoTissueArteryTibial_data)
        if (diacoTissueArteryTibial_serializer.is_valid()):
            diacoTissueArteryTibial_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueArteryTibial=DiacoTissueArteryTibial.objects.get(diacoTissueArteryTibialId=id)
        diacoTissueArteryTibial.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

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
        return JsonResponse ("Elimiato con successo!",safe=False)

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
        return JsonResponse ("Elimiato con successo!",safe=False)

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
        return JsonResponse ("Elimiato con successo!",safe=False)

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
        return JsonResponse ("Elimiato con successo!",safe=False)

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
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueBrainCerebellumApi(request,id=0):
    if request.method=='GET':
        diacoTissueBrainCerebellums=DiacoTissueBrainCerebellum.objects.all()
        diacoTissueBrainCerebellum_serializer=DiacoTissueBrainCerebellumSerializer(diacoTissueBrainCerebellums,many=True)
        return JsonResponse(diacoTissueBrainCerebellum_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueBrainCerebellum_data=JSONParser().parse(request)
        diacoTissueBrainCerebellum_serializer=DiacoTissueBrainCerebellumSerializer(data=diacoTissueBrainCerebellum_data)
        if (diacoTissueBrainCerebellum_serializer.is_valid()):
            diacoTissueBrainCerebellum_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueBrainCerebellum_data=JSONParser().parse(request)
        diacoTissueBrainCerebellum=DiacoTissueBrainCerebellum.objects.get(diacoTissueBrainCerebellumId=diacoTissueBrainCerebellum_data['subjid'])
        diacoTissueBrainCerebellum_serializer=DiacoTissueBrainCerebellumSerializer(diacoTissueBrainCerebellum,data=diacoTissueBrainCerebellum_data)
        if (diacoTissueBrainCerebellum_serializer.is_valid()):
            diacoTissueBrainCerebellum_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueBrainCerebellum=DiacoTissueBrainCerebellum.objects.get(diacoTissueBrainCerebellumId=id)
        diacoTissueBrainCerebellum.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueBrainCortexApi(request,id=0):
    if request.method=='GET':
        diacoTissueBrainCortexs=DiacoTissueBrainCortex.objects.all()
        diacoTissueBrainCortex_serializer=DiacoTissueBrainCortexSerializer(diacoTissueBrainCortexs,many=True)
        return JsonResponse(diacoTissueBrainCortex_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueBrainCortex_data=JSONParser().parse(request)
        diacoTissueBrainCortex_serializer=DiacoTissueBrainCortexSerializer(data=diacoTissueBrainCortex_data)
        if (diacoTissueBrainCortex_serializer.is_valid()):
            diacoTissueBrainCortex_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueBrainCortex_data=JSONParser().parse(request)
        diacoTissueBrainCortex=DiacoTissueBrainCortex.objects.get(diacoTissueBrainCortexId=diacoTissueBrainCortex_data['subjid'])
        diacoTissueBrainCortex_serializer=DiacoTissueBrainCortexSerializer(diacoTissueBrainCortex,data=diacoTissueBrainCortex_data)
        if (diacoTissueBrainCortex_serializer.is_valid()):
            diacoTissueBrainCortex_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueBrainCortex=DiacoTissueBrainCortex.objects.get(DiacoTissueBrainCortexId=id)
        diacoTissueBrainCortex.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueBrainFrontalCortexBa9Api(request,id=0):
    if request.method=='GET':
        diacoTissueBrainFrontalCortexBa9s=DiacoTissueBrainFrontalCortexBa9.objects.all()
        diacoTissueBrainFrontalCortexBa9_serializer=DiacoTissueBrainFrontalCortexBa9Serializer(diacoTissueBrainFrontalCortexBa9s,many=True)
        return JsonResponse(diacoTissueBrainFrontalCortexBa9_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueBrainFrontalCortexBa9_data=JSONParser().parse(request)
        diacoTissueBrainFrontalCortexBa9_serializer=DiacoTissueBrainFrontalCortexBa9Serializer(data=diacoTissueBrainFrontalCortexBa9_data)
        if (diacoTissueBrainFrontalCortexBa9_serializer.is_valid()):
            diacoTissueBrainFrontalCortexBa9_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueBrainFrontalCortexBa9_data=JSONParser().parse(request)
        diacoTissueBrainFrontalCortexBa9=DiacoTissueBrainFrontalCortexBa9.objects.get(diacoTissueBrainFrontalCortexBa9Id=diacoTissueBrainFrontalCortexBa9_data['subjid'])
        diacoTissueBrainFrontalCortexBa9_serializer=DiacoTissueBrainFrontalCortexBa9Serializer(diacoTissueBrainFrontalCortexBa9,data=diacoTissueBrainFrontalCortexBa9_data)
        if (diacoTissueBrainFrontalCortexBa9_serializer.is_valid()):
            diacoTissueBrainFrontalCortexBa9_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueBrainFrontalCortexBa9=DiacoTissueBrainFrontalCortexBa9.objects.get(diacoTissueBrainFrontalCortexBa9Id=id)
        diacoTissueBrainFrontalCortexBa9.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueBrainHippocampusApi(request,id=0):
    if request.method=='GET':
        diacoTissueBrainHippocampuss=DiacoTissueBrainHippocampus.objects.all()
        diacoTissueBrainHippocampus_serializer=DiacoTissueBrainHippocampusSerializer(diacoTissueBrainHippocampuss,many=True)
        return JsonResponse(diacoTissueBrainHippocampus_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueBrainHippocampus_data=JSONParser().parse(request)
        diacoTissueBrainHippocampus_serializer=DiacoTissueBrainHippocampusSerializer(data=diacoTissueBrainHippocampus_data)
        if (diacoTissueBrainHippocampus_serializer.is_valid()):
            diacoTissueBrainHippocampus_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueBrainHippocampus_data=JSONParser().parse(request)
        diacoTissueBrainHippocampus=DiacoTissueBrainHippocampus.objects.get(diacoTissueBrainHippocampusId=diacoTissueBrainHippocampus_data['subjid'])
        diacoTissueBrainHippocampus_serializer=DiacoTissueBrainHippocampusSerializer(diacoTissueBrainHippocampus,data=diacoTissueBrainHippocampus_data)
        if (diacoTissueBrainHippocampus_serializer.is_valid()):
            diacoTissueBrainHippocampus_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueBrainHippocampus=DiacoTissueBrainHippocampus.objects.get(diacoTissueBrainHippocampusId=id)
        diacoTissueBrainHippocampus.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueBrainHypothalamusApi(request,id=0):
    if request.method=='GET':
        diacoTissueBrainHypothalamuss=DiacoTissueBrainHypothalamus.objects.all()
        diacoTissueBrainHypothalamus_serializer=DiacoTissueBrainHypothalamusSerializer(diacoTissueBrainHypothalamuss,many=True)
        return JsonResponse(diacoTissueBrainHypothalamus_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueBrainHypothalamus_data=JSONParser().parse(request)
        diacoTissueBrainHypothalamus_serializer=DiacoTissueBrainHypothalamusSerializer(data=diacoTissueBrainHypothalamus_data)
        if (diacoTissueBrainHypothalamus_serializer.is_valid()):
            diacoTissueBrainHypothalamus_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueBrainHypothalamus_data=JSONParser().parse(request)
        diacoTissueBrainHypothalamus=DiacoTissueBrainHypothalamus.objects.get(diacoTissueBrainHypothalamusId=diacoTissueBrainHypothalamus_data['subjid'])
        diacoTissueBrainHypothalamus_serializer=DiacoTissueBrainHypothalamusSerializer(diacoTissueBrainHypothalamus,data=diacoTissueBrainHypothalamus_data)
        if (diacoTissueBrainHypothalamus_serializer.is_valid()):
            diacoTissueBrainHypothalamus_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueBrainHypothalamus=DiacoTissueBrainHypothalamus.objects.get(diacoTissueBrainHypothalamusId=id)
        diacoTissueBrainHypothalamus.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueBrainSpinalCordCervicalC1Api(request,id=0):
    if request.method=='GET':
        diacoTissueBrainSpinalCordCervicalC1s=DiacoTissueBrainSpinalCordCervicalC1.objects.all()
        diacoTissueBrainSpinalCordCervicalC1_serializer=DiacoTissueBrainSpinalCordCervicalC1Serializer(diacoTissueBrainSpinalCordCervicalC1s,many=True)
        return JsonResponse(diacoTissueBrainSpinalCordCervicalC1_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueBrainSpinalCordCervicalC1_data=JSONParser().parse(request)
        diacoTissueBrainSpinalCordCervicalC1_serializer=DiacoTissueBrainSpinalCordCervicalC1Serializer(data=diacoTissueBrainSpinalCordCervicalC1_data)
        if (diacoTissueBrainSpinalCordCervicalC1_serializer.is_valid()):
            diacoTissueBrainSpinalCordCervicalC1_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueBrainSpinalCordCervicalC1_data=JSONParser().parse(request)
        diacoTissueBrainSpinalCordCervicalC1=DiacoTissueBrainSpinalCordCervicalC1.objects.get(diacoTissueBrainSpinalCordCervicalC1Id=diacoTissueBrainSpinalCordCervicalC1_data['subjid'])
        diacoTissueBrainSpinalCordCervicalC1_serializer=DiacoTissueBrainSpinalCordCervicalC1Serializer(diacoTissueBrainSpinalCordCervicalC1,data=diacoTissueBrainSpinalCordCervicalC1_data)
        if (diacoTissueBrainSpinalCordCervicalC1_serializer.is_valid()):
            diacoTissueBrainSpinalCordCervicalC1_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueBrainSpinalCordCervicalC1=DiacoTissueBrainSpinalCordCervicalC1.objects.get(diacoTissueBrainSpinalCordCervicalC1Id=id)
        diacoTissueBrainSpinalCordCervicalC1.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueBrainSubstantiaNigraApi(request,id=0):
    if request.method=='GET':
        diacoTissueBrainSubstantiaNigras=DiacoTissueBrainSubstantiaNigra.objects.all()
        diacoTissueBrainSubstantiaNigra_serializer=DiacoTissueBrainSubstantiaNigraSerializer(diacoTissueBrainSubstantiaNigras,many=True)
        return JsonResponse(diacoTissueBrainSubstantiaNigra_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueBrainSubstantiaNigra_data=JSONParser().parse(request)
        diacoTissueBrainSubstantiaNigra_serializer=DiacoTissueBrainSubstantiaNigraSerializer(data=diacoTissueBrainSubstantiaNigra_data)
        if (diacoTissueBrainSubstantiaNigra_serializer.is_valid()):
            diacoTissueBrainSubstantiaNigra_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueBrainSubstantiaNigra_data=JSONParser().parse(request)
        diacoTissueBrainSubstantiaNigra=DiacoTissueBrainSubstantiaNigra.objects.get(diacoTissueBrainSubstantiaNigraId=diacoTissueBrainSubstantiaNigra_data['subjid'])
        diacoTissueBrainSubstantiaNigra_serializer=DiacoTissueBrainSubstantiaNigraSerializer(diacoTissueBrainSubstantiaNigra,data=diacoTissueBrainSubstantiaNigra_data)
        if (diacoTissueBrainSubstantiaNigra_serializer.is_valid()):
            diacoTissueBrainSubstantiaNigra_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueBrainSubstantiaNigra=DiacoTissueBrainSubstantiaNigra.objects.get(diacoTissueBrainSubstantiaNigraId=id)
        diacoTissueBrainSubstantiaNigra.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueBrainPutamenBasalGangliaApi(request,id=0):
    if request.method=='GET':
        diacoTissueBrainPutamenBasalGanglias=DiacoTissueBrainPutamenBasalGanglia.objects.all()
        diacoTissueBrainPutamenBasalGanglia_serializer=DiacoTissueBrainPutamenBasalGangliaSerializer(diacoTissueBrainPutamenBasalGanglias,many=True)
        return JsonResponse(diacoTissueBrainPutamenBasalGanglia_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueBrainPutamenBasalGanglia_data=JSONParser().parse(request)
        diacoTissueBrainPutamenBasalGanglia_serializer=DiacoTissueBrainPutamenBasalGangliaSerializer(data=diacoTissueBrainPutamenBasalGanglia_data)
        if (diacoTissueBrainPutamenBasalGanglia_serializer.is_valid()):
            diacoTissueBrainPutamenBasalGanglia_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueBrainPutamenBasalGanglia_data=JSONParser().parse(request)
        diacoTissueBrainPutamenBasalGanglia=DiacoTissueBrainPutamenBasalGanglia.objects.get(diacoTissueBrainPutamenBasalGangliaId=diacoTissueBrainPutamenBasalGanglia_data['subjid'])
        diacoTissueBrainPutamenBasalGanglia_serializer=DiacoTissueBrainPutamenBasalGangliaSerializer(diacoTissueBrainPutamenBasalGanglia,data=diacoTissueBrainPutamenBasalGanglia_data)
        if (diacoTissueBrainPutamenBasalGanglia_serializer.is_valid()):
            diacoTissueBrainPutamenBasalGanglia_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueBrainPutamenBasalGanglia=DiacoTissueBrainPutamenBasalGanglia.objects.get(diacoTissueBrainPutamenBasalGangliaId=id)
        diacoTissueBrainPutamenBasalGanglia.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueBrainNucleusAccumbensBgApi(request,id=0):
    if request.method=='GET':
        diacoTissueBrainNucleusAccumbensBgs=DiacoTissueBrainNucleusAccumbensBg.objects.all()
        diacoTissueBrainNucleusAccumbensBg_serializer=DiacoTissueBrainNucleusAccumbensBgSerializer(diacoTissueBrainNucleusAccumbensBgs,many=True)
        return JsonResponse(diacoTissueBrainNucleusAccumbensBg_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueBrainNucleusAccumbensBg_data=JSONParser().parse(request)
        diacoTissueBrainNucleusAccumbensBg_serializer=DiacoTissueBrainNucleusAccumbensBgSerializer(data=diacoTissueBrainNucleusAccumbensBg_data)
        if (diacoTissueBrainNucleusAccumbensBg_serializer.is_valid()):
            diacoTissueBrainNucleusAccumbensBg_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueBrainNucleusAccumbensBg_data=JSONParser().parse(request)
        diacoTissueBrainNucleusAccumbensBg=DiacoTissueBrainNucleusAccumbensBg.objects.get(diacoTissueBrainNucleusAccumbensBgId=diacoTissueBrainNucleusAccumbensBg_data['subjid'])
        diacoTissueBrainNucleusAccumbensBg_serializer=DiacoTissueBrainNucleusAccumbensBgSerializer(diacoTissueBrainNucleusAccumbensBg,data=diacoTissueBrainNucleusAccumbensBg_data)
        if (diacoTissueBrainNucleusAccumbensBg_serializer.is_valid()):
            diacoTissueBrainNucleusAccumbensBg_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueBrainNucleusAccumbensBg=DiacoTissueBrainNucleusAccumbensBg.objects.get(diacoTissueBrainNucleusAccumbensBgId=id)
        diacoTissueBrainNucleusAccumbensBg.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)         

@csrf_exempt
def diacoTissueBreastMammaryApi(request,id=0):
    if request.method=='GET':
        diacoTissueBreastMammarys=DiacoTissueBreastMammary.objects.all()
        diacoTissueBreastMammary_serializer=DiacoTissueBreastMammarySerializer(diacoTissueBreastMammarys,many=True)
        return JsonResponse(diacoTissueBreastMammary_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueBreastMammary_data=JSONParser().parse(request)
        diacoTissueBreastMammary_serializer=DiacoTissueBreastMammarySerializer(data=diacoTissueBreastMammary_data)
        if (diacoTissueBreastMammary_serializer.is_valid()):
            diacoTissueBreastMammary_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueBreastMammary_data=JSONParser().parse(request)
        diacoTissueBreastMammary=DiacoTissueBreastMammary.objects.get(diacoTissueBreastMammaryId=diacoTissueBreastMammary_data['subjid'])
        diacoTissueBreastMammary_serializer=DiacoTissueBreastMammarySerializer(diacoTissueBreastMammary,data=diacoTissueBreastMammary_data)
        if (diacoTissueBreastMammary_serializer.is_valid()):
            diacoTissueBreastMammary_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueBreastMammary=DiacoTissueBreastMammary.objects.get(diacoTissueBreastMammaryId=id)
        diacoTissueBreastMammary.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueCellsCulturedFibroblastsApi(request,id=0):
    if request.method=='GET':
        diacoTissueCellsCulturedFibroblastss=DiacoTissueCellsCulturedFibroblasts.objects.all()
        diacoTissueCellsCulturedFibroblasts_serializer=DiacoTissueCellsCulturedFibroblastsSerializer(diacoTissueCellsCulturedFibroblastss,many=True)
        return JsonResponse(diacoTissueCellsCulturedFibroblasts_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueCellsCulturedFibroblasts_data=JSONParser().parse(request)
        diacoTissueCellsCulturedFibroblasts_serializer=DiacoTissueCellsCulturedFibroblastsSerializer(data=diacoTissueCellsCulturedFibroblasts_data)
        if (diacoTissueCellsCulturedFibroblasts_serializer.is_valid()):
            diacoTissueCellsCulturedFibroblasts_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueCellsCulturedFibroblasts_data=JSONParser().parse(request)
        diacoTissueCellsCulturedFibroblasts=DiacoTissueCellsCulturedFibroblasts.objects.get(diacoTissueCellsCulturedFibroblastsId=diacoTissueCellsCulturedFibroblasts_data['subjid'])
        diacoTissueCellsCulturedFibroblasts_serializer=DiacoTissueCellsCulturedFibroblastsSerializer(diacoTissueCellsCulturedFibroblasts,data=diacoTissueCellsCulturedFibroblasts_data)
        if (diacoTissueCellsCulturedFibroblasts_serializer.is_valid()):
            diacoTissueCellsCulturedFibroblasts_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueCellsCulturedFibroblasts=DiacoTissueCellsCulturedFibroblasts.objects.get(diacoTissueCellsCulturedFibroblastsId=id)
        diacoTissueCellsCulturedFibroblasts.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueCellsEbvTransformedLymphocytesApi(request,id=0):
    if request.method=='GET':
        diacoTissueCellsEbvTransformedLymphocytess=DiacoTissueCellsEbvTransformedLymphocytes.objects.all()
        diacoTissueCellsEbvTransformedLymphocytes_serializer=DiacoTissueCellsEbvTransformedLymphocytesSerializer(diacoTissueCellsEbvTransformedLymphocytess,many=True)
        return JsonResponse(diacoTissueCellsEbvTransformedLymphocytes_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueCellsEbvTransformedLymphocytes_data=JSONParser().parse(request)
        diacoTissueCellsEbvTransformedLymphocytes_serializer=DiacoTissueCellsEbvTransformedLymphocytesSerializer(data=diacoTissueCellsEbvTransformedLymphocytes_data)
        if (diacoTissueCellsEbvTransformedLymphocytes_serializer.is_valid()):
            diacoTissueCellsEbvTransformedLymphocytes_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueCellsEbvTransformedLymphocytes_data=JSONParser().parse(request)
        diacoTissueCellsEbvTransformedLymphocytes=DiacoTissueCellsEbvTransformedLymphocytes.objects.get(diacoTissueCellsEbvTransformedLymphocytesId=diacoTissueCellsEbvTransformedLymphocytes_data['subjid'])
        diacoTissueCellsEbvTransformedLymphocytes_serializer=DiacoTissueCellsEbvTransformedLymphocytesSerializer(diacoTissueCellsEbvTransformedLymphocytes,data=diacoTissueCellsEbvTransformedLymphocytes_data)
        if (diacoTissueCellsEbvTransformedLymphocytes_serializer.is_valid()):
            diacoTissueCellsEbvTransformedLymphocytes_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueCellsEbvTransformedLymphocytes=DiacoTissueCellsEbvTransformedLymphocytes.objects.get(diacoTissueCellsEbvTransformedLymphocytesId=id)
        diacoTissueCellsEbvTransformedLymphocytes.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)    

@csrf_exempt
def diacoTissueCervixEctocervixApi(request,id=0):
    if request.method=='GET':
        diacoTissueCervixEctocervixs=DiacoTissueCervixEctocervix.objects.all()
        diacoTissueCervixEctocervix_serializer=DiacoTissueCervixEctocervixSerializer(diacoTissueCervixEctocervixs,many=True)
        return JsonResponse(diacoTissueCervixEctocervix_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueCervixEctocervix_data=JSONParser().parse(request)
        diacoTissueCervixEctocervix_serializer=DiacoTissueCervixEctocervixSerializer(data=diacoTissueCervixEctocervix_data)
        if (diacoTissueCervixEctocervix_serializer.is_valid()):
            diacoTissueCervixEctocervix_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueCervixEctocervix_data=JSONParser().parse(request)
        diacoTissueCervixEctocervix=DiacoTissueCervixEctocervix.objects.get(diacoTissueCervixEctocervixId=diacoTissueCervixEctocervix_data['subjid'])
        diacoTissueCervixEctocervix_serializer=DiacoTissueCervixEctocervixSerializer(diacoTissueCervixEctocervix,data=diacoTissueCervixEctocervix_data)
        if (diacoTissueCervixEctocervix_serializer.is_valid()):
            diacoTissueCervixEctocervix_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueCervixEctocervix=DiacoTissueCervixEctocervix.objects.get(diacoTissueCervixEctocervixId=id)
        diacoTissueCervixEctocervix.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueCervixEndocervixApi(request,id=0):
    if request.method=='GET':
        diacoTissueCervixEndocervixs=DiacoTissueCervixEndocervix.objects.all()
        diacoTissueCervixEndocervix_serializer=DiacoTissueCervixEndocervixSerializer(diacoTissueCervixEndocervixs,many=True)
        return JsonResponse(diacoTissueCervixEndocervix_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueCervixEndocervix_data=JSONParser().parse(request)
        diacoTissueCervixEndocervix_serializer=DiacoTissueCervixEndocervixSerializer(data=diacoTissueCervixEndocervix_data)
        if (diacoTissueCervixEndocervix_serializer.is_valid()):
            diacoTissueCervixEndocervix_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueCervixEndocervix_data=JSONParser().parse(request)
        diacoTissueCervixEndocervix=DiacoTissueCervixEndocervix.objects.get(diacoTissueCervixEndocervixId=diacoTissueCervixEndocervix_data['subjid'])
        diacoTissueCervixEndocervix_serializer=DiacoTissueCervixEndocervixSerializer(diacoTissueCervixEndocervix,data=diacoTissueCervixEndocervix_data)
        if (diacoTissueCervixEndocervix_serializer.is_valid()):
            diacoTissueCervixEndocervix_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueCervixEndocervix=DiacoTissueCervixEndocervix.objects.get(diacoTissueCervixEndocervixId=id)
        diacoTissueCervixEndocervix.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueColonSigmoidApi(request,id=0):
    if request.method=='GET':
        diacoTissueColonSigmoids=DiacoTissueColonSigmoid.objects.all()
        diacoTissueColonSigmoid_serializer=DiacoTissueColonSigmoidSerializer(diacoTissueColonSigmoids,many=True)
        return JsonResponse(diacoTissueColonSigmoid_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueColonSigmoid_data=JSONParser().parse(request)
        diacoTissueColonSigmoid_serializer=DiacoTissueColonSigmoidSerializer(data=diacoTissueColonSigmoid_data)
        if (diacoTissueColonSigmoid_serializer.is_valid()):
            diacoTissueColonSigmoid_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueColonSigmoid_data=JSONParser().parse(request)
        diacoTissueColonSigmoid=DiacoTissueColonSigmoid.objects.get(diacoTissueColonSigmoidId=diacoTissueColonSigmoid_data['subjid'])
        diacoTissueColonSigmoid_serializer=DiacoTissueColonSigmoidSerializer(diacoTissueColonSigmoid,data=diacoTissueColonSigmoid_data)
        if (diacoTissueColonSigmoid_serializer.is_valid()):
            diacoTissueColonSigmoid_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueColonSigmoid=DiacoTissueColonSigmoid.objects.get(diacoTissueCervixEndocervixId=id)
        diacoTissueColonSigmoid.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueColonTransverseApi(request,id=0):
    if request.method=='GET':
        diacoTissueColonTransverses=DiacoTissueColonTransverse.objects.all()
        diacoTissueColonTransverse_serializer=DiacoTissueColonTransverseSerializer(diacoTissueColonTransverses,many=True)
        return JsonResponse(diacoTissueColonTransverse_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueColonTransverse_data=JSONParser().parse(request)
        diacoTissueColonTransverse_serializer=DiacoTissueColonTransverseSerializer(data=diacoTissueColonTransverse_data)
        if (diacoTissueColonTransverse_serializer.is_valid()):
            diacoTissueColonTransverse_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueColonTransverse_data=JSONParser().parse(request)
        diacoTissueColonTransverse=DiacoTissueColonTransverse.objects.get(diacoTissueColonTransverseId=diacoTissueColonTransverse_data['subjid'])
        diacoTissueColonTransverse_serializer=DiacoTissueColonTransverseSerializer(diacoTissueColonTransverse,data=diacoTissueColonTransverse_data)
        if (diacoTissueColonTransverse_serializer.is_valid()):
            diacoTissueColonTransverse_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueColonTransverse=DiacoTissueColonTransverse.objects.get(diacoTissueColonTransverseId=id)
        diacoTissueColonTransverse.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueEsophagusGastroesophagealJunctionApi(request,id=0):
    if request.method=='GET':
        diacoTissueEsophagusGastroesophagealJunctions=DiacoTissueEsophagusGastroesophagealJunction.objects.all()
        diacoTissueEsophagusGastroesophagealJunction_serializer=DiacoTissueEsophagusGastroesophagealJunctionSerializer(diacoTissueEsophagusGastroesophagealJunctions,many=True)
        return JsonResponse(diacoTissueEsophagusGastroesophagealJunction_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueEsophagusGastroesophagealJunction_data=JSONParser().parse(request)
        diacoTissueEsophagusGastroesophagealJunction_serializer=DiacoTissueEsophagusGastroesophagealJunctionSerializer(data=diacoTissueEsophagusGastroesophagealJunction_data)
        if (diacoTissueEsophagusGastroesophagealJunction_serializer.is_valid()):
            diacoTissueEsophagusGastroesophagealJunction_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueEsophagusGastroesophagealJunction_data=JSONParser().parse(request)
        diacoTissueEsophagusGastroesophagealJunction=DiacoTissueEsophagusGastroesophagealJunction.objects.get(diacoTissueEsophagusGastroesophagealJunctionId=diacoTissueEsophagusGastroesophagealJunction_data['subjid'])
        diacoTissueEsophagusGastroesophagealJunction_serializer=DiacoTissueEsophagusGastroesophagealJunctionSerializer(diacoTissueEsophagusGastroesophagealJunction,data=diacoTissueEsophagusGastroesophagealJunction_data)
        if (diacoTissueEsophagusGastroesophagealJunction_serializer.is_valid()):
            diacoTissueEsophagusGastroesophagealJunction_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueEsophagusGastroesophagealJunction=DiacoTissueEsophagusGastroesophagealJunction.objects.get(diacoTissueEsophagusGastroesophagealJunctionId=id)
        diacoTissueEsophagusGastroesophagealJunction.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

def diacoTissueEsophagusMucosaApi(request,id=0):
    if request.method=='GET':
        diacoTissueEsophagusMucosas=DiacoTissueEsophagusMucosa.objects.all()
        diacoTissueEsophagusMucosa_serializer=DiacoTissueEsophagusMucosaSerializer(diacoTissueEsophagusMucosas,many=True)
        return JsonResponse(diacoTissueEsophagusMucosa_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueEsophagusMucosa_data=JSONParser().parse(request)
        diacoTissueEsophagusMucosa_serializer=DiacoTissueEsophagusMucosaSerializer(data=diacoTissueEsophagusMucosa_data)
        if (diacoTissueEsophagusMucosa_serializer.is_valid()):
            diacoTissueEsophagusMucosa_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueEsophagusMucosa_data=JSONParser().parse(request)
        diacoTissueEsophagusMucosa=DiacoTissueEsophagusMucosa.objects.get(diacoTissueEsophagusMucosaId=diacoTissueEsophagusMucosa_data['subjid'])
        diacoTissueEsophagusMucosa_serializer=DiacoTissueEsophagusMucosaSerializer(diacoTissueEsophagusMucosa,data=diacoTissueEsophagusMucosa_data)
        if (diacoTissueEsophagusMucosa_serializer.is_valid()):
            diacoTissueEsophagusMucosa_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueEsophagusMucosa=DiacoTissueEsophagusMucosa.objects.get(diacoTissueEsophagusMucosaId=id)
        diacoTissueEsophagusMucosa.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)
    
def diacoTissueEsophagusMuscularisApi(request,id=0):
    if request.method=='GET':
        diacoTissueEsophagusMusculariss=DiacoTissueEsophagusMuscularis.objects.all()
        diacoTissueEsophagusMuscularis_serializer=DiacoTissueEsophagusMuscularisSerializer(diacoTissueEsophagusMusculariss,many=True)
        return JsonResponse(diacoTissueEsophagusMuscularis_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueEsophagusMuscularis_data=JSONParser().parse(request)
        diacoTissueEsophagusMuscularis_serializer=DiacoTissueEsophagusMuscularisSerializer(data=diacoTissueEsophagusMuscularis_data)
        if (diacoTissueEsophagusMuscularis_serializer.is_valid()):
            diacoTissueEsophagusMuscularis_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueEsophagusMuscularis_data=JSONParser().parse(request)
        diacoTissueEsophagusMuscularis=DiacoTissueEsophagusMuscularis.objects.get(diacoTissueEsophagusMuscularisId=diacoTissueEsophagusMuscularis_data['subjid'])
        diacoTissueEsophagusMuscularis_serializer=DiacoTissueEsophagusMuscularisSerializer(diacoTissueEsophagusMuscularis,data=diacoTissueEsophagusMuscularis_data)
        if (diacoTissueEsophagusMuscularis_serializer.is_valid()):
            diacoTissueEsophagusMuscularis_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueEsophagusMuscularis=DiacoTissueEsophagusMuscularis.objects.get(diacoTissueEsophagusMuscularisId=id)
        diacoTissueEsophagusMuscularis.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)
 
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
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueStomachApi(request,id=0):
    if request.method=='GET':
        diacoTissueStomachs=DiacoTissueStomach.objects.all()
        diacoTissueStomach_serializer=DiacoTissueStomachSerializer(diacoTissueStomachs,many=True)
        return JsonResponse(diacoTissueStomach_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueStomach_data=JSONParser().parse(request)
        diacoTissueStomach_serializer=DiacoTissueStomachSerializer(data=diacoTissueStomach_data)
        if (diacoTissueStomach_serializer.is_valid()):
            diacoTissueStomach_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueStomach_data=JSONParser().parse(request)
        diacoTissueStomach=DiacoTissueStomach.objects.get(diacoTissueStomachId=diacoTissueStomach_data['subjid'])
        diacoTissueStomach_serializer=DiacoTissueStomachSerializer(diacoTissueStomach,data=diacoTissueStomach_data)
        if (diacoTissueStomach_serializer.is_valid()):
            diacoTissueStomach_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueStomach=DiacoTissueStomach.objects.get(diacoTissueStomachId=id)
        diacoTissueStomach.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

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
        return JsonResponse ("Elimiato con successo!",safe=False)

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
        return JsonResponse ("Elimiato con successo!",safe=False)

