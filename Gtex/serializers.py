from dataclasses import fields
from rest_framework import serializers
from Gtex.models import DiacoTissueAdiposeVisceralOm, GeneMedianTpm, ListaTabelle, SampleAttributesDs, SubjectPhenotypesDd, ListaGeni, ListaTabelle

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

class DiacoTissueAdiposeVisceralOmSerializer(serializers.ModelSerializer):
    class Meta:
        model=DiacoTissueAdiposeVisceralOm
        fields=('subjid','sampid','sesso','età','errfi1','mad2l2','mthfr','nppa','tnfrsf1b','pla2g2a','alpl','hspg2','cnr2','slc9a1','col8a2','cap1','slc2a1','cyp2j2','ddah1','cyr61','ngf','hmgcs2','ctss','s100a12','lmna','cd247','sele','fmo3','prdx6','glul','lamc1','ptgs2','chi3l1','chit1','fmod','il10','pfkfb2','cd34','cog2','nlrp3','rock2','apob','pomc','gckr','plekhh2','prkce','pigf','msh2','gfpt1','tacr1','reg1a','eif2ak3','adra2b','il1b','proc','polr2d','zeb2','acvr1c','dpp4','nfe2l2','igfbp5','ccl20','hdac4','capn10','ghrl','pparg','raf1','myd88','cx3cr1','cck','exosc7','ccr1','ccr5','gpx1','rhoa','cish','tkt','appl1','slmap','col8a1','cd47','gap43','cd80','rho','trh','tf','rbp1','trpc1','agtr1','sucnr1','p2ry1','mme','slc2a2','pik3ca','parl','ahsg','adipoq','spon2','wfs1','cd38','prom1','ppargc1a','igfbp7','cxcl5','cxcl9','cxcl10','cxcl11','hpse','spp1','adh1b','egf','alpk1','fabp2','pde5a','setd7','smad1','ednra','nr3c2','tlr2','npy5r','fbxo8','vegfc','acsl1','sorbs2','f11','basp1','ptger4','prkaa1','ghr','itga2','cdk7','f2r','erap2','apc','tnfaip8','vdac1','pdgfrb','cd74','sparc','ebf1','gfpt2','rreb1','edn1','cdkal1','hfe','hla_a','lta','tnf','hspa1a','hspa1b','hla_dqa1','mapk14','cdkn1a','glo1','vegfa','cd2ap','cnr1','enpp1','ctgf','rps12','sgk1','map3k5','cited2','utrn','mthfd1l','vip','sod2','lpa','thbs2','pdgfa','il6','npy','jazf1','cpvl','aqp1','elmo1','igfbp3','egfr','eln','ncf1','hspb1','sema3a','pon3','pon2','nampt','cav1','lep','akr1b1','akr1b10','pip','rarres2','nos3','angpt2','defa1','lpl','ebf2','adrb3','eif4ebp1','fgfr1','crh','sgk3','fabp5','fabp4','mmp16','ncald','klf10','enpp2','pvt1','jak2','psip1','plin2','rps6','aldh1a1','frmd3','gas1','baat','abca1','txn','ambp','c5','hspa5','angptl2','ptges','tsc1','abo','adamts13','ptgds','klf6','cdc123','bambi','cxcl12','mbl2','tfam','sirt1','srgn','unc5b','adk','pten','rbp4','cyp2c19','entpd1','tcf7l2','bnip3','igf2','ins','th','kcnq1','hbg2','smpd1','ilk','adm','pth','nucb2','kcnj11','saa1','bdnf','wt1','cd59','pdhx','traf6','api5','nr1h3','ndufs3','folh1','aplnr','p2rx3','cntf','fads1','fads2','fkbp2','syvn1','pc','dhcr7','prcp','nox4','pdgfd','atm','il18','apoa1','hyou1','esam','fkbp4','fgf23','ntf3','vwf','cd9','gapdh','cd4','gnb3','cd163','slc2a3','cd69','irak4','vdr','aqp5','acvrl1','nfe2','cd63','erbb3','ddit3','ifng','nts','igf1','acacb','trpv4','atp2a2','aldh2','nos1','pebp1','psmd9','scarb1','p2rx2','alox5ap','kl','postn','foxo1','htr2a','gpc5','irs2','gas6','ang','mmp14','ltb4r2','nfkbia','bmp4','rtn1','pgf','ngb','ahsa1','bdkrb2','bdkrb1','akt1','grem1','thbs1','pak6','b2m','myo5c','onecut1','adam10','ctsh','plin1','igf1r','mrpl28','cacna1h','pdpk1','ercc4','smg1','itgam','fto','mmp2','slc12a3','cetp','cx3cl1','cdh1','nqo1','hp','znrf1','cyba','tubb3','crk','serpinf2','serpinf1','trpv3','cxcl16','slc2a4','cd68','shbg','pmp22','srebf1','mapk7','ccl2','ccl5','hnf1b','erbb2','fkbp10','stat5a','stat3','naglu','aoc2','aoc3','ppy','sth','itgb3','gip','mpo','pecam1','sox9','timp2','dcxr','fasn','colec12','adcyap1','smad7','nedd4l','mc4r','bcl2','cndp2','znf236','stk11','sirt6','uhrf1','timm44','angptl4','dnmt1','icam1','ldlr','epor','prdx2','ptger1','unc13a','gdf15','fkbp8','usf2','ffar1','ffar2','nphs1','tgfb1','xrcc1','ercc1','gipr','fgf21','clec11a','fpr1','trib3','bmp2','thbd','cst3','id1','src','mafb','sgk2','hnf4a','pltp','mmp9','cd40','ptpn1','cyp24a1','rcan1','abcg1','prmt2','comt','mapk1','mif','ggt1','xbp1','osm','limk2','sfi1','timp3','hmox1','apol1','myh9','pdgfb','atf4','tspo','miox','prdx4','gk','rgn','timp1','clcn5','ar','foxo4','rps6ka6','nox1','xiap','cd40lg','l1cam','irak1','g6pd','f8')

class ListaGeniSerializer(serializers.ModelSerializer):
    class Meta:
        model=ListaGeni
        fields=('id','codice','gene','riferimento_gtex_tissue')

class ListaTabelleSerializer(serializers.ModelSerializer):
    class Meta:
        model=ListaTabelle
        fields=('tessuto','tabella')
