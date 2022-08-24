from rest_framework import serializers
from Gtex.models import GeneMedianTpm, SampleAttributesDs, SubjectPhenotypesDd

class GeneMedianTpmSerializer(serializers.ModelSerializer):
    class Meta:
        model=GeneMedianTpm
        fields=('id','name','description','adipose_subcutaneous','adipose_visceral_omentum_field','adrenal_gland','artery_aorta','artery_coronary','artery_tibial','bladder','brain_amygdala','brain_anterior_cingulate_cortex_ba24_field','brain_caudate_basal_ganglia_field','brain_cerebellar_hemisphere','brain_cerebellum','brain_cortex','brain_frontal_cortex_ba9_field','brain_hippocampus','brain_hypothalamus','brain_nucleus_accumbens_basal_ganglia_field','brain_putamen_basal_ganglia_field','brain_spinal_cord_cervical_c_1_field','brain_substantia_nigra','breast_mammary_tissue','cells_cultured_fibroblasts','cells_ebv_transformed_lymphocytes','cervix_ectocervix','cervix_endocervix','colon_sigmoid','colon_transverse','esophagus_gastroesophageal_junction','esophagus_mucosa','esophagus_muscularis','fallopian_tube','heart_atrial_appendage','heart_left_ventricle','kidney_cortex','kidney_medulla','liver','lung','minor_salivary_gland','muscle_skeletal','nerve_tibial','ovary','pancreas','pituitary','prostate','skin_not_sun_exposed_suprapubic_field','skin_sun_exposed_lower_leg_field','small_intestine_terminal_ileum','spleen','stomach','testis','thyroid','uterus','vagina','whole_blood')

class SampleAttributesDsSerializer(serializers.ModelSerializer):
    class Meta:
        model=SampleAttributesDs
        fields=('id','sampid','smatsscr','smcenter','smpthnts','smrin','smts','smtsd','smubrid','smtsisch','smtspax','smnabtch','smnabtcht','smnabtchd','smgebtch','smgebtchd','smgebtcht','smafrze','smgtc','sme2mprt','smchmprs','smntrart','smnumgps','smmaprt','smexncrt','sm550nrm','smgnsdtc','smunmprt','sm350nrm','smrdlgth','smmncpb','sme1mmrt','smsflgth','smestlbs','smmppd','smnterrt','smrrnanm','smrdttl','smvqcfl','smmncv','smtrscpt','smmppdpr','smcglgth','smgappct','smunpdrd','smntrnrt','smmpunrt','smexpeff','smmppdun','sme2mmrt','sme2anti','smaltalg','sme2snse','smmflgth','sme1anti','smspltrd','smbsmmrt','sme1snse','sme1pcts','smrrnart','sme1mprt','smnum5cd','smdpmprt','sme2pcts')

class SubjectPhenotypesDdSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubjectPhenotypesDd
        fields=('id','subjid','sex','age','dthhrdy')