from django.conf.urls import url
from Gtex import views

urlpatterns=[
    url(r'^geneMedianTpm$', views.geneMedianTpmApi),
    url(r'^geneMedianTpm/([0-9]+)$', views.geneMedianTpmApi),
    url(r'^subjectPhenotypesDd$', views.subjectPhenotypesDdApi),
    url(r'^subjectPhenotypesDd/([0-9]+)$', views.subjectPhenotypesDdApi),
    url(r'^sampleAttributesDs$', views.sampleAttributesDsApi),
    url(r'^sampleAttributesDs/([0-9]+)$', views.sampleAttributesDsApi),
    url(r'^diacoTissueAdiposeVisceralOm$', views.diacoTissueAdiposeVisceralOmApi),
    url(r'^diacoTissueAdiposeVisceralOm/([0-9]+)$', views.diacoTissueAdiposeVisceralOmApi),
    url(r'^listaGeni$', views.listaGeniApi),
    url(r'^listaGeni/([0-9]+)$', views.listaGeniApi)
]
