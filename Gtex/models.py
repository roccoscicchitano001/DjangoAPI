from tkinter.messagebox import YES
from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
class GeneMedianTpm(models.Model):
    id = models.AutoField(primary_key=True) # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    adipose_subcutaneous = models.FloatField(db_column='Adipose - Subcutaneous', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adipose_visceral_omentum_field = models.FloatField(db_column='Adipose - Visceral (Omentum)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    adrenal_gland = models.FloatField(db_column='Adrenal Gland', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    artery_aorta = models.FloatField(db_column='Artery - Aorta', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    artery_coronary = models.FloatField(db_column='Artery - Coronary', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    artery_tibial = models.FloatField(db_column='Artery - Tibial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bladder = models.FloatField(db_column='Bladder', blank=True, null=True)  # Field name made lowercase.
    brain_amygdala = models.FloatField(db_column='Brain - Amygdala', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    brain_anterior_cingulate_cortex_ba24_field = models.FloatField(db_column='Brain - Anterior cingulate cortex (BA24)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    brain_caudate_basal_ganglia_field = models.FloatField(db_column='Brain - Caudate (basal ganglia)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    brain_cerebellar_hemisphere = models.FloatField(db_column='Brain - Cerebellar Hemisphere', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    brain_cerebellum = models.FloatField(db_column='Brain - Cerebellum', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    brain_cortex = models.FloatField(db_column='Brain - Cortex', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    brain_frontal_cortex_ba9_field = models.FloatField(db_column='Brain - Frontal Cortex (BA9)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    brain_hippocampus = models.FloatField(db_column='Brain - Hippocampus', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    brain_hypothalamus = models.FloatField(db_column='Brain - Hypothalamus', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    brain_nucleus_accumbens_basal_ganglia_field = models.FloatField(db_column='Brain - Nucleus accumbens (basal ganglia)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    brain_putamen_basal_ganglia_field = models.FloatField(db_column='Brain - Putamen (basal ganglia)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    brain_spinal_cord_cervical_c_1_field = models.FloatField(db_column='Brain - Spinal cord (cervical c-1)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    brain_substantia_nigra = models.FloatField(db_column='Brain - Substantia nigra', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    breast_mammary_tissue = models.FloatField(db_column='Breast - Mammary Tissue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cells_cultured_fibroblasts = models.FloatField(db_column='Cells - Cultured fibroblasts', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cells_ebv_transformed_lymphocytes = models.FloatField(db_column='Cells - EBV-transformed lymphocytes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cervix_ectocervix = models.FloatField(db_column='Cervix - Ectocervix', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cervix_endocervix = models.FloatField(db_column='Cervix - Endocervix', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    colon_sigmoid = models.FloatField(db_column='Colon - Sigmoid', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    colon_transverse = models.FloatField(db_column='Colon - Transverse', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    esophagus_gastroesophageal_junction = models.FloatField(db_column='Esophagus - Gastroesophageal Junction', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    esophagus_mucosa = models.FloatField(db_column='Esophagus - Mucosa', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    esophagus_muscularis = models.FloatField(db_column='Esophagus - Muscularis', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fallopian_tube = models.FloatField(db_column='Fallopian Tube', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heart_atrial_appendage = models.FloatField(db_column='Heart - Atrial Appendage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heart_left_ventricle = models.FloatField(db_column='Heart - Left Ventricle', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kidney_cortex = models.FloatField(db_column='Kidney - Cortex', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kidney_medulla = models.FloatField(db_column='Kidney - Medulla', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    liver = models.FloatField(db_column='Liver', blank=True, null=True)  # Field name made lowercase.
    lung = models.FloatField(db_column='Lung', blank=True, null=True)  # Field name made lowercase.
    minor_salivary_gland = models.FloatField(db_column='Minor Salivary Gland', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    muscle_skeletal = models.FloatField(db_column='Muscle - Skeletal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nerve_tibial = models.FloatField(db_column='Nerve - Tibial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ovary = models.FloatField(db_column='Ovary', blank=True, null=True)  # Field name made lowercase.
    pancreas = models.FloatField(db_column='Pancreas', blank=True, null=True)  # Field name made lowercase.
    pituitary = models.FloatField(db_column='Pituitary', blank=True, null=True)  # Field name made lowercase.
    prostate = models.FloatField(db_column='Prostate', blank=True, null=True)  # Field name made lowercase.
    skin_not_sun_exposed_suprapubic_field = models.FloatField(db_column='Skin - Not Sun Exposed (Suprapubic)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    skin_sun_exposed_lower_leg_field = models.FloatField(db_column='Skin - Sun Exposed (Lower leg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    small_intestine_terminal_ileum = models.FloatField(db_column='Small Intestine - Terminal Ileum', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    spleen = models.FloatField(db_column='Spleen', blank=True, null=True)  # Field name made lowercase.
    stomach = models.FloatField(db_column='Stomach', blank=True, null=True)  # Field name made lowercase.
    testis = models.FloatField(db_column='Testis', blank=True, null=True)  # Field name made lowercase.
    thyroid = models.FloatField(db_column='Thyroid', blank=True, null=True)  # Field name made lowercase.
    uterus = models.FloatField(db_column='Uterus', blank=True, null=True)  # Field name made lowercase.
    vagina = models.FloatField(db_column='Vagina', blank=True, null=True)  # Field name made lowercase.
    whole_blood = models.FloatField(db_column='Whole Blood', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'gene_median_tpm'
