from django.conf.urls import url
from Gtex import views

urlpatterns=[
    url(r'^geneMedianTpm$', views.geneMedianTpmApi),
    url(r'^geneMedianTpm/([0-9]+)$', views.geneMedianTpmApi),
    url(r'^subjectPhenotypesDd$', views.subjectPhenotypesDdApi),
    url(r'^subjectPhenotypesDd/([0-9]+)$', views.subjectPhenotypesDdApi),
    url(r'^sampleAttributesDs$', views.sampleAttributesDsApi),
    url(r'^sampleAttributesDs/([0-9]+)$', views.sampleAttributesDsApi),
    url(r'^diacoTissueAdiposeSubcutaneous$', views.diacoTissueAdiposeSubcutaneousApi),
    url(r'^diacoTissueAdiposeSubcutaneous/([0-9]+)$', views.diacoTissueAdiposeSubcutaneousApi),
    url(r'^diacoTissueAdiposeVisceralOm$', views.diacoTissueAdiposeVisceralOmApi),
    url(r'^diacoTissueAdiposeVisceralOm/([0-9]+)$', views.diacoTissueAdiposeVisceralOmApi),
    url(r'^diacoTissueAdrenalGland$', views.diacoTissueAdrenalGlandApi),
    url(r'^diacoTissueAdrenalGland/([0-9]+)$', views.diacoTissueAdrenalGlandApi),
    url(r'^diacoTissueArteryAorta$', views.diacoTissueArteryAortaApi),
    url(r'^diacoTissueArteryAorta/([0-9]+)$', views.diacoTissueArteryAortaApi),
    url(r'^diacoTissueArteryCoronary$', views.diacoTissueArteryCoronaryApi),
    url(r'^diacoTissueArteryCoronary/([0-9]+)$', views.diacoTissueArteryCoronaryApi),
    url(r'^diacoTissueBladder$', views.diacoTissueBladderApi),
    url(r'^diacoTissueBladder/([0-9]+)$', views.diacoTissueBladderApi),
    url(r'^diacoTissueBrainAmygdala$', views.diacoTissueBrainAmygdalaApi),
    url(r'^diacoTissueBrainAmygdala/([0-9]+)$', views.diacoTissueBrainAmygdalaApi),
    url(r'^diacoTissueBrainAnteriorCcBa24$', views.diacoTissueBrainAnteriorCcBa24Api),
    url(r'^diacoTissueBrainAnteriorCcBa24/([0-9]+)$', views.diacoTissueBrainAnteriorCcBa24Api),
    url(r'^diacoTissueBrainCaudateBg$', views.diacoTissueBrainCaudateBgApi),
    url(r'^diacoTissueBrainCaudateBg/([0-9]+)$', views.diacoTissueBrainCaudateBgApi),
    url(r'^diacoTissueBrainCerebellarHs$', views.diacoTissueBrainCerebellarHsApi),
    url(r'^diacoTissueBrainCerebellarHs/([0-9]+)$', views.diacoTissueBrainCerebellarHsApi),
    url(r'^diacoTissueLiver$', views.diacoTissueLiverApi),
    url(r'^diacoTissueLiver/([0-9]+)$', views.diacoTissueLiverApi),
    url(r'^listaGeni$', views.listaGeniApi),
    url(r'^listaGeni/([0-9]+)$', views.listaGeniApi),
    url(r'^listaTabelle$', views.listaTabelleApi),
    url(r'^listaTabelle/([0-9]+)$', views.listaTabelleApi)
]
