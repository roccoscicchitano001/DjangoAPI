from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Gtex.models import GeneMedianTpm,SampleAttributesDs,SubjectPhenotypesDd, DiacoTissueAdiposeSubcutaneous, DiacoTissueAdiposeVisceralOm, DiacoTissueAdrenalGland, DiacoTissueArteryAorta, DiacoTissueArteryCoronary, DiacoTissueArteryTibial,DiacoTissueBladder, DiacoTissueBrainAmygdala, DiacoTissueBrainAnteriorCcBa24, DiacoTissueBrainCaudateBg, DiacoTissueBrainCerebellarHs, DiacoTissueBrainCerebellum, DiacoTissueBrainCortex, DiacoTissueBrainFrontalCortexBa9, DiacoTissueBrainHippocampus, DiacoTissueBrainHypothalamus, DiacoTissueBrainNucleusAccumbensBg, DiacoTissueBrainSpinalCordCervicalC1, DiacoTissueBrainPutamenBasalGanglia, DiacoTissueBrainSubstantiaNigra, DiacoTissueBreastMammary, DiacoTissueCellsCulturedFibroblasts, DiacoTissueCellsEbvTransformedLymphocytes, DiacoTissueEsophagusMuscularis, DiacoTissueEsophagusMucosa, DiacoTissueCervixEctocervix, DiacoTissueCervixEndocervix, DiacoTissueColonSigmoid, DiacoTissueColonTransverse, DiacoTissueEsophagusGastroesophagealJunction, DiacoTissueFallopianTube, DiacoTissueHeartAtrialAppendage, DiacoTissueHeartLeftVentricle, DiacoTissueKidneyCortex, DiacoTissueKidneyMedulla, DiacoTissueLiver, DiacoTissueLung, DiacoTissueSpleen, DiacoTissueMinorSalivaryGland, DiacoTissueMuscleSkeletal, DiacoTissueNerveTibial, DiacoTissueOvary, DiacoTissuePancreas, DiacoTissuePituitary, DiacoTissueProstate, DiacoTissueSkinNotSunExposedSuprapubic, DiacoTissueSkinSunExposedLowerLeg, DiacoTissueSmallIntestineTerminalIleum, DiacoTissueStomach, DiacoTissueWholeBlood, DiacoTissueVagina, DiacoTissueTestis, DiacoTissueThyroid, DiacoTissueUterus, ListaGeni, ListaTabelle
from Gtex.serializers import GeneMedianTpmSerializer,SampleAttributesDsSerializer,SubjectPhenotypesDdSerializer, DiacoTissueAdiposeSubcutaneousSerializer, DiacoTissueAdiposeVisceralOmSerializer, DiacoTissueAdrenalGlandSerializer, DiacoTissueArteryAortaSerializer, DiacoTissueArteryCoronarySerializer, DiacoTissueArteryTibialSerializer, DiacoTissueBladderSerializer, DiacoTissueBrainAmygdalaSerializer, DiacoTissueBrainAnteriorCcBa24Serializer, DiacoTissueBrainCaudateBgSerializer, DiacoTissueBrainCerebellarHsSerializer, DiacoTissueBrainCerebellumSerializer, DiacoTissueBrainCortexSerializer, DiacoTissueBrainFrontalCortexBa9Serializer, DiacoTissueBrainHippocampusSerializer, DiacoTissueBrainHypothalamusSerializer, DiacoTissueBrainSpinalCordCervicalC1Serializer, DiacoTissueBrainSubstantiaNigraSerializer , DiacoTissueBrainNucleusAccumbensBgSerializer, DiacoTissueBrainPutamenBasalGangliaSerializer, DiacoTissueBreastMammarySerializer, DiacoTissueCellsCulturedFibroblastsSerializer, DiacoTissueCellsEbvTransformedLymphocytesSerializer, DiacoTissueColonSigmoidSerializer, DiacoTissueColonTransverseSerializer, DiacoTissueEsophagusMucosaSerializer, DiacoTissueCervixEctocervixSerializer, DiacoTissueCervixEndocervixSerializer, DiacoTissueEsophagusMuscularisSerializer, DiacoTissueEsophagusGastroesophagealJunctionSerializer, DiacoTissueFallopianTubeSerializer, DiacoTissueHeartAtrialAppendageSerializer, DiacoTissueHeartLeftVentricleSerializer, DiacoTissueKidneyCortexSerializer, DiacoTissueKidneyMedullaSerializer, DiacoTissueLiverSerializer, DiacoTissueLungSerializer, DiacoTissueOvarySerializer, DiacoTissueSpleenSerializer, DiacoTissuePancreasSerializer, DiacoTissueProstateSerializer, DiacoTissuePituitarySerializer, DiacoTissueNerveTibialSerializer, DiacoTissueMuscleSkeletalSerializer, DiacoTissueMinorSalivaryGlandSerializer, DiacoTissueSkinSunExposedLowerLegSerializer, DiacoTissueSkinNotSunExposedSuprapubicSerializer, DiacoTissueSmallIntestineTerminalIleumSerializer, DiacoTissueStomachSerializer, DiacoTissueTestisSerializer, DiacoTissueUterusSerializer, DiacoTissueVaginaSerializer, DiacoTissueThyroidSerializer, DiacoTissueWholeBloodSerializer, ListaGeniSerializer, ListaTabelleSerializer

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
def diacoTissueFallopianTubeApi(request,id=0):
    if request.method=='GET':
        diacoTissueFallopianTubes=DiacoTissueFallopianTube.objects.all()
        diacoTissueFallopianTube_serializer=DiacoTissueFallopianTubeSerializer(diacoTissueFallopianTubes,many=True)
        return JsonResponse(diacoTissueFallopianTube_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueFallopianTube_data=JSONParser().parse(request)
        diacoTissueFallopianTube_serializer=DiacoTissueFallopianTubeSerializer(data=diacoTissueFallopianTube_data)
        if (diacoTissueFallopianTube_serializer.is_valid()):
            diacoTissueFallopianTube_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueFallopianTube_data=JSONParser().parse(request)
        diacoTissueFallopianTube=DiacoTissueFallopianTube.objects.get(diacoTissueFallopianTubeId=diacoTissueFallopianTube_data['subjid'])
        diacoTissueFallopianTube_serializer=DiacoTissueFallopianTubeSerializer(diacoTissueFallopianTube,data=diacoTissueFallopianTube_data)
        if (diacoTissueFallopianTube_serializer.is_valid()):
            diacoTissueFallopianTube_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueFallopianTube=DiacoTissueFallopianTube.objects.get(diacoTissueFallopianTubeId=id)
        diacoTissueFallopianTube.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueHeartAtrialAppendageApi(request,id=0):
    if request.method=='GET':
        diacoTissueHeartAtrialAppendages=DiacoTissueHeartAtrialAppendage.objects.all()
        diacoTissueHeartAtrialAppendage_serializer=DiacoTissueHeartAtrialAppendageSerializer(diacoTissueHeartAtrialAppendages,many=True)
        return JsonResponse(diacoTissueHeartAtrialAppendage_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueHeartAtrialAppendage_data=JSONParser().parse(request)
        diacoTissueHeartAtrialAppendage_serializer=DiacoTissueHeartAtrialAppendageSerializer(data=diacoTissueHeartAtrialAppendage_data)
        if (diacoTissueHeartAtrialAppendage_serializer.is_valid()):
            diacoTissueHeartAtrialAppendage_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueHeartAtrialAppendage_data=JSONParser().parse(request)
        diacoTissueHeartAtrialAppendage=DiacoTissueHeartAtrialAppendage.objects.get(diacoTissueHeartAtrialAppendageId=diacoTissueHeartAtrialAppendage_data['subjid'])
        diacoTissueHeartAtrialAppendage_serializer=DiacoTissueHeartAtrialAppendageSerializer(diacoTissueHeartAtrialAppendage,data=diacoTissueHeartAtrialAppendage_data)
        if (diacoTissueHeartAtrialAppendage_serializer.is_valid()):
            diacoTissueHeartAtrialAppendage_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueHeartAtrialAppendage=DiacoTissueHeartAtrialAppendage.objects.get(diacoTissueHeartAtrialAppendageId=id)
        diacoTissueHeartAtrialAppendage.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueHeartLeftVentricleApi(request,id=0):
    if request.method=='GET':
        diacoTissueHeartLeftVentricles=DiacoTissueHeartLeftVentricle.objects.all()
        diacoTissueHeartLeftVentricle_serializer=DiacoTissueHeartLeftVentricleSerializer(diacoTissueHeartLeftVentricles,many=True)
        return JsonResponse(diacoTissueHeartLeftVentricle_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueHeartLeftVentricle_data=JSONParser().parse(request)
        diacoTissueHeartLeftVentricle_serializer=DiacoTissueHeartLeftVentricleSerializer(data=diacoTissueHeartLeftVentricle_data)
        if (diacoTissueHeartLeftVentricle_serializer.is_valid()):
            diacoTissueHeartLeftVentricle_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueHeartLeftVentricle_data=JSONParser().parse(request)
        diacoTissueHeartLeftVentricle=DiacoTissueHeartLeftVentricle.objects.get(diacoTissueHeartLeftVentricleId=diacoTissueHeartLeftVentricle_data['subjid'])
        diacoTissueHeartLeftVentricle_serializer=DiacoTissueHeartLeftVentricleSerializer(diacoTissueHeartLeftVentricle,data=diacoTissueHeartLeftVentricle_data)
        if (diacoTissueHeartLeftVentricle_serializer.is_valid()):
            diacoTissueHeartLeftVentricle_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueHeartLeftVentricle=DiacoTissueHeartLeftVentricle.objects.get(diacoTissueHeartLeftVentricleId=id)
        diacoTissueHeartLeftVentricle.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueKidneyCortexApi(request,id=0):
    if request.method=='GET':
        diacoTissueKidneyCortexs=DiacoTissueKidneyCortex.objects.all()
        diacoTissueKidneyCortex_serializer=DiacoTissueKidneyCortexSerializer(diacoTissueKidneyCortexs,many=True)
        return JsonResponse(diacoTissueKidneyCortex_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueKidneyCortex_data=JSONParser().parse(request)
        diacoTissueKidneyCortex_serializer=DiacoTissueKidneyCortexSerializer(data=diacoTissueKidneyCortex_data)
        if (diacoTissueKidneyCortex_serializer.is_valid()):
            diacoTissueKidneyCortex_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueKidneyCortex_data=JSONParser().parse(request)
        diacoTissueKidneyCortex=DiacoTissueKidneyCortex.objects.get(diacoTissueKidneyCortexId=diacoTissueKidneyCortex_data['subjid'])
        diacoTissueKidneyCortex_serializer=DiacoTissueKidneyCortexSerializer(diacoTissueKidneyCortex,data=diacoTissueKidneyCortex_data)
        if (diacoTissueKidneyCortex_serializer.is_valid()):
            diacoTissueKidneyCortex_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueKidneyCortex=DiacoTissueKidneyCortex.objects.get(diacoTissueKidneyCortexId=id)
        diacoTissueKidneyCortex.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueKidneyMedullaApi(request,id=0):
    if request.method=='GET':
        diacoTissueKidneyMedullas=DiacoTissueKidneyMedulla.objects.all()
        diacoTissueKidneyMedulla_serializer=DiacoTissueKidneyMedullaSerializer(diacoTissueKidneyMedullas,many=True)
        return JsonResponse(diacoTissueKidneyMedulla_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueKidneyMedulla_data=JSONParser().parse(request)
        diacoTissueKidneyMedulla_serializer=DiacoTissueKidneyMedullaSerializer(data=diacoTissueKidneyMedulla_data)
        if (diacoTissueKidneyMedulla_serializer.is_valid()):
            diacoTissueKidneyMedulla_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueKidneyMedulla_data=JSONParser().parse(request)
        diacoTissueKidneyMedulla=DiacoTissueKidneyMedulla.objects.get(diacoTissueKidneyMedullaId=diacoTissueKidneyMedulla_data['subjid'])
        diacoTissueKidneyMedulla_serializer=DiacoTissueKidneyMedullaSerializer(diacoTissueKidneyMedulla,data=diacoTissueKidneyMedulla_data)
        if (diacoTissueKidneyMedulla_serializer.is_valid()):
            diacoTissueKidneyMedulla_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueKidneyMedulla=DiacoTissueKidneyMedulla.objects.get(diacoTissueKidneyMedullaId=id)
        diacoTissueKidneyMedulla.delete()
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
def diacoTissueLungApi(request,id=0):
    if request.method=='GET':
        diacoTissueLungs=DiacoTissueLung.objects.all()
        diacoTissueLung_serializer=DiacoTissueLungSerializer(diacoTissueLungs,many=True)
        return JsonResponse(diacoTissueLung_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueLung_data=JSONParser().parse(request)
        diacoTissueLung_serializer=DiacoTissueLungSerializer(data=diacoTissueLung_data)
        if (diacoTissueLung_serializer.is_valid()):
            diacoTissueLung_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueLung_data=JSONParser().parse(request)
        diacoTissueLung=DiacoTissueLung.objects.get(diacoTissueLungId=diacoTissueLung_data['subjid'])
        diacoTissueLung_serializer=DiacoTissueLungSerializer(diacoTissueLung,data=diacoTissueLung_data)
        if (diacoTissueLung_serializer.is_valid()):
            diacoTissueLung_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueLung=DiacoTissueLung.objects.get(diacoTissueLungId=id)
        diacoTissueLung.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueMinorSalivaryGlandApi(request,id=0):
    if request.method=='GET':
        diacoTissueMinorSalivaryGlands=DiacoTissueMinorSalivaryGland.objects.all()
        diacoTissueMinorSalivaryGland_serializer=DiacoTissueMinorSalivaryGlandSerializer(diacoTissueMinorSalivaryGlands,many=True)
        return JsonResponse(diacoTissueMinorSalivaryGland_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueMinorSalivaryGland_data=JSONParser().parse(request)
        diacoTissueMinorSalivaryGland_serializer=DiacoTissueMinorSalivaryGlandSerializer(data=diacoTissueMinorSalivaryGland_data)
        if (diacoTissueMinorSalivaryGland_serializer.is_valid()):
            diacoTissueMinorSalivaryGland_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueMinorSalivaryGland_data=JSONParser().parse(request)
        diacoTissueMinorSalivaryGland=DiacoTissueMinorSalivaryGland.objects.get(diacoTissueMinorSalivaryGlandId=diacoTissueMinorSalivaryGland_data['subjid'])
        diacoTissueMinorSalivaryGland_serializer=DiacoTissueMinorSalivaryGlandSerializer(diacoTissueMinorSalivaryGland,data=diacoTissueMinorSalivaryGland_data)
        if (diacoTissueMinorSalivaryGland_serializer.is_valid()):
            diacoTissueMinorSalivaryGland_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueMinorSalivaryGland=DiacoTissueMinorSalivaryGland.objects.get(diacoTissueMinorSalivaryGlandId=id)
        diacoTissueMinorSalivaryGland.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueMuscleSkeletalApi(request,id=0):
    if request.method=='GET':
        diacoTissueMuscleSkeletals=DiacoTissueMuscleSkeletal.objects.all()
        diacoTissueMuscleSkeletal_serializer=DiacoTissueMuscleSkeletalSerializer(diacoTissueMuscleSkeletals,many=True)
        return JsonResponse(diacoTissueMuscleSkeletal_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueMuscleSkeletal_data=JSONParser().parse(request)
        diacoTissueMuscleSkeletal_serializer=DiacoTissueMuscleSkeletalSerializer(data=diacoTissueMuscleSkeletal_data)
        if (diacoTissueMuscleSkeletal_serializer.is_valid()):
            diacoTissueMuscleSkeletal_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueMuscleSkeletal_data=JSONParser().parse(request)
        diacoTissueMuscleSkeletal=DiacoTissueMuscleSkeletal.objects.get(diacoTissueMuscleSkeletalId=diacoTissueMuscleSkeletal_data['subjid'])
        diacoTissueMuscleSkeletal_serializer=DiacoTissueMuscleSkeletalSerializer(diacoTissueMuscleSkeletal,data=diacoTissueMuscleSkeletal_data)
        if (diacoTissueMuscleSkeletal_serializer.is_valid()):
            diacoTissueMuscleSkeletal_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueMuscleSkeletal=DiacoTissueMuscleSkeletal.objects.get(diacoTissueMuscleSkeletalId=id)
        diacoTissueMuscleSkeletal.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueNerveTibialApi(request,id=0):
    if request.method=='GET':
        diacoTissueNerveTibials=DiacoTissueNerveTibial.objects.all()
        diacoTissueNerveTibial_serializer=DiacoTissueNerveTibialSerializer(diacoTissueNerveTibials,many=True)
        return JsonResponse(diacoTissueNerveTibial_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueNerveTibial_data=JSONParser().parse(request)
        diacoTissueNerveTibial_serializer=DiacoTissueNerveTibialSerializer(data=diacoTissueNerveTibial_data)
        if (diacoTissueNerveTibial_serializer.is_valid()):
            diacoTissueNerveTibial_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueNerveTibial_data=JSONParser().parse(request)
        diacoTissueNerveTibial=DiacoTissueNerveTibial.objects.get(diacoTissueNerveTibialId=diacoTissueNerveTibial_data['subjid'])
        diacoTissueNerveTibial_serializer=DiacoTissueNerveTibialSerializer(diacoTissueNerveTibial,data=diacoTissueNerveTibial_data)
        if (diacoTissueNerveTibial_serializer.is_valid()):
            diacoTissueNerveTibial_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueNerveTibial=DiacoTissueNerveTibial.objects.get(diacoTissueNerveTibialId=id)
        diacoTissueNerveTibial.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueOvaryApi(request,id=0):
    if request.method=='GET':
        diacoTissueOvarys=DiacoTissueOvary.objects.all()
        diacoTissueOvary_serializer=DiacoTissueOvarySerializer(diacoTissueOvarys,many=True)
        return JsonResponse(diacoTissueOvary_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueOvary_data=JSONParser().parse(request)
        diacoTissueOvary_serializer=DiacoTissueOvarySerializer(data=diacoTissueOvary_data)
        if (diacoTissueOvary_serializer.is_valid()):
            diacoTissueOvary_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueOvary_data=JSONParser().parse(request)
        diacoTissueOvary=DiacoTissueOvary.objects.get(diacoTissueOvaryId=diacoTissueOvary_data['subjid'])
        diacoTissueOvary_serializer=DiacoTissueOvarySerializer(diacoTissueOvary,data=diacoTissueOvary_data)
        if (diacoTissueOvary_serializer.is_valid()):
            diacoTissueOvary_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueOvary=DiacoTissueOvary.objects.get(diacoTissueOvaryId=id)
        diacoTissueOvary.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissuePancreasApi(request,id=0):
    if request.method=='GET':
        diacoTissuePancreass=DiacoTissuePancreas.objects.all()
        diacoTissuePancreas_serializer=DiacoTissuePancreasSerializer(diacoTissuePancreass,many=True)
        return JsonResponse(diacoTissuePancreas_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissuePancreas_data=JSONParser().parse(request)
        diacoTissuePancreas_serializer=DiacoTissuePancreasSerializer(data=diacoTissuePancreas_data)
        if (diacoTissuePancreas_serializer.is_valid()):
            diacoTissuePancreas_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissuePancreas_data=JSONParser().parse(request)
        diacoTissuePancreas=DiacoTissuePancreas.objects.get(diacoTissuePancreasId=diacoTissuePancreas_data['subjid'])
        diacoTissuePancreas_serializer=DiacoTissuePancreasSerializer(diacoTissuePancreas,data=diacoTissuePancreas_data)
        if (diacoTissuePancreas_serializer.is_valid()):
            diacoTissuePancreas_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissuePancreas=DiacoTissuePancreas.objects.get(diacoTissuePancreasId=id)
        diacoTissuePancreas.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissuePituitaryApi(request,id=0):
    if request.method=='GET':
        diacoTissuePituitarys=DiacoTissuePituitary.objects.all()
        diacoTissuePituitary_serializer=DiacoTissuePituitarySerializer(diacoTissuePituitarys,many=True)
        return JsonResponse(diacoTissuePituitary_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissuePituitary_data=JSONParser().parse(request)
        diacoTissuePituitary_serializer=DiacoTissuePituitarySerializer(data=diacoTissuePituitary_data)
        if (diacoTissuePituitary_serializer.is_valid()):
            diacoTissuePituitary_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissuePituitary_data=JSONParser().parse(request)
        diacoTissuePituitary=DiacoTissuePituitary.objects.get(diacoTissuePituitaryId=diacoTissuePituitary_data['subjid'])
        diacoTissuePituitary_serializer=DiacoTissuePituitarySerializer(diacoTissuePituitary,data=diacoTissuePituitary_data)
        if (diacoTissuePituitary_serializer.is_valid()):
            diacoTissuePituitary_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissuePituitary=DiacoTissuePituitary.objects.get(diacoTissuePituitaryId=id)
        diacoTissuePituitary.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueProstateApi(request,id=0):
    if request.method=='GET':
        diacoTissueProstates=DiacoTissueProstate.objects.all()
        diacoTissueProstate_serializer=DiacoTissueProstateSerializer(diacoTissueProstates,many=True)
        return JsonResponse(diacoTissueProstate_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueProstate_data=JSONParser().parse(request)
        diacoTissueProstate_serializer=DiacoTissueProstateSerializer(data=diacoTissueProstate_data)
        if (diacoTissueProstate_serializer.is_valid()):
            diacoTissueProstate_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueProstate_data=JSONParser().parse(request)
        diacoTissueProstate=DiacoTissueProstate.objects.get(diacoTissueProstateId=diacoTissueProstate_data['subjid'])
        diacoTissueProstate_serializer=DiacoTissueProstateSerializer(diacoTissueProstate,data=diacoTissueProstate_data)
        if (diacoTissueProstate_serializer.is_valid()):
            diacoTissueProstate_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueProstate=DiacoTissueProstate.objects.get(diacoTissueProstateId=id)
        diacoTissueProstate.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueSkinNotSunExposedSuprapubicApi(request,id=0):
    if request.method=='GET':
        diacoTissueSkinNotSunExposedSuprapubics=DiacoTissueSkinNotSunExposedSuprapubic.objects.all()
        diacoTissueSkinNotSunExposedSuprapubic_serializer=DiacoTissueSkinNotSunExposedSuprapubicSerializer(diacoTissueSkinNotSunExposedSuprapubics,many=True)
        return JsonResponse(diacoTissueSkinNotSunExposedSuprapubic_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueSkinNotSunExposedSuprapubic_data=JSONParser().parse(request)
        diacoTissueSkinNotSunExposedSuprapubic_serializer=DiacoTissueSkinNotSunExposedSuprapubicSerializer(data=diacoTissueSkinNotSunExposedSuprapubic_data)
        if (diacoTissueSkinNotSunExposedSuprapubic_serializer.is_valid()):
            diacoTissueSkinNotSunExposedSuprapubic_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueSkinNotSunExposedSuprapubic_data=JSONParser().parse(request)
        diacoTissueSkinNotSunExposedSuprapubic=DiacoTissueSkinNotSunExposedSuprapubic.objects.get(diacoTissueSkinNotSunExposedSuprapubicId=diacoTissueSkinNotSunExposedSuprapubic_data['subjid'])
        diacoTissueSkinNotSunExposedSuprapubic_serializer=DiacoTissueSkinNotSunExposedSuprapubicSerializer(diacoTissueSkinNotSunExposedSuprapubic,data=diacoTissueSkinNotSunExposedSuprapubic_data)
        if (diacoTissueSkinNotSunExposedSuprapubic_serializer.is_valid()):
            diacoTissueSkinNotSunExposedSuprapubic_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueSkinNotSunExposedSuprapubic=DiacoTissueSkinNotSunExposedSuprapubic.objects.get(diacoTissueSkinNotSunExposedSuprapubicId=id)
        diacoTissueSkinNotSunExposedSuprapubic.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueSkinSunExposedLowerLegApi(request,id=0):
    if request.method=='GET':
        diacoTissueSkinSunExposedLowerLegs=DiacoTissueSkinSunExposedLowerLeg.objects.all()
        diacoTissueSkinSunExposedLowerLeg_serializer=DiacoTissueSkinSunExposedLowerLegSerializer(diacoTissueSkinSunExposedLowerLegs,many=True)
        return JsonResponse(diacoTissueSkinSunExposedLowerLeg_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueSkinSunExposedLowerLeg_data=JSONParser().parse(request)
        diacoTissueSkinSunExposedLowerLeg_serializer=DiacoTissueSkinSunExposedLowerLegSerializer(data=diacoTissueSkinSunExposedLowerLeg_data)
        if (diacoTissueSkinSunExposedLowerLeg_serializer.is_valid()):
            diacoTissueSkinSunExposedLowerLeg_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueSkinSunExposedLowerLeg_data=JSONParser().parse(request)
        diacoTissueSkinSunExposedLowerLeg=DiacoTissueSkinSunExposedLowerLeg.objects.get(diacoTissueSkinSunExposedLowerLegId=diacoTissueSkinSunExposedLowerLeg_data['subjid'])
        diacoTissueSkinSunExposedLowerLeg_serializer=DiacoTissueSkinSunExposedLowerLegSerializer(diacoTissueSkinSunExposedLowerLeg,data=diacoTissueSkinSunExposedLowerLeg_data)
        if (diacoTissueSkinSunExposedLowerLeg_serializer.is_valid()):
            diacoTissueSkinSunExposedLowerLeg_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueSkinSunExposedLowerLeg=DiacoTissueSkinSunExposedLowerLeg.objects.get(diacoTissueSkinSunExposedLowerLegId=id)
        diacoTissueSkinSunExposedLowerLeg.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueSmallIntestineTerminalIleumApi(request,id=0):
    if request.method=='GET':
        diacoTissueSmallIntestineTerminalIleums=DiacoTissueSmallIntestineTerminalIleum.objects.all()
        diacoTissueSmallIntestineTerminalIleum_serializer=DiacoTissueSmallIntestineTerminalIleumSerializer(diacoTissueSmallIntestineTerminalIleums,many=True)
        return JsonResponse(diacoTissueSmallIntestineTerminalIleum_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueSmallIntestineTerminalIleum_data=JSONParser().parse(request)
        diacoTissueSmallIntestineTerminalIleum_serializer=DiacoTissueSmallIntestineTerminalIleumSerializer(data=diacoTissueSmallIntestineTerminalIleum_data)
        if (diacoTissueSmallIntestineTerminalIleum_serializer.is_valid()):
            diacoTissueSmallIntestineTerminalIleum_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueSmallIntestineTerminalIleum_data=JSONParser().parse(request)
        diacoTissueSmallIntestineTerminalIleum=DiacoTissueSmallIntestineTerminalIleum.objects.get(diacoTissueSmallIntestineTerminalIleumId=diacoTissueSmallIntestineTerminalIleum_data['subjid'])
        diacoTissueSmallIntestineTerminalIleum_serializer=DiacoTissueSmallIntestineTerminalIleumSerializer(diacoTissueSmallIntestineTerminalIleum,data=diacoTissueSmallIntestineTerminalIleum_data)
        if (diacoTissueSmallIntestineTerminalIleum_serializer.is_valid()):
            diacoTissueSmallIntestineTerminalIleum_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueSmallIntestineTerminalIleum=DiacoTissueSmallIntestineTerminalIleum.objects.get(diacoTissueSmallIntestineTerminalIleumId=id)
        diacoTissueSmallIntestineTerminalIleum.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueSpleenApi(request,id=0):
    if request.method=='GET':
        diacoTissueSpleens=DiacoTissueSpleen.objects.all()
        diacoTissueSpleen_serializer=DiacoTissueSpleenSerializer(diacoTissueSpleens,many=True)
        return JsonResponse(diacoTissueSpleen_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueSpleen_data=JSONParser().parse(request)
        diacoTissueSpleen_serializer=DiacoTissueSpleenSerializer(data=diacoTissueSpleen_data)
        if (diacoTissueSpleen_serializer.is_valid()):
            diacoTissueSpleen_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueSpleen_data=JSONParser().parse(request)
        diacoTissueSpleen=DiacoTissueSpleen.objects.get(diacoTissueSpleenId=diacoTissueSpleen_data['subjid'])
        diacoTissueSpleen_serializer=DiacoTissueSpleenSerializer(diacoTissueSpleen,data=diacoTissueSpleen_data)
        if (diacoTissueSpleen_serializer.is_valid()):
            diacoTissueSpleen_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueSpleen=DiacoTissueSpleen.objects.get(diacoTissueSpleenId=id)
        diacoTissueSpleen.delete()
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

@csrf_exempt
def diacoTissueTestisApi(request,id=0):
    if request.method=='GET':
        diacoTissueTestiss=DiacoTissueTestis.objects.all()
        diacoTissueTestis_serializer=DiacoTissueTestisSerializer(diacoTissueTestiss,many=True)
        return JsonResponse(diacoTissueTestis_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueTestis_data=JSONParser().parse(request)
        diacoTissueTestis_serializer=DiacoTissueTestisSerializer(data=diacoTissueTestis_data)
        if (diacoTissueTestis_serializer.is_valid()):
            diacoTissueTestis_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueTestis_data=JSONParser().parse(request)
        diacoTissueTestis=DiacoTissueTestis.objects.get(diacoTissueTestisId=diacoTissueTestis_data['subjid'])
        diacoTissueTestis_serializer=DiacoTissueTestisSerializer(diacoTissueTestis,data=diacoTissueTestis_data)
        if (diacoTissueTestis_serializer.is_valid()):
            diacoTissueTestis_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueTestis=DiacoTissueTestis.objects.get(diacoTissueTestisId=id)
        diacoTissueTestis.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueThyroidApi(request,id=0):
    if request.method=='GET':
        diacoTissueThyroids=DiacoTissueThyroid.objects.all()
        diacoTissueThyroid_serializer=DiacoTissueThyroidSerializer(diacoTissueThyroids,many=True)
        return JsonResponse(diacoTissueThyroid_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueThyroid_data=JSONParser().parse(request)
        diacoTissueThyroid_serializer=DiacoTissueThyroidSerializer(data=diacoTissueThyroid_data)
        if (diacoTissueThyroid_serializer.is_valid()):
            diacoTissueThyroid_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueThyroid_data=JSONParser().parse(request)
        diacoTissueThyroid=DiacoTissueThyroid.objects.get(diacoTissueThyroidId=diacoTissueThyroid_data['subjid'])
        diacoTissueThyroid_serializer=DiacoTissueThyroidSerializer(diacoTissueThyroid,data=diacoTissueThyroid_data)
        if (diacoTissueThyroid_serializer.is_valid()):
            diacoTissueThyroid_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueThyroid=DiacoTissueThyroid.objects.get(diacoTissueThyroidId=id)
        diacoTissueThyroid.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueUterusApi(request,id=0):
    if request.method=='GET':
        diacoTissueUteruss=DiacoTissueUterus.objects.all()
        diacoTissueUterus_serializer=DiacoTissueUterusSerializer(diacoTissueUteruss,many=True)
        return JsonResponse(diacoTissueUterus_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueUterus_data=JSONParser().parse(request)
        diacoTissueUterus_serializer=DiacoTissueUterusSerializer(data=diacoTissueUterus_data)
        if (diacoTissueUterus_serializer.is_valid()):
            diacoTissueUterus_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueUterus_data=JSONParser().parse(request)
        diacoTissueUterus=DiacoTissueUterus.objects.get(diacoTissueUterusId=diacoTissueUterus_data['subjid'])
        diacoTissueUterus_serializer=DiacoTissueUterusSerializer(diacoTissueUterus,data=diacoTissueUterus_data)
        if (diacoTissueUterus_serializer.is_valid()):
            diacoTissueUterus_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueUterus=DiacoTissueUterus.objects.get(diacoTissueUterusId=id)
        diacoTissueUterus.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueVaginaApi(request,id=0):
    if request.method=='GET':
        diacoTissueVaginas=DiacoTissueVagina.objects.all()
        diacoTissueVagina_serializer=DiacoTissueVaginaSerializer(diacoTissueVaginas,many=True)
        return JsonResponse(diacoTissueVagina_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueVagina_data=JSONParser().parse(request)
        diacoTissueVagina_serializer=DiacoTissueVaginaSerializer(data=diacoTissueVagina_data)
        if (diacoTissueVagina_serializer.is_valid()):
            diacoTissueVagina_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueVagina_data=JSONParser().parse(request)
        diacoTissueVagina=DiacoTissueVagina.objects.get(diacoTissueVaginaId=diacoTissueVagina_data['subjid'])
        diacoTissueVagina_serializer=DiacoTissueVaginaSerializer(diacoTissueVagina,data=diacoTissueVagina_data)
        if (diacoTissueVagina_serializer.is_valid()):
            diacoTissueVagina_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueVagina=DiacoTissueVagina.objects.get(diacoTissueVaginaId=id)
        diacoTissueVagina.delete()
        return JsonResponse ("Elimiato con successo!",safe=False)

@csrf_exempt
def diacoTissueWholeBloodApi(request,id=0):
    if request.method=='GET':
        diacoTissueWholeBloods=DiacoTissueWholeBlood.objects.all()
        diacoTissueWholeBlood_serializer=DiacoTissueWholeBloodSerializer(diacoTissueWholeBloods,many=True)
        return JsonResponse(diacoTissueWholeBlood_serializer.data,safe=False)
    elif request.method=='POST':
        diacoTissueWholeBlood_data=JSONParser().parse(request)
        diacoTissueWholeBlood_serializer=DiacoTissueWholeBloodSerializer(data=diacoTissueWholeBlood_data)
        if (diacoTissueWholeBlood_serializer.is_valid()):
            diacoTissueWholeBlood_serializer.save()
            return JsonResponse ("Aggiunto con successo!", safe=False)
        return JsonResponse ("Errore nell'inserimento",safe=False)
    elif request.method=='PUT':
        diacoTissueWholeBlood_data=JSONParser().parse(request)
        diacoTissueWholeBlood=DiacoTissueWholeBlood.objects.get(diacoTissueWholeBloodId=diacoTissueWholeBlood_data['subjid'])
        diacoTissueWholeBlood_serializer=DiacoTissueWholeBloodSerializer(diacoTissueWholeBlood,data=diacoTissueWholeBlood_data)
        if (diacoTissueWholeBlood_serializer.is_valid()):
            diacoTissueWholeBlood_serializer.save()
            return JsonResponse ("Aggiornato con successo!", safe=False)
        return JsonResponse ("Errore nell'argionamento",safe=False)
    elif request.method=='DELETE':
        diacoTissueWholeBlood=DiacoTissueWholeBlood.objects.get(diacoTissueWholeBloodId=id)
        diacoTissueWholeBlood.delete()
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

