from lib2to3.pgen2.token import NUMBER
from tkinter.messagebox import YES
from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdiposeSubcutaneous(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    gtex_1117f_0226_sm_5gzz7 = models.FloatField(db_column='GTEX-1117F-0226-SM-5GZZ7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_111cu_1826_sm_5gzyn = models.FloatField(db_column='GTEX-111CU-1826-SM-5GZYN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_111fc_0226_sm_5n9b8 = models.FloatField(db_column='GTEX-111FC-0226-SM-5N9B8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_111vg_2326_sm_5n9bk = models.FloatField(db_column='GTEX-111VG-2326-SM-5N9BK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_111ys_2426_sm_5gzzq = models.FloatField(db_column='GTEX-111YS-2426-SM-5GZZQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1122o_2026_sm_9yfmg = models.FloatField(db_column='GTEX-1122O-2026-SM-9YFMG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1128s_2126_sm_5h12u = models.FloatField(db_column='GTEX-1128S-2126-SM-5H12U', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_113ic_0226_sm_5hl5c = models.FloatField(db_column='GTEX-113IC-0226-SM-5HL5C', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_117yx_2226_sm_5egjj = models.FloatField(db_column='GTEX-117YX-2226-SM-5EGJJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11dxw_0326_sm_5h11w = models.FloatField(db_column='GTEX-11DXW-0326-SM-5H11W', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11dxx_2326_sm_9yfks = models.FloatField(db_column='GTEX-11DXX-2326-SM-9YFKS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11dz1_0226_sm_5a5kf = models.FloatField(db_column='GTEX-11DZ1-0226-SM-5A5KF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11ei6_0226_sm_5eq64 = models.FloatField(db_column='GTEX-11EI6-0226-SM-5EQ64', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11em3_2326_sm_5h12b = models.FloatField(db_column='GTEX-11EM3-2326-SM-5H12B', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11emc_2826_sm_5pny6 = models.FloatField(db_column='GTEX-11EMC-2826-SM-5PNY6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11eq8_0226_sm_5eq5g = models.FloatField(db_column='GTEX-11EQ8-0226-SM-5EQ5G', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11eq9_2526_sm_5hl66 = models.FloatField(db_column='GTEX-11EQ9-2526-SM-5HL66', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11gs4_2626_sm_5a5ld = models.FloatField(db_column='GTEX-11GS4-2626-SM-5A5LD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11gso_2326_sm_5a5lx = models.FloatField(db_column='GTEX-11GSO-2326-SM-5A5LX', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11h98_0226_sm_5nq89 = models.FloatField(db_column='GTEX-11H98-0226-SM-5NQ89', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11i78_2626_sm_5q5ai = models.FloatField(db_column='GTEX-11I78-2626-SM-5Q5AI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11lck_1126_sm_5a5kc = models.FloatField(db_column='GTEX-11LCK-1126-SM-5A5KC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11nuk_0326_sm_5hl5k = models.FloatField(db_column='GTEX-11NUK-0326-SM-5HL5K', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11o72_0226_sm_59869 = models.FloatField(db_column='GTEX-11O72-0226-SM-59869', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11of3_2426_sm_5q5as = models.FloatField(db_column='GTEX-11OF3-2426-SM-5Q5AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11onc_2526_sm_5986w = models.FloatField(db_column='GTEX-11ONC-2526-SM-5986W', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11p7k_2026_sm_5gu74 = models.FloatField(db_column='GTEX-11P7K-2026-SM-5GU74', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11p81_2426_sm_5gu65 = models.FloatField(db_column='GTEX-11P81-2426-SM-5GU65', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11p82_1726_sm_5q5at = models.FloatField(db_column='GTEX-11P82-1726-SM-5Q5AT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11prg_0626_sm_5bc56 = models.FloatField(db_column='GTEX-11PRG-0626-SM-5BC56', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11tt1_2426_sm_5eqmk = models.FloatField(db_column='GTEX-11TT1-2426-SM-5EQMK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11ttk_0226_sm_5n9ec = models.FloatField(db_column='GTEX-11TTK-0226-SM-5N9EC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11tuw_2626_sm_5eqkz = models.FloatField(db_column='GTEX-11TUW-2626-SM-5EQKZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11ud1_0226_sm_5eqkl = models.FloatField(db_column='GTEX-11UD1-0226-SM-5EQKL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11ud2_0126_sm_5eql2 = models.FloatField(db_column='GTEX-11UD2-0126-SM-5EQL2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11wqc_2426_sm_5eqkq = models.FloatField(db_column='GTEX-11WQC-2426-SM-5EQKQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11xuk_2126_sm_5eqlr = models.FloatField(db_column='GTEX-11XUK-2126-SM-5EQLR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11zts_0226_sm_5eqkd = models.FloatField(db_column='GTEX-11ZTS-0226-SM-5EQKD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11ztt_2526_sm_5eqm9 = models.FloatField(db_column='GTEX-11ZTT-2526-SM-5EQM9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11zu8_2426_sm_5eqmv = models.FloatField(db_column='GTEX-11ZU8-2426-SM-5EQMV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11zus_0726_sm_59886 = models.FloatField(db_column='GTEX-11ZUS-0726-SM-59886', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11zvc_2626_sm_5fqta = models.FloatField(db_column='GTEX-11ZVC-2626-SM-5FQTA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1211k_2226_sm_5fqu6 = models.FloatField(db_column='GTEX-1211K-2226-SM-5FQU6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12126_0426_sm_5q5ap = models.FloatField(db_column='GTEX-12126-0426-SM-5Q5AP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1212z_2426_sm_5eq5d = models.FloatField(db_column='GTEX-1212Z-2426-SM-5EQ5D', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12584_0226_sm_5eql5 = models.FloatField(db_column='GTEX-12584-0226-SM-5EQL5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12696_2526_sm_5eqln = models.FloatField(db_column='GTEX-12696-2526-SM-5EQLN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1269c_2726_sm_5egj4 = models.FloatField(db_column='GTEX-1269C-2726-SM-5EGJ4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12c56_1626_sm_5fquo = models.FloatField(db_column='GTEX-12C56-1626-SM-5FQUO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12ks4_0426_sm_5eqmc = models.FloatField(db_column='GTEX-12KS4-0426-SM-5EQMC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12wsa_0326_sm_5bc6i = models.FloatField(db_column='GTEX-12WSA-0326-SM-5BC6I', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12wsc_0226_sm_5eq52 = models.FloatField(db_column='GTEX-12WSC-0226-SM-5EQ52', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12wsd_0226_sm_59hko = models.FloatField(db_column='GTEX-12WSD-0226-SM-59HKO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12wsl_2426_sm_5gcn7 = models.FloatField(db_column='GTEX-12WSL-2426-SM-5GCN7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12wsm_0226_sm_5lzv6 = models.FloatField(db_column='GTEX-12WSM-0226-SM-5LZV6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12zzx_0226_sm_5duxu = models.FloatField(db_column='GTEX-12ZZX-0226-SM-5DUXU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12zzy_0326_sm_5lzvq = models.FloatField(db_column='GTEX-12ZZY-0326-SM-5LZVQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12zzz_0526_sm_5dux6 = models.FloatField(db_column='GTEX-12ZZZ-0526-SM-5DUX6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13111_1726_sm_5egjz = models.FloatField(db_column='GTEX-13111-1726-SM-5EGJZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13112_2726_sm_5duw5 = models.FloatField(db_column='GTEX-13112-2726-SM-5DUW5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13113_1826_sm_5lzw4 = models.FloatField(db_column='GTEX-13113-1826-SM-5LZW4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1313w_0226_sm_5lzv7 = models.FloatField(db_column='GTEX-1313W-0226-SM-5LZV7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1314g_1626_sm_5eq67 = models.FloatField(db_column='GTEX-1314G-1626-SM-5EQ67', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_131xe_2426_sm_5eq5v = models.FloatField(db_column='GTEX-131XE-2426-SM-5EQ5V', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_131xf_2226_sm_5eqkg = models.FloatField(db_column='GTEX-131XF-2226-SM-5EQKG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_131xw_0526_sm_5pnxz = models.FloatField(db_column='GTEX-131XW-0526-SM-5PNXZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_131ys_0226_sm_5ijeh = models.FloatField(db_column='GTEX-131YS-0226-SM-5IJEH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_132ar_0226_sm_5ijbe = models.FloatField(db_column='GTEX-132AR-0226-SM-5IJBE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_132qs_2526_sm_62lfj = models.FloatField(db_column='GTEX-132QS-2526-SM-62LFJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_133le_1926_sm_5n9fv = models.FloatField(db_column='GTEX-133LE-1926-SM-5N9FV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1399r_2626_sm_5klz7 = models.FloatField(db_column='GTEX-1399R-2626-SM-5KLZ7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1399t_2726_sm_5k7xk = models.FloatField(db_column='GTEX-1399T-2726-SM-5K7XK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1399u_2426_sm_5k7xb = models.FloatField(db_column='GTEX-1399U-2426-SM-5K7XB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_139d8_0326_sm_5ijcj = models.FloatField(db_column='GTEX-139D8-0326-SM-5IJCJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_139t4_0126_sm_5hl5g = models.FloatField(db_column='GTEX-139T4-0126-SM-5HL5G', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_139t6_2126_sm_5km37 = models.FloatField(db_column='GTEX-139T6-2126-SM-5KM37', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_139t8_0226_sm_5l3ea = models.FloatField(db_column='GTEX-139T8-0226-SM-5L3EA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_139tt_0226_sm_5k7yh = models.FloatField(db_column='GTEX-139TT-0226-SM-5K7YH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_139tu_0226_sm_5j1nm = models.FloatField(db_column='GTEX-139TU-0226-SM-5J1NM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_139yr_2426_sm_5j1ob = models.FloatField(db_column='GTEX-139YR-2426-SM-5J1OB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13cf2_2626_sm_5lzza = models.FloatField(db_column='GTEX-13CF2-2626-SM-5LZZA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13cf3_2326_sm_5ifgl = models.FloatField(db_column='GTEX-13CF3-2326-SM-5IFGL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13d11_2326_sm_5ijcy = models.FloatField(db_column='GTEX-13D11-2326-SM-5IJCY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13fh7_2226_sm_5ijd4 = models.FloatField(db_column='GTEX-13FH7-2226-SM-5IJD4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13fho_0326_sm_5ijbh = models.FloatField(db_column='GTEX-13FHO-0326-SM-5IJBH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13fhp_0226_sm_5k7wd = models.FloatField(db_column='GTEX-13FHP-0226-SM-5K7WD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13ftw_2526_sm_5ijc8 = models.FloatField(db_column='GTEX-13FTW-2526-SM-5IJC8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13fty_0626_sm_5l3f8 = models.FloatField(db_column='GTEX-13FTY-0626-SM-5L3F8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13g51_2626_sm_5lzyw = models.FloatField(db_column='GTEX-13G51-2626-SM-5LZYW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13ivo_0226_sm_5lzxu = models.FloatField(db_column='GTEX-13IVO-0226-SM-5LZXU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13juv_2826_sm_5lzwu = models.FloatField(db_column='GTEX-13JUV-2826-SM-5LZWU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13jvg_0226_sm_5j1mw = models.FloatField(db_column='GTEX-13JVG-0226-SM-5J1MW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13n11_2626_sm_5k7uq = models.FloatField(db_column='GTEX-13N11-2626-SM-5K7UQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13n1w_0226_sm_5k7w6 = models.FloatField(db_column='GTEX-13N1W-0226-SM-5K7W6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13n2g_2726_sm_5j1mg = models.FloatField(db_column='GTEX-13N2G-2726-SM-5J1MG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13nyb_2626_sm_9yfmi = models.FloatField(db_column='GTEX-13NYB-2626-SM-9YFMI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13nys_0226_sm_5mr49 = models.FloatField(db_column='GTEX-13NYS-0226-SM-5MR49', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13nz8_0926_sm_5mr3u = models.FloatField(db_column='GTEX-13NZ8-0926-SM-5MR3U', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13nz9_0526_sm_5j1ox = models.FloatField(db_column='GTEX-13NZ9-0526-SM-5J1OX', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13nza_0126_sm_5k7uh = models.FloatField(db_column='GTEX-13NZA-0126-SM-5K7UH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13nzb_2426_sm_5k7uf = models.FloatField(db_column='GTEX-13NZB-2426-SM-5K7UF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13o1r_0226_sm_5k7u5 = models.FloatField(db_column='GTEX-13O1R-0226-SM-5K7U5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13o21_1526_sm_5k7w4 = models.FloatField(db_column='GTEX-13O21-1526-SM-5K7W4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13o3p_0226_sm_5km3z = models.FloatField(db_column='GTEX-13O3P-0226-SM-5KM3Z', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13o3q_2326_sm_5km3g = models.FloatField(db_column='GTEX-13O3Q-2326-SM-5KM3G', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13o61_2426_sm_5j1nv = models.FloatField(db_column='GTEX-13O61-2426-SM-5J1NV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13ovi_1326_sm_5ijbo = models.FloatField(db_column='GTEX-13OVI-1326-SM-5IJBO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13ovj_0326_sm_5l3gl = models.FloatField(db_column='GTEX-13OVJ-0326-SM-5L3GL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13ovk_2126_sm_6pan1 = models.FloatField(db_column='GTEX-13OVK-2126-SM-6PAN1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13ovl_0326_sm_5ijcs = models.FloatField(db_column='GTEX-13OVL-0326-SM-5IJCS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13ow6_0526_sm_5l3hy = models.FloatField(db_column='GTEX-13OW6-0526-SM-5L3HY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13ow7_0226_sm_5mr3n = models.FloatField(db_column='GTEX-13OW7-0226-SM-5MR3N', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13ow8_1226_sm_5k7xd = models.FloatField(db_column='GTEX-13OW8-1226-SM-5K7XD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13pdp_0226_sm_5k7w9 = models.FloatField(db_column='GTEX-13PDP-0226-SM-5K7W9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13plj_0126_sm_5l3hu = models.FloatField(db_column='GTEX-13PLJ-0126-SM-5L3HU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13pvq_0226_sm_5sibg = models.FloatField(db_column='GTEX-13PVQ-0226-SM-5SIBG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13pvr_2426_sm_5rqhn = models.FloatField(db_column='GTEX-13PVR-2426-SM-5RQHN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13qbu_2526_sm_5lu4x = models.FloatField(db_column='GTEX-13QBU-2526-SM-5LU4X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13qj3_0426_sm_5rqhp = models.FloatField(db_column='GTEX-13QJ3-0426-SM-5RQHP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13rtj_2526_sm_5s2q3 = models.FloatField(db_column='GTEX-13RTJ-2526-SM-5S2Q3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13s7m_0226_sm_5s2ug = models.FloatField(db_column='GTEX-13S7M-0226-SM-5S2UG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13slw_0226_sm_5s2na = models.FloatField(db_column='GTEX-13SLW-0226-SM-5S2NA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13slx_0426_sm_5qgrc = models.FloatField(db_column='GTEX-13SLX-0426-SM-5QGRC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13u4i_0226_sm_5sib1 = models.FloatField(db_column='GTEX-13U4I-0226-SM-5SIB1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13vxt_0226_sm_5lu9q = models.FloatField(db_column='GTEX-13VXT-0226-SM-5LU9Q', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13vxu_0226_sm_5si9r = models.FloatField(db_column='GTEX-13VXU-0226-SM-5SI9R', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13w3w_2526_sm_5si9p = models.FloatField(db_column='GTEX-13W3W-2526-SM-5SI9P', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13x6j_0226_sm_7epgc = models.FloatField(db_column='GTEX-13X6J-0226-SM-7EPGC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13x6k_0226_sm_5qgpb = models.FloatField(db_column='GTEX-13X6K-0226-SM-5QGPB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13yan_0426_sm_5o9dr = models.FloatField(db_column='GTEX-13YAN-0426-SM-5O9DR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_144fl_0226_sm_5q5d4 = models.FloatField(db_column='GTEX-144FL-0226-SM-5Q5D4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_144gl_0226_sm_5qgox = models.FloatField(db_column='GTEX-144GL-0226-SM-5QGOX', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_144gm_1926_sm_5luan = models.FloatField(db_column='GTEX-144GM-1926-SM-5LUAN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_144go_1626_sm_7epg5 = models.FloatField(db_column='GTEX-144GO-1626-SM-7EPG5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_145ls_0226_sm_5o9a5 = models.FloatField(db_column='GTEX-145LS-0226-SM-5O9A5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_145lt_1826_sm_5qgp4 = models.FloatField(db_column='GTEX-145LT-1826-SM-5QGP4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_145me_1926_sm_5mr6t = models.FloatField(db_column='GTEX-145ME-1926-SM-5MR6T', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_145mf_0526_sm_5lua6 = models.FloatField(db_column='GTEX-145MF-0526-SM-5LUA6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_145mg_0126_sm_5tdda = models.FloatField(db_column='GTEX-145MG-0126-SM-5TDDA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_145mi_0426_sm_5o99v = models.FloatField(db_column='GTEX-145MI-0426-SM-5O99V', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_145mn_2626_sm_5nqah = models.FloatField(db_column='GTEX-145MN-2626-SM-5NQAH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_145mo_0426_sm_5qgp6 = models.FloatField(db_column='GTEX-145MO-0426-SM-5QGP6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_146fh_0226_sm_5qgpq = models.FloatField(db_column='GTEX-146FH-0226-SM-5QGPQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_146fq_0226_sm_5nqal = models.FloatField(db_column='GTEX-146FQ-0226-SM-5NQAL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_146fr_1826_sm_5qgpf = models.FloatField(db_column='GTEX-146FR-1826-SM-5QGPF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14753_0326_sm_5qgqb = models.FloatField(db_column='GTEX-14753-0326-SM-5QGQB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_147f3_0626_sm_5nq9i = models.FloatField(db_column='GTEX-147F3-0626-SM-5NQ9I', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_147gr_0426_sm_5s2ol = models.FloatField(db_column='GTEX-147GR-0426-SM-5S2OL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_147js_0426_sm_5tdd2 = models.FloatField(db_column='GTEX-147JS-0426-SM-5TDD2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_148vi_1726_sm_5s2w9 = models.FloatField(db_column='GTEX-148VI-1726-SM-5S2W9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1497j_2326_sm_5nqbk = models.FloatField(db_column='GTEX-1497J-2326-SM-5NQBK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14a5h_0526_sm_5tdcn = models.FloatField(db_column='GTEX-14A5H-0526-SM-5TDCN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14aby_0326_sm_5tddk = models.FloatField(db_column='GTEX-14ABY-0326-SM-5TDDK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14as3_2026_sm_5tdd9 = models.FloatField(db_column='GTEX-14AS3-2026-SM-5TDD9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14bil_0226_sm_5si9e = models.FloatField(db_column='GTEX-14BIL-0226-SM-5SI9E', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14bin_0726_sm_793dq = models.FloatField(db_column='GTEX-14BIN-0726-SM-793DQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14bmu_2126_sm_5s2ts = models.FloatField(db_column='GTEX-14BMU-2126-SM-5S2TS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14bmv_0226_sm_5s2n2 = models.FloatField(db_column='GTEX-14BMV-0226-SM-5S2N2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14c39_2526_sm_5s2uh = models.FloatField(db_column='GTEX-14C39-2526-SM-5S2UH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14c5o_0226_sm_5si6o = models.FloatField(db_column='GTEX-14C5O-0226-SM-5SI6O', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14daq_0226_sm_664mq = models.FloatField(db_column='GTEX-14DAQ-0226-SM-664MQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14dar_1926_sm_5s2nq = models.FloatField(db_column='GTEX-14DAR-1926-SM-5S2NQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14e1k_2126_sm_793du = models.FloatField(db_column='GTEX-14E1K-2126-SM-793DU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14e6c_0226_sm_5s2n3 = models.FloatField(db_column='GTEX-14E6C-0226-SM-5S2N3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14e6d_0226_sm_62ldw = models.FloatField(db_column='GTEX-14E6D-0226-SM-62LDW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14e6e_1926_sm_664n4 = models.FloatField(db_column='GTEX-14E6E-1926-SM-664N4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14h4a_1026_sm_62ldy = models.FloatField(db_column='GTEX-14H4A-1026-SM-62LDY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14ick_0326_sm_6lliz = models.FloatField(db_column='GTEX-14ICK-0326-SM-6LLIZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14icl_2026_sm_62ldn = models.FloatField(db_column='GTEX-14ICL-2026-SM-62LDN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14jg1_0526_sm_6llhw = models.FloatField(db_column='GTEX-14JG1-0526-SM-6LLHW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14jg6_2326_sm_6llh3 = models.FloatField(db_column='GTEX-14JG6-2326-SM-6LLH3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14jiy_0526_sm_62lfh = models.FloatField(db_column='GTEX-14JIY-0526-SM-62LFH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14llw_0226_sm_62lel = models.FloatField(db_column='GTEX-14LLW-0226-SM-62LEL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14phx_2426_sm_62len = models.FloatField(db_column='GTEX-14PHX-2426-SM-62LEN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14pii_0326_sm_6lliq = models.FloatField(db_column='GTEX-14PII-0326-SM-6LLIQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14pj2_0226_sm_6llh4 = models.FloatField(db_column='GTEX-14PJ2-0226-SM-6LLH4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14pj3_1926_sm_62ley = models.FloatField(db_column='GTEX-14PJ3-1926-SM-62LEY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14pj4_2226_sm_6llis = models.FloatField(db_column='GTEX-14PJ4-2226-SM-6LLIS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14pj6_2226_sm_6lliv = models.FloatField(db_column='GTEX-14PJ6-2226-SM-6LLIV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14pjm_0326_sm_62lf2 = models.FloatField(db_column='GTEX-14PJM-0326-SM-62LF2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14pk6_2026_sm_6llhp = models.FloatField(db_column='GTEX-14PK6-2026-SM-6LLHP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14pn3_2526_sm_6eu15 = models.FloatField(db_column='GTEX-14PN3-2526-SM-6EU15', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15chq_0226_sm_6eu2s = models.FloatField(db_column='GTEX-15CHQ-0226-SM-6EU2S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15dcd_0226_sm_6lpkc = models.FloatField(db_column='GTEX-15DCD-0226-SM-6LPKC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15dde_0226_sm_6llj6 = models.FloatField(db_column='GTEX-15DDE-0226-SM-6LLJ6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15er7_0426_sm_6pam3 = models.FloatField(db_column='GTEX-15ER7-0426-SM-6PAM3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15ets_0426_sm_6pani = models.FloatField(db_column='GTEX-15ETS-0426-SM-6PANI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15g19_0226_sm_6pal2 = models.FloatField(db_column='GTEX-15G19-0226-SM-6PAL2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15rie_2326_sm_7kfsc = models.FloatField(db_column='GTEX-15RIE-2326-SM-7KFSC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15sde_2426_sm_7kfrc = models.FloatField(db_column='GTEX-15SDE-2426-SM-7KFRC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15ukp_0526_sm_7kfro = models.FloatField(db_column='GTEX-15UKP-0526-SM-7KFRO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_169bo_1426_sm_9mqjt = models.FloatField(db_column='GTEX-169BO-1426-SM-9MQJT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_16aah_2026_sm_7lg5f = models.FloatField(db_column='GTEX-16AAH-2026-SM-7LG5F', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_16bqi_0526_sm_6pam8 = models.FloatField(db_column='GTEX-16BQI-0526-SM-6PAM8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_16gpk_0226_sm_7dufi = models.FloatField(db_column='GTEX-16GPK-0226-SM-7DUFI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_16mt8_0526_sm_6pam6 = models.FloatField(db_column='GTEX-16MT8-0526-SM-6PAM6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_16mta_2126_sm_6palc = models.FloatField(db_column='GTEX-16MTA-2126-SM-6PALC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_16nga_1826_sm_7lg5l = models.FloatField(db_column='GTEX-16NGA-1826-SM-7LG5L', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_16npx_0326_sm_7ewdi = models.FloatField(db_column='GTEX-16NPX-0326-SM-7EWDI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_16xzy_2526_sm_7dhl2 = models.FloatField(db_column='GTEX-16XZY-2526-SM-7DHL2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_16xzz_0226_sm_7mgvj = models.FloatField(db_column='GTEX-16XZZ-0226-SM-7MGVJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_16yqh_0226_sm_6pald = models.FloatField(db_column='GTEX-16YQH-0226-SM-6PALD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17euy_0526_sm_7ewde = models.FloatField(db_column='GTEX-17EUY-0526-SM-7EWDE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17evp_0426_sm_79okg = models.FloatField(db_column='GTEX-17EVP-0426-SM-79OKG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17f96_1726_sm_7igmb = models.FloatField(db_column='GTEX-17F96-1726-SM-7IGMB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17f97_0426_sm_7lt9u = models.FloatField(db_column='GTEX-17F97-0426-SM-7LT9U', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17f98_1126_sm_79ojs = models.FloatField(db_column='GTEX-17F98-1126-SM-79OJS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17f9y_0326_sm_7igls = models.FloatField(db_column='GTEX-17F9Y-0326-SM-7IGLS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17hg3_2326_sm_79okh = models.FloatField(db_column='GTEX-17HG3-2326-SM-79OKH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17hgu_0326_sm_7duer = models.FloatField(db_column='GTEX-17HGU-0326-SM-7DUER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17hhe_1926_sm_7epgw = models.FloatField(db_column='GTEX-17HHE-1926-SM-7EPGW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17hhy_0226_sm_793bq = models.FloatField(db_column='GTEX-17HHY-0226-SM-793BQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17hii_0326_sm_7lg4x = models.FloatField(db_column='GTEX-17HII-0326-SM-7LG4X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17knj_2226_sm_dkpou = models.FloatField(db_column='GTEX-17KNJ-2226-SM-DKPOU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17mf6_0226_sm_7lg4g = models.FloatField(db_column='GTEX-17MF6-0226-SM-7LG4G', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17mfq_1826_sm_7dhls = models.FloatField(db_column='GTEX-17MFQ-1826-SM-7DHLS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_183fy_0326_sm_793by = models.FloatField(db_column='GTEX-183FY-0326-SM-793BY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_183wm_0226_sm_7lt8t = models.FloatField(db_column='GTEX-183WM-0226-SM-7LT8T', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_18465_0226_sm_7lg5m = models.FloatField(db_column='GTEX-18465-0226-SM-7LG5M', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_18a66_0326_sm_718be = models.FloatField(db_column='GTEX-18A66-0326-SM-718BE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_18a67_0226_sm_7lg67 = models.FloatField(db_column='GTEX-18A67-0226-SM-7LG67', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_18a6q_0226_sm_718as = models.FloatField(db_column='GTEX-18A6Q-0226-SM-718AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_18a7a_0326_sm_731at = models.FloatField(db_column='GTEX-18A7A-0326-SM-731AT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_18d9a_2026_sm_718bl = models.FloatField(db_column='GTEX-18D9A-2026-SM-718BL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_18d9u_0726_sm_7lg5j = models.FloatField(db_column='GTEX-18D9U-0726-SM-7LG5J', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_18qfq_0226_sm_731bq = models.FloatField(db_column='GTEX-18QFQ-0226-SM-731BQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1a32a_0226_sm_718b2 = models.FloatField(db_column='GTEX-1A32A-0226-SM-718B2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1a3mv_2126_sm_718bv = models.FloatField(db_column='GTEX-1A3MV-2126-SM-718BV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1a3mw_0226_sm_7939o = models.FloatField(db_column='GTEX-1A3MW-0226-SM-7939O', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1a3mx_0226_sm_731c4 = models.FloatField(db_column='GTEX-1A3MX-0226-SM-731C4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1a8fm_0126_sm_7sb7p = models.FloatField(db_column='GTEX-1A8FM-0126-SM-7SB7P', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1a8g6_0526_sm_7pc1e = models.FloatField(db_column='GTEX-1A8G6-0526-SM-7PC1E', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1a8g7_0226_sm_731as = models.FloatField(db_column='GTEX-1A8G7-0226-SM-731AS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1amey_1426_sm_7939i = models.FloatField(db_column='GTEX-1AMEY-1426-SM-7939I', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1amfi_2126_sm_731bt = models.FloatField(db_column='GTEX-1AMFI-2126-SM-731BT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ax9i_0226_sm_7sb75 = models.FloatField(db_column='GTEX-1AX9I-0226-SM-7SB75', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ax9j_0326_sm_73kxy = models.FloatField(db_column='GTEX-1AX9J-0326-SM-73KXY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ax9k_2426_sm_73kz4 = models.FloatField(db_column='GTEX-1AX9K-2426-SM-73KZ4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ayct_2226_sm_7sb98 = models.FloatField(db_column='GTEX-1AYCT-2226-SM-7SB98', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ayd5_2326_sm_73kxf = models.FloatField(db_column='GTEX-1AYD5-2326-SM-73KXF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1b8ke_2526_sm_73kyq = models.FloatField(db_column='GTEX-1B8KE-2526-SM-73KYQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1b8kz_1926_sm_7dug8 = models.FloatField(db_column='GTEX-1B8KZ-1926-SM-7DUG8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1b8l1_2626_sm_7sb77 = models.FloatField(db_column='GTEX-1B8L1-2626-SM-7SB77', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1b8sf_0526_sm_7939f = models.FloatField(db_column='GTEX-1B8SF-0526-SM-7939F', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1b8sg_0226_sm_7939q = models.FloatField(db_column='GTEX-1B8SG-0226-SM-7939Q', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1b932_0226_sm_7pbyh = models.FloatField(db_column='GTEX-1B932-0226-SM-7PBYH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1b933_0526_sm_7ephm = models.FloatField(db_column='GTEX-1B933-0526-SM-7EPHM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1b97i_1726_sm_7939v = models.FloatField(db_column='GTEX-1B97I-1726-SM-7939V', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1b996_0126_sm_7pbyf = models.FloatField(db_column='GTEX-1B996-0126-SM-7PBYF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1bajh_0426_sm_73kwy = models.FloatField(db_column='GTEX-1BAJH-0426-SM-73KWY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1c2ji_2226_sm_7igpj = models.FloatField(db_column='GTEX-1C2JI-2226-SM-7IGPJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1c475_1926_sm_7dufv = models.FloatField(db_column='GTEX-1C475-1926-SM-7DUFV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1c4cl_0426_sm_7939n = models.FloatField(db_column='GTEX-1C4CL-0426-SM-7939N', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1c64o_0226_sm_73kxb = models.FloatField(db_column='GTEX-1C64O-0226-SM-73KXB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1c6vq_0226_sm_7p8s5 = models.FloatField(db_column='GTEX-1C6VQ-0226-SM-7P8S5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1c6vr_2626_sm_7mgx2 = models.FloatField(db_column='GTEX-1C6VR-2626-SM-7MGX2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1c6vs_0426_sm_79ojv = models.FloatField(db_column='GTEX-1C6VS-0426-SM-79OJV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1c6wa_0226_sm_7igpo = models.FloatField(db_column='GTEX-1C6WA-0226-SM-7IGPO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1camq_0126_sm_7sb7s = models.FloatField(db_column='GTEX-1CAMQ-0126-SM-7SB7S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1camr_1826_sm_7mxuj = models.FloatField(db_column='GTEX-1CAMR-1826-SM-7MXUJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1cams_0326_sm_7pc35 = models.FloatField(db_column='GTEX-1CAMS-0326-SM-7PC35', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1cb4e_1826_sm_7rhg8 = models.FloatField(db_column='GTEX-1CB4E-1826-SM-7RHG8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1cb4f_0526_sm_9knw2 = models.FloatField(db_column='GTEX-1CB4F-0526-SM-9KNW2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1cb4g_0326_sm_7sb8r = models.FloatField(db_column='GTEX-1CB4G-0326-SM-7SB8R', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1cb4h_0326_sm_9wg5g = models.FloatField(db_column='GTEX-1CB4H-0326-SM-9WG5G', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1cb4i_0426_sm_7igpr = models.FloatField(db_column='GTEX-1CB4I-0426-SM-7IGPR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1cb4j_1126_sm_7pby1 = models.FloatField(db_column='GTEX-1CB4J-1126-SM-7PBY1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1e1vi_0226_sm_793cz = models.FloatField(db_column='GTEX-1E1VI-0226-SM-793CZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1e2ya_0226_sm_9mqly = models.FloatField(db_column='GTEX-1E2YA-0226-SM-9MQLY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1eh9u_0226_sm_7pby8 = models.FloatField(db_column='GTEX-1EH9U-0226-SM-7PBY8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ekgg_0126_sm_9yfls = models.FloatField(db_column='GTEX-1EKGG-0126-SM-9YFLS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1emgi_0226_sm_9mql1 = models.FloatField(db_column='GTEX-1EMGI-0226-SM-9MQL1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1eu9m_0326_sm_7rhgf = models.FloatField(db_column='GTEX-1EU9M-0326-SM-7RHGF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ewiq_0226_sm_793d3 = models.FloatField(db_column='GTEX-1EWIQ-0226-SM-793D3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ex96_1426_sm_7pbz5 = models.FloatField(db_column='GTEX-1EX96-1426-SM-7PBZ5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1f48j_0226_sm_7sb82 = models.FloatField(db_column='GTEX-1F48J-0226-SM-7SB82', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1f52s_0226_sm_7sb7u = models.FloatField(db_column='GTEX-1F52S-0226-SM-7SB7U', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1f5pk_2526_sm_9mqkn = models.FloatField(db_column='GTEX-1F5PK-2526-SM-9MQKN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1f6i4_0226_sm_9mqma = models.FloatField(db_column='GTEX-1F6I4-0226-SM-9MQMA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1f6rs_0226_sm_9mqko = models.FloatField(db_column='GTEX-1F6RS-0226-SM-9MQKO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1f75a_0226_sm_7pc2k = models.FloatField(db_column='GTEX-1F75A-0226-SM-7PC2K', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1f75i_0426_sm_7pc3s = models.FloatField(db_column='GTEX-1F75I-0426-SM-7PC3S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1f75w_0226_sm_9jggp = models.FloatField(db_column='GTEX-1F75W-0226-SM-9JGGP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1f88e_0526_sm_7sb8j = models.FloatField(db_column='GTEX-1F88E-0526-SM-7SB8J', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1f88f_2626_sm_9wg5k = models.FloatField(db_column='GTEX-1F88F-2626-SM-9WG5K', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1figz_1626_sm_7sb8l = models.FloatField(db_column='GTEX-1FIGZ-1626-SM-7SB8L', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gf9v_0226_sm_9mqka = models.FloatField(db_column='GTEX-1GF9V-0226-SM-9MQKA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gf9x_1926_sm_adeic = models.FloatField(db_column='GTEX-1GF9X-1926-SM-ADEIC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gmr2_2526_sm_9mqkw = models.FloatField(db_column='GTEX-1GMR2-2526-SM-9MQKW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gmr3_2026_sm_9mqlg = models.FloatField(db_column='GTEX-1GMR3-2026-SM-9MQLG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gmr8_0226_sm_9yfl3 = models.FloatField(db_column='GTEX-1GMR8-0226-SM-9YFL3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gmru_0226_sm_9yflw = models.FloatField(db_column='GTEX-1GMRU-0226-SM-9YFLW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gn1u_0226_sm_9yflq = models.FloatField(db_column='GTEX-1GN1U-0226-SM-9YFLQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gn1v_0226_sm_9wytn = models.FloatField(db_column='GTEX-1GN1V-0226-SM-9WYTN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gn1w_0626_sm_9mqk3 = models.FloatField(db_column='GTEX-1GN1W-0626-SM-9MQK3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gn2e_0326_sm_coh3c = models.FloatField(db_column='GTEX-1GN2E-0326-SM-COH3C', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gn73_0326_sm_9kntw = models.FloatField(db_column='GTEX-1GN73-0326-SM-9KNTW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gpi7_0226_sm_9mqkb = models.FloatField(db_column='GTEX-1GPI7-0226-SM-9MQKB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gtwx_0226_sm_9yfll = models.FloatField(db_column='GTEX-1GTWX-0226-SM-9YFLL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gz2q_0326_sm_9wg6n = models.FloatField(db_column='GTEX-1GZ2Q-0326-SM-9WG6N', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gz4h_1826_sm_9mqle = models.FloatField(db_column='GTEX-1GZ4H-1826-SM-9MQLE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gz4i_0226_sm_7rhho = models.FloatField(db_column='GTEX-1GZ4I-0226-SM-7RHHO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1h1cy_2626_sm_9mqkj = models.FloatField(db_column='GTEX-1H1CY-2626-SM-9MQKJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1h1de_2026_sm_9wg6q = models.FloatField(db_column='GTEX-1H1DE-2026-SM-9WG6Q', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1h1df_0226_sm_arl9a = models.FloatField(db_column='GTEX-1H1DF-0226-SM-ARL9A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1h1e6_2026_sm_9knvk = models.FloatField(db_column='GTEX-1H1E6-2026-SM-9KNVK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1h1zs_0526_sm_9wg5l = models.FloatField(db_column='GTEX-1H1ZS-0526-SM-9WG5L', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1h23p_0226_sm_9yflo = models.FloatField(db_column='GTEX-1H23P-0226-SM-9YFLO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1h2fu_0226_sm_9yfko = models.FloatField(db_column='GTEX-1H2FU-0226-SM-9YFKO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1h3o1_0526_sm_9mqls = models.FloatField(db_column='GTEX-1H3O1-0526-SM-9MQLS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1h3ve_0226_sm_9wyst = models.FloatField(db_column='GTEX-1H3VE-0226-SM-9WYST', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1h3vy_0226_sm_9yfmf = models.FloatField(db_column='GTEX-1H3VY-0226-SM-9YFMF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1h4p4_0226_sm_9yfkt = models.FloatField(db_column='GTEX-1H4P4-0226-SM-9YFKT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hb9e_0426_sm_cnppv = models.FloatField(db_column='GTEX-1HB9E-0426-SM-CNPPV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hbph_0526_sm_9yfmn = models.FloatField(db_column='GTEX-1HBPH-0526-SM-9YFMN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hbpi_1426_sm_b2lw7 = models.FloatField(db_column='GTEX-1HBPI-1426-SM-B2LW7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hbpm_0326_sm_cmkgr = models.FloatField(db_column='GTEX-1HBPM-0326-SM-CMKGR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hcu6_0226_sm_cgqes = models.FloatField(db_column='GTEX-1HCU6-0226-SM-CGQES', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hcu7_0326_sm_cmkgi = models.FloatField(db_column='GTEX-1HCU7-0326-SM-CMKGI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hcu8_0726_sm_adeir = models.FloatField(db_column='GTEX-1HCU8-0726-SM-ADEIR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hcua_2226_sm_adehf = models.FloatField(db_column='GTEX-1HCUA-2226-SM-ADEHF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hcve_0226_sm_cgqev = models.FloatField(db_column='GTEX-1HCVE-0226-SM-CGQEV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hfi6_0326_sm_adei5 = models.FloatField(db_column='GTEX-1HFI6-0326-SM-ADEI5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hfi7_2026_sm_cgqfr = models.FloatField(db_column='GTEX-1HFI7-2026-SM-CGQFR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hgf4_2526_sm_adeiz = models.FloatField(db_column='GTEX-1HGF4-2526-SM-ADEIZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hr98_0226_sm_cgqek = models.FloatField(db_column='GTEX-1HR98-0226-SM-CGQEK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hr9m_0226_sm_coh3e = models.FloatField(db_column='GTEX-1HR9M-0226-SM-COH3E', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hseh_0226_sm_ackvv = models.FloatField(db_column='GTEX-1HSEH-0226-SM-ACKVV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hsgn_0126_sm_cgqfu = models.FloatField(db_column='GTEX-1HSGN-0126-SM-CGQFU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hskv_0326_sm_adejc = models.FloatField(db_column='GTEX-1HSKV-0326-SM-ADEJC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hsmo_0226_sm_cgqez = models.FloatField(db_column='GTEX-1HSMO-0226-SM-CGQEZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hsmp_0226_sm_cgqfi = models.FloatField(db_column='GTEX-1HSMP-0226-SM-CGQFI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hsmq_1426_sm_adeht = models.FloatField(db_column='GTEX-1HSMQ-1426-SM-ADEHT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ht8w_0226_sm_cmkgt = models.FloatField(db_column='GTEX-1HT8W-0226-SM-CMKGT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hub1_0326_sm_a9skq = models.FloatField(db_column='GTEX-1HUB1-0326-SM-A9SKQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i19n_0426_sm_ackvy = models.FloatField(db_column='GTEX-1I19N-0426-SM-ACKVY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i1cd_0226_sm_cm2tl = models.FloatField(db_column='GTEX-1I1CD-0226-SM-CM2TL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i1gp_2326_sm_cgqfl = models.FloatField(db_column='GTEX-1I1GP-2326-SM-CGQFL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i1gq_0226_sm_coh3i = models.FloatField(db_column='GTEX-1I1GQ-0226-SM-COH3I', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i1gr_0226_sm_cmkhq = models.FloatField(db_column='GTEX-1I1GR-0226-SM-CMKHQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i1gs_0226_sm_b2lvx = models.FloatField(db_column='GTEX-1I1GS-0226-SM-B2LVX', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i1gt_0526_sm_cgqeq = models.FloatField(db_column='GTEX-1I1GT-0526-SM-CGQEQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i1gu_2326_sm_cgqfb = models.FloatField(db_column='GTEX-1I1GU-2326-SM-CGQFB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i1gv_0426_sm_arzlx = models.FloatField(db_column='GTEX-1I1GV-0426-SM-ARZLX', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i1hk_0226_sm_coh4a = models.FloatField(db_column='GTEX-1I1HK-0226-SM-COH4A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i4mk_2026_sm_b2lvr = models.FloatField(db_column='GTEX-1I4MK-2026-SM-B2LVR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i6k6_0226_sm_adeid = models.FloatField(db_column='GTEX-1I6K6-0226-SM-ADEID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i6k7_0226_sm_cji46 = models.FloatField(db_column='GTEX-1I6K7-0226-SM-CJI46', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1icg6_2626_sm_cgqg1 = models.FloatField(db_column='GTEX-1ICG6-2626-SM-CGQG1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1icly_0226_sm_arl7r = models.FloatField(db_column='GTEX-1ICLY-0226-SM-ARL7R', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1iclz_0226_sm_ckzpp = models.FloatField(db_column='GTEX-1ICLZ-0226-SM-CKZPP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1idfm_0226_sm_cmkfx = models.FloatField(db_column='GTEX-1IDFM-0226-SM-CMKFX', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1idjd_1226_sm_cm2tp = models.FloatField(db_column='GTEX-1IDJD-1226-SM-CM2TP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1idjf_0226_sm_cmkge = models.FloatField(db_column='GTEX-1IDJF-0226-SM-CMKGE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1idju_2526_sm_cmkgf = models.FloatField(db_column='GTEX-1IDJU-2526-SM-CMKGF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ie54_0226_sm_cmkhx = models.FloatField(db_column='GTEX-1IE54-0226-SM-CMKHX', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1igqw_0226_sm_coh43 = models.FloatField(db_column='GTEX-1IGQW-0226-SM-COH43', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ikjj_0226_sm_coh3t = models.FloatField(db_column='GTEX-1IKJJ-0226-SM-COH3T', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ikk5_0526_sm_cmkgg = models.FloatField(db_column='GTEX-1IKK5-0526-SM-CMKGG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1il2u_0326_sm_ce6t9 = models.FloatField(db_column='GTEX-1IL2U-0326-SM-CE6T9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1il2v_0226_sm_cmki2 = models.FloatField(db_column='GTEX-1IL2V-0226-SM-CMKI2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ioxb_0226_sm_cmkhy = models.FloatField(db_column='GTEX-1IOXB-0226-SM-CMKHY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1iy9m_0226_sm_cmkhp = models.FloatField(db_column='GTEX-1IY9M-0226-SM-CMKHP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1j1oq_0326_sm_cyptj = models.FloatField(db_column='GTEX-1J1OQ-0326-SM-CYPTJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1j1r8_2226_sm_arzmp = models.FloatField(db_column='GTEX-1J1R8-2226-SM-ARZMP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1j8ew_0226_sm_cypsw = models.FloatField(db_column='GTEX-1J8EW-0226-SM-CYPSW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1j8jj_0326_sm_cmkg6 = models.FloatField(db_column='GTEX-1J8JJ-0326-SM-CMKG6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1j8q3_1526_sm_cmkgb = models.FloatField(db_column='GTEX-1J8Q3-1526-SM-CMKGB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1j8qm_2326_sm_cypsl = models.FloatField(db_column='GTEX-1J8QM-2326-SM-CYPSL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jj6o_0226_sm_e6ci9 = models.FloatField(db_column='GTEX-1JJ6O-0226-SM-E6CI9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jje9_1226_sm_cnpoi = models.FloatField(db_column='GTEX-1JJE9-1226-SM-CNPOI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jjea_0226_sm_coh2x = models.FloatField(db_column='GTEX-1JJEA-0226-SM-COH2X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jk1u_2126_sm_cnpou = models.FloatField(db_column='GTEX-1JK1U-2126-SM-CNPOU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jkyn_1226_sm_cgqg8 = models.FloatField(db_column='GTEX-1JKYN-1226-SM-CGQG8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jkyr_0226_sm_cnpok = models.FloatField(db_column='GTEX-1JKYR-0226-SM-CNPOK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jmlx_0126_sm_cmkg9 = models.FloatField(db_column='GTEX-1JMLX-0126-SM-CMKG9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jmpy_1426_sm_arl8z = models.FloatField(db_column='GTEX-1JMPY-1426-SM-ARL8Z', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jmqi_2026_sm_cmkgp = models.FloatField(db_column='GTEX-1JMQI-2026-SM-CMKGP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jmqk_0126_sm_cm2s3 = models.FloatField(db_column='GTEX-1JMQK-0126-SM-CM2S3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jmql_0326_sm_cnpp6 = models.FloatField(db_column='GTEX-1JMQL-0326-SM-CNPP6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jn1m_0126_sm_d4p23 = models.FloatField(db_column='GTEX-1JN1M-0126-SM-D4P23', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jn6p_0226_sm_coh34 = models.FloatField(db_column='GTEX-1JN6P-0226-SM-COH34', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jn76_0226_sm_cmkgo = models.FloatField(db_column='GTEX-1JN76-0226-SM-CMKGO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1k2da_2126_sm_cgqgl = models.FloatField(db_column='GTEX-1K2DA-2126-SM-CGQGL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1k9t9_0226_sm_e9u6k = models.FloatField(db_column='GTEX-1K9T9-0226-SM-E9U6K', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1kafj_2426_sm_d4p32 = models.FloatField(db_column='GTEX-1KAFJ-2426-SM-D4P32', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1kana_0826_sm_d3l9j = models.FloatField(db_column='GTEX-1KANA-0826-SM-D3L9J', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1kd5a_0326_sm_d5ovd = models.FloatField(db_column='GTEX-1KD5A-0326-SM-D5OVD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1kwve_1326_sm_e6cj1 = models.FloatField(db_column='GTEX-1KWVE-1326-SM-E6CJ1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1kxam_2326_sm_cyptd = models.FloatField(db_column='GTEX-1KXAM-2326-SM-CYPTD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1l5ne_2626_sm_e9u6p = models.FloatField(db_column='GTEX-1L5NE-2626-SM-E9U6P', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lb8k_0326_sm_e9tjc = models.FloatField(db_column='GTEX-1LB8K-0326-SM-E9TJC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lbac_0226_sm_dhxjz = models.FloatField(db_column='GTEX-1LBAC-0226-SM-DHXJZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lg7y_0426_sm_dkpqb = models.FloatField(db_column='GTEX-1LG7Y-0426-SM-DKPQB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lg7z_2026_sm_dlhbp = models.FloatField(db_column='GTEX-1LG7Z-2026-SM-DLHBP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lgou_2226_sm_e9u56 = models.FloatField(db_column='GTEX-1LGOU-2226-SM-E9U56', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lgrb_2426_sm_cnpp3 = models.FloatField(db_column='GTEX-1LGRB-2426-SM-CNPP3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lh75_2526_sm_e9u5a = models.FloatField(db_column='GTEX-1LH75-2526-SM-E9U5A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lsnl_0526_sm_dipfi = models.FloatField(db_column='GTEX-1LSNL-0526-SM-DIPFI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lsnm_2026_sm_e6cij = models.FloatField(db_column='GTEX-1LSNM-2026-SM-E6CIJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lsvx_0126_sm_evycy = models.FloatField(db_column='GTEX-1LSVX-0126-SM-EVYCY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lva9_0226_sm_e9u5n = models.FloatField(db_column='GTEX-1LVA9-0226-SM-E9U5N', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lvan_0126_sm_coh4h = models.FloatField(db_column='GTEX-1LVAN-0126-SM-COH4H', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lvao_0226_sm_e9u6o = models.FloatField(db_column='GTEX-1LVAO-0226-SM-E9U6O', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1m5qr_2126_sm_dkpqm = models.FloatField(db_column='GTEX-1M5QR-2126-SM-DKPQM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ma7w_1926_sm_e6cio = models.FloatField(db_column='GTEX-1MA7W-1926-SM-E6CIO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ma7x_2126_sm_e6cix = models.FloatField(db_column='GTEX-1MA7X-2126-SM-E6CIX', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1mcc2_2326_sm_e9u5g = models.FloatField(db_column='GTEX-1MCC2-2326-SM-E9U5G', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1mcyp_1826_sm_e9j2q = models.FloatField(db_column='GTEX-1MCYP-1826-SM-E9J2Q', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1mgnq_0226_sm_evyck = models.FloatField(db_column='GTEX-1MGNQ-0226-SM-EVYCK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1mjk2_0526_sm_dtxe6 = models.FloatField(db_column='GTEX-1MJK2-0526-SM-DTXE6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1muqo_0526_sm_e9j31 = models.FloatField(db_column='GTEX-1MUQO-0526-SM-E9J31', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1n2dw_0326_sm_e9tk3 = models.FloatField(db_column='GTEX-1N2DW-0326-SM-E9TK3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1n2ef_0626_sm_e9j32 = models.FloatField(db_column='GTEX-1N2EF-0626-SM-E9J32', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1nhnu_1126_sm_e9j2c = models.FloatField(db_column='GTEX-1NHNU-1126-SM-E9J2C', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ofpy_2326_sm_e8vnu = models.FloatField(db_column='GTEX-1OFPY-2326-SM-E8VNU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ojc4_1726_sm_exusv = models.FloatField(db_column='GTEX-1OJC4-1726-SM-EXUSV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1pbji_0426_sm_e8vnm = models.FloatField(db_column='GTEX-1PBJI-0426-SM-E8VNM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1pdj9_0426_sm_e9j3e = models.FloatField(db_column='GTEX-1PDJ9-0426-SM-E9J3E', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1pfey_1626_sm_e9j3m = models.FloatField(db_column='GTEX-1PFEY-1626-SM-E9J3M', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1pige_0526_sm_dtxfa = models.FloatField(db_column='GTEX-1PIGE-0526-SM-DTXFA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1piig_0326_sm_evybv = models.FloatField(db_column='GTEX-1PIIG-0326-SM-EVYBV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1poen_0226_sm_eyyxe = models.FloatField(db_column='GTEX-1POEN-0226-SM-EYYXE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ppgy_0326_sm_dtxfd = models.FloatField(db_column='GTEX-1PPGY-0326-SM-DTXFD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1pph8_0626_sm_ewrn9 = models.FloatField(db_column='GTEX-1PPH8-0626-SM-EWRN9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1pwst_0326_sm_eaz42 = models.FloatField(db_column='GTEX-1PWST-0326-SM-EAZ42', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qaet_1126_sm_e8vml = models.FloatField(db_column='GTEX-1QAET-1126-SM-E8VML', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qcly_0526_sm_eaz47 = models.FloatField(db_column='GTEX-1QCLY-0526-SM-EAZ47', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qepi_0226_sm_ewrmr = models.FloatField(db_column='GTEX-1QEPI-0226-SM-EWRMR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qp28_0226_sm_e9j2n = models.FloatField(db_column='GTEX-1QP28-0226-SM-E9J2N', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qp29_0726_sm_dtxfm = models.FloatField(db_column='GTEX-1QP29-0726-SM-DTXFM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qp2a_0226_sm_evybc = models.FloatField(db_column='GTEX-1QP2A-0226-SM-EVYBC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qp66_1326_sm_dtxdq = models.FloatField(db_column='GTEX-1QP66-1326-SM-DTXDQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qp67_1726_sm_e8vop = models.FloatField(db_column='GTEX-1QP67-1726-SM-E8VOP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qp6s_0126_sm_e9j4k = models.FloatField(db_column='GTEX-1QP6S-0126-SM-E9J4K', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qp9n_1526_sm_dtxfk = models.FloatField(db_column='GTEX-1QP9N-1526-SM-DTXFK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qpfj_0126_sm_e9j4b = models.FloatField(db_column='GTEX-1QPFJ-0126-SM-E9J4B', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qw4y_1626_sm_eaz41 = models.FloatField(db_column='GTEX-1QW4Y-1626-SM-EAZ41', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1r46s_0526_sm_evybz = models.FloatField(db_column='GTEX-1R46S-0526-SM-EVYBZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1r7eu_0326_sm_ewrnj = models.FloatField(db_column='GTEX-1R7EU-0326-SM-EWRNJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1r7ev_1926_sm_evybf = models.FloatField(db_column='GTEX-1R7EV-1926-SM-EVYBF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1r9k5_0226_sm_ewrnf = models.FloatField(db_column='GTEX-1R9K5-0226-SM-EWRNF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1r9pm_2126_sm_e8vob = models.FloatField(db_column='GTEX-1R9PM-2126-SM-E8VOB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1raza_0226_sm_e9u4w = models.FloatField(db_column='GTEX-1RAZA-0226-SM-E9U4W', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1razq_0626_sm_e8vor = models.FloatField(db_column='GTEX-1RAZQ-0626-SM-E8VOR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1razr_0226_sm_evyc6 = models.FloatField(db_column='GTEX-1RAZR-0226-SM-EVYC6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1rdx4_0226_sm_dtxg1 = models.FloatField(db_column='GTEX-1RDX4-0226-SM-DTXG1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1rqec_0526_sm_e6chv = models.FloatField(db_column='GTEX-1RQEC-0526-SM-E6CHV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1s5zu_0226_sm_e6chw = models.FloatField(db_column='GTEX-1S5ZU-0226-SM-E6CHW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1s82p_0226_sm_e6ci6 = models.FloatField(db_column='GTEX-1S82P-0226-SM-E6CI6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1s831_0326_sm_evyd3 = models.FloatField(db_column='GTEX-1S831-0326-SM-EVYD3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1s83e_0226_sm_evycw = models.FloatField(db_column='GTEX-1S83E-0226-SM-EVYCW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_n7ms_0326_sm_4e3k2 = models.FloatField(db_column='GTEX-N7MS-0326-SM-4E3K2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_nfk9_0326_sm_3mjgv = models.FloatField(db_column='GTEX-NFK9-0326-SM-3MJGV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_npj8_0226_sm_48tbn = models.FloatField(db_column='GTEX-NPJ8-0226-SM-48TBN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_o5yt_0226_sm_32pk5 = models.FloatField(db_column='GTEX-O5YT-0226-SM-32PK5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_o5yv_0226_sm_48tby = models.FloatField(db_column='GTEX-O5YV-0226-SM-48TBY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ohpk_0226_sm_3mjh6 = models.FloatField(db_column='GTEX-OHPK-0226-SM-3MJH6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ohpm_0226_sm_3lk61 = models.FloatField(db_column='GTEX-OHPM-0226-SM-3LK61', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ohpn_0226_sm_48tbv = models.FloatField(db_column='GTEX-OHPN-0226-SM-48TBV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_oizf_0226_sm_e9ti3 = models.FloatField(db_column='GTEX-OIZF-0226-SM-E9TI3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_oizg_0826_sm_e9ti4 = models.FloatField(db_column='GTEX-OIZG-0826-SM-E9TI4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_oizh_0226_sm_2yumh = models.FloatField(db_column='GTEX-OIZH-0226-SM-2YUMH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_oizi_0226_sm_2xcee = models.FloatField(db_column='GTEX-OIZI-0226-SM-2XCEE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_oobj_0226_sm_2yumm = models.FloatField(db_column='GTEX-OOBJ-0226-SM-2YUMM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_oobk_0226_sm_2yumf = models.FloatField(db_column='GTEX-OOBK-0226-SM-2YUMF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_oxrk_0326_sm_3nb3r = models.FloatField(db_column='GTEX-OXRK-0326-SM-3NB3R', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_oxrl_0226_sm_3nb18 = models.FloatField(db_column='GTEX-OXRL-0226-SM-3NB18', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_oxrn_0226_sm_2i5ej = models.FloatField(db_column='GTEX-OXRN-0226-SM-2I5EJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_oxro_0226_sm_3lk6f = models.FloatField(db_column='GTEX-OXRO-0226-SM-3LK6F', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_oxrp_0226_sm_3nb14 = models.FloatField(db_column='GTEX-OXRP-0226-SM-3NB14', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_p44g_2326_sm_2xccz = models.FloatField(db_column='GTEX-P44G-2326-SM-2XCCZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_p44h_0326_sm_2xces = models.FloatField(db_column='GTEX-P44H-0326-SM-2XCES', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_p4pp_0226_sm_d4p1z = models.FloatField(db_column='GTEX-P4PP-0226-SM-D4P1Z', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_p4pq_0226_sm_2s1nk = models.FloatField(db_column='GTEX-P4PQ-0226-SM-2S1NK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_p4qs_0226_sm_3nb1u = models.FloatField(db_column='GTEX-P4QS-0226-SM-3NB1U', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_p4qt_0226_sm_3lk68 = models.FloatField(db_column='GTEX-P4QT-0226-SM-3LK68', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_p78b_0226_sm_3nb1z = models.FloatField(db_column='GTEX-P78B-0226-SM-3NB1Z', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_plz4_0226_sm_cypr1 = models.FloatField(db_column='GTEX-PLZ4-0226-SM-CYPR1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_plz5_1826_sm_3nb22 = models.FloatField(db_column='GTEX-PLZ5-1826-SM-3NB22', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_plz6_1326_sm_3nb24 = models.FloatField(db_column='GTEX-PLZ6-1326-SM-3NB24', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_pomq_2326_sm_dhxis = models.FloatField(db_column='GTEX-POMQ-2326-SM-DHXIS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_poyw_0726_sm_2xceo = models.FloatField(db_column='GTEX-POYW-0726-SM-2XCEO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_psdg_0326_sm_48tcp = models.FloatField(db_column='GTEX-PSDG-0326-SM-48TCP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_pwcy_1926_sm_3nb25 = models.FloatField(db_column='GTEX-PWCY-1926-SM-3NB25', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_pwn1_0226_sm_dkpo9 = models.FloatField(db_column='GTEX-PWN1-0226-SM-DKPO9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_px3g_0226_sm_dkpof = models.FloatField(db_column='GTEX-PX3G-0226-SM-DKPOF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_q2ag_0226_sm_2s1p4 = models.FloatField(db_column='GTEX-Q2AG-0226-SM-2S1P4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_q2ah_1726_sm_dipdv = models.FloatField(db_column='GTEX-Q2AH-1726-SM-DIPDV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_q2ai_1426_sm_2s1p5 = models.FloatField(db_column='GTEX-Q2AI-1426-SM-2S1P5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_q734_1826_sm_2i3el = models.FloatField(db_column='GTEX-Q734-1826-SM-2I3EL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qcqg_1826_sm_2s1p2 = models.FloatField(db_column='GTEX-QCQG-1826-SM-2S1P2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qdt8_0226_sm_32pl4 = models.FloatField(db_column='GTEX-QDT8-0226-SM-32PL4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qdvj_1826_sm_2s1p3 = models.FloatField(db_column='GTEX-QDVJ-1826-SM-2S1P3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qdvn_2126_sm_33hbs = models.FloatField(db_column='GTEX-QDVN-2126-SM-33HBS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qeg4_0326_sm_dipe3 = models.FloatField(db_column='GTEX-QEG4-0326-SM-DIPE3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qeg5_0326_sm_2s1pb = models.FloatField(db_column='GTEX-QEG5-0326-SM-2S1PB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qel4_0326_sm_3gae5 = models.FloatField(db_column='GTEX-QEL4-0326-SM-3GAE5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qesd_1526_sm_2s1qt = models.FloatField(db_column='GTEX-QESD-1526-SM-2S1QT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qlq7_1526_sm_2s1qa = models.FloatField(db_column='GTEX-QLQ7-1526-SM-2S1QA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qlqw_1226_sm_2s1q9 = models.FloatField(db_column='GTEX-QLQW-1226-SM-2S1Q9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qmrm_1726_sm_2s1qg = models.FloatField(db_column='GTEX-QMRM-1726-SM-2S1QG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qv31_1326_sm_2s1qe = models.FloatField(db_column='GTEX-QV31-1326-SM-2S1QE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qv44_1825_sm_447cf = models.FloatField(db_column='GTEX-QV44-1825-SM-447CF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_r3rs_0226_sm_eyyve = models.FloatField(db_column='GTEX-R3RS-0226-SM-EYYVE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_r45c_0226_sm_evyaj = models.FloatField(db_column='GTEX-R45C-0226-SM-EVYAJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_r53t_1626_sm_3gaew = models.FloatField(db_column='GTEX-R53T-1626-SM-3GAEW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_r55c_1626_sm_48feg = models.FloatField(db_column='GTEX-R55C-1626-SM-48FEG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_r55d_0326_sm_48fes = models.FloatField(db_column='GTEX-R55D-0326-SM-48FES', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_r55g_2426_sm_2tc5i = models.FloatField(db_column='GTEX-R55G-2426-SM-2TC5I', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_rey6_0326_sm_2tf5a = models.FloatField(db_column='GTEX-REY6-0326-SM-2TF5A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_rm2n_1726_sm_2tf55 = models.FloatField(db_column='GTEX-RM2N-1726-SM-2TF55', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_rnor_0226_sm_ez6mf = models.FloatField(db_column='GTEX-RNOR-0226-SM-EZ6MF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_rtls_0226_sm_2tf5e = models.FloatField(db_column='GTEX-RTLS-0226-SM-2TF5E', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ru72_1026_sm_46mug = models.FloatField(db_column='GTEX-RU72-1026-SM-46MUG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_rusq_1626_sm_ez6l4 = models.FloatField(db_column='GTEX-RUSQ-1626-SM-EZ6L4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_rvpv_1526_sm_exohf = models.FloatField(db_column='GTEX-RVPV-1526-SM-EXOHF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_rwsa_0226_sm_2xcba = models.FloatField(db_column='GTEX-RWSA-0226-SM-2XCBA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_s32w_2226_sm_2xcay = models.FloatField(db_column='GTEX-S32W-2226-SM-2XCAY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_s33h_1126_sm_2xcb6 = models.FloatField(db_column='GTEX-S33H-1126-SM-2XCB6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_s4p3_1526_sm_e9j3w = models.FloatField(db_column='GTEX-S4P3-1526-SM-E9J3W', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_s7se_0226_sm_2xcd4 = models.FloatField(db_column='GTEX-S7SE-0226-SM-2XCD4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_s95s_1326_sm_2xcdk = models.FloatField(db_column='GTEX-S95S-1326-SM-2XCDK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_siu8_0226_sm_2xcds = models.FloatField(db_column='GTEX-SIU8-0226-SM-2XCDS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_sjxc_0226_sm_2xcdu = models.FloatField(db_column='GTEX-SJXC-0226-SM-2XCDU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_sn8g_0226_sm_4dm6b = models.FloatField(db_column='GTEX-SN8G-0226-SM-4DM6B', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_snmc_1326_sm_2xcfk = models.FloatField(db_column='GTEX-SNMC-1326-SM-2XCFK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_snos_1426_sm_32ply = models.FloatField(db_column='GTEX-SNOS-1426-SM-32PLY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ssa3_0226_sm_32qpn = models.FloatField(db_column='GTEX-SSA3-0226-SM-32QPN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_sucs_1826_sm_32pm1 = models.FloatField(db_column='GTEX-SUCS-1826-SM-32PM1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_t2is_0226_sm_32qph = models.FloatField(db_column='GTEX-T2IS-0226-SM-32QPH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_t5jc_0526_sm_32pm7 = models.FloatField(db_column='GTEX-T5JC-0526-SM-32PM7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_t5jw_1726_sm_3gadn = models.FloatField(db_column='GTEX-T5JW-1726-SM-3GADN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_t6mn_0226_sm_32pmd = models.FloatField(db_column='GTEX-T6MN-0226-SM-32PMD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_t6mo_1726_sm_33hb8 = models.FloatField(db_column='GTEX-T6MO-1726-SM-33HB8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_t8em_1126_sm_3db7d = models.FloatField(db_column='GTEX-T8EM-1126-SM-3DB7D', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_tkq1_1126_sm_4giaz = models.FloatField(db_column='GTEX-TKQ1-1126-SM-4GIAZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_tml8_2026_sm_32qop = models.FloatField(db_column='GTEX-TML8-2026-SM-32QOP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_tmzs_0226_sm_3db9n = models.FloatField(db_column='GTEX-TMZS-0226-SM-3DB9N', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_tse9_0226_sm_3db84 = models.FloatField(db_column='GTEX-TSE9-0226-SM-3DB84', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_u3zm_1026_sm_ez6ld = models.FloatField(db_column='GTEX-U3ZM-1026-SM-EZ6LD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_u3zn_2626_sm_3db7t = models.FloatField(db_column='GTEX-U3ZN-2626-SM-3DB7T', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_u412_0526_sm_3db9i = models.FloatField(db_column='GTEX-U412-0526-SM-3DB9I', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_u4b1_1726_sm_3db9f = models.FloatField(db_column='GTEX-U4B1-1726-SM-3DB9F', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_u8xe_0426_sm_3db91 = models.FloatField(db_column='GTEX-U8XE-0426-SM-3DB91', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ujhi_1626_sm_3db9a = models.FloatField(db_column='GTEX-UJHI-1626-SM-3DB9A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_utho_0426_sm_ce6qu = models.FloatField(db_column='GTEX-UTHO-0426-SM-CE6QU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_vjwn_0226_sm_ez6lf = models.FloatField(db_column='GTEX-VJWN-0226-SM-EZ6LF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_vjya_1326_sm_3gijc = models.FloatField(db_column='GTEX-VJYA-1326-SM-3GIJC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_vusg_2426_sm_4kkzg = models.FloatField(db_column='GTEX-VUSG-2426-SM-4KKZG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_vush_0226_sm_exuqv = models.FloatField(db_column='GTEX-VUSH-0226-SM-EXUQV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_w5wg_2526_sm_4soj2 = models.FloatField(db_column='GTEX-W5WG-2526-SM-4SOJ2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_w5x1_2626_sm_4lmi8 = models.FloatField(db_column='GTEX-W5X1-2626-SM-4LMI8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wey5_1926_sm_3gil8 = models.FloatField(db_column='GTEX-WEY5-1926-SM-3GIL8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wfg7_2526_sm_ewrm5 = models.FloatField(db_column='GTEX-WFG7-2526-SM-EWRM5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wfg8_2326_sm_dipdx = models.FloatField(db_column='GTEX-WFG8-2326-SM-DIPDX', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wfjo_1926_sm_3gila = models.FloatField(db_column='GTEX-WFJO-1926-SM-3GILA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wfon_2226_sm_3tw8w = models.FloatField(db_column='GTEX-WFON-2226-SM-3TW8W', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wh7g_2226_sm_3nmbn = models.FloatField(db_column='GTEX-WH7G-2226-SM-3NMBN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_whpg_2126_sm_4m1zm = models.FloatField(db_column='GTEX-WHPG-2126-SM-4M1ZM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wi4n_1126_sm_3lk7q = models.FloatField(db_column='GTEX-WI4N-1126-SM-3LK7Q', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wl46_0326_sm_3lk6y = models.FloatField(db_column='GTEX-WL46-0326-SM-3LK6Y', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wvjs_0226_sm_4mvou = models.FloatField(db_column='GTEX-WVJS-0226-SM-4MVOU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wvlh_0226_sm_3mjg6 = models.FloatField(db_column='GTEX-WVLH-0226-SM-3MJG6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wy7c_2426_sm_3nb2v = models.FloatField(db_column='GTEX-WY7C-2426-SM-3NB2V', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wyjk_0226_sm_eyyv8 = models.FloatField(db_column='GTEX-WYJK-0226-SM-EYYV8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_x15g_2326_sm_4pqzs = models.FloatField(db_column='GTEX-X15G-2326-SM-4PQZS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_x261_0226_sm_3nmd2 = models.FloatField(db_column='GTEX-X261-0226-SM-3NMD2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_x4eo_0426_sm_4qasa = models.FloatField(db_column='GTEX-X4EO-0426-SM-4QASA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_x4lf_1726_sm_3nmbz = models.FloatField(db_column='GTEX-X4LF-1726-SM-3NMBZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_x4xy_0326_sm_46mvz = models.FloatField(db_column='GTEX-X4XY-0326-SM-46MVZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_x5eb_2426_sm_4e3hx = models.FloatField(db_column='GTEX-X5EB-2426-SM-4E3HX', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_x638_0226_sm_47jz9 = models.FloatField(db_column='GTEX-X638-0226-SM-47JZ9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_x88g_0226_sm_4gie4 = models.FloatField(db_column='GTEX-X88G-0226-SM-4GIE4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_x8hc_0226_sm_4e3k1 = models.FloatField(db_column='GTEX-X8HC-0226-SM-4E3K1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xaj8_0926_sm_47jxz = models.FloatField(db_column='GTEX-XAJ8-0926-SM-47JXZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xbec_0326_sm_4at4m = models.FloatField(db_column='GTEX-XBEC-0326-SM-4AT4M', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xbed_2326_sm_47jyr = models.FloatField(db_column='GTEX-XBED-2326-SM-47JYR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xbew_0726_sm_4qarx = models.FloatField(db_column='GTEX-XBEW-0726-SM-4QARX', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xgq4_2226_sm_4at4y = models.FloatField(db_column='GTEX-XGQ4-2226-SM-4AT4Y', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xk95_0426_sm_4at4r = models.FloatField(db_column='GTEX-XK95-0426-SM-4AT4R', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xlm4_0226_sm_4at4n = models.FloatField(db_column='GTEX-XLM4-0226-SM-4AT4N', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xmd2_0226_sm_4wwee = models.FloatField(db_column='GTEX-XMD2-0226-SM-4WWEE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xmk1_2226_sm_4b673 = models.FloatField(db_column='GTEX-XMK1-2226-SM-4B673', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xot4_0226_sm_4b66z = models.FloatField(db_column='GTEX-XOT4-0226-SM-4B66Z', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xpvg_2726_sm_4b66w = models.FloatField(db_column='GTEX-XPVG-2726-SM-4B66W', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xq3s_1626_sm_4wayn = models.FloatField(db_column='GTEX-XQ3S-1626-SM-4WAYN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xq8i_0526_sm_4bops = models.FloatField(db_column='GTEX-XQ8I-0526-SM-4BOPS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xuw1_0526_sm_4bop3 = models.FloatField(db_column='GTEX-XUW1-0526-SM-4BOP3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xuys_0226_sm_47jx1 = models.FloatField(db_column='GTEX-XUYS-0226-SM-47JX1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xuzc_1826_sm_4brvo = models.FloatField(db_column='GTEX-XUZC-1826-SM-4BRVO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xv7q_2626_sm_4brva = models.FloatField(db_column='GTEX-XV7Q-2626-SM-4BRVA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xxek_2426_sm_4brus = models.FloatField(db_column='GTEX-XXEK-2426-SM-4BRUS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xyks_2726_sm_4e3ic = models.FloatField(db_column='GTEX-XYKS-2726-SM-4E3IC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y111_0226_sm_4soiw = models.FloatField(db_column='GTEX-Y111-0226-SM-4SOIW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y114_2326_sm_4tt7x = models.FloatField(db_column='GTEX-Y114-2326-SM-4TT7X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y3i4_2226_sm_4tt7o = models.FloatField(db_column='GTEX-Y3I4-2226-SM-4TT7O', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y3ik_2526_sm_4wwdm = models.FloatField(db_column='GTEX-Y3IK-2526-SM-4WWDM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y5v5_2426_sm_5ifja = models.FloatField(db_column='GTEX-Y5V5-2426-SM-5IFJA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y5v6_2526_sm_5ifjv = models.FloatField(db_column='GTEX-Y5V6-2526-SM-5IFJV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y8e4_0726_sm_4wwfn = models.FloatField(db_column='GTEX-Y8E4-0726-SM-4WWFN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y8e5_0226_sm_57wcm = models.FloatField(db_column='GTEX-Y8E5-0226-SM-57WCM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y8lw_1926_sm_4wwfz = models.FloatField(db_column='GTEX-Y8LW-1926-SM-4WWFZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y9lg_2026_sm_62lfs = models.FloatField(db_column='GTEX-Y9LG-2026-SM-62LFS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_yb5e_2126_sm_5ifi7 = models.FloatField(db_column='GTEX-YB5E-2126-SM-5IFI7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_yb5k_2226_sm_4wwg1 = models.FloatField(db_column='GTEX-YB5K-2226-SM-4WWG1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_yec3_1226_sm_5ifi8 = models.FloatField(db_column='GTEX-YEC3-1226-SM-5IFI8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_yec4_2426_sm_57wfo = models.FloatField(db_column='GTEX-YEC4-2426-SM-57WFO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_yeck_0226_sm_4w215 = models.FloatField(db_column='GTEX-YECK-0226-SM-4W215', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_yf7o_2426_sm_5ifjl = models.FloatField(db_column='GTEX-YF7O-2426-SM-5IFJL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_yfc4_0226_sm_57wd2 = models.FloatField(db_column='GTEX-YFC4-0226-SM-57WD2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_yfco_2026_sm_4w21q = models.FloatField(db_column='GTEX-YFCO-2026-SM-4W21Q', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_yj89_0226_sm_4tt3y = models.FloatField(db_column='GTEX-YJ89-0226-SM-4TT3Y', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_yj8a_0526_sm_5ifht = models.FloatField(db_column='GTEX-YJ8A-0526-SM-5IFHT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_yj8o_2426_sm_5hl7s = models.FloatField(db_column='GTEX-YJ8O-2426-SM-5HL7S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_z93s_0226_sm_5hl7r = models.FloatField(db_column='GTEX-Z93S-0226-SM-5HL7R', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_z93t_0226_sm_5hl5z = models.FloatField(db_column='GTEX-Z93T-0226-SM-5HL5Z', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_z9ew_1826_sm_5cvma = models.FloatField(db_column='GTEX-Z9EW-1826-SM-5CVMA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zajg_0226_sm_5hl81 = models.FloatField(db_column='GTEX-ZAJG-0226-SM-5HL81', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zak1_0226_sm_5cvmx = models.FloatField(db_column='GTEX-ZAK1-0226-SM-5CVMX', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zc5h_0126_sm_4wayl = models.FloatField(db_column='GTEX-ZC5H-0126-SM-4WAYL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zdts_0226_sm_5hl7q = models.FloatField(db_column='GTEX-ZDTS-0226-SM-5HL7Q', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zdtt_2626_sm_5s2op = models.FloatField(db_column='GTEX-ZDTT-2626-SM-5S2OP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zdxo_2426_sm_5s2nj = models.FloatField(db_column='GTEX-ZDXO-2426-SM-5S2NJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zdys_2126_sm_5s2p2 = models.FloatField(db_column='GTEX-ZDYS-2126-SM-5S2P2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ze7o_0226_sm_5s2n1 = models.FloatField(db_column='GTEX-ZE7O-0226-SM-5S2N1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ze9c_2826_sm_5s2mo = models.FloatField(db_column='GTEX-ZE9C-2826-SM-5S2MO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zex8_2326_sm_5s2mn = models.FloatField(db_column='GTEX-ZEX8-2326-SM-5S2MN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zf28_0226_sm_5s2oe = models.FloatField(db_column='GTEX-ZF28-0226-SM-5S2OE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zf29_2226_sm_4wwb9 = models.FloatField(db_column='GTEX-ZF29-2226-SM-4WWB9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zf3c_0226_sm_4wwb3 = models.FloatField(db_column='GTEX-ZF3C-0226-SM-4WWB3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zgay_0626_sm_do92e = models.FloatField(db_column='GTEX-ZGAY-0626-SM-DO92E', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zlfu_2626_sm_do91l = models.FloatField(db_column='GTEX-ZLFU-2626-SM-DO91L', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zlv1_1826_sm_5fqu5 = models.FloatField(db_column='GTEX-ZLV1-1826-SM-5FQU5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zlwg_2226_sm_do92v = models.FloatField(db_column='GTEX-ZLWG-2226-SM-DO92V', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zp4g_2326_sm_57wem = models.FloatField(db_column='GTEX-ZP4G-2326-SM-57WEM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zpcl_2126_sm_57wfz = models.FloatField(db_column='GTEX-ZPCL-2126-SM-57WFZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zpic_1826_sm_57wfe = models.FloatField(db_column='GTEX-ZPIC-1826-SM-57WFE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zpu1_2426_sm_4wwfm = models.FloatField(db_column='GTEX-ZPU1-2426-SM-4WWFM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zqg8_1526_sm_5hl65 = models.FloatField(db_column='GTEX-ZQG8-1526-SM-5HL65', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zt9x_1926_sm_57we7 = models.FloatField(db_column='GTEX-ZT9X-1926-SM-57WE7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ztpg_0226_sm_5o99i = models.FloatField(db_column='GTEX-ZTPG-0226-SM-5O99I', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ztss_2026_sm_5987k = models.FloatField(db_column='GTEX-ZTSS-2026-SM-5987K', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ztx8_1526_sm_5n9gi = models.FloatField(db_column='GTEX-ZTX8-1526-SM-5N9GI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zua1_0226_sm_5nq9q = models.FloatField(db_column='GTEX-ZUA1-0226-SM-5NQ9Q', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zv68_0226_sm_59hjf = models.FloatField(db_column='GTEX-ZV68-0226-SM-59HJF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zve2_0326_sm_57wfc = models.FloatField(db_column='GTEX-ZVE2-0326-SM-57WFC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zvp2_1826_sm_5gu62 = models.FloatField(db_column='GTEX-ZVP2-1826-SM-5GU62', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zvt2_2226_sm_5nq6p = models.FloatField(db_column='GTEX-ZVT2-2226-SM-5NQ6P', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zvt4_0226_sm_51msd = models.FloatField(db_column='GTEX-ZVT4-0226-SM-51MSD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zvtk_0526_sm_5gzwt = models.FloatField(db_column='GTEX-ZVTK-0526-SM-5GZWT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zvzo_0226_sm_5a5la = models.FloatField(db_column='GTEX-ZVZO-0226-SM-5A5LA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zvzp_2326_sm_59hl4 = models.FloatField(db_column='GTEX-ZVZP-2326-SM-59HL4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zxes_2026_sm_5nq6r = models.FloatField(db_column='GTEX-ZXES-2026-SM-5NQ6R', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zxg5_0226_sm_59hji = models.FloatField(db_column='GTEX-ZXG5-0226-SM-59HJI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zyfc_0326_sm_5nq7h = models.FloatField(db_column='GTEX-ZYFC-0326-SM-5NQ7H', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zyfd_0226_sm_5nq86 = models.FloatField(db_column='GTEX-ZYFD-0226-SM-5NQ86', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zyt6_0326_sm_7lg5r = models.FloatField(db_column='GTEX-ZYT6-0326-SM-7LG5R', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zyvf_0226_sm_5gieg = models.FloatField(db_column='GTEX-ZYVF-0226-SM-5GIEG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zyw4_0226_sm_5e44m = models.FloatField(db_column='GTEX-ZYW4-0226-SM-5E44M', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zyy3_0226_sm_5e45m = models.FloatField(db_column='GTEX-ZYY3-0226-SM-5E45M', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zz64_1626_sm_5e43w = models.FloatField(db_column='GTEX-ZZ64-1626-SM-5E43W', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zzpu_2726_sm_5nq8o = models.FloatField(db_column='GTEX-ZZPU-2726-SM-5NQ8O', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'adipose_subcutaneous'


class ArteryAorta(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    gtex_111ys_0526_sm_5gzxj = models.FloatField(db_column='GTEX-111YS-0526-SM-5GZXJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1122o_1126_sm_5nq8x = models.FloatField(db_column='GTEX-1122O-1126-SM-5NQ8X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1128s_0326_sm_5gzzf = models.FloatField(db_column='GTEX-1128S-0326-SM-5GZZF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_117xs_0426_sm_5gzzn = models.FloatField(db_column='GTEX-117XS-0426-SM-5GZZN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_117yw_0226_sm_5n9cm = models.FloatField(db_column='GTEX-117YW-0226-SM-5N9CM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11dxx_0426_sm_5eq5f = models.FloatField(db_column='GTEX-11DXX-0426-SM-5EQ5F', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11dxz_0426_sm_5987y = models.FloatField(db_column='GTEX-11DXZ-0426-SM-5987Y', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11dyg_1226_sm_5n9dc = models.FloatField(db_column='GTEX-11DYG-1226-SM-5N9DC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11em3_0226_sm_5985y = models.FloatField(db_column='GTEX-11EM3-0226-SM-5985Y', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11emc_0926_sm_59863 = models.FloatField(db_column='GTEX-11EMC-0926-SM-59863', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11gs4_0326_sm_5n9f7 = models.FloatField(db_column='GTEX-11GS4-0326-SM-5N9F7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11gsp_1126_sm_5a5lm = models.FloatField(db_column='GTEX-11GSP-1126-SM-5A5LM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11i78_0726_sm_5a5m1 = models.FloatField(db_column='GTEX-11I78-0726-SM-5A5M1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11lck_0726_sm_5pnyc = models.FloatField(db_column='GTEX-11LCK-0726-SM-5PNYC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11nuk_0726_sm_5a5me = models.FloatField(db_column='GTEX-11NUK-0726-SM-5A5ME', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11onc_0926_sm_5bc5e = models.FloatField(db_column='GTEX-11ONC-0926-SM-5BC5E', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11p81_0326_sm_5hl6b = models.FloatField(db_column='GTEX-11P81-0326-SM-5HL6B', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11p82_0126_sm_5hl72 = models.FloatField(db_column='GTEX-11P82-0126-SM-5HL72', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11tt1_1226_sm_5q5av = models.FloatField(db_column='GTEX-11TT1-1226-SM-5Q5AV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11tuw_0926_sm_5eqmw = models.FloatField(db_column='GTEX-11TUW-0926-SM-5EQMW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11ud2_0826_sm_5eqks = models.FloatField(db_column='GTEX-11UD2-0826-SM-5EQKS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11wqk_0326_sm_5eql1 = models.FloatField(db_column='GTEX-11WQK-0326-SM-5EQL1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11zts_0826_sm_5eq49 = models.FloatField(db_column='GTEX-11ZTS-0826-SM-5EQ49', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_11zvc_0326_sm_5cvlc = models.FloatField(db_column='GTEX-11ZVC-0326-SM-5CVLC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1211k_0326_sm_5fqt1 = models.FloatField(db_column='GTEX-1211K-0326-SM-5FQT1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1212z_0826_sm_5eq51 = models.FloatField(db_column='GTEX-1212Z-0826-SM-5EQ51', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12696_0426_sm_5egl5 = models.FloatField(db_column='GTEX-12696-0426-SM-5EGL5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12c56_0226_sm_5n9fb = models.FloatField(db_column='GTEX-12C56-0226-SM-5N9FB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12ks4_0626_sm_5pny4 = models.FloatField(db_column='GTEX-12KS4-0626-SM-5PNY4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12wsd_1326_sm_5gcnu = models.FloatField(db_column='GTEX-12WSD-1326-SM-5GCNU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12wsk_0426_sm_5gcns = models.FloatField(db_column='GTEX-12WSK-0426-SM-5GCNS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12wsn_0326_sm_5gcp6 = models.FloatField(db_column='GTEX-12WSN-0326-SM-5GCP6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12zzx_1026_sm_5lzuw = models.FloatField(db_column='GTEX-12ZZX-1026-SM-5LZUW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_12zzy_1326_sm_5gcnw = models.FloatField(db_column='GTEX-12ZZY-1326-SM-5GCNW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13111_0526_sm_5lzvf = models.FloatField(db_column='GTEX-13111-0526-SM-5LZVF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13113_0526_sm_5gcn2 = models.FloatField(db_column='GTEX-13113-0526-SM-5GCN2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1313w_1026_sm_5eq5i = models.FloatField(db_column='GTEX-1313W-1026-SM-5EQ5I', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_131xf_0626_sm_5gids = models.FloatField(db_column='GTEX-131XF-0626-SM-5GIDS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_131xw_2226_sm_5pny1 = models.FloatField(db_column='GTEX-131XW-2226-SM-5PNY1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_131ys_1126_sm_5n9fq = models.FloatField(db_column='GTEX-131YS-1126-SM-5N9FQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_132ar_2126_sm_5k7xg = models.FloatField(db_column='GTEX-132AR-2126-SM-5K7XG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_132qs_0626_sm_62lfm = models.FloatField(db_column='GTEX-132QS-0626-SM-62LFM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1339x_0526_sm_5klyw = models.FloatField(db_column='GTEX-1339X-0526-SM-5KLYW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_133le_0226_sm_5pny3 = models.FloatField(db_column='GTEX-133LE-0226-SM-5PNY3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1399r_0626_sm_5k7uz = models.FloatField(db_column='GTEX-1399R-0626-SM-5K7UZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1399t_0526_sm_5j1nc = models.FloatField(db_column='GTEX-1399T-0526-SM-5J1NC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1399u_0426_sm_5k7uu = models.FloatField(db_column='GTEX-1399U-0426-SM-5K7UU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_139d8_1226_sm_5l3ed = models.FloatField(db_column='GTEX-139D8-1226-SM-5L3ED', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_139ts_0226_sm_5k7w5 = models.FloatField(db_column='GTEX-139TS-0226-SM-5K7W5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_139tu_1126_sm_5j1ny = models.FloatField(db_column='GTEX-139TU-1126-SM-5J1NY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_139uw_0426_sm_5k7v4 = models.FloatField(db_column='GTEX-139UW-0426-SM-5K7V4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_139yr_0626_sm_5ijbt = models.FloatField(db_column='GTEX-139YR-0626-SM-5IJBT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13cf3_0526_sm_5ijbv = models.FloatField(db_column='GTEX-13CF3-0526-SM-5IJBV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13d11_1426_sm_5k7y9 = models.FloatField(db_column='GTEX-13D11-1426-SM-5K7Y9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13fh7_0326_sm_5j1mr = models.FloatField(db_column='GTEX-13FH7-0326-SM-5J1MR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13fho_1626_sm_5ijgb = models.FloatField(db_column='GTEX-13FHO-1626-SM-5IJGB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13flv_1426_sm_5j1n4 = models.FloatField(db_column='GTEX-13FLV-1426-SM-5J1N4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13ftw_0726_sm_9wg72 = models.FloatField(db_column='GTEX-13FTW-0726-SM-9WG72', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13ftx_0226_sm_5k7tx = models.FloatField(db_column='GTEX-13FTX-0226-SM-5K7TX', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13ftz_0126_sm_5k7v3 = models.FloatField(db_column='GTEX-13FTZ-0126-SM-5K7V3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13n2g_0526_sm_5mr5l = models.FloatField(db_column='GTEX-13N2G-0526-SM-5MR5L', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13nyb_0426_sm_5ijdd = models.FloatField(db_column='GTEX-13NYB-0426-SM-5IJDD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13nz9_1226_sm_5mr3j = models.FloatField(db_column='GTEX-13NZ9-1226-SM-5MR3J', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13o1r_1026_sm_5km2l = models.FloatField(db_column='GTEX-13O1R-1026-SM-5KM2L', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13o21_0426_sm_5k7vr = models.FloatField(db_column='GTEX-13O21-0426-SM-5K7VR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13o3o_1126_sm_5km4q = models.FloatField(db_column='GTEX-13O3O-1126-SM-5KM4Q', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13o3p_1126_sm_5l3fg = models.FloatField(db_column='GTEX-13O3P-1126-SM-5L3FG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13o61_0326_sm_5km2o = models.FloatField(db_column='GTEX-13O61-0326-SM-5KM2O', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13ovg_0826_sm_5l3d8 = models.FloatField(db_column='GTEX-13OVG-0826-SM-5L3D8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13ovi_0626_sm_5ijcn = models.FloatField(db_column='GTEX-13OVI-0626-SM-5IJCN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13ow5_0826_sm_5j1ne = models.FloatField(db_column='GTEX-13OW5-0826-SM-5J1NE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13ow6_1526_sm_5l3hx = models.FloatField(db_column='GTEX-13OW6-1526-SM-5L3HX', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13ow8_1826_sm_5l3h1 = models.FloatField(db_column='GTEX-13OW8-1826-SM-5L3H1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13pvq_1426_sm_5j1o4 = models.FloatField(db_column='GTEX-13PVQ-1426-SM-5J1O4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13pvr_0826_sm_5s2pv = models.FloatField(db_column='GTEX-13PVR-0826-SM-5S2PV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13qbu_0326_sm_5lu3f = models.FloatField(db_column='GTEX-13QBU-0326-SM-5LU3F', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13rtk_0126_sm_5rqhq = models.FloatField(db_column='GTEX-13RTK-0126-SM-5RQHQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13u4i_1026_sm_5lu3g = models.FloatField(db_column='GTEX-13U4I-1026-SM-5LU3G', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13vxt_0826_sm_5siap = models.FloatField(db_column='GTEX-13VXT-0826-SM-5SIAP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13w3w_0226_sm_731et = models.FloatField(db_column='GTEX-13W3W-0226-SM-731ET', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13w46_1826_sm_5k7va = models.FloatField(db_column='GTEX-13W46-1826-SM-5K7VA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13x6h_0126_sm_5qgos = models.FloatField(db_column='GTEX-13X6H-0126-SM-5QGOS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13x6i_0926_sm_5luab = models.FloatField(db_column='GTEX-13X6I-0926-SM-5LUAB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13x6k_1926_sm_5lu4o = models.FloatField(db_column='GTEX-13X6K-1926-SM-5LU4O', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_13yan_1526_sm_5lu3e = models.FloatField(db_column='GTEX-13YAN-1526-SM-5LU3E', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_144gn_0326_sm_5o9ad = models.FloatField(db_column='GTEX-144GN-0326-SM-5O9AD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_145mh_1026_sm_5q5ci = models.FloatField(db_column='GTEX-145MH-1026-SM-5Q5CI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_145mo_1226_sm_5qgpc = models.FloatField(db_column='GTEX-145MO-1226-SM-5QGPC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_146fh_1326_sm_5nqbi = models.FloatField(db_column='GTEX-146FH-1326-SM-5NQBI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_146fq_0826_sm_5luaj = models.FloatField(db_column='GTEX-146FQ-0826-SM-5LUAJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_146fr_1026_sm_5nq9t = models.FloatField(db_column='GTEX-146FR-1026-SM-5NQ9T', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_147f4_1026_sm_5q5f9 = models.FloatField(db_column='GTEX-147F4-1026-SM-5Q5F9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1497j_1026_sm_5nqav = models.FloatField(db_column='GTEX-1497J-1026-SM-5NQAV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14a5i_1326_sm_5siaq = models.FloatField(db_column='GTEX-14A5I-1326-SM-5SIAQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14as3_0526_sm_5qgqq = models.FloatField(db_column='GTEX-14AS3-0526-SM-5QGQQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14asi_1126_sm_5qgpn = models.FloatField(db_column='GTEX-14ASI-1126-SM-5QGPN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14b4r_0226_sm_5tddo = models.FloatField(db_column='GTEX-14B4R-0226-SM-5TDDO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14bim_2626_sm_5s2of = models.FloatField(db_column='GTEX-14BIM-2626-SM-5S2OF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14bmu_0326_sm_793do = models.FloatField(db_column='GTEX-14BMU-0326-SM-793DO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14bmv_1226_sm_5tddy = models.FloatField(db_column='GTEX-14BMV-1226-SM-5TDDY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14c39_0126_sm_6128r = models.FloatField(db_column='GTEX-14C39-0126-SM-6128R', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14c5o_1526_sm_7dhkt = models.FloatField(db_column='GTEX-14C5O-1526-SM-7DHKT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14daq_1326_sm_5rqim = models.FloatField(db_column='GTEX-14DAQ-1326-SM-5RQIM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14e1k_0726_sm_62ldu = models.FloatField(db_column='GTEX-14E1K-0726-SM-62LDU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14e6c_0626_sm_664na = models.FloatField(db_column='GTEX-14E6C-0626-SM-664NA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14e7w_1426_sm_6llj2 = models.FloatField(db_column='GTEX-14E7W-1426-SM-6LLJ2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14icl_0326_sm_5s2os = models.FloatField(db_column='GTEX-14ICL-0326-SM-5S2OS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14pj2_1226_sm_62lfe = models.FloatField(db_column='GTEX-14PJ2-1226-SM-62LFE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14pj3_0226_sm_6eu37 = models.FloatField(db_column='GTEX-14PJ3-0226-SM-6EU37', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14pj4_0826_sm_6llh5 = models.FloatField(db_column='GTEX-14PJ4-0826-SM-6LLH5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14pj6_0526_sm_6lliu = models.FloatField(db_column='GTEX-14PJ6-0526-SM-6LLIU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14pjm_1426_sm_62lf3 = models.FloatField(db_column='GTEX-14PJM-1426-SM-62LF3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_14pk6_0626_sm_6aj9p = models.FloatField(db_column='GTEX-14PK6-0626-SM-6AJ9P', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15chc_0626_sm_686yv = models.FloatField(db_column='GTEX-15CHC-0626-SM-686YV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15chr_0126_sm_7sb7x = models.FloatField(db_column='GTEX-15CHR-0126-SM-7SB7X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15dde_1326_sm_6lljm = models.FloatField(db_column='GTEX-15DDE-1326-SM-6LLJM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15dyw_1226_sm_6palv = models.FloatField(db_column='GTEX-15DYW-1226-SM-6PALV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15dza_1226_sm_7kfs1 = models.FloatField(db_column='GTEX-15DZA-1226-SM-7KFS1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15er7_2026_sm_793b8 = models.FloatField(db_column='GTEX-15ER7-2026-SM-793B8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15ets_0726_sm_6lpkl = models.FloatField(db_column='GTEX-15ETS-0726-SM-6LPKL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15f5u_0226_sm_6pank = models.FloatField(db_column='GTEX-15F5U-0226-SM-6PANK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15fzz_0426_sm_6panm = models.FloatField(db_column='GTEX-15FZZ-0426-SM-6PANM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15g19_1026_sm_6palm = models.FloatField(db_column='GTEX-15G19-1026-SM-6PALM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15rif_0126_sm_7kug3 = models.FloatField(db_column='GTEX-15RIF-0126-SM-7KUG3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15rje_2426_sm_6pam9 = models.FloatField(db_column='GTEX-15RJE-2426-SM-6PAM9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15shu_1226_sm_718by = models.FloatField(db_column='GTEX-15SHU-1226-SM-718BY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15shv_0826_sm_7kufa = models.FloatField(db_column='GTEX-15SHV-0826-SM-7KUFA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_15uf6_0226_sm_7kuf6 = models.FloatField(db_column='GTEX-15UF6-0226-SM-7KUF6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_16xzz_1426_sm_7kue3 = models.FloatField(db_column='GTEX-16XZZ-1426-SM-7KUE3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17evp_0926_sm_7igoy = models.FloatField(db_column='GTEX-17EVP-0926-SM-7IGOY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17evq_1626_sm_79onh = models.FloatField(db_column='GTEX-17EVQ-1626-SM-79ONH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17f96_1126_sm_7ewdf = models.FloatField(db_column='GTEX-17F96-1126-SM-7EWDF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17f98_0726_sm_793bj = models.FloatField(db_column='GTEX-17F98-0726-SM-793BJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17gql_2326_sm_731ej = models.FloatField(db_column='GTEX-17GQL-2326-SM-731EJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17hii_1826_sm_7dufq = models.FloatField(db_column='GTEX-17HII-1826-SM-7DUFQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17knj_0526_sm_7pc3y = models.FloatField(db_column='GTEX-17KNJ-0526-SM-7PC3Y', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_17mf6_1026_sm_7ewe1 = models.FloatField(db_column='GTEX-17MF6-1026-SM-7EWE1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_18465_1026_sm_7pc23 = models.FloatField(db_column='GTEX-18465-1026-SM-7PC23', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_18a66_1326_sm_7lg4m = models.FloatField(db_column='GTEX-18A66-1326-SM-7LG4M', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_18a67_0926_sm_7lg5y = models.FloatField(db_column='GTEX-18A67-0926-SM-7LG5Y', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_18a6q_1426_sm_7lg63 = models.FloatField(db_column='GTEX-18A6Q-1426-SM-7LG63', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_18a7a_1426_sm_731ap = models.FloatField(db_column='GTEX-18A7A-1426-SM-731AP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_18d9u_1326_sm_731bi = models.FloatField(db_column='GTEX-18D9U-1326-SM-731BI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1a3mv_0426_sm_73kxl = models.FloatField(db_column='GTEX-1A3MV-0426-SM-73KXL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1amey_0726_sm_72d5x = models.FloatField(db_column='GTEX-1AMEY-0726-SM-72D5X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1amfi_0426_sm_731c7 = models.FloatField(db_column='GTEX-1AMFI-0426-SM-731C7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ax8z_1226_sm_7dhm7 = models.FloatField(db_column='GTEX-1AX8Z-1226-SM-7DHM7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ax9i_1226_sm_731cj = models.FloatField(db_column='GTEX-1AX9I-1226-SM-731CJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ax9j_0726_sm_7pc2e = models.FloatField(db_column='GTEX-1AX9J-0726-SM-7PC2E', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ax9k_0726_sm_73kyr = models.FloatField(db_column='GTEX-1AX9K-0726-SM-73KYR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ayct_0326_sm_73kvn = models.FloatField(db_column='GTEX-1AYCT-0326-SM-73KVN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ayd5_0726_sm_7sb6y = models.FloatField(db_column='GTEX-1AYD5-0726-SM-7SB6Y', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1b8ke_0226_sm_7ewek = models.FloatField(db_column='GTEX-1B8KE-0226-SM-7EWEK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1b8l1_0226_sm_7pbye = models.FloatField(db_column='GTEX-1B8L1-0226-SM-7PBYE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1b8sg_0626_sm_79ol3 = models.FloatField(db_column='GTEX-1B8SG-0626-SM-79OL3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1b933_1126_sm_73kx2 = models.FloatField(db_column='GTEX-1B933-1126-SM-73KX2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1b97j_0526_sm_793c2 = models.FloatField(db_column='GTEX-1B97J-0526-SM-793C2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1bajh_1126_sm_7pbyg = models.FloatField(db_column='GTEX-1BAJH-1126-SM-7PBYG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1c2ji_0426_sm_79oof = models.FloatField(db_column='GTEX-1C2JI-0426-SM-79OOF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1c4cl_1226_sm_7duft = models.FloatField(db_column='GTEX-1C4CL-1226-SM-7DUFT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1c64o_1026_sm_7pc3l = models.FloatField(db_column='GTEX-1C64O-1026-SM-7PC3L', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1c6vq_1326_sm_7939x = models.FloatField(db_column='GTEX-1C6VQ-1326-SM-7939X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1cams_1026_sm_7pc2i = models.FloatField(db_column='GTEX-1CAMS-1026-SM-7PC2I', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1cb4e_0426_sm_7pby5 = models.FloatField(db_column='GTEX-1CB4E-0426-SM-7PBY5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1cb4g_1126_sm_7pbxw = models.FloatField(db_column='GTEX-1CB4G-1126-SM-7PBXW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1cb4i_1826_sm_793cx = models.FloatField(db_column='GTEX-1CB4I-1826-SM-793CX', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1cb4j_0126_sm_7pc3k = models.FloatField(db_column='GTEX-1CB4J-0126-SM-7PC3K', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1e1vi_1226_sm_7rhgd = models.FloatField(db_column='GTEX-1E1VI-1226-SM-7RHGD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ekgg_0826_sm_79oll = models.FloatField(db_column='GTEX-1EKGG-0826-SM-79OLL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1emgi_0926_sm_7igpv = models.FloatField(db_column='GTEX-1EMGI-0926-SM-7IGPV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1en7a_1126_sm_7igq1 = models.FloatField(db_column='GTEX-1EN7A-1126-SM-7IGQ1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1eu9m_1726_sm_7ewf3 = models.FloatField(db_column='GTEX-1EU9M-1726-SM-7EWF3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ewiq_1026_sm_7p8s1 = models.FloatField(db_column='GTEX-1EWIQ-1026-SM-7P8S1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ex96_2726_sm_7sb88 = models.FloatField(db_column='GTEX-1EX96-2726-SM-7SB88', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1f48j_1326_sm_7rhgj = models.FloatField(db_column='GTEX-1F48J-1326-SM-7RHGJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1f5pk_0626_sm_7sb6s = models.FloatField(db_column='GTEX-1F5PK-0626-SM-7SB6S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1f75i_1226_sm_9yfm4 = models.FloatField(db_column='GTEX-1F75I-1226-SM-9YFM4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1f7rk_1326_sm_7pc39 = models.FloatField(db_column='GTEX-1F7RK-1326-SM-7PC39', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1f88f_0226_sm_9wyt1 = models.FloatField(db_column='GTEX-1F88F-0226-SM-9WYT1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gf9u_0326_sm_7sb91 = models.FloatField(db_column='GTEX-1GF9U-0326-SM-7SB91', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gf9v_1526_sm_7pc3e = models.FloatField(db_column='GTEX-1GF9V-1526-SM-7PC3E', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gf9w_1926_sm_9knum = models.FloatField(db_column='GTEX-1GF9W-1926-SM-9KNUM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gl5r_0126_sm_9wyti = models.FloatField(db_column='GTEX-1GL5R-0126-SM-9WYTI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gmr2_1126_sm_7rhi6 = models.FloatField(db_column='GTEX-1GMR2-1126-SM-7RHI6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gmr3_0526_sm_9yfli = models.FloatField(db_column='GTEX-1GMR3-0526-SM-9YFLI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gn1u_1626_sm_9mqkp = models.FloatField(db_column='GTEX-1GN1U-1626-SM-9MQKP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gn2e_1126_sm_9mqk9 = models.FloatField(db_column='GTEX-1GN2E-1126-SM-9MQK9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gn73_2226_sm_9yflf = models.FloatField(db_column='GTEX-1GN73-2226-SM-9YFLF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gz4h_0726_sm_9wg6x = models.FloatField(db_column='GTEX-1GZ4H-0726-SM-9WG6X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gz4i_1126_sm_9qehr = models.FloatField(db_column='GTEX-1GZ4I-1126-SM-9QEHR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1gzhy_1626_sm_9wg79 = models.FloatField(db_column='GTEX-1GZHY-1626-SM-9WG79', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1h1e6_1526_sm_9qehp = models.FloatField(db_column='GTEX-1H1E6-1526-SM-9QEHP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1h1zs_1226_sm_9wytv = models.FloatField(db_column='GTEX-1H1ZS-1226-SM-9WYTV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1h3nz_1226_sm_9mqkt = models.FloatField(db_column='GTEX-1H3NZ-1226-SM-9MQKT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1h3vy_1026_sm_ackxf = models.FloatField(db_column='GTEX-1H3VY-1026-SM-ACKXF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hb9e_0926_sm_coh3d = models.FloatField(db_column='GTEX-1HB9E-0926-SM-COH3D', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hbph_1026_sm_adeiu = models.FloatField(db_column='GTEX-1HBPH-1026-SM-ADEIU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hbpi_0126_sm_cmkgq = models.FloatField(db_column='GTEX-1HBPI-0126-SM-CMKGQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hbpm_1326_sm_9yfmb = models.FloatField(db_column='GTEX-1HBPM-1326-SM-9YFMB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hbpn_1026_sm_9yflz = models.FloatField(db_column='GTEX-1HBPN-1026-SM-9YFLZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hc8u_1126_sm_coh35 = models.FloatField(db_column='GTEX-1HC8U-1126-SM-COH35', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hcu8_0926_sm_cm2s9 = models.FloatField(db_column='GTEX-1HCU8-0926-SM-CM2S9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hcu9_0526_sm_cgqfp = models.FloatField(db_column='GTEX-1HCU9-0526-SM-CGQFP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hcua_0326_sm_cgqeh = models.FloatField(db_column='GTEX-1HCUA-0326-SM-CGQEH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hcve_1026_sm_ackxr = models.FloatField(db_column='GTEX-1HCVE-1026-SM-ACKXR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hfi7_0426_sm_9yflp = models.FloatField(db_column='GTEX-1HFI7-0426-SM-9YFLP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hsgn_1026_sm_cnpq1 = models.FloatField(db_column='GTEX-1HSGN-1026-SM-CNPQ1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hskv_0626_sm_cnppl = models.FloatField(db_column='GTEX-1HSKV-0626-SM-CNPPL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hsmp_0826_sm_a9skw = models.FloatField(db_column='GTEX-1HSMP-0826-SM-A9SKW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hsmq_0326_sm_d4p2j = models.FloatField(db_column='GTEX-1HSMQ-0326-SM-D4P2J', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ht8w_1826_sm_adejd = models.FloatField(db_column='GTEX-1HT8W-1826-SM-ADEJD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1hub1_0626_sm_cypr9 = models.FloatField(db_column='GTEX-1HUB1-0626-SM-CYPR9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i1cd_1226_sm_cnpq2 = models.FloatField(db_column='GTEX-1I1CD-1226-SM-CNPQ2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i1gp_0926_sm_coh3o = models.FloatField(db_column='GTEX-1I1GP-0926-SM-COH3O', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i1gq_1526_sm_ackvq = models.FloatField(db_column='GTEX-1I1GQ-1526-SM-ACKVQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i1gs_1226_sm_exohj = models.FloatField(db_column='GTEX-1I1GS-1226-SM-EXOHJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i1gu_0426_sm_arl7y = models.FloatField(db_column='GTEX-1I1GU-0426-SM-ARL7Y', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i1hk_0926_sm_b2lvy = models.FloatField(db_column='GTEX-1I1HK-0926-SM-B2LVY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i4mk_0626_sm_arzlz = models.FloatField(db_column='GTEX-1I4MK-0626-SM-ARZLZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1i6k7_0826_sm_ackwi = models.FloatField(db_column='GTEX-1I6K7-0826-SM-ACKWI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1icly_1126_sm_d4p37 = models.FloatField(db_column='GTEX-1ICLY-1126-SM-D4P37', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1idjc_0426_sm_b2lw1 = models.FloatField(db_column='GTEX-1IDJC-0426-SM-B2LW1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1idje_1026_sm_adeie = models.FloatField(db_column='GTEX-1IDJE-1026-SM-ADEIE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1idjf_0926_sm_arl85 = models.FloatField(db_column='GTEX-1IDJF-0926-SM-ARL85', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1idju_0526_sm_ackwm = models.FloatField(db_column='GTEX-1IDJU-0526-SM-ACKWM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1ikoe_0726_sm_ce6t4 = models.FloatField(db_column='GTEX-1IKOE-0726-SM-CE6T4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1il2u_1026_sm_coh3p = models.FloatField(db_column='GTEX-1IL2U-1026-SM-COH3P', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1j1oq_2026_sm_cmkhz = models.FloatField(db_column='GTEX-1J1OQ-2026-SM-CMKHZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1j1r8_0826_sm_ackwp = models.FloatField(db_column='GTEX-1J1R8-0826-SM-ACKWP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1j8jj_0926_sm_arzmr = models.FloatField(db_column='GTEX-1J8JJ-0926-SM-ARZMR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1j8q3_1026_sm_cgqed = models.FloatField(db_column='GTEX-1J8Q3-1026-SM-CGQED', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1j8qm_0126_sm_d3l9a = models.FloatField(db_column='GTEX-1J8QM-0126-SM-D3L9A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jj6o_1826_sm_cl53j = models.FloatField(db_column='GTEX-1JJ6O-1826-SM-CL53J', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jjea_0726_sm_cypsn = models.FloatField(db_column='GTEX-1JJEA-0726-SM-CYPSN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jk1u_0426_sm_cypsp = models.FloatField(db_column='GTEX-1JK1U-0426-SM-CYPSP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jkyn_0226_sm_arl9h = models.FloatField(db_column='GTEX-1JKYN-0226-SM-ARL9H', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jmou_0126_sm_e9u53 = models.FloatField(db_column='GTEX-1JMOU-0126-SM-E9U53', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jmqi_0226_sm_arzn3 = models.FloatField(db_column='GTEX-1JMQI-0226-SM-ARZN3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1jmqj_2426_sm_e9til = models.FloatField(db_column='GTEX-1JMQJ-2426-SM-E9TIL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1k2da_0926_sm_cgqge = models.FloatField(db_column='GTEX-1K2DA-0926-SM-CGQGE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1k2du_1326_sm_cypt5 = models.FloatField(db_column='GTEX-1K2DU-1326-SM-CYPT5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1k9t9_1326_sm_e6cjn = models.FloatField(db_column='GTEX-1K9T9-1326-SM-E6CJN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1kanc_0326_sm_d3la7 = models.FloatField(db_column='GTEX-1KANC-0326-SM-D3LA7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1kd5a_0826_sm_dkpq9 = models.FloatField(db_column='GTEX-1KD5A-0826-SM-DKPQ9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1kxam_1226_sm_e9tjv = models.FloatField(db_column='GTEX-1KXAM-1226-SM-E9TJV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1l5ne_0326_sm_e6cic = models.FloatField(db_column='GTEX-1L5NE-0326-SM-E6CIC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lb8k_1126_sm_dipep = models.FloatField(db_column='GTEX-1LB8K-1126-SM-DIPEP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lg7y_1326_sm_d4p45 = models.FloatField(db_column='GTEX-1LG7Y-1326-SM-D4P45', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lg7z_0626_sm_d3la2 = models.FloatField(db_column='GTEX-1LG7Z-0626-SM-D3LA2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lgrb_0726_sm_coh3b = models.FloatField(db_column='GTEX-1LGRB-0726-SM-COH3B', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lkk1_1126_sm_dkpqd = models.FloatField(db_column='GTEX-1LKK1-1126-SM-DKPQD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lncm_0326_sm_dipf5 = models.FloatField(db_column='GTEX-1LNCM-0326-SM-DIPF5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lvan_1426_sm_coh3x = models.FloatField(db_column='GTEX-1LVAN-1426-SM-COH3X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1lvao_0826_sm_e6ciu = models.FloatField(db_column='GTEX-1LVAO-0826-SM-E6CIU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1mcc2_0426_sm_dkpqh = models.FloatField(db_column='GTEX-1MCC2-0426-SM-DKPQH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1mcyp_0426_sm_e6ciq = models.FloatField(db_column='GTEX-1MCYP-0426-SM-E6CIQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1mgnq_0626_sm_e9j2x = models.FloatField(db_column='GTEX-1MGNQ-0626-SM-E9J2X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1nsgn_1126_sm_exur3 = models.FloatField(db_column='GTEX-1NSGN-1126-SM-EXUR3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1pdj9_0926_sm_e8vos = models.FloatField(db_column='GTEX-1PDJ9-0926-SM-E8VOS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1pfey_0526_sm_e76pg = models.FloatField(db_column='GTEX-1PFEY-0526-SM-E76PG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1poen_1026_sm_e8vnf = models.FloatField(db_column='GTEX-1POEN-1026-SM-E8VNF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qaet_0526_sm_eyyxf = models.FloatField(db_column='GTEX-1QAET-0526-SM-EYYXF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qp29_0226_sm_evybm = models.FloatField(db_column='GTEX-1QP29-0226-SM-EVYBM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qp2a_0826_sm_dtxf5 = models.FloatField(db_column='GTEX-1QP2A-0826-SM-DTXF5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qp66_1126_sm_dtxdp = models.FloatField(db_column='GTEX-1QP66-1126-SM-DTXDP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qp9n_0226_sm_e9j4a = models.FloatField(db_column='GTEX-1QP9N-0226-SM-E9J4A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qpfj_0726_sm_dtxds = models.FloatField(db_column='GTEX-1QPFJ-0726-SM-DTXDS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1qw4y_0326_sm_e8vot = models.FloatField(db_column='GTEX-1QW4Y-0326-SM-E8VOT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1r46s_0726_sm_e9j42 = models.FloatField(db_column='GTEX-1R46S-0726-SM-E9J42', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1r9jw_0726_sm_dtxfh = models.FloatField(db_column='GTEX-1R9JW-0726-SM-DTXFH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1r9k5_1426_sm_dtx9f = models.FloatField(db_column='GTEX-1R9K5-1426-SM-DTX9F', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1r9pm_0326_sm_evybi = models.FloatField(db_column='GTEX-1R9PM-0326-SM-EVYBI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1r9pn_0226_sm_dtx84 = models.FloatField(db_column='GTEX-1R9PN-0226-SM-DTX84', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1r9po_0226_sm_e6chs = models.FloatField(db_column='GTEX-1R9PO-0226-SM-E6CHS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1raza_1126_sm_e8vmv = models.FloatField(db_column='GTEX-1RAZA-1126-SM-E8VMV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1razr_0626_sm_e6cjo = models.FloatField(db_column='GTEX-1RAZR-0626-SM-E6CJO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1rlm8_0526_sm_e8vok = models.FloatField(db_column='GTEX-1RLM8-0526-SM-E8VOK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1rntq_0726_sm_e9u6f = models.FloatField(db_column='GTEX-1RNTQ-0726-SM-E9U6F', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1rqed_1126_sm_evycu = models.FloatField(db_column='GTEX-1RQED-1126-SM-EVYCU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1s3dn_0626_sm_e9u51 = models.FloatField(db_column='GTEX-1S3DN-0626-SM-E9U51', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_1s5za_1126_sm_evybu = models.FloatField(db_column='GTEX-1S5ZA-1126-SM-EVYBU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_n7mt_1426_sm_3lk5m = models.FloatField(db_column='GTEX-N7MT-1426-SM-3LK5M', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_nfk9_1326_sm_3lk5i = models.FloatField(db_column='GTEX-NFK9-1326-SM-3LK5I', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_npj8_0526_sm_3mjhn = models.FloatField(db_column='GTEX-NPJ8-0526-SM-3MJHN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_o5yt_0426_sm_3mjhd = models.FloatField(db_column='GTEX-O5YT-0426-SM-3MJHD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_o5yv_0626_sm_3lk64 = models.FloatField(db_column='GTEX-O5YV-0626-SM-3LK64', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_o5yw_0426_sm_3mjhj = models.FloatField(db_column='GTEX-O5YW-0426-SM-3MJHJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ohpk_0426_sm_3mjh3 = models.FloatField(db_column='GTEX-OHPK-0426-SM-3MJH3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ohpl_0426_sm_3tw8x = models.FloatField(db_column='GTEX-OHPL-0426-SM-3TW8X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ohpm_0426_sm_3tw8v = models.FloatField(db_column='GTEX-OHPM-0426-SM-3TW8V', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_oizf_0426_sm_7pbzp = models.FloatField(db_column='GTEX-OIZF-0426-SM-7PBZP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_oizg_0426_sm_3lk5w = models.FloatField(db_column='GTEX-OIZG-0426-SM-3LK5W', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_oizi_1126_sm_3nb1f = models.FloatField(db_column='GTEX-OIZI-1126-SM-3NB1F', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_oobj_0426_sm_3nb1s = models.FloatField(db_column='GTEX-OOBJ-0426-SM-3NB1S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_oobk_0425_sm_3lk5o = models.FloatField(db_column='GTEX-OOBK-0425-SM-3LK5O', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_oxrl_0426_sm_3nm97 = models.FloatField(db_column='GTEX-OXRL-0426-SM-3NM97', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_p44h_1026_sm_3nm96 = models.FloatField(db_column='GTEX-P44H-1026-SM-3NM96', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_p4pp_0426_sm_3nm9h = models.FloatField(db_column='GTEX-P4PP-0426-SM-3NM9H', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_p4pq_0426_sm_3nmci = models.FloatField(db_column='GTEX-P4PQ-0426-SM-3NMCI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_p4qs_0426_sm_3nmcq = models.FloatField(db_column='GTEX-P4QS-0426-SM-3NMCQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_p78b_0826_sm_3nmca = models.FloatField(db_column='GTEX-P78B-0826-SM-3NMCA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_plz5_0426_sm_3p612 = models.FloatField(db_column='GTEX-PLZ5-0426-SM-3P612', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_plz6_0326_sm_3p61j = models.FloatField(db_column='GTEX-PLZ6-0326-SM-3P61J', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_pomq_0426_sm_3p61g = models.FloatField(db_column='GTEX-POMQ-0426-SM-3P61G', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_poyw_1126_sm_48tci = models.FloatField(db_column='GTEX-POYW-1126-SM-48TCI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_psdg_1026_sm_48tcv = models.FloatField(db_column='GTEX-PSDG-1026-SM-48TCV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_pvow_1426_sm_ez6lo = models.FloatField(db_column='GTEX-PVOW-1426-SM-EZ6LO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_pw2o_0426_sm_48tcc = models.FloatField(db_column='GTEX-PW2O-0426-SM-48TCC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_pwcy_0326_sm_43iru = models.FloatField(db_column='GTEX-PWCY-0326-SM-43IRU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_px3g_0426_sm_48u1c = models.FloatField(db_column='GTEX-PX3G-0426-SM-48U1C', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_q2ag_0926_sm_48u1q = models.FloatField(db_column='GTEX-Q2AG-0926-SM-48U1Q', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_q2ah_0326_sm_48u1k = models.FloatField(db_column='GTEX-Q2AH-0326-SM-48U1K', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qcqg_1526_sm_48u25 = models.FloatField(db_column='GTEX-QCQG-1526-SM-48U25', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qdt8_1026_sm_43v6x = models.FloatField(db_column='GTEX-QDT8-1026-SM-43V6X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qdvj_0626_sm_48u1t = models.FloatField(db_column='GTEX-QDVJ-0626-SM-48U1T', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qdvn_0226_sm_48tz9 = models.FloatField(db_column='GTEX-QDVN-0226-SM-48TZ9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qeg4_0926_sm_4r1jo = models.FloatField(db_column='GTEX-QEG4-0926-SM-4R1JO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qeg5_1226_sm_447ar = models.FloatField(db_column='GTEX-QEG5-1226-SM-447AR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qel4_1126_sm_dlzq4 = models.FloatField(db_column='GTEX-QEL4-1126-SM-DLZQ4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qesd_0426_sm_dkpog = models.FloatField(db_column='GTEX-QESD-0426-SM-DKPOG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qlq7_0426_sm_dhxin = models.FloatField(db_column='GTEX-QLQ7-0426-SM-DHXIN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qmrm_0626_sm_447bq = models.FloatField(db_column='GTEX-QMRM-0626-SM-447BQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qv31_0326_sm_447bm = models.FloatField(db_column='GTEX-QV31-0326-SM-447BM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qv44_0626_sm_4r1kj = models.FloatField(db_column='GTEX-QV44-0626-SM-4R1KJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qvjo_0526_sm_447ce = models.FloatField(db_column='GTEX-QVJO-0526-SM-447CE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qvus_0426_sm_48fe3 = models.FloatField(db_column='GTEX-QVUS-0426-SM-48FE3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_qxcu_0926_sm_48fep = models.FloatField(db_column='GTEX-QXCU-0926-SM-48FEP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_r53t_0826_sm_48fcp = models.FloatField(db_column='GTEX-R53T-0826-SM-48FCP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_r55c_0426_sm_evr2w = models.FloatField(db_column='GTEX-R55C-0426-SM-EVR2W', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_r55d_1026_sm_3gaeq = models.FloatField(db_column='GTEX-R55D-1026-SM-3GAEQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_r55e_1126_sm_48fdz = models.FloatField(db_column='GTEX-R55E-1126-SM-48FDZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_r55g_0626_sm_48fdb = models.FloatField(db_column='GTEX-R55G-0626-SM-48FDB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_rey6_1126_sm_48fdu = models.FloatField(db_column='GTEX-REY6-1126-SM-48FDU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_rnor_1026_sm_48fdf = models.FloatField(db_column='GTEX-RNOR-1026-SM-48FDF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_rusq_0326_sm_47jws = models.FloatField(db_column='GTEX-RUSQ-0326-SM-47JWS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_rws6_0526_sm_4giaj = models.FloatField(db_column='GTEX-RWS6-0526-SM-4GIAJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_rwsa_0926_sm_47jxw = models.FloatField(db_column='GTEX-RWSA-0926-SM-47JXW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_s32w_0426_sm_4ad6h = models.FloatField(db_column='GTEX-S32W-0426-SM-4AD6H', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_s33h_0726_sm_4ad6m = models.FloatField(db_column='GTEX-S33H-0726-SM-4AD6M', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_s3xe_0326_sm_4ad6l = models.FloatField(db_column='GTEX-S3XE-0326-SM-4AD6L', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_s4p3_0326_sm_4ad6p = models.FloatField(db_column='GTEX-S4P3-0326-SM-4AD6P', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_s4z8_0626_sm_4ad6j = models.FloatField(db_column='GTEX-S4Z8-0626-SM-4AD6J', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_s95s_0226_sm_4b656 = models.FloatField(db_column='GTEX-S95S-0226-SM-4B656', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_snos_0326_sm_4dm6c = models.FloatField(db_column='GTEX-SNOS-0326-SM-4DM6C', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_t5jc_0326_sm_4dm5c = models.FloatField(db_column='GTEX-T5JC-0326-SM-4DM5C', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_t6mn_1126_sm_4dm71 = models.FloatField(db_column='GTEX-T6MN-1126-SM-4DM71', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_t8em_0426_sm_4dm7e = models.FloatField(db_column='GTEX-T8EM-0426-SM-4DM7E', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_tmmy_1026_sm_4dxti = models.FloatField(db_column='GTEX-TMMY-1026-SM-4DXTI', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_u3zh_0626_sm_4dxt3 = models.FloatField(db_column='GTEX-U3ZH-0626-SM-4DXT3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_u3zm_0326_sm_4dxuj = models.FloatField(db_column='GTEX-U3ZM-0326-SM-4DXUJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_u3zn_0526_sm_4dxth = models.FloatField(db_column='GTEX-U3ZN-0526-SM-4DXTH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_u8xe_1226_sm_4e3hn = models.FloatField(db_column='GTEX-U8XE-1226-SM-4E3HN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ujhi_0226_sm_4ihjl = models.FloatField(db_column='GTEX-UJHI-0226-SM-4IHJL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ujmc_0626_sm_4ihjq = models.FloatField(db_column='GTEX-UJMC-0626-SM-4IHJQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_upjh_0926_sm_4ihka = models.FloatField(db_column='GTEX-UPJH-0926-SM-4IHKA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_upk5_1526_sm_4jbja = models.FloatField(db_column='GTEX-UPK5-1526-SM-4JBJA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_v1d1_0326_sm_4jbiy = models.FloatField(db_column='GTEX-V1D1-0326-SM-4JBIY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_v955_0926_sm_4jbj8 = models.FloatField(db_column='GTEX-V955-0926-SM-4JBJ8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_vjya_0226_sm_4kl1q = models.FloatField(db_column='GTEX-VJYA-0226-SM-4KL1Q', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_vusg_0526_sm_4kl22 = models.FloatField(db_column='GTEX-VUSG-0526-SM-4KL22', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_w5wg_0726_sm_exuqz = models.FloatField(db_column='GTEX-W5WG-0726-SM-EXUQZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wfg7_0926_sm_4lmk7 = models.FloatField(db_column='GTEX-WFG7-0926-SM-4LMK7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wfg8_0826_sm_4lvn5 = models.FloatField(db_column='GTEX-WFG8-0826-SM-4LVN5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wfon_0526_sm_4lvly = models.FloatField(db_column='GTEX-WFON-0526-SM-4LVLY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wh7g_0626_sm_4lvmo = models.FloatField(db_column='GTEX-WH7G-0626-SM-4LVMO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_whpg_0926_sm_4m1xy = models.FloatField(db_column='GTEX-WHPG-0926-SM-4M1XY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_whsb_0226_sm_4m1xe = models.FloatField(db_column='GTEX-WHSB-0226-SM-4M1XE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_whwd_0526_sm_4oorw = models.FloatField(db_column='GTEX-WHWD-0526-SM-4OORW', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wquq_1526_sm_4oosm = models.FloatField(db_column='GTEX-WQUQ-1526-SM-4OOSM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wrhu_1326_sm_4e3k7 = models.FloatField(db_column='GTEX-WRHU-1326-SM-4E3K7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wy7c_0626_sm_4onct = models.FloatField(db_column='GTEX-WY7C-0626-SM-4ONCT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wyjk_1226_sm_4oncp = models.FloatField(db_column='GTEX-WYJK-1226-SM-4ONCP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wyvs_0426_sm_4ondl = models.FloatField(db_column='GTEX-WYVS-0426-SM-4ONDL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_wzto_1626_sm_4pqyr = models.FloatField(db_column='GTEX-WZTO-1626-SM-4PQYR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_x3y1_0326_sm_4pqz7 = models.FloatField(db_column='GTEX-X3Y1-0326-SM-4PQZ7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_x4eo_1026_sm_4qarp = models.FloatField(db_column='GTEX-X4EO-1026-SM-4QARP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_x4ep_1426_sm_4pqzp = models.FloatField(db_column='GTEX-X4EP-1426-SM-4PQZP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_x4xy_1526_sm_4qase = models.FloatField(db_column='GTEX-X4XY-1526-SM-4QASE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xbed_0726_sm_4giar = models.FloatField(db_column='GTEX-XBED-0726-SM-4GIAR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xbew_0526_sm_4qaso = models.FloatField(db_column='GTEX-XBEW-0526-SM-4QASO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xpt6_0326_sm_4b66v = models.FloatField(db_column='GTEX-XPT6-0326-SM-4B66V', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xpvg_0226_sm_evyaq = models.FloatField(db_column='GTEX-XPVG-0226-SM-EVYAQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xq3s_0126_sm_4boo9 = models.FloatField(db_column='GTEX-XQ3S-0126-SM-4BOO9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xq8i_1326_sm_4bopv = models.FloatField(db_column='GTEX-XQ8I-1326-SM-4BOPV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xuw1_1126_sm_4bonz = models.FloatField(db_column='GTEX-XUW1-1126-SM-4BONZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xuzc_0626_sm_4bopg = models.FloatField(db_column='GTEX-XUZC-0626-SM-4BOPG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xv7q_0526_sm_4brwr = models.FloatField(db_column='GTEX-XV7Q-0526-SM-4BRWR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xxek_0726_sm_4brwf = models.FloatField(db_column='GTEX-XXEK-0726-SM-4BRWF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_xyks_0426_sm_4brw4 = models.FloatField(db_column='GTEX-XYKS-0426-SM-4BRW4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y114_0426_sm_4tt6v = models.FloatField(db_column='GTEX-Y114-0426-SM-4TT6V', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y3i4_0326_sm_4tt28 = models.FloatField(db_column='GTEX-Y3I4-0326-SM-4TT28', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y3ik_0726_sm_4wwe5 = models.FloatField(db_column='GTEX-Y3IK-0726-SM-4WWE5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y5lm_0226_sm_4vbrm = models.FloatField(db_column='GTEX-Y5LM-0226-SM-4VBRM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y5v5_0426_sm_4vbpu = models.FloatField(db_column='GTEX-Y5V5-0426-SM-4VBPU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y5v6_0426_sm_4vbrz = models.FloatField(db_column='GTEX-Y5V6-0426-SM-4VBRZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y8e4_1126_sm_5ifia = models.FloatField(db_column='GTEX-Y8E4-1126-SM-5IFIA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y8lw_0426_sm_4vbq6 = models.FloatField(db_column='GTEX-Y8LW-0426-SM-4VBQ6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_y9lg_0226_sm_4vbs4 = models.FloatField(db_column='GTEX-Y9LG-0226-SM-4VBS4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_yb5k_0326_sm_5ifjq = models.FloatField(db_column='GTEX-YB5K-0326-SM-5IFJQ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_yec3_0526_sm_d4p1x = models.FloatField(db_column='GTEX-YEC3-0526-SM-D4P1X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_yec4_0726_sm_5cvlv = models.FloatField(db_column='GTEX-YEC4-0726-SM-5CVLV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_yeck_1326_sm_4w1zf = models.FloatField(db_column='GTEX-YECK-1326-SM-4W1ZF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_yfc4_0326_sm_4tt3u = models.FloatField(db_column='GTEX-YFC4-0326-SM-4TT3U', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_yj8o_0226_sm_5s2nl = models.FloatField(db_column='GTEX-YJ8O-0226-SM-5S2NL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_z9ew_0126_sm_5cvm6 = models.FloatField(db_column='GTEX-Z9EW-0126-SM-5CVM6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_za64_0126_sm_5hl8z = models.FloatField(db_column='GTEX-ZA64-0126-SM-5HL8Z', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zab4_0526_sm_5hl7z = models.FloatField(db_column='GTEX-ZAB4-0526-SM-5HL7Z', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zajg_1226_sm_5s2mh = models.FloatField(db_column='GTEX-ZAJG-1226-SM-5S2MH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zak1_1226_sm_5q5aa = models.FloatField(db_column='GTEX-ZAK1-1226-SM-5Q5AA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zc5h_1026_sm_5cvn1 = models.FloatField(db_column='GTEX-ZC5H-1026-SM-5CVN1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zdts_1426_sm_5k7wc = models.FloatField(db_column='GTEX-ZDTS-1426-SM-5K7WC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zdtt_0226_sm_4wkhm = models.FloatField(db_column='GTEX-ZDTT-0226-SM-4WKHM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zdxo_2726_sm_4wkfa = models.FloatField(db_column='GTEX-ZDXO-2726-SM-4WKFA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zdys_0526_sm_5l3ee = models.FloatField(db_column='GTEX-ZDYS-0526-SM-5L3EE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ze9c_0726_sm_4wkga = models.FloatField(db_column='GTEX-ZE9C-0726-SM-4WKGA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zf28_1026_sm_4wkgv = models.FloatField(db_column='GTEX-ZF28-1026-SM-4WKGV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zf29_0326_sm_4wkfb = models.FloatField(db_column='GTEX-ZF29-0326-SM-4WKFB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zf2s_0926_sm_4wwbj = models.FloatField(db_column='GTEX-ZF2S-0926-SM-4WWBJ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zf3c_1426_sm_4wwcd = models.FloatField(db_column='GTEX-ZF3C-1426-SM-4WWCD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zg7y_0126_sm_4wwex = models.FloatField(db_column='GTEX-ZG7Y-0126-SM-4WWEX', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zp4g_0526_sm_4yced = models.FloatField(db_column='GTEX-ZP4G-0526-SM-4YCED', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zpic_1026_sm_59hkz = models.FloatField(db_column='GTEX-ZPIC-1026-SM-59HKZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zqud_0226_sm_4yceb = models.FloatField(db_column='GTEX-ZQUD-0226-SM-4YCEB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_ztpg_0726_sm_5duxp = models.FloatField(db_column='GTEX-ZTPG-0726-SM-5DUXP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zvt2_0726_sm_5gier = models.FloatField(db_column='GTEX-ZVT2-0726-SM-5GIER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zvzp_0126_sm_5nq6q = models.FloatField(db_column='GTEX-ZVZP-0126-SM-5NQ6Q', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zyfd_2126_sm_5e43d = models.FloatField(db_column='GTEX-ZYFD-2126-SM-5E43D', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zyfg_0326_sm_5e45z = models.FloatField(db_column='GTEX-ZYFG-0326-SM-5E45Z', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zyt6_1026_sm_dkpov = models.FloatField(db_column='GTEX-ZYT6-1026-SM-DKPOV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zyw4_1226_sm_5e45b = models.FloatField(db_column='GTEX-ZYW4-1226-SM-5E45B', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zyy3_1226_sm_5eqkm = models.FloatField(db_column='GTEX-ZYY3-1226-SM-5EQKM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtex_zzpu_0226_sm_5n9bv = models.FloatField(db_column='GTEX-ZZPU-0226-SM-5N9BV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'artery_aorta'


class DiacoTissueAdiposeSubcutaneous(models.Model):
    subjid = models.CharField(db_column='SUBJID', max_length=50, primary_key=True)  # Field name made lowercase.
    sampid = models.CharField(db_column='SAMPID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sesso = models.CharField(db_column='Sesso', max_length=1)  # Field name made lowercase.
    eta = models.CharField(db_column='Età', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errfi1 = models.FloatField(db_column='ERRFI1', blank=True, null=True)  # Field name made lowercase.
    mad2l2 = models.FloatField(db_column='MAD2L2', blank=True, null=True)  # Field name made lowercase.
    mthfr = models.FloatField(db_column='MTHFR', blank=True, null=True)  # Field name made lowercase.
    nppa = models.FloatField(db_column='NPPA', blank=True, null=True)  # Field name made lowercase.
    tnfrsf1b = models.FloatField(db_column='TNFRSF1B', blank=True, null=True)  # Field name made lowercase.
    pla2g2a = models.FloatField(db_column='PLA2G2A', blank=True, null=True)  # Field name made lowercase.
    alpl = models.FloatField(db_column='ALPL', blank=True, null=True)  # Field name made lowercase.
    hspg2 = models.FloatField(db_column='HSPG2', blank=True, null=True)  # Field name made lowercase.
    cnr2 = models.FloatField(db_column='CNR2', blank=True, null=True)  # Field name made lowercase.
    slc9a1 = models.FloatField(db_column='SLC9A1', blank=True, null=True)  # Field name made lowercase.
    col8a2 = models.FloatField(db_column='COL8A2', blank=True, null=True)  # Field name made lowercase.
    cap1 = models.FloatField(db_column='CAP1', blank=True, null=True)  # Field name made lowercase.
    slc2a1 = models.FloatField(db_column='SLC2A1', blank=True, null=True)  # Field name made lowercase.
    cyp2j2 = models.FloatField(db_column='CYP2J2', blank=True, null=True)  # Field name made lowercase.
    ddah1 = models.FloatField(db_column='DDAH1', blank=True, null=True)  # Field name made lowercase.
    cyr61 = models.FloatField(db_column='CYR61', blank=True, null=True)  # Field name made lowercase.
    ngf = models.FloatField(db_column='NGF', blank=True, null=True)  # Field name made lowercase.
    hmgcs2 = models.FloatField(db_column='HMGCS2', blank=True, null=True)  # Field name made lowercase.
    ctss = models.FloatField(db_column='CTSS', blank=True, null=True)  # Field name made lowercase.
    s100a12 = models.FloatField(db_column='S100A12', blank=True, null=True)  # Field name made lowercase.
    lmna = models.FloatField(db_column='LMNA', blank=True, null=True)  # Field name made lowercase.
    cd247 = models.FloatField(db_column='CD247', blank=True, null=True)  # Field name made lowercase.
    sele = models.FloatField(db_column='SELE', blank=True, null=True)  # Field name made lowercase.
    fmo3 = models.FloatField(db_column='FMO3', blank=True, null=True)  # Field name made lowercase.
    prdx6 = models.FloatField(db_column='PRDX6', blank=True, null=True)  # Field name made lowercase.
    glul = models.FloatField(db_column='GLUL', blank=True, null=True)  # Field name made lowercase.
    lamc1 = models.FloatField(db_column='LAMC1', blank=True, null=True)  # Field name made lowercase.
    ptgs2 = models.FloatField(db_column='PTGS2', blank=True, null=True)  # Field name made lowercase.
    chi3l1 = models.FloatField(db_column='CHI3L1', blank=True, null=True)  # Field name made lowercase.
    chit1 = models.FloatField(db_column='CHIT1', blank=True, null=True)  # Field name made lowercase.
    fmod = models.FloatField(db_column='FMOD', blank=True, null=True)  # Field name made lowercase.
    il10 = models.FloatField(db_column='IL10', blank=True, null=True)  # Field name made lowercase.
    pfkfb2 = models.FloatField(db_column='PFKFB2', blank=True, null=True)  # Field name made lowercase.
    cd34 = models.FloatField(db_column='CD34', blank=True, null=True)  # Field name made lowercase.
    cog2 = models.FloatField(db_column='COG2', blank=True, null=True)  # Field name made lowercase.
    nlrp3 = models.FloatField(db_column='NLRP3', blank=True, null=True)  # Field name made lowercase.
    rock2 = models.FloatField(db_column='ROCK2', blank=True, null=True)  # Field name made lowercase.
    apob = models.FloatField(db_column='APOB', blank=True, null=True)  # Field name made lowercase.
    pomc = models.FloatField(db_column='POMC', blank=True, null=True)  # Field name made lowercase.
    gckr = models.FloatField(db_column='GCKR', blank=True, null=True)  # Field name made lowercase.
    plekhh2 = models.FloatField(db_column='PLEKHH2', blank=True, null=True)  # Field name made lowercase.
    prkce = models.FloatField(db_column='PRKCE', blank=True, null=True)  # Field name made lowercase.
    pigf = models.FloatField(db_column='PIGF', blank=True, null=True)  # Field name made lowercase.
    msh2 = models.FloatField(db_column='MSH2', blank=True, null=True)  # Field name made lowercase.
    gfpt1 = models.FloatField(db_column='GFPT1', blank=True, null=True)  # Field name made lowercase.
    tacr1 = models.FloatField(db_column='TACR1', blank=True, null=True)  # Field name made lowercase.
    reg1a = models.FloatField(db_column='REG1A', blank=True, null=True)  # Field name made lowercase.
    eif2ak3 = models.FloatField(db_column='EIF2AK3', blank=True, null=True)  # Field name made lowercase.
    adra2b = models.FloatField(db_column='ADRA2B', blank=True, null=True)  # Field name made lowercase.
    il1b = models.FloatField(db_column='IL1B', blank=True, null=True)  # Field name made lowercase.
    proc = models.FloatField(db_column='PROC', blank=True, null=True)  # Field name made lowercase.
    polr2d = models.FloatField(db_column='POLR2D', blank=True, null=True)  # Field name made lowercase.
    zeb2 = models.FloatField(db_column='ZEB2', blank=True, null=True)  # Field name made lowercase.
    acvr1c = models.FloatField(db_column='ACVR1C', blank=True, null=True)  # Field name made lowercase.
    dpp4 = models.FloatField(db_column='DPP4', blank=True, null=True)  # Field name made lowercase.
    nfe2l2 = models.FloatField(db_column='NFE2L2', blank=True, null=True)  # Field name made lowercase.
    igfbp5 = models.FloatField(db_column='IGFBP5', blank=True, null=True)  # Field name made lowercase.
    ccl20 = models.FloatField(db_column='CCL20', blank=True, null=True)  # Field name made lowercase.
    hdac4 = models.FloatField(db_column='HDAC4', blank=True, null=True)  # Field name made lowercase.
    capn10 = models.FloatField(db_column='CAPN10', blank=True, null=True)  # Field name made lowercase.
    ghrl = models.FloatField(db_column='GHRL', blank=True, null=True)  # Field name made lowercase.
    pparg = models.FloatField(db_column='PPARG', blank=True, null=True)  # Field name made lowercase.
    raf1 = models.FloatField(db_column='RAF1', blank=True, null=True)  # Field name made lowercase.
    myd88 = models.FloatField(db_column='MYD88', blank=True, null=True)  # Field name made lowercase.
    cx3cr1 = models.FloatField(db_column='CX3CR1', blank=True, null=True)  # Field name made lowercase.
    cck = models.FloatField(db_column='CCK', blank=True, null=True)  # Field name made lowercase.
    exosc7 = models.FloatField(db_column='EXOSC7', blank=True, null=True)  # Field name made lowercase.
    ccr1 = models.FloatField(db_column='CCR1', blank=True, null=True)  # Field name made lowercase.
    ccr5 = models.FloatField(db_column='CCR5', blank=True, null=True)  # Field name made lowercase.
    gpx1 = models.FloatField(db_column='GPX1', blank=True, null=True)  # Field name made lowercase.
    rhoa = models.FloatField(db_column='RHOA', blank=True, null=True)  # Field name made lowercase.
    cish = models.FloatField(db_column='CISH', blank=True, null=True)  # Field name made lowercase.
    tkt = models.FloatField(db_column='TKT', blank=True, null=True)  # Field name made lowercase.
    appl1 = models.FloatField(db_column='APPL1', blank=True, null=True)  # Field name made lowercase.
    slmap = models.FloatField(db_column='SLMAP', blank=True, null=True)  # Field name made lowercase.
    col8a1 = models.FloatField(db_column='COL8A1', blank=True, null=True)  # Field name made lowercase.
    cd47 = models.FloatField(db_column='CD47', blank=True, null=True)  # Field name made lowercase.
    gap43 = models.FloatField(db_column='GAP43', blank=True, null=True)  # Field name made lowercase.
    cd80 = models.FloatField(db_column='CD80', blank=True, null=True)  # Field name made lowercase.
    rho = models.FloatField(db_column='RHO', blank=True, null=True)  # Field name made lowercase.
    trh = models.FloatField(db_column='TRH', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='TF', blank=True, null=True)  # Field name made lowercase.
    rbp1 = models.FloatField(db_column='RBP1', blank=True, null=True)  # Field name made lowercase.
    trpc1 = models.FloatField(db_column='TRPC1', blank=True, null=True)  # Field name made lowercase.
    agtr1 = models.FloatField(db_column='AGTR1', blank=True, null=True)  # Field name made lowercase.
    sucnr1 = models.FloatField(db_column='SUCNR1', blank=True, null=True)  # Field name made lowercase.
    p2ry1 = models.FloatField(db_column='P2RY1', blank=True, null=True)  # Field name made lowercase.
    mme = models.FloatField(db_column='MME', blank=True, null=True)  # Field name made lowercase.
    slc2a2 = models.FloatField(db_column='SLC2A2', blank=True, null=True)  # Field name made lowercase.
    pik3ca = models.FloatField(db_column='PIK3CA', blank=True, null=True)  # Field name made lowercase.
    parl = models.FloatField(db_column='PARL', blank=True, null=True)  # Field name made lowercase.
    ahsg = models.FloatField(db_column='AHSG', blank=True, null=True)  # Field name made lowercase.
    adipoq = models.FloatField(db_column='ADIPOQ', blank=True, null=True)  # Field name made lowercase.
    spon2 = models.FloatField(db_column='SPON2', blank=True, null=True)  # Field name made lowercase.
    wfs1 = models.FloatField(db_column='WFS1', blank=True, null=True)  # Field name made lowercase.
    cd38 = models.FloatField(db_column='CD38', blank=True, null=True)  # Field name made lowercase.
    prom1 = models.FloatField(db_column='PROM1', blank=True, null=True)  # Field name made lowercase.
    ppargc1a = models.FloatField(db_column='PPARGC1A', blank=True, null=True)  # Field name made lowercase.
    igfbp7 = models.FloatField(db_column='IGFBP7', blank=True, null=True)  # Field name made lowercase.
    cxcl5 = models.FloatField(db_column='CXCL5', blank=True, null=True)  # Field name made lowercase.
    cxcl9 = models.FloatField(db_column='CXCL9', blank=True, null=True)  # Field name made lowercase.
    cxcl10 = models.FloatField(db_column='CXCL10', blank=True, null=True)  # Field name made lowercase.
    cxcl11 = models.FloatField(db_column='CXCL11', blank=True, null=True)  # Field name made lowercase.
    hpse = models.FloatField(db_column='HPSE', blank=True, null=True)  # Field name made lowercase.
    spp1 = models.FloatField(db_column='SPP1', blank=True, null=True)  # Field name made lowercase.
    adh1b = models.FloatField(db_column='ADH1B', blank=True, null=True)  # Field name made lowercase.
    egf = models.FloatField(db_column='EGF', blank=True, null=True)  # Field name made lowercase.
    alpk1 = models.FloatField(db_column='ALPK1', blank=True, null=True)  # Field name made lowercase.
    fabp2 = models.FloatField(db_column='FABP2', blank=True, null=True)  # Field name made lowercase.
    pde5a = models.FloatField(db_column='PDE5A', blank=True, null=True)  # Field name made lowercase.
    setd7 = models.FloatField(db_column='SETD7', blank=True, null=True)  # Field name made lowercase.
    smad1 = models.FloatField(db_column='SMAD1', blank=True, null=True)  # Field name made lowercase.
    ednra = models.FloatField(db_column='EDNRA', blank=True, null=True)  # Field name made lowercase.
    nr3c2 = models.FloatField(db_column='NR3C2', blank=True, null=True)  # Field name made lowercase.
    tlr2 = models.FloatField(db_column='TLR2', blank=True, null=True)  # Field name made lowercase.
    npy5r = models.FloatField(db_column='NPY5R', blank=True, null=True)  # Field name made lowercase.
    fbxo8 = models.FloatField(db_column='FBXO8', blank=True, null=True)  # Field name made lowercase.
    vegfc = models.FloatField(db_column='VEGFC', blank=True, null=True)  # Field name made lowercase.
    acsl1 = models.FloatField(db_column='ACSL1', blank=True, null=True)  # Field name made lowercase.
    sorbs2 = models.FloatField(db_column='SORBS2', blank=True, null=True)  # Field name made lowercase.
    f11 = models.FloatField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    basp1 = models.FloatField(db_column='BASP1', blank=True, null=True)  # Field name made lowercase.
    ptger4 = models.FloatField(db_column='PTGER4', blank=True, null=True)  # Field name made lowercase.
    prkaa1 = models.FloatField(db_column='PRKAA1', blank=True, null=True)  # Field name made lowercase.
    ghr = models.FloatField(db_column='GHR', blank=True, null=True)  # Field name made lowercase.
    itga2 = models.FloatField(db_column='ITGA2', blank=True, null=True)  # Field name made lowercase.
    cdk7 = models.FloatField(db_column='CDK7', blank=True, null=True)  # Field name made lowercase.
    f2r = models.FloatField(db_column='F2R', blank=True, null=True)  # Field name made lowercase.
    erap2 = models.FloatField(db_column='ERAP2', blank=True, null=True)  # Field name made lowercase.
    apc = models.FloatField(db_column='APC', blank=True, null=True)  # Field name made lowercase.
    tnfaip8 = models.FloatField(db_column='TNFAIP8', blank=True, null=True)  # Field name made lowercase.
    vdac1 = models.FloatField(db_column='VDAC1', blank=True, null=True)  # Field name made lowercase.
    pdgfrb = models.FloatField(db_column='PDGFRB', blank=True, null=True)  # Field name made lowercase.
    cd74 = models.FloatField(db_column='CD74', blank=True, null=True)  # Field name made lowercase.
    sparc = models.FloatField(db_column='SPARC', blank=True, null=True)  # Field name made lowercase.
    ebf1 = models.FloatField(db_column='EBF1', blank=True, null=True)  # Field name made lowercase.
    gfpt2 = models.FloatField(db_column='GFPT2', blank=True, null=True)  # Field name made lowercase.
    rreb1 = models.FloatField(db_column='RREB1', blank=True, null=True)  # Field name made lowercase.
    edn1 = models.FloatField(db_column='EDN1', blank=True, null=True)  # Field name made lowercase.
    cdkal1 = models.FloatField(db_column='CDKAL1', blank=True, null=True)  # Field name made lowercase.
    hfe = models.FloatField(db_column='HFE', blank=True, null=True)  # Field name made lowercase.
    hla_a = models.FloatField(db_column='HLA-A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  # Field name made lowercase.
    tnf = models.FloatField(db_column='TNF', blank=True, null=True)  # Field name made lowercase.
    hspa1a = models.FloatField(db_column='HSPA1A', blank=True, null=True)  # Field name made lowercase.
    hspa1b = models.FloatField(db_column='HSPA1B', blank=True, null=True)  # Field name made lowercase.
    hla_dqa1 = models.FloatField(db_column='HLA-DQA1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mapk14 = models.FloatField(db_column='MAPK14', blank=True, null=True)  # Field name made lowercase.
    cdkn1a = models.FloatField(db_column='CDKN1A', blank=True, null=True)  # Field name made lowercase.
    glo1 = models.FloatField(db_column='GLO1', blank=True, null=True)  # Field name made lowercase.
    vegfa = models.FloatField(db_column='VEGFA', blank=True, null=True)  # Field name made lowercase.
    cd2ap = models.FloatField(db_column='CD2AP', blank=True, null=True)  # Field name made lowercase.
    cnr1 = models.FloatField(db_column='CNR1', blank=True, null=True)  # Field name made lowercase.
    enpp1 = models.FloatField(db_column='ENPP1', blank=True, null=True)  # Field name made lowercase.
    ctgf = models.FloatField(db_column='CTGF', blank=True, null=True)  # Field name made lowercase.
    rps12 = models.FloatField(db_column='RPS12', blank=True, null=True)  # Field name made lowercase.
    sgk1 = models.FloatField(db_column='SGK1', blank=True, null=True)  # Field name made lowercase.
    map3k5 = models.FloatField(db_column='MAP3K5', blank=True, null=True)  # Field name made lowercase.
    cited2 = models.FloatField(db_column='CITED2', blank=True, null=True)  # Field name made lowercase.
    utrn = models.FloatField(db_column='UTRN', blank=True, null=True)  # Field name made lowercase.
    mthfd1l = models.FloatField(db_column='MTHFD1L', blank=True, null=True)  # Field name made lowercase.
    vip = models.FloatField(db_column='VIP', blank=True, null=True)  # Field name made lowercase.
    sod2 = models.FloatField(db_column='SOD2', blank=True, null=True)  # Field name made lowercase.
    lpa = models.FloatField(db_column='LPA', blank=True, null=True)  # Field name made lowercase.
    thbs2 = models.FloatField(db_column='THBS2', blank=True, null=True)  # Field name made lowercase.
    pdgfa = models.FloatField(db_column='PDGFA', blank=True, null=True)  # Field name made lowercase.
    il6 = models.FloatField(db_column='IL6', blank=True, null=True)  # Field name made lowercase.
    npy = models.FloatField(db_column='NPY', blank=True, null=True)  # Field name made lowercase.
    jazf1 = models.FloatField(db_column='JAZF1', blank=True, null=True)  # Field name made lowercase.
    cpvl = models.FloatField(db_column='CPVL', blank=True, null=True)  # Field name made lowercase.
    aqp1 = models.FloatField(db_column='AQP1', blank=True, null=True)  # Field name made lowercase.
    elmo1 = models.FloatField(db_column='ELMO1', blank=True, null=True)  # Field name made lowercase.
    igfbp3 = models.FloatField(db_column='IGFBP3', blank=True, null=True)  # Field name made lowercase.
    egfr = models.FloatField(db_column='EGFR', blank=True, null=True)  # Field name made lowercase.
    eln = models.FloatField(db_column='ELN', blank=True, null=True)  # Field name made lowercase.
    ncf1 = models.FloatField(db_column='NCF1', blank=True, null=True)  # Field name made lowercase.
    hspb1 = models.FloatField(db_column='HSPB1', blank=True, null=True)  # Field name made lowercase.
    sema3a = models.FloatField(db_column='SEMA3A', blank=True, null=True)  # Field name made lowercase.
    pon3 = models.FloatField(db_column='PON3', blank=True, null=True)  # Field name made lowercase.
    pon2 = models.FloatField(db_column='PON2', blank=True, null=True)  # Field name made lowercase.
    nampt = models.FloatField(db_column='NAMPT', blank=True, null=True)  # Field name made lowercase.
    cav1 = models.FloatField(db_column='CAV1', blank=True, null=True)  # Field name made lowercase.
    lep = models.FloatField(db_column='LEP', blank=True, null=True)  # Field name made lowercase.
    akr1b1 = models.FloatField(db_column='AKR1B1', blank=True, null=True)  # Field name made lowercase.
    akr1b10 = models.FloatField(db_column='AKR1B10', blank=True, null=True)  # Field name made lowercase.
    pip = models.FloatField(db_column='PIP', blank=True, null=True)  # Field name made lowercase.
    rarres2 = models.FloatField(db_column='RARRES2', blank=True, null=True)  # Field name made lowercase.
    nos3 = models.FloatField(db_column='NOS3', blank=True, null=True)  # Field name made lowercase.
    angpt2 = models.FloatField(db_column='ANGPT2', blank=True, null=True)  # Field name made lowercase.
    defa1 = models.FloatField(db_column='DEFA1', blank=True, null=True)  # Field name made lowercase.
    lpl = models.FloatField(db_column='LPL', blank=True, null=True)  # Field name made lowercase.
    ebf2 = models.FloatField(db_column='EBF2', blank=True, null=True)  # Field name made lowercase.
    adrb3 = models.FloatField(db_column='ADRB3', blank=True, null=True)  # Field name made lowercase.
    eif4ebp1 = models.FloatField(db_column='EIF4EBP1', blank=True, null=True)  # Field name made lowercase.
    fgfr1 = models.FloatField(db_column='FGFR1', blank=True, null=True)  # Field name made lowercase.
    crh = models.FloatField(db_column='CRH', blank=True, null=True)  # Field name made lowercase.
    sgk3 = models.FloatField(db_column='SGK3', blank=True, null=True)  # Field name made lowercase.
    fabp5 = models.FloatField(db_column='FABP5', blank=True, null=True)  # Field name made lowercase.
    fabp4 = models.FloatField(db_column='FABP4', blank=True, null=True)  # Field name made lowercase.
    mmp16 = models.FloatField(db_column='MMP16', blank=True, null=True)  # Field name made lowercase.
    ncald = models.FloatField(db_column='NCALD', blank=True, null=True)  # Field name made lowercase.
    klf10 = models.FloatField(db_column='KLF10', blank=True, null=True)  # Field name made lowercase.
    enpp2 = models.FloatField(db_column='ENPP2', blank=True, null=True)  # Field name made lowercase.
    pvt1 = models.FloatField(db_column='PVT1', blank=True, null=True)  # Field name made lowercase.
    jak2 = models.FloatField(db_column='JAK2', blank=True, null=True)  # Field name made lowercase.
    psip1 = models.FloatField(db_column='PSIP1', blank=True, null=True)  # Field name made lowercase.
    plin2 = models.FloatField(db_column='PLIN2', blank=True, null=True)  # Field name made lowercase.
    rps6 = models.FloatField(db_column='RPS6', blank=True, null=True)  # Field name made lowercase.
    aldh1a1 = models.FloatField(db_column='ALDH1A1', blank=True, null=True)  # Field name made lowercase.
    frmd3 = models.FloatField(db_column='FRMD3', blank=True, null=True)  # Field name made lowercase.
    gas1 = models.FloatField(db_column='GAS1', blank=True, null=True)  # Field name made lowercase.
    baat = models.FloatField(db_column='BAAT', blank=True, null=True)  # Field name made lowercase.
    abca1 = models.FloatField(db_column='ABCA1', blank=True, null=True)  # Field name made lowercase.
    txn = models.FloatField(db_column='TXN', blank=True, null=True)  # Field name made lowercase.
    ambp = models.FloatField(db_column='AMBP', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    hspa5 = models.FloatField(db_column='HSPA5', blank=True, null=True)  # Field name made lowercase.
    angptl2 = models.FloatField(db_column='ANGPTL2', blank=True, null=True)  # Field name made lowercase.
    ptges = models.FloatField(db_column='PTGES', blank=True, null=True)  # Field name made lowercase.
    tsc1 = models.FloatField(db_column='TSC1', blank=True, null=True)  # Field name made lowercase.
    abo = models.FloatField(db_column='ABO', blank=True, null=True)  # Field name made lowercase.
    adamts13 = models.FloatField(db_column='ADAMTS13', blank=True, null=True)  # Field name made lowercase.
    ptgds = models.FloatField(db_column='PTGDS', blank=True, null=True)  # Field name made lowercase.
    klf6 = models.FloatField(db_column='KLF6', blank=True, null=True)  # Field name made lowercase.
    cdc123 = models.FloatField(db_column='CDC123', blank=True, null=True)  # Field name made lowercase.
    bambi = models.FloatField(db_column='BAMBI', blank=True, null=True)  # Field name made lowercase.
    cxcl12 = models.FloatField(db_column='CXCL12', blank=True, null=True)  # Field name made lowercase.
    mbl2 = models.FloatField(db_column='MBL2', blank=True, null=True)  # Field name made lowercase.
    tfam = models.FloatField(db_column='TFAM', blank=True, null=True)  # Field name made lowercase.
    sirt1 = models.FloatField(db_column='SIRT1', blank=True, null=True)  # Field name made lowercase.
    srgn = models.FloatField(db_column='SRGN', blank=True, null=True)  # Field name made lowercase.
    unc5b = models.FloatField(db_column='UNC5B', blank=True, null=True)  # Field name made lowercase.
    adk = models.FloatField(db_column='ADK', blank=True, null=True)  # Field name made lowercase.
    pten = models.FloatField(db_column='PTEN', blank=True, null=True)  # Field name made lowercase.
    rbp4 = models.FloatField(db_column='RBP4', blank=True, null=True)  # Field name made lowercase.
    cyp2c19 = models.FloatField(db_column='CYP2C19', blank=True, null=True)  # Field name made lowercase.
    entpd1 = models.FloatField(db_column='ENTPD1', blank=True, null=True)  # Field name made lowercase.
    tcf7l2 = models.FloatField(db_column='TCF7L2', blank=True, null=True)  # Field name made lowercase.
    bnip3 = models.FloatField(db_column='BNIP3', blank=True, null=True)  # Field name made lowercase.
    igf2 = models.FloatField(db_column='IGF2', blank=True, null=True)  # Field name made lowercase.
    ins = models.FloatField(db_column='INS', blank=True, null=True)  # Field name made lowercase.
    th = models.FloatField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    kcnq1 = models.FloatField(db_column='KCNQ1', blank=True, null=True)  # Field name made lowercase.
    hbg2 = models.FloatField(db_column='HBG2', blank=True, null=True)  # Field name made lowercase.
    smpd1 = models.FloatField(db_column='SMPD1', blank=True, null=True)  # Field name made lowercase.
    ilk = models.FloatField(db_column='ILK', blank=True, null=True)  # Field name made lowercase.
    adm = models.FloatField(db_column='ADM', blank=True, null=True)  # Field name made lowercase.
    pth = models.FloatField(db_column='PTH', blank=True, null=True)  # Field name made lowercase.
    nucb2 = models.FloatField(db_column='NUCB2', blank=True, null=True)  # Field name made lowercase.
    kcnj11 = models.FloatField(db_column='KCNJ11', blank=True, null=True)  # Field name made lowercase.
    saa1 = models.FloatField(db_column='SAA1', blank=True, null=True)  # Field name made lowercase.
    bdnf = models.FloatField(db_column='BDNF', blank=True, null=True)  # Field name made lowercase.
    wt1 = models.FloatField(db_column='WT1', blank=True, null=True)  # Field name made lowercase.
    cd59 = models.FloatField(db_column='CD59', blank=True, null=True)  # Field name made lowercase.
    pdhx = models.FloatField(db_column='PDHX', blank=True, null=True)  # Field name made lowercase.
    traf6 = models.FloatField(db_column='TRAF6', blank=True, null=True)  # Field name made lowercase.
    api5 = models.FloatField(db_column='API5', blank=True, null=True)  # Field name made lowercase.
    nr1h3 = models.FloatField(db_column='NR1H3', blank=True, null=True)  # Field name made lowercase.
    ndufs3 = models.FloatField(db_column='NDUFS3', blank=True, null=True)  # Field name made lowercase.
    folh1 = models.FloatField(db_column='FOLH1', blank=True, null=True)  # Field name made lowercase.
    aplnr = models.FloatField(db_column='APLNR', blank=True, null=True)  # Field name made lowercase.
    p2rx3 = models.FloatField(db_column='P2RX3', blank=True, null=True)  # Field name made lowercase.
    cntf = models.FloatField(db_column='CNTF', blank=True, null=True)  # Field name made lowercase.
    fads1 = models.FloatField(db_column='FADS1', blank=True, null=True)  # Field name made lowercase.
    fads2 = models.FloatField(db_column='FADS2', blank=True, null=True)  # Field name made lowercase.
    fkbp2 = models.FloatField(db_column='FKBP2', blank=True, null=True)  # Field name made lowercase.
    syvn1 = models.FloatField(db_column='SYVN1', blank=True, null=True)  # Field name made lowercase.
    pc = models.FloatField(db_column='PC', blank=True, null=True)  # Field name made lowercase.
    dhcr7 = models.FloatField(db_column='DHCR7', blank=True, null=True)  # Field name made lowercase.
    prcp = models.FloatField(db_column='PRCP', blank=True, null=True)  # Field name made lowercase.
    nox4 = models.FloatField(db_column='NOX4', blank=True, null=True)  # Field name made lowercase.
    pdgfd = models.FloatField(db_column='PDGFD', blank=True, null=True)  # Field name made lowercase.
    atm = models.FloatField(db_column='ATM', blank=True, null=True)  # Field name made lowercase.
    il18 = models.FloatField(db_column='IL18', blank=True, null=True)  # Field name made lowercase.
    apoa1 = models.FloatField(db_column='APOA1', blank=True, null=True)  # Field name made lowercase.
    hyou1 = models.FloatField(db_column='HYOU1', blank=True, null=True)  # Field name made lowercase.
    esam = models.FloatField(db_column='ESAM', blank=True, null=True)  # Field name made lowercase.
    fkbp4 = models.FloatField(db_column='FKBP4', blank=True, null=True)  # Field name made lowercase.
    fgf23 = models.FloatField(db_column='FGF23', blank=True, null=True)  # Field name made lowercase.
    ntf3 = models.FloatField(db_column='NTF3', blank=True, null=True)  # Field name made lowercase.
    vwf = models.FloatField(db_column='VWF', blank=True, null=True)  # Field name made lowercase.
    cd9 = models.FloatField(db_column='CD9', blank=True, null=True)  # Field name made lowercase.
    gapdh = models.FloatField(db_column='GAPDH', blank=True, null=True)  # Field name made lowercase.
    cd4 = models.FloatField(db_column='CD4', blank=True, null=True)  # Field name made lowercase.
    gnb3 = models.FloatField(db_column='GNB3', blank=True, null=True)  # Field name made lowercase.
    cd163 = models.FloatField(db_column='CD163', blank=True, null=True)  # Field name made lowercase.
    slc2a3 = models.FloatField(db_column='SLC2A3', blank=True, null=True)  # Field name made lowercase.
    cd69 = models.FloatField(db_column='CD69', blank=True, null=True)  # Field name made lowercase.
    irak4 = models.FloatField(db_column='IRAK4', blank=True, null=True)  # Field name made lowercase.
    vdr = models.FloatField(db_column='VDR', blank=True, null=True)  # Field name made lowercase.
    aqp5 = models.FloatField(db_column='AQP5', blank=True, null=True)  # Field name made lowercase.
    acvrl1 = models.FloatField(db_column='ACVRL1', blank=True, null=True)  # Field name made lowercase.
    nfe2 = models.FloatField(db_column='NFE2', blank=True, null=True)  # Field name made lowercase.
    cd63 = models.FloatField(db_column='CD63', blank=True, null=True)  # Field name made lowercase.
    erbb3 = models.FloatField(db_column='ERBB3', blank=True, null=True)  # Field name made lowercase.
    ddit3 = models.FloatField(db_column='DDIT3', blank=True, null=True)  # Field name made lowercase.
    ifng = models.FloatField(db_column='IFNG', blank=True, null=True)  # Field name made lowercase.
    nts = models.FloatField(db_column='NTS', blank=True, null=True)  # Field name made lowercase.
    igf1 = models.FloatField(db_column='IGF1', blank=True, null=True)  # Field name made lowercase.
    acacb = models.FloatField(db_column='ACACB', blank=True, null=True)  # Field name made lowercase.
    trpv4 = models.FloatField(db_column='TRPV4', blank=True, null=True)  # Field name made lowercase.
    atp2a2 = models.FloatField(db_column='ATP2A2', blank=True, null=True)  # Field name made lowercase.
    aldh2 = models.FloatField(db_column='ALDH2', blank=True, null=True)  # Field name made lowercase.
    nos1 = models.FloatField(db_column='NOS1', blank=True, null=True)  # Field name made lowercase.
    pebp1 = models.FloatField(db_column='PEBP1', blank=True, null=True)  # Field name made lowercase.
    psmd9 = models.FloatField(db_column='PSMD9', blank=True, null=True)  # Field name made lowercase.
    scarb1 = models.FloatField(db_column='SCARB1', blank=True, null=True)  # Field name made lowercase.
    p2rx2 = models.FloatField(db_column='P2RX2', blank=True, null=True)  # Field name made lowercase.
    alox5ap = models.FloatField(db_column='ALOX5AP', blank=True, null=True)  # Field name made lowercase.
    kl = models.FloatField(db_column='KL', blank=True, null=True)  # Field name made lowercase.
    postn = models.FloatField(db_column='POSTN', blank=True, null=True)  # Field name made lowercase.
    foxo1 = models.FloatField(db_column='FOXO1', blank=True, null=True)  # Field name made lowercase.
    htr2a = models.FloatField(db_column='HTR2A', blank=True, null=True)  # Field name made lowercase.
    gpc5 = models.FloatField(db_column='GPC5', blank=True, null=True)  # Field name made lowercase.
    irs2 = models.FloatField(db_column='IRS2', blank=True, null=True)  # Field name made lowercase.
    gas6 = models.FloatField(db_column='GAS6', blank=True, null=True)  # Field name made lowercase.
    ang = models.FloatField(db_column='ANG', blank=True, null=True)  # Field name made lowercase.
    mmp14 = models.FloatField(db_column='MMP14', blank=True, null=True)  # Field name made lowercase.
    ltb4r2 = models.FloatField(db_column='LTB4R2', blank=True, null=True)  # Field name made lowercase.
    nfkbia = models.FloatField(db_column='NFKBIA', blank=True, null=True)  # Field name made lowercase.
    bmp4 = models.FloatField(db_column='BMP4', blank=True, null=True)  # Field name made lowercase.
    rtn1 = models.FloatField(db_column='RTN1', blank=True, null=True)  # Field name made lowercase.
    pgf = models.FloatField(db_column='PGF', blank=True, null=True)  # Field name made lowercase.
    ngb = models.FloatField(db_column='NGB', blank=True, null=True)  # Field name made lowercase.
    ahsa1 = models.FloatField(db_column='AHSA1', blank=True, null=True)  # Field name made lowercase.
    bdkrb2 = models.FloatField(db_column='BDKRB2', blank=True, null=True)  # Field name made lowercase.
    bdkrb1 = models.FloatField(db_column='BDKRB1', blank=True, null=True)  # Field name made lowercase.
    akt1 = models.FloatField(db_column='AKT1', blank=True, null=True)  # Field name made lowercase.
    grem1 = models.FloatField(db_column='GREM1', blank=True, null=True)  # Field name made lowercase.
    thbs1 = models.FloatField(db_column='THBS1', blank=True, null=True)  # Field name made lowercase.
    pak6 = models.FloatField(db_column='PAK6', blank=True, null=True)  # Field name made lowercase.
    b2m = models.FloatField(db_column='B2M', blank=True, null=True)  # Field name made lowercase.
    myo5c = models.FloatField(db_column='MYO5C', blank=True, null=True)  # Field name made lowercase.
    onecut1 = models.FloatField(db_column='ONECUT1', blank=True, null=True)  # Field name made lowercase.
    adam10 = models.FloatField(db_column='ADAM10', blank=True, null=True)  # Field name made lowercase.
    ctsh = models.FloatField(db_column='CTSH', blank=True, null=True)  # Field name made lowercase.
    plin1 = models.FloatField(db_column='PLIN1', blank=True, null=True)  # Field name made lowercase.
    igf1r = models.FloatField(db_column='IGF1R', blank=True, null=True)  # Field name made lowercase.
    mrpl28 = models.FloatField(db_column='MRPL28', blank=True, null=True)  # Field name made lowercase.
    cacna1h = models.FloatField(db_column='CACNA1H', blank=True, null=True)  # Field name made lowercase.
    pdpk1 = models.FloatField(db_column='PDPK1', blank=True, null=True)  # Field name made lowercase.
    ercc4 = models.FloatField(db_column='ERCC4', blank=True, null=True)  # Field name made lowercase.
    smg1 = models.FloatField(db_column='SMG1', blank=True, null=True)  # Field name made lowercase.
    itgam = models.FloatField(db_column='ITGAM', blank=True, null=True)  # Field name made lowercase.
    fto = models.FloatField(db_column='FTO', blank=True, null=True)  # Field name made lowercase.
    mmp2 = models.FloatField(db_column='MMP2', blank=True, null=True)  # Field name made lowercase.
    slc12a3 = models.FloatField(db_column='SLC12A3', blank=True, null=True)  # Field name made lowercase.
    cetp = models.FloatField(db_column='CETP', blank=True, null=True)  # Field name made lowercase.
    cx3cl1 = models.FloatField(db_column='CX3CL1', blank=True, null=True)  # Field name made lowercase.
    cdh1 = models.FloatField(db_column='CDH1', blank=True, null=True)  # Field name made lowercase.
    nqo1 = models.FloatField(db_column='NQO1', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    znrf1 = models.FloatField(db_column='ZNRF1', blank=True, null=True)  # Field name made lowercase.
    cyba = models.FloatField(db_column='CYBA', blank=True, null=True)  # Field name made lowercase.
    tubb3 = models.FloatField(db_column='TUBB3', blank=True, null=True)  # Field name made lowercase.
    crk = models.FloatField(db_column='CRK', blank=True, null=True)  # Field name made lowercase.
    serpinf2 = models.FloatField(db_column='SERPINF2', blank=True, null=True)  # Field name made lowercase.
    serpinf1 = models.FloatField(db_column='SERPINF1', blank=True, null=True)  # Field name made lowercase.
    trpv3 = models.FloatField(db_column='TRPV3', blank=True, null=True)  # Field name made lowercase.
    cxcl16 = models.FloatField(db_column='CXCL16', blank=True, null=True)  # Field name made lowercase.
    slc2a4 = models.FloatField(db_column='SLC2A4', blank=True, null=True)  # Field name made lowercase.
    cd68 = models.FloatField(db_column='CD68', blank=True, null=True)  # Field name made lowercase.
    shbg = models.FloatField(db_column='SHBG', blank=True, null=True)  # Field name made lowercase.
    pmp22 = models.FloatField(db_column='PMP22', blank=True, null=True)  # Field name made lowercase.
    srebf1 = models.FloatField(db_column='SREBF1', blank=True, null=True)  # Field name made lowercase.
    mapk7 = models.FloatField(db_column='MAPK7', blank=True, null=True)  # Field name made lowercase.
    ccl2 = models.FloatField(db_column='CCL2', blank=True, null=True)  # Field name made lowercase.
    ccl5 = models.FloatField(db_column='CCL5', blank=True, null=True)  # Field name made lowercase.
    hnf1b = models.FloatField(db_column='HNF1B', blank=True, null=True)  # Field name made lowercase.
    erbb2 = models.FloatField(db_column='ERBB2', blank=True, null=True)  # Field name made lowercase.
    fkbp10 = models.FloatField(db_column='FKBP10', blank=True, null=True)  # Field name made lowercase.
    stat5a = models.FloatField(db_column='STAT5A', blank=True, null=True)  # Field name made lowercase.
    stat3 = models.FloatField(db_column='STAT3', blank=True, null=True)  # Field name made lowercase.
    naglu = models.FloatField(db_column='NAGLU', blank=True, null=True)  # Field name made lowercase.
    aoc2 = models.FloatField(db_column='AOC2', blank=True, null=True)  # Field name made lowercase.
    aoc3 = models.FloatField(db_column='AOC3', blank=True, null=True)  # Field name made lowercase.
    ppy = models.FloatField(db_column='PPY', blank=True, null=True)  # Field name made lowercase.
    sth = models.FloatField(db_column='STH', blank=True, null=True)  # Field name made lowercase.
    itgb3 = models.FloatField(db_column='ITGB3', blank=True, null=True)  # Field name made lowercase.
    gip = models.FloatField(db_column='GIP', blank=True, null=True)  # Field name made lowercase.
    mpo = models.FloatField(db_column='MPO', blank=True, null=True)  # Field name made lowercase.
    pecam1 = models.FloatField(db_column='PECAM1', blank=True, null=True)  # Field name made lowercase.
    sox9 = models.FloatField(db_column='SOX9', blank=True, null=True)  # Field name made lowercase.
    timp2 = models.FloatField(db_column='TIMP2', blank=True, null=True)  # Field name made lowercase.
    dcxr = models.FloatField(db_column='DCXR', blank=True, null=True)  # Field name made lowercase.
    fasn = models.FloatField(db_column='FASN', blank=True, null=True)  # Field name made lowercase.
    colec12 = models.FloatField(db_column='COLEC12', blank=True, null=True)  # Field name made lowercase.
    adcyap1 = models.FloatField(db_column='ADCYAP1', blank=True, null=True)  # Field name made lowercase.
    smad7 = models.FloatField(db_column='SMAD7', blank=True, null=True)  # Field name made lowercase.
    nedd4l = models.FloatField(db_column='NEDD4L', blank=True, null=True)  # Field name made lowercase.
    mc4r = models.FloatField(db_column='MC4R', blank=True, null=True)  # Field name made lowercase.
    bcl2 = models.FloatField(db_column='BCL2', blank=True, null=True)  # Field name made lowercase.
    cndp2 = models.FloatField(db_column='CNDP2', blank=True, null=True)  # Field name made lowercase.
    znf236 = models.FloatField(db_column='ZNF236', blank=True, null=True)  # Field name made lowercase.
    stk11 = models.FloatField(db_column='STK11', blank=True, null=True)  # Field name made lowercase.
    sirt6 = models.FloatField(db_column='SIRT6', blank=True, null=True)  # Field name made lowercase.
    uhrf1 = models.FloatField(db_column='UHRF1', blank=True, null=True)  # Field name made lowercase.
    timm44 = models.FloatField(db_column='TIMM44', blank=True, null=True)  # Field name made lowercase.
    angptl4 = models.FloatField(db_column='ANGPTL4', blank=True, null=True)  # Field name made lowercase.
    dnmt1 = models.FloatField(db_column='DNMT1', blank=True, null=True)  # Field name made lowercase.
    icam1 = models.FloatField(db_column='ICAM1', blank=True, null=True)  # Field name made lowercase.
    ldlr = models.FloatField(db_column='LDLR', blank=True, null=True)  # Field name made lowercase.
    epor = models.FloatField(db_column='EPOR', blank=True, null=True)  # Field name made lowercase.
    prdx2 = models.FloatField(db_column='PRDX2', blank=True, null=True)  # Field name made lowercase.
    ptger1 = models.FloatField(db_column='PTGER1', blank=True, null=True)  # Field name made lowercase.
    unc13a = models.FloatField(db_column='UNC13A', blank=True, null=True)  # Field name made lowercase.
    gdf15 = models.FloatField(db_column='GDF15', blank=True, null=True)  # Field name made lowercase.
    fkbp8 = models.FloatField(db_column='FKBP8', blank=True, null=True)  # Field name made lowercase.
    usf2 = models.FloatField(db_column='USF2', blank=True, null=True)  # Field name made lowercase.
    ffar1 = models.FloatField(db_column='FFAR1', blank=True, null=True)  # Field name made lowercase.
    ffar2 = models.FloatField(db_column='FFAR2', blank=True, null=True)  # Field name made lowercase.
    nphs1 = models.FloatField(db_column='NPHS1', blank=True, null=True)  # Field name made lowercase.
    tgfb1 = models.FloatField(db_column='TGFB1', blank=True, null=True)  # Field name made lowercase.
    xrcc1 = models.FloatField(db_column='XRCC1', blank=True, null=True)  # Field name made lowercase.
    ercc1 = models.FloatField(db_column='ERCC1', blank=True, null=True)  # Field name made lowercase.
    gipr = models.FloatField(db_column='GIPR', blank=True, null=True)  # Field name made lowercase.
    fgf21 = models.FloatField(db_column='FGF21', blank=True, null=True)  # Field name made lowercase.
    clec11a = models.FloatField(db_column='CLEC11A', blank=True, null=True)  # Field name made lowercase.
    fpr1 = models.FloatField(db_column='FPR1', blank=True, null=True)  # Field name made lowercase.
    trib3 = models.FloatField(db_column='TRIB3', blank=True, null=True)  # Field name made lowercase.
    bmp2 = models.FloatField(db_column='BMP2', blank=True, null=True)  # Field name made lowercase.
    thbd = models.FloatField(db_column='THBD', blank=True, null=True)  # Field name made lowercase.
    cst3 = models.FloatField(db_column='CST3', blank=True, null=True)  # Field name made lowercase.
    id1 = models.FloatField(db_column='ID1', blank=True, null=True)  # Field name made lowercase.
    src = models.FloatField(db_column='SRC', blank=True, null=True)  # Field name made lowercase.
    mafb = models.FloatField(db_column='MAFB', blank=True, null=True)  # Field name made lowercase.
    sgk2 = models.FloatField(db_column='SGK2', blank=True, null=True)  # Field name made lowercase.
    hnf4a = models.FloatField(db_column='HNF4A', blank=True, null=True)  # Field name made lowercase.
    pltp = models.FloatField(db_column='PLTP', blank=True, null=True)  # Field name made lowercase.
    mmp9 = models.FloatField(db_column='MMP9', blank=True, null=True)  # Field name made lowercase.
    cd40 = models.FloatField(db_column='CD40', blank=True, null=True)  # Field name made lowercase.
    ptpn1 = models.FloatField(db_column='PTPN1', blank=True, null=True)  # Field name made lowercase.
    cyp24a1 = models.FloatField(db_column='CYP24A1', blank=True, null=True)  # Field name made lowercase.
    rcan1 = models.FloatField(db_column='RCAN1', blank=True, null=True)  # Field name made lowercase.
    abcg1 = models.FloatField(db_column='ABCG1', blank=True, null=True)  # Field name made lowercase.
    prmt2 = models.FloatField(db_column='PRMT2', blank=True, null=True)  # Field name made lowercase.
    comt = models.FloatField(db_column='COMT', blank=True, null=True)  # Field name made lowercase.
    mapk1 = models.FloatField(db_column='MAPK1', blank=True, null=True)  # Field name made lowercase.
    mif = models.FloatField(db_column='MIF', blank=True, null=True)  # Field name made lowercase.
    ggt1 = models.FloatField(db_column='GGT1', blank=True, null=True)  # Field name made lowercase.
    xbp1 = models.FloatField(db_column='XBP1', blank=True, null=True)  # Field name made lowercase.
    osm = models.FloatField(db_column='OSM', blank=True, null=True)  # Field name made lowercase.
    limk2 = models.FloatField(db_column='LIMK2', blank=True, null=True)  # Field name made lowercase.
    sfi1 = models.FloatField(db_column='SFI1', blank=True, null=True)  # Field name made lowercase.
    timp3 = models.FloatField(db_column='TIMP3', blank=True, null=True)  # Field name made lowercase.
    hmox1 = models.FloatField(db_column='HMOX1', blank=True, null=True)  # Field name made lowercase.
    apol1 = models.FloatField(db_column='APOL1', blank=True, null=True)  # Field name made lowercase.
    myh9 = models.FloatField(db_column='MYH9', blank=True, null=True)  # Field name made lowercase.
    pdgfb = models.FloatField(db_column='PDGFB', blank=True, null=True)  # Field name made lowercase.
    atf4 = models.FloatField(db_column='ATF4', blank=True, null=True)  # Field name made lowercase.
    tspo = models.FloatField(db_column='TSPO', blank=True, null=True)  # Field name made lowercase.
    miox = models.FloatField(db_column='MIOX', blank=True, null=True)  # Field name made lowercase.
    prdx4 = models.FloatField(db_column='PRDX4', blank=True, null=True)  # Field name made lowercase.
    gk = models.FloatField(db_column='GK', blank=True, null=True)  # Field name made lowercase.
    rgn = models.FloatField(db_column='RGN', blank=True, null=True)  # Field name made lowercase.
    timp1 = models.FloatField(db_column='TIMP1', blank=True, null=True)  # Field name made lowercase.
    clcn5 = models.FloatField(db_column='CLCN5', blank=True, null=True)  # Field name made lowercase.
    ar = models.FloatField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    foxo4 = models.FloatField(db_column='FOXO4', blank=True, null=True)  # Field name made lowercase.
    rps6ka6 = models.FloatField(db_column='RPS6KA6', blank=True, null=True)  # Field name made lowercase.
    nox1 = models.FloatField(db_column='NOX1', blank=True, null=True)  # Field name made lowercase.
    xiap = models.FloatField(db_column='XIAP', blank=True, null=True)  # Field name made lowercase.
    cd40lg = models.FloatField(db_column='CD40LG', blank=True, null=True)  # Field name made lowercase.
    l1cam = models.FloatField(db_column='L1CAM', blank=True, null=True)  # Field name made lowercase.
    irak1 = models.FloatField(db_column='IRAK1', blank=True, null=True)  # Field name made lowercase.
    g6pd = models.FloatField(db_column='G6PD', blank=True, null=True)  # Field name made lowercase.
    f8 = models.FloatField(db_column='F8', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diaco_tissue_adipose_subcutaneous'


class DiacoTissueAdiposeVisceralOm(models.Model):
    subjid = models.CharField(db_column='SUBJID', max_length=50, primary_key=True)  # Field name made lowercase.
    sampid = models.CharField(db_column='SAMPID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sesso = models.CharField(db_column='Sesso', max_length=1)  # Field name made lowercase.
    eta = models.CharField(db_column='Età', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errfi1 = models.FloatField(db_column='ERRFI1', blank=True, null=True)  # Field name made lowercase.
    mad2l2 = models.FloatField(db_column='MAD2L2', blank=True, null=True)  # Field name made lowercase.
    mthfr = models.FloatField(db_column='MTHFR', blank=True, null=True)  # Field name made lowercase.
    nppa = models.FloatField(db_column='NPPA', blank=True, null=True)  # Field name made lowercase.
    tnfrsf1b = models.FloatField(db_column='TNFRSF1B', blank=True, null=True)  # Field name made lowercase.
    pla2g2a = models.FloatField(db_column='PLA2G2A', blank=True, null=True)  # Field name made lowercase.
    alpl = models.FloatField(db_column='ALPL', blank=True, null=True)  # Field name made lowercase.
    hspg2 = models.FloatField(db_column='HSPG2', blank=True, null=True)  # Field name made lowercase.
    cnr2 = models.FloatField(db_column='CNR2', blank=True, null=True)  # Field name made lowercase.
    slc9a1 = models.FloatField(db_column='SLC9A1', blank=True, null=True)  # Field name made lowercase.
    col8a2 = models.FloatField(db_column='COL8A2', blank=True, null=True)  # Field name made lowercase.
    cap1 = models.FloatField(db_column='CAP1', blank=True, null=True)  # Field name made lowercase.
    slc2a1 = models.FloatField(db_column='SLC2A1', blank=True, null=True)  # Field name made lowercase.
    cyp2j2 = models.FloatField(db_column='CYP2J2', blank=True, null=True)  # Field name made lowercase.
    ddah1 = models.FloatField(db_column='DDAH1', blank=True, null=True)  # Field name made lowercase.
    cyr61 = models.FloatField(db_column='CYR61', blank=True, null=True)  # Field name made lowercase.
    ngf = models.FloatField(db_column='NGF', blank=True, null=True)  # Field name made lowercase.
    hmgcs2 = models.FloatField(db_column='HMGCS2', blank=True, null=True)  # Field name made lowercase.
    ctss = models.FloatField(db_column='CTSS', blank=True, null=True)  # Field name made lowercase.
    s100a12 = models.FloatField(db_column='S100A12', blank=True, null=True)  # Field name made lowercase.
    lmna = models.FloatField(db_column='LMNA', blank=True, null=True)  # Field name made lowercase.
    cd247 = models.FloatField(db_column='CD247', blank=True, null=True)  # Field name made lowercase.
    sele = models.FloatField(db_column='SELE', blank=True, null=True)  # Field name made lowercase.
    fmo3 = models.FloatField(db_column='FMO3', blank=True, null=True)  # Field name made lowercase.
    prdx6 = models.FloatField(db_column='PRDX6', blank=True, null=True)  # Field name made lowercase.
    glul = models.FloatField(db_column='GLUL', blank=True, null=True)  # Field name made lowercase.
    lamc1 = models.FloatField(db_column='LAMC1', blank=True, null=True)  # Field name made lowercase.
    ptgs2 = models.FloatField(db_column='PTGS2', blank=True, null=True)  # Field name made lowercase.
    chi3l1 = models.FloatField(db_column='CHI3L1', blank=True, null=True)  # Field name made lowercase.
    chit1 = models.FloatField(db_column='CHIT1', blank=True, null=True)  # Field name made lowercase.
    fmod = models.FloatField(db_column='FMOD', blank=True, null=True)  # Field name made lowercase.
    il10 = models.FloatField(db_column='IL10', blank=True, null=True)  # Field name made lowercase.
    pfkfb2 = models.FloatField(db_column='PFKFB2', blank=True, null=True)  # Field name made lowercase.
    cd34 = models.FloatField(db_column='CD34', blank=True, null=True)  # Field name made lowercase.
    cog2 = models.FloatField(db_column='COG2', blank=True, null=True)  # Field name made lowercase.
    nlrp3 = models.FloatField(db_column='NLRP3', blank=True, null=True)  # Field name made lowercase.
    rock2 = models.FloatField(db_column='ROCK2', blank=True, null=True)  # Field name made lowercase.
    apob = models.FloatField(db_column='APOB', blank=True, null=True)  # Field name made lowercase.
    pomc = models.FloatField(db_column='POMC', blank=True, null=True)  # Field name made lowercase.
    gckr = models.FloatField(db_column='GCKR', blank=True, null=True)  # Field name made lowercase.
    plekhh2 = models.FloatField(db_column='PLEKHH2', blank=True, null=True)  # Field name made lowercase.
    prkce = models.FloatField(db_column='PRKCE', blank=True, null=True)  # Field name made lowercase.
    pigf = models.FloatField(db_column='PIGF', blank=True, null=True)  # Field name made lowercase.
    msh2 = models.FloatField(db_column='MSH2', blank=True, null=True)  # Field name made lowercase.
    gfpt1 = models.FloatField(db_column='GFPT1', blank=True, null=True)  # Field name made lowercase.
    tacr1 = models.FloatField(db_column='TACR1', blank=True, null=True)  # Field name made lowercase.
    reg1a = models.FloatField(db_column='REG1A', blank=True, null=True)  # Field name made lowercase.
    eif2ak3 = models.FloatField(db_column='EIF2AK3', blank=True, null=True)  # Field name made lowercase.
    adra2b = models.FloatField(db_column='ADRA2B', blank=True, null=True)  # Field name made lowercase.
    il1b = models.FloatField(db_column='IL1B', blank=True, null=True)  # Field name made lowercase.
    proc = models.FloatField(db_column='PROC', blank=True, null=True)  # Field name made lowercase.
    polr2d = models.FloatField(db_column='POLR2D', blank=True, null=True)  # Field name made lowercase.
    zeb2 = models.FloatField(db_column='ZEB2', blank=True, null=True)  # Field name made lowercase.
    acvr1c = models.FloatField(db_column='ACVR1C', blank=True, null=True)  # Field name made lowercase.
    dpp4 = models.FloatField(db_column='DPP4', blank=True, null=True)  # Field name made lowercase.
    nfe2l2 = models.FloatField(db_column='NFE2L2', blank=True, null=True)  # Field name made lowercase.
    igfbp5 = models.FloatField(db_column='IGFBP5', blank=True, null=True)  # Field name made lowercase.
    ccl20 = models.FloatField(db_column='CCL20', blank=True, null=True)  # Field name made lowercase.
    hdac4 = models.FloatField(db_column='HDAC4', blank=True, null=True)  # Field name made lowercase.
    capn10 = models.FloatField(db_column='CAPN10', blank=True, null=True)  # Field name made lowercase.
    ghrl = models.FloatField(db_column='GHRL', blank=True, null=True)  # Field name made lowercase.
    pparg = models.FloatField(db_column='PPARG', blank=True, null=True)  # Field name made lowercase.
    raf1 = models.FloatField(db_column='RAF1', blank=True, null=True)  # Field name made lowercase.
    myd88 = models.FloatField(db_column='MYD88', blank=True, null=True)  # Field name made lowercase.
    cx3cr1 = models.FloatField(db_column='CX3CR1', blank=True, null=True)  # Field name made lowercase.
    cck = models.FloatField(db_column='CCK', blank=True, null=True)  # Field name made lowercase.
    exosc7 = models.FloatField(db_column='EXOSC7', blank=True, null=True)  # Field name made lowercase.
    ccr1 = models.FloatField(db_column='CCR1', blank=True, null=True)  # Field name made lowercase.
    ccr5 = models.FloatField(db_column='CCR5', blank=True, null=True)  # Field name made lowercase.
    gpx1 = models.FloatField(db_column='GPX1', blank=True, null=True)  # Field name made lowercase.
    rhoa = models.FloatField(db_column='RHOA', blank=True, null=True)  # Field name made lowercase.
    cish = models.FloatField(db_column='CISH', blank=True, null=True)  # Field name made lowercase.
    tkt = models.FloatField(db_column='TKT', blank=True, null=True)  # Field name made lowercase.
    appl1 = models.FloatField(db_column='APPL1', blank=True, null=True)  # Field name made lowercase.
    slmap = models.FloatField(db_column='SLMAP', blank=True, null=True)  # Field name made lowercase.
    col8a1 = models.FloatField(db_column='COL8A1', blank=True, null=True)  # Field name made lowercase.
    cd47 = models.FloatField(db_column='CD47', blank=True, null=True)  # Field name made lowercase.
    gap43 = models.FloatField(db_column='GAP43', blank=True, null=True)  # Field name made lowercase.
    cd80 = models.FloatField(db_column='CD80', blank=True, null=True)  # Field name made lowercase.
    rho = models.FloatField(db_column='RHO', blank=True, null=True)  # Field name made lowercase.
    trh = models.FloatField(db_column='TRH', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='TF', blank=True, null=True)  # Field name made lowercase.
    rbp1 = models.FloatField(db_column='RBP1', blank=True, null=True)  # Field name made lowercase.
    trpc1 = models.FloatField(db_column='TRPC1', blank=True, null=True)  # Field name made lowercase.
    agtr1 = models.FloatField(db_column='AGTR1', blank=True, null=True)  # Field name made lowercase.
    sucnr1 = models.FloatField(db_column='SUCNR1', blank=True, null=True)  # Field name made lowercase.
    p2ry1 = models.FloatField(db_column='P2RY1', blank=True, null=True)  # Field name made lowercase.
    mme = models.FloatField(db_column='MME', blank=True, null=True)  # Field name made lowercase.
    slc2a2 = models.FloatField(db_column='SLC2A2', blank=True, null=True)  # Field name made lowercase.
    pik3ca = models.FloatField(db_column='PIK3CA', blank=True, null=True)  # Field name made lowercase.
    parl = models.FloatField(db_column='PARL', blank=True, null=True)  # Field name made lowercase.
    ahsg = models.FloatField(db_column='AHSG', blank=True, null=True)  # Field name made lowercase.
    adipoq = models.FloatField(db_column='ADIPOQ', blank=True, null=True)  # Field name made lowercase.
    spon2 = models.FloatField(db_column='SPON2', blank=True, null=True)  # Field name made lowercase.
    wfs1 = models.FloatField(db_column='WFS1', blank=True, null=True)  # Field name made lowercase.
    cd38 = models.FloatField(db_column='CD38', blank=True, null=True)  # Field name made lowercase.
    prom1 = models.FloatField(db_column='PROM1', blank=True, null=True)  # Field name made lowercase.
    ppargc1a = models.FloatField(db_column='PPARGC1A', blank=True, null=True)  # Field name made lowercase.
    igfbp7 = models.FloatField(db_column='IGFBP7', blank=True, null=True)  # Field name made lowercase.
    cxcl5 = models.FloatField(db_column='CXCL5', blank=True, null=True)  # Field name made lowercase.
    cxcl9 = models.FloatField(db_column='CXCL9', blank=True, null=True)  # Field name made lowercase.
    cxcl10 = models.FloatField(db_column='CXCL10', blank=True, null=True)  # Field name made lowercase.
    cxcl11 = models.FloatField(db_column='CXCL11', blank=True, null=True)  # Field name made lowercase.
    hpse = models.FloatField(db_column='HPSE', blank=True, null=True)  # Field name made lowercase.
    spp1 = models.FloatField(db_column='SPP1', blank=True, null=True)  # Field name made lowercase.
    adh1b = models.FloatField(db_column='ADH1B', blank=True, null=True)  # Field name made lowercase.
    egf = models.FloatField(db_column='EGF', blank=True, null=True)  # Field name made lowercase.
    alpk1 = models.FloatField(db_column='ALPK1', blank=True, null=True)  # Field name made lowercase.
    fabp2 = models.FloatField(db_column='FABP2', blank=True, null=True)  # Field name made lowercase.
    pde5a = models.FloatField(db_column='PDE5A', blank=True, null=True)  # Field name made lowercase.
    setd7 = models.FloatField(db_column='SETD7', blank=True, null=True)  # Field name made lowercase.
    smad1 = models.FloatField(db_column='SMAD1', blank=True, null=True)  # Field name made lowercase.
    ednra = models.FloatField(db_column='EDNRA', blank=True, null=True)  # Field name made lowercase.
    nr3c2 = models.FloatField(db_column='NR3C2', blank=True, null=True)  # Field name made lowercase.
    tlr2 = models.FloatField(db_column='TLR2', blank=True, null=True)  # Field name made lowercase.
    npy5r = models.FloatField(db_column='NPY5R', blank=True, null=True)  # Field name made lowercase.
    fbxo8 = models.FloatField(db_column='FBXO8', blank=True, null=True)  # Field name made lowercase.
    vegfc = models.FloatField(db_column='VEGFC', blank=True, null=True)  # Field name made lowercase.
    acsl1 = models.FloatField(db_column='ACSL1', blank=True, null=True)  # Field name made lowercase.
    sorbs2 = models.FloatField(db_column='SORBS2', blank=True, null=True)  # Field name made lowercase.
    f11 = models.FloatField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    basp1 = models.FloatField(db_column='BASP1', blank=True, null=True)  # Field name made lowercase.
    ptger4 = models.FloatField(db_column='PTGER4', blank=True, null=True)  # Field name made lowercase.
    prkaa1 = models.FloatField(db_column='PRKAA1', blank=True, null=True)  # Field name made lowercase.
    ghr = models.FloatField(db_column='GHR', blank=True, null=True)  # Field name made lowercase.
    itga2 = models.FloatField(db_column='ITGA2', blank=True, null=True)  # Field name made lowercase.
    cdk7 = models.FloatField(db_column='CDK7', blank=True, null=True)  # Field name made lowercase.
    f2r = models.FloatField(db_column='F2R', blank=True, null=True)  # Field name made lowercase.
    erap2 = models.FloatField(db_column='ERAP2', blank=True, null=True)  # Field name made lowercase.
    apc = models.FloatField(db_column='APC', blank=True, null=True)  # Field name made lowercase.
    tnfaip8 = models.FloatField(db_column='TNFAIP8', blank=True, null=True)  # Field name made lowercase.
    vdac1 = models.FloatField(db_column='VDAC1', blank=True, null=True)  # Field name made lowercase.
    pdgfrb = models.FloatField(db_column='PDGFRB', blank=True, null=True)  # Field name made lowercase.
    cd74 = models.FloatField(db_column='CD74', blank=True, null=True)  # Field name made lowercase.
    sparc = models.FloatField(db_column='SPARC', blank=True, null=True)  # Field name made lowercase.
    ebf1 = models.FloatField(db_column='EBF1', blank=True, null=True)  # Field name made lowercase.
    gfpt2 = models.FloatField(db_column='GFPT2', blank=True, null=True)  # Field name made lowercase.
    rreb1 = models.FloatField(db_column='RREB1', blank=True, null=True)  # Field name made lowercase.
    edn1 = models.FloatField(db_column='EDN1', blank=True, null=True)  # Field name made lowercase.
    cdkal1 = models.FloatField(db_column='CDKAL1', blank=True, null=True)  # Field name made lowercase.
    hfe = models.FloatField(db_column='HFE', blank=True, null=True)  # Field name made lowercase.
    hla_a = models.FloatField(db_column='HLA-A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  # Field name made lowercase.
    tnf = models.FloatField(db_column='TNF', blank=True, null=True)  # Field name made lowercase.
    hspa1a = models.FloatField(db_column='HSPA1A', blank=True, null=True)  # Field name made lowercase.
    hspa1b = models.FloatField(db_column='HSPA1B', blank=True, null=True)  # Field name made lowercase.
    hla_dqa1 = models.FloatField(db_column='HLA-DQA1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mapk14 = models.FloatField(db_column='MAPK14', blank=True, null=True)  # Field name made lowercase.
    cdkn1a = models.FloatField(db_column='CDKN1A', blank=True, null=True)  # Field name made lowercase.
    glo1 = models.FloatField(db_column='GLO1', blank=True, null=True)  # Field name made lowercase.
    vegfa = models.FloatField(db_column='VEGFA', blank=True, null=True)  # Field name made lowercase.
    cd2ap = models.FloatField(db_column='CD2AP', blank=True, null=True)  # Field name made lowercase.
    cnr1 = models.FloatField(db_column='CNR1', blank=True, null=True)  # Field name made lowercase.
    enpp1 = models.FloatField(db_column='ENPP1', blank=True, null=True)  # Field name made lowercase.
    ctgf = models.FloatField(db_column='CTGF', blank=True, null=True)  # Field name made lowercase.
    rps12 = models.FloatField(db_column='RPS12', blank=True, null=True)  # Field name made lowercase.
    sgk1 = models.FloatField(db_column='SGK1', blank=True, null=True)  # Field name made lowercase.
    map3k5 = models.FloatField(db_column='MAP3K5', blank=True, null=True)  # Field name made lowercase.
    cited2 = models.FloatField(db_column='CITED2', blank=True, null=True)  # Field name made lowercase.
    utrn = models.FloatField(db_column='UTRN', blank=True, null=True)  # Field name made lowercase.
    mthfd1l = models.FloatField(db_column='MTHFD1L', blank=True, null=True)  # Field name made lowercase.
    vip = models.FloatField(db_column='VIP', blank=True, null=True)  # Field name made lowercase.
    sod2 = models.FloatField(db_column='SOD2', blank=True, null=True)  # Field name made lowercase.
    lpa = models.FloatField(db_column='LPA', blank=True, null=True)  # Field name made lowercase.
    thbs2 = models.FloatField(db_column='THBS2', blank=True, null=True)  # Field name made lowercase.
    pdgfa = models.FloatField(db_column='PDGFA', blank=True, null=True)  # Field name made lowercase.
    il6 = models.FloatField(db_column='IL6', blank=True, null=True)  # Field name made lowercase.
    npy = models.FloatField(db_column='NPY', blank=True, null=True)  # Field name made lowercase.
    jazf1 = models.FloatField(db_column='JAZF1', blank=True, null=True)  # Field name made lowercase.
    cpvl = models.FloatField(db_column='CPVL', blank=True, null=True)  # Field name made lowercase.
    aqp1 = models.FloatField(db_column='AQP1', blank=True, null=True)  # Field name made lowercase.
    elmo1 = models.FloatField(db_column='ELMO1', blank=True, null=True)  # Field name made lowercase.
    igfbp3 = models.FloatField(db_column='IGFBP3', blank=True, null=True)  # Field name made lowercase.
    egfr = models.FloatField(db_column='EGFR', blank=True, null=True)  # Field name made lowercase.
    eln = models.FloatField(db_column='ELN', blank=True, null=True)  # Field name made lowercase.
    ncf1 = models.FloatField(db_column='NCF1', blank=True, null=True)  # Field name made lowercase.
    hspb1 = models.FloatField(db_column='HSPB1', blank=True, null=True)  # Field name made lowercase.
    sema3a = models.FloatField(db_column='SEMA3A', blank=True, null=True)  # Field name made lowercase.
    pon3 = models.FloatField(db_column='PON3', blank=True, null=True)  # Field name made lowercase.
    pon2 = models.FloatField(db_column='PON2', blank=True, null=True)  # Field name made lowercase.
    nampt = models.FloatField(db_column='NAMPT', blank=True, null=True)  # Field name made lowercase.
    cav1 = models.FloatField(db_column='CAV1', blank=True, null=True)  # Field name made lowercase.
    lep = models.FloatField(db_column='LEP', blank=True, null=True)  # Field name made lowercase.
    akr1b1 = models.FloatField(db_column='AKR1B1', blank=True, null=True)  # Field name made lowercase.
    akr1b10 = models.FloatField(db_column='AKR1B10', blank=True, null=True)  # Field name made lowercase.
    pip = models.FloatField(db_column='PIP', blank=True, null=True)  # Field name made lowercase.
    rarres2 = models.FloatField(db_column='RARRES2', blank=True, null=True)  # Field name made lowercase.
    nos3 = models.FloatField(db_column='NOS3', blank=True, null=True)  # Field name made lowercase.
    angpt2 = models.FloatField(db_column='ANGPT2', blank=True, null=True)  # Field name made lowercase.
    defa1 = models.FloatField(db_column='DEFA1', blank=True, null=True)  # Field name made lowercase.
    lpl = models.FloatField(db_column='LPL', blank=True, null=True)  # Field name made lowercase.
    ebf2 = models.FloatField(db_column='EBF2', blank=True, null=True)  # Field name made lowercase.
    adrb3 = models.FloatField(db_column='ADRB3', blank=True, null=True)  # Field name made lowercase.
    eif4ebp1 = models.FloatField(db_column='EIF4EBP1', blank=True, null=True)  # Field name made lowercase.
    fgfr1 = models.FloatField(db_column='FGFR1', blank=True, null=True)  # Field name made lowercase.
    crh = models.FloatField(db_column='CRH', blank=True, null=True)  # Field name made lowercase.
    sgk3 = models.FloatField(db_column='SGK3', blank=True, null=True)  # Field name made lowercase.
    fabp5 = models.FloatField(db_column='FABP5', blank=True, null=True)  # Field name made lowercase.
    fabp4 = models.FloatField(db_column='FABP4', blank=True, null=True)  # Field name made lowercase.
    mmp16 = models.FloatField(db_column='MMP16', blank=True, null=True)  # Field name made lowercase.
    ncald = models.FloatField(db_column='NCALD', blank=True, null=True)  # Field name made lowercase.
    klf10 = models.FloatField(db_column='KLF10', blank=True, null=True)  # Field name made lowercase.
    enpp2 = models.FloatField(db_column='ENPP2', blank=True, null=True)  # Field name made lowercase.
    pvt1 = models.FloatField(db_column='PVT1', blank=True, null=True)  # Field name made lowercase.
    jak2 = models.FloatField(db_column='JAK2', blank=True, null=True)  # Field name made lowercase.
    psip1 = models.FloatField(db_column='PSIP1', blank=True, null=True)  # Field name made lowercase.
    plin2 = models.FloatField(db_column='PLIN2', blank=True, null=True)  # Field name made lowercase.
    rps6 = models.FloatField(db_column='RPS6', blank=True, null=True)  # Field name made lowercase.
    aldh1a1 = models.FloatField(db_column='ALDH1A1', blank=True, null=True)  # Field name made lowercase.
    frmd3 = models.FloatField(db_column='FRMD3', blank=True, null=True)  # Field name made lowercase.
    gas1 = models.FloatField(db_column='GAS1', blank=True, null=True)  # Field name made lowercase.
    baat = models.FloatField(db_column='BAAT', blank=True, null=True)  # Field name made lowercase.
    abca1 = models.FloatField(db_column='ABCA1', blank=True, null=True)  # Field name made lowercase.
    txn = models.FloatField(db_column='TXN', blank=True, null=True)  # Field name made lowercase.
    ambp = models.FloatField(db_column='AMBP', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    hspa5 = models.FloatField(db_column='HSPA5', blank=True, null=True)  # Field name made lowercase.
    angptl2 = models.FloatField(db_column='ANGPTL2', blank=True, null=True)  # Field name made lowercase.
    ptges = models.FloatField(db_column='PTGES', blank=True, null=True)  # Field name made lowercase.
    tsc1 = models.FloatField(db_column='TSC1', blank=True, null=True)  # Field name made lowercase.
    abo = models.FloatField(db_column='ABO', blank=True, null=True)  # Field name made lowercase.
    adamts13 = models.FloatField(db_column='ADAMTS13', blank=True, null=True)  # Field name made lowercase.
    ptgds = models.FloatField(db_column='PTGDS', blank=True, null=True)  # Field name made lowercase.
    klf6 = models.FloatField(db_column='KLF6', blank=True, null=True)  # Field name made lowercase.
    cdc123 = models.FloatField(db_column='CDC123', blank=True, null=True)  # Field name made lowercase.
    bambi = models.FloatField(db_column='BAMBI', blank=True, null=True)  # Field name made lowercase.
    cxcl12 = models.FloatField(db_column='CXCL12', blank=True, null=True)  # Field name made lowercase.
    mbl2 = models.FloatField(db_column='MBL2', blank=True, null=True)  # Field name made lowercase.
    tfam = models.FloatField(db_column='TFAM', blank=True, null=True)  # Field name made lowercase.
    sirt1 = models.FloatField(db_column='SIRT1', blank=True, null=True)  # Field name made lowercase.
    srgn = models.FloatField(db_column='SRGN', blank=True, null=True)  # Field name made lowercase.
    unc5b = models.FloatField(db_column='UNC5B', blank=True, null=True)  # Field name made lowercase.
    adk = models.FloatField(db_column='ADK', blank=True, null=True)  # Field name made lowercase.
    pten = models.FloatField(db_column='PTEN', blank=True, null=True)  # Field name made lowercase.
    rbp4 = models.FloatField(db_column='RBP4', blank=True, null=True)  # Field name made lowercase.
    cyp2c19 = models.FloatField(db_column='CYP2C19', blank=True, null=True)  # Field name made lowercase.
    entpd1 = models.FloatField(db_column='ENTPD1', blank=True, null=True)  # Field name made lowercase.
    tcf7l2 = models.FloatField(db_column='TCF7L2', blank=True, null=True)  # Field name made lowercase.
    bnip3 = models.FloatField(db_column='BNIP3', blank=True, null=True)  # Field name made lowercase.
    igf2 = models.FloatField(db_column='IGF2', blank=True, null=True)  # Field name made lowercase.
    ins = models.FloatField(db_column='INS', blank=True, null=True)  # Field name made lowercase.
    th = models.FloatField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    kcnq1 = models.FloatField(db_column='KCNQ1', blank=True, null=True)  # Field name made lowercase.
    hbg2 = models.FloatField(db_column='HBG2', blank=True, null=True)  # Field name made lowercase.
    smpd1 = models.FloatField(db_column='SMPD1', blank=True, null=True)  # Field name made lowercase.
    ilk = models.FloatField(db_column='ILK', blank=True, null=True)  # Field name made lowercase.
    adm = models.FloatField(db_column='ADM', blank=True, null=True)  # Field name made lowercase.
    pth = models.FloatField(db_column='PTH', blank=True, null=True)  # Field name made lowercase.
    nucb2 = models.FloatField(db_column='NUCB2', blank=True, null=True)  # Field name made lowercase.
    kcnj11 = models.FloatField(db_column='KCNJ11', blank=True, null=True)  # Field name made lowercase.
    saa1 = models.FloatField(db_column='SAA1', blank=True, null=True)  # Field name made lowercase.
    bdnf = models.FloatField(db_column='BDNF', blank=True, null=True)  # Field name made lowercase.
    wt1 = models.FloatField(db_column='WT1', blank=True, null=True)  # Field name made lowercase.
    cd59 = models.FloatField(db_column='CD59', blank=True, null=True)  # Field name made lowercase.
    pdhx = models.FloatField(db_column='PDHX', blank=True, null=True)  # Field name made lowercase.
    traf6 = models.FloatField(db_column='TRAF6', blank=True, null=True)  # Field name made lowercase.
    api5 = models.FloatField(db_column='API5', blank=True, null=True)  # Field name made lowercase.
    nr1h3 = models.FloatField(db_column='NR1H3', blank=True, null=True)  # Field name made lowercase.
    ndufs3 = models.FloatField(db_column='NDUFS3', blank=True, null=True)  # Field name made lowercase.
    folh1 = models.FloatField(db_column='FOLH1', blank=True, null=True)  # Field name made lowercase.
    aplnr = models.FloatField(db_column='APLNR', blank=True, null=True)  # Field name made lowercase.
    p2rx3 = models.FloatField(db_column='P2RX3', blank=True, null=True)  # Field name made lowercase.
    cntf = models.FloatField(db_column='CNTF', blank=True, null=True)  # Field name made lowercase.
    fads1 = models.FloatField(db_column='FADS1', blank=True, null=True)  # Field name made lowercase.
    fads2 = models.FloatField(db_column='FADS2', blank=True, null=True)  # Field name made lowercase.
    fkbp2 = models.FloatField(db_column='FKBP2', blank=True, null=True)  # Field name made lowercase.
    syvn1 = models.FloatField(db_column='SYVN1', blank=True, null=True)  # Field name made lowercase.
    pc = models.FloatField(db_column='PC', blank=True, null=True)  # Field name made lowercase.
    dhcr7 = models.FloatField(db_column='DHCR7', blank=True, null=True)  # Field name made lowercase.
    prcp = models.FloatField(db_column='PRCP', blank=True, null=True)  # Field name made lowercase.
    nox4 = models.FloatField(db_column='NOX4', blank=True, null=True)  # Field name made lowercase.
    pdgfd = models.FloatField(db_column='PDGFD', blank=True, null=True)  # Field name made lowercase.
    atm = models.FloatField(db_column='ATM', blank=True, null=True)  # Field name made lowercase.
    il18 = models.FloatField(db_column='IL18', blank=True, null=True)  # Field name made lowercase.
    apoa1 = models.FloatField(db_column='APOA1', blank=True, null=True)  # Field name made lowercase.
    hyou1 = models.FloatField(db_column='HYOU1', blank=True, null=True)  # Field name made lowercase.
    esam = models.FloatField(db_column='ESAM', blank=True, null=True)  # Field name made lowercase.
    fkbp4 = models.FloatField(db_column='FKBP4', blank=True, null=True)  # Field name made lowercase.
    fgf23 = models.FloatField(db_column='FGF23', blank=True, null=True)  # Field name made lowercase.
    ntf3 = models.FloatField(db_column='NTF3', blank=True, null=True)  # Field name made lowercase.
    vwf = models.FloatField(db_column='VWF', blank=True, null=True)  # Field name made lowercase.
    cd9 = models.FloatField(db_column='CD9', blank=True, null=True)  # Field name made lowercase.
    gapdh = models.FloatField(db_column='GAPDH', blank=True, null=True)  # Field name made lowercase.
    cd4 = models.FloatField(db_column='CD4', blank=True, null=True)  # Field name made lowercase.
    gnb3 = models.FloatField(db_column='GNB3', blank=True, null=True)  # Field name made lowercase.
    cd163 = models.FloatField(db_column='CD163', blank=True, null=True)  # Field name made lowercase.
    slc2a3 = models.FloatField(db_column='SLC2A3', blank=True, null=True)  # Field name made lowercase.
    cd69 = models.FloatField(db_column='CD69', blank=True, null=True)  # Field name made lowercase.
    irak4 = models.FloatField(db_column='IRAK4', blank=True, null=True)  # Field name made lowercase.
    vdr = models.FloatField(db_column='VDR', blank=True, null=True)  # Field name made lowercase.
    aqp5 = models.FloatField(db_column='AQP5', blank=True, null=True)  # Field name made lowercase.
    acvrl1 = models.FloatField(db_column='ACVRL1', blank=True, null=True)  # Field name made lowercase.
    nfe2 = models.FloatField(db_column='NFE2', blank=True, null=True)  # Field name made lowercase.
    cd63 = models.FloatField(db_column='CD63', blank=True, null=True)  # Field name made lowercase.
    erbb3 = models.FloatField(db_column='ERBB3', blank=True, null=True)  # Field name made lowercase.
    ddit3 = models.FloatField(db_column='DDIT3', blank=True, null=True)  # Field name made lowercase.
    ifng = models.FloatField(db_column='IFNG', blank=True, null=True)  # Field name made lowercase.
    nts = models.FloatField(db_column='NTS', blank=True, null=True)  # Field name made lowercase.
    igf1 = models.FloatField(db_column='IGF1', blank=True, null=True)  # Field name made lowercase.
    acacb = models.FloatField(db_column='ACACB', blank=True, null=True)  # Field name made lowercase.
    trpv4 = models.FloatField(db_column='TRPV4', blank=True, null=True)  # Field name made lowercase.
    atp2a2 = models.FloatField(db_column='ATP2A2', blank=True, null=True)  # Field name made lowercase.
    aldh2 = models.FloatField(db_column='ALDH2', blank=True, null=True)  # Field name made lowercase.
    nos1 = models.FloatField(db_column='NOS1', blank=True, null=True)  # Field name made lowercase.
    pebp1 = models.FloatField(db_column='PEBP1', blank=True, null=True)  # Field name made lowercase.
    psmd9 = models.FloatField(db_column='PSMD9', blank=True, null=True)  # Field name made lowercase.
    scarb1 = models.FloatField(db_column='SCARB1', blank=True, null=True)  # Field name made lowercase.
    p2rx2 = models.FloatField(db_column='P2RX2', blank=True, null=True)  # Field name made lowercase.
    alox5ap = models.FloatField(db_column='ALOX5AP', blank=True, null=True)  # Field name made lowercase.
    kl = models.FloatField(db_column='KL', blank=True, null=True)  # Field name made lowercase.
    postn = models.FloatField(db_column='POSTN', blank=True, null=True)  # Field name made lowercase.
    foxo1 = models.FloatField(db_column='FOXO1', blank=True, null=True)  # Field name made lowercase.
    htr2a = models.FloatField(db_column='HTR2A', blank=True, null=True)  # Field name made lowercase.
    gpc5 = models.FloatField(db_column='GPC5', blank=True, null=True)  # Field name made lowercase.
    irs2 = models.FloatField(db_column='IRS2', blank=True, null=True)  # Field name made lowercase.
    gas6 = models.FloatField(db_column='GAS6', blank=True, null=True)  # Field name made lowercase.
    ang = models.FloatField(db_column='ANG', blank=True, null=True)  # Field name made lowercase.
    mmp14 = models.FloatField(db_column='MMP14', blank=True, null=True)  # Field name made lowercase.
    ltb4r2 = models.FloatField(db_column='LTB4R2', blank=True, null=True)  # Field name made lowercase.
    nfkbia = models.FloatField(db_column='NFKBIA', blank=True, null=True)  # Field name made lowercase.
    bmp4 = models.FloatField(db_column='BMP4', blank=True, null=True)  # Field name made lowercase.
    rtn1 = models.FloatField(db_column='RTN1', blank=True, null=True)  # Field name made lowercase.
    pgf = models.FloatField(db_column='PGF', blank=True, null=True)  # Field name made lowercase.
    ngb = models.FloatField(db_column='NGB', blank=True, null=True)  # Field name made lowercase.
    ahsa1 = models.FloatField(db_column='AHSA1', blank=True, null=True)  # Field name made lowercase.
    bdkrb2 = models.FloatField(db_column='BDKRB2', blank=True, null=True)  # Field name made lowercase.
    bdkrb1 = models.FloatField(db_column='BDKRB1', blank=True, null=True)  # Field name made lowercase.
    akt1 = models.FloatField(db_column='AKT1', blank=True, null=True)  # Field name made lowercase.
    grem1 = models.FloatField(db_column='GREM1', blank=True, null=True)  # Field name made lowercase.
    thbs1 = models.FloatField(db_column='THBS1', blank=True, null=True)  # Field name made lowercase.
    pak6 = models.FloatField(db_column='PAK6', blank=True, null=True)  # Field name made lowercase.
    b2m = models.FloatField(db_column='B2M', blank=True, null=True)  # Field name made lowercase.
    myo5c = models.FloatField(db_column='MYO5C', blank=True, null=True)  # Field name made lowercase.
    onecut1 = models.FloatField(db_column='ONECUT1', blank=True, null=True)  # Field name made lowercase.
    adam10 = models.FloatField(db_column='ADAM10', blank=True, null=True)  # Field name made lowercase.
    ctsh = models.FloatField(db_column='CTSH', blank=True, null=True)  # Field name made lowercase.
    plin1 = models.FloatField(db_column='PLIN1', blank=True, null=True)  # Field name made lowercase.
    igf1r = models.FloatField(db_column='IGF1R', blank=True, null=True)  # Field name made lowercase.
    mrpl28 = models.FloatField(db_column='MRPL28', blank=True, null=True)  # Field name made lowercase.
    cacna1h = models.FloatField(db_column='CACNA1H', blank=True, null=True)  # Field name made lowercase.
    pdpk1 = models.FloatField(db_column='PDPK1', blank=True, null=True)  # Field name made lowercase.
    ercc4 = models.FloatField(db_column='ERCC4', blank=True, null=True)  # Field name made lowercase.
    smg1 = models.FloatField(db_column='SMG1', blank=True, null=True)  # Field name made lowercase.
    itgam = models.FloatField(db_column='ITGAM', blank=True, null=True)  # Field name made lowercase.
    fto = models.FloatField(db_column='FTO', blank=True, null=True)  # Field name made lowercase.
    mmp2 = models.FloatField(db_column='MMP2', blank=True, null=True)  # Field name made lowercase.
    slc12a3 = models.FloatField(db_column='SLC12A3', blank=True, null=True)  # Field name made lowercase.
    cetp = models.FloatField(db_column='CETP', blank=True, null=True)  # Field name made lowercase.
    cx3cl1 = models.FloatField(db_column='CX3CL1', blank=True, null=True)  # Field name made lowercase.
    cdh1 = models.FloatField(db_column='CDH1', blank=True, null=True)  # Field name made lowercase.
    nqo1 = models.FloatField(db_column='NQO1', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    znrf1 = models.FloatField(db_column='ZNRF1', blank=True, null=True)  # Field name made lowercase.
    cyba = models.FloatField(db_column='CYBA', blank=True, null=True)  # Field name made lowercase.
    tubb3 = models.FloatField(db_column='TUBB3', blank=True, null=True)  # Field name made lowercase.
    crk = models.FloatField(db_column='CRK', blank=True, null=True)  # Field name made lowercase.
    serpinf2 = models.FloatField(db_column='SERPINF2', blank=True, null=True)  # Field name made lowercase.
    serpinf1 = models.FloatField(db_column='SERPINF1', blank=True, null=True)  # Field name made lowercase.
    trpv3 = models.FloatField(db_column='TRPV3', blank=True, null=True)  # Field name made lowercase.
    cxcl16 = models.FloatField(db_column='CXCL16', blank=True, null=True)  # Field name made lowercase.
    slc2a4 = models.FloatField(db_column='SLC2A4', blank=True, null=True)  # Field name made lowercase.
    cd68 = models.FloatField(db_column='CD68', blank=True, null=True)  # Field name made lowercase.
    shbg = models.FloatField(db_column='SHBG', blank=True, null=True)  # Field name made lowercase.
    pmp22 = models.FloatField(db_column='PMP22', blank=True, null=True)  # Field name made lowercase.
    srebf1 = models.FloatField(db_column='SREBF1', blank=True, null=True)  # Field name made lowercase.
    mapk7 = models.FloatField(db_column='MAPK7', blank=True, null=True)  # Field name made lowercase.
    ccl2 = models.FloatField(db_column='CCL2', blank=True, null=True)  # Field name made lowercase.
    ccl5 = models.FloatField(db_column='CCL5', blank=True, null=True)  # Field name made lowercase.
    hnf1b = models.FloatField(db_column='HNF1B', blank=True, null=True)  # Field name made lowercase.
    erbb2 = models.FloatField(db_column='ERBB2', blank=True, null=True)  # Field name made lowercase.
    fkbp10 = models.FloatField(db_column='FKBP10', blank=True, null=True)  # Field name made lowercase.
    stat5a = models.FloatField(db_column='STAT5A', blank=True, null=True)  # Field name made lowercase.
    stat3 = models.FloatField(db_column='STAT3', blank=True, null=True)  # Field name made lowercase.
    naglu = models.FloatField(db_column='NAGLU', blank=True, null=True)  # Field name made lowercase.
    aoc2 = models.FloatField(db_column='AOC2', blank=True, null=True)  # Field name made lowercase.
    aoc3 = models.FloatField(db_column='AOC3', blank=True, null=True)  # Field name made lowercase.
    ppy = models.FloatField(db_column='PPY', blank=True, null=True)  # Field name made lowercase.
    sth = models.FloatField(db_column='STH', blank=True, null=True)  # Field name made lowercase.
    itgb3 = models.FloatField(db_column='ITGB3', blank=True, null=True)  # Field name made lowercase.
    gip = models.FloatField(db_column='GIP', blank=True, null=True)  # Field name made lowercase.
    mpo = models.FloatField(db_column='MPO', blank=True, null=True)  # Field name made lowercase.
    pecam1 = models.FloatField(db_column='PECAM1', blank=True, null=True)  # Field name made lowercase.
    sox9 = models.FloatField(db_column='SOX9', blank=True, null=True)  # Field name made lowercase.
    timp2 = models.FloatField(db_column='TIMP2', blank=True, null=True)  # Field name made lowercase.
    dcxr = models.FloatField(db_column='DCXR', blank=True, null=True)  # Field name made lowercase.
    fasn = models.FloatField(db_column='FASN', blank=True, null=True)  # Field name made lowercase.
    colec12 = models.FloatField(db_column='COLEC12', blank=True, null=True)  # Field name made lowercase.
    adcyap1 = models.FloatField(db_column='ADCYAP1', blank=True, null=True)  # Field name made lowercase.
    smad7 = models.FloatField(db_column='SMAD7', blank=True, null=True)  # Field name made lowercase.
    nedd4l = models.FloatField(db_column='NEDD4L', blank=True, null=True)  # Field name made lowercase.
    mc4r = models.FloatField(db_column='MC4R', blank=True, null=True)  # Field name made lowercase.
    bcl2 = models.FloatField(db_column='BCL2', blank=True, null=True)  # Field name made lowercase.
    cndp2 = models.FloatField(db_column='CNDP2', blank=True, null=True)  # Field name made lowercase.
    znf236 = models.FloatField(db_column='ZNF236', blank=True, null=True)  # Field name made lowercase.
    stk11 = models.FloatField(db_column='STK11', blank=True, null=True)  # Field name made lowercase.
    sirt6 = models.FloatField(db_column='SIRT6', blank=True, null=True)  # Field name made lowercase.
    uhrf1 = models.FloatField(db_column='UHRF1', blank=True, null=True)  # Field name made lowercase.
    timm44 = models.FloatField(db_column='TIMM44', blank=True, null=True)  # Field name made lowercase.
    angptl4 = models.FloatField(db_column='ANGPTL4', blank=True, null=True)  # Field name made lowercase.
    dnmt1 = models.FloatField(db_column='DNMT1', blank=True, null=True)  # Field name made lowercase.
    icam1 = models.FloatField(db_column='ICAM1', blank=True, null=True)  # Field name made lowercase.
    ldlr = models.FloatField(db_column='LDLR', blank=True, null=True)  # Field name made lowercase.
    epor = models.FloatField(db_column='EPOR', blank=True, null=True)  # Field name made lowercase.
    prdx2 = models.FloatField(db_column='PRDX2', blank=True, null=True)  # Field name made lowercase.
    ptger1 = models.FloatField(db_column='PTGER1', blank=True, null=True)  # Field name made lowercase.
    unc13a = models.FloatField(db_column='UNC13A', blank=True, null=True)  # Field name made lowercase.
    gdf15 = models.FloatField(db_column='GDF15', blank=True, null=True)  # Field name made lowercase.
    fkbp8 = models.FloatField(db_column='FKBP8', blank=True, null=True)  # Field name made lowercase.
    usf2 = models.FloatField(db_column='USF2', blank=True, null=True)  # Field name made lowercase.
    ffar1 = models.FloatField(db_column='FFAR1', blank=True, null=True)  # Field name made lowercase.
    ffar2 = models.FloatField(db_column='FFAR2', blank=True, null=True)  # Field name made lowercase.
    nphs1 = models.FloatField(db_column='NPHS1', blank=True, null=True)  # Field name made lowercase.
    tgfb1 = models.FloatField(db_column='TGFB1', blank=True, null=True)  # Field name made lowercase.
    xrcc1 = models.FloatField(db_column='XRCC1', blank=True, null=True)  # Field name made lowercase.
    ercc1 = models.FloatField(db_column='ERCC1', blank=True, null=True)  # Field name made lowercase.
    gipr = models.FloatField(db_column='GIPR', blank=True, null=True)  # Field name made lowercase.
    fgf21 = models.FloatField(db_column='FGF21', blank=True, null=True)  # Field name made lowercase.
    clec11a = models.FloatField(db_column='CLEC11A', blank=True, null=True)  # Field name made lowercase.
    fpr1 = models.FloatField(db_column='FPR1', blank=True, null=True)  # Field name made lowercase.
    trib3 = models.FloatField(db_column='TRIB3', blank=True, null=True)  # Field name made lowercase.
    bmp2 = models.FloatField(db_column='BMP2', blank=True, null=True)  # Field name made lowercase.
    thbd = models.FloatField(db_column='THBD', blank=True, null=True)  # Field name made lowercase.
    cst3 = models.FloatField(db_column='CST3', blank=True, null=True)  # Field name made lowercase.
    id1 = models.FloatField(db_column='ID1', blank=True, null=True)  # Field name made lowercase.
    src = models.FloatField(db_column='SRC', blank=True, null=True)  # Field name made lowercase.
    mafb = models.FloatField(db_column='MAFB', blank=True, null=True)  # Field name made lowercase.
    sgk2 = models.FloatField(db_column='SGK2', blank=True, null=True)  # Field name made lowercase.
    hnf4a = models.FloatField(db_column='HNF4A', blank=True, null=True)  # Field name made lowercase.
    pltp = models.FloatField(db_column='PLTP', blank=True, null=True)  # Field name made lowercase.
    mmp9 = models.FloatField(db_column='MMP9', blank=True, null=True)  # Field name made lowercase.
    cd40 = models.FloatField(db_column='CD40', blank=True, null=True)  # Field name made lowercase.
    ptpn1 = models.FloatField(db_column='PTPN1', blank=True, null=True)  # Field name made lowercase.
    cyp24a1 = models.FloatField(db_column='CYP24A1', blank=True, null=True)  # Field name made lowercase.
    rcan1 = models.FloatField(db_column='RCAN1', blank=True, null=True)  # Field name made lowercase.
    abcg1 = models.FloatField(db_column='ABCG1', blank=True, null=True)  # Field name made lowercase.
    prmt2 = models.FloatField(db_column='PRMT2', blank=True, null=True)  # Field name made lowercase.
    comt = models.FloatField(db_column='COMT', blank=True, null=True)  # Field name made lowercase.
    mapk1 = models.FloatField(db_column='MAPK1', blank=True, null=True)  # Field name made lowercase.
    mif = models.FloatField(db_column='MIF', blank=True, null=True)  # Field name made lowercase.
    ggt1 = models.FloatField(db_column='GGT1', blank=True, null=True)  # Field name made lowercase.
    xbp1 = models.FloatField(db_column='XBP1', blank=True, null=True)  # Field name made lowercase.
    osm = models.FloatField(db_column='OSM', blank=True, null=True)  # Field name made lowercase.
    limk2 = models.FloatField(db_column='LIMK2', blank=True, null=True)  # Field name made lowercase.
    sfi1 = models.FloatField(db_column='SFI1', blank=True, null=True)  # Field name made lowercase.
    timp3 = models.FloatField(db_column='TIMP3', blank=True, null=True)  # Field name made lowercase.
    hmox1 = models.FloatField(db_column='HMOX1', blank=True, null=True)  # Field name made lowercase.
    apol1 = models.FloatField(db_column='APOL1', blank=True, null=True)  # Field name made lowercase.
    myh9 = models.FloatField(db_column='MYH9', blank=True, null=True)  # Field name made lowercase.
    pdgfb = models.FloatField(db_column='PDGFB', blank=True, null=True)  # Field name made lowercase.
    atf4 = models.FloatField(db_column='ATF4', blank=True, null=True)  # Field name made lowercase.
    tspo = models.FloatField(db_column='TSPO', blank=True, null=True)  # Field name made lowercase.
    miox = models.FloatField(db_column='MIOX', blank=True, null=True)  # Field name made lowercase.
    prdx4 = models.FloatField(db_column='PRDX4', blank=True, null=True)  # Field name made lowercase.
    gk = models.FloatField(db_column='GK', blank=True, null=True)  # Field name made lowercase.
    rgn = models.FloatField(db_column='RGN', blank=True, null=True)  # Field name made lowercase.
    timp1 = models.FloatField(db_column='TIMP1', blank=True, null=True)  # Field name made lowercase.
    clcn5 = models.FloatField(db_column='CLCN5', blank=True, null=True)  # Field name made lowercase.
    ar = models.FloatField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    foxo4 = models.FloatField(db_column='FOXO4', blank=True, null=True)  # Field name made lowercase.
    rps6ka6 = models.FloatField(db_column='RPS6KA6', blank=True, null=True)  # Field name made lowercase.
    nox1 = models.FloatField(db_column='NOX1', blank=True, null=True)  # Field name made lowercase.
    xiap = models.FloatField(db_column='XIAP', blank=True, null=True)  # Field name made lowercase.
    cd40lg = models.FloatField(db_column='CD40LG', blank=True, null=True)  # Field name made lowercase.
    l1cam = models.FloatField(db_column='L1CAM', blank=True, null=True)  # Field name made lowercase.
    irak1 = models.FloatField(db_column='IRAK1', blank=True, null=True)  # Field name made lowercase.
    g6pd = models.FloatField(db_column='G6PD', blank=True, null=True)  # Field name made lowercase.
    f8 = models.FloatField(db_column='F8', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diaco_tissue_adipose_visceral_om'


class DiacoTissueAdrenalGland(models.Model):
    subjid = models.CharField(db_column='SUBJID', max_length=50, primary_key=True)  # Field name made lowercase.
    sampid = models.CharField(db_column='SAMPID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sesso = models.CharField(db_column='Sesso', max_length=1)  # Field name made lowercase.
    eta = models.CharField(db_column='Età', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errfi1 = models.FloatField(db_column='ERRFI1', blank=True, null=True)  # Field name made lowercase.
    mad2l2 = models.FloatField(db_column='MAD2L2', blank=True, null=True)  # Field name made lowercase.
    mthfr = models.FloatField(db_column='MTHFR', blank=True, null=True)  # Field name made lowercase.
    nppa = models.FloatField(db_column='NPPA', blank=True, null=True)  # Field name made lowercase.
    tnfrsf1b = models.FloatField(db_column='TNFRSF1B', blank=True, null=True)  # Field name made lowercase.
    pla2g2a = models.FloatField(db_column='PLA2G2A', blank=True, null=True)  # Field name made lowercase.
    alpl = models.FloatField(db_column='ALPL', blank=True, null=True)  # Field name made lowercase.
    hspg2 = models.FloatField(db_column='HSPG2', blank=True, null=True)  # Field name made lowercase.
    cnr2 = models.FloatField(db_column='CNR2', blank=True, null=True)  # Field name made lowercase.
    slc9a1 = models.FloatField(db_column='SLC9A1', blank=True, null=True)  # Field name made lowercase.
    col8a2 = models.FloatField(db_column='COL8A2', blank=True, null=True)  # Field name made lowercase.
    cap1 = models.FloatField(db_column='CAP1', blank=True, null=True)  # Field name made lowercase.
    slc2a1 = models.FloatField(db_column='SLC2A1', blank=True, null=True)  # Field name made lowercase.
    cyp2j2 = models.FloatField(db_column='CYP2J2', blank=True, null=True)  # Field name made lowercase.
    ddah1 = models.FloatField(db_column='DDAH1', blank=True, null=True)  # Field name made lowercase.
    cyr61 = models.FloatField(db_column='CYR61', blank=True, null=True)  # Field name made lowercase.
    ngf = models.FloatField(db_column='NGF', blank=True, null=True)  # Field name made lowercase.
    hmgcs2 = models.FloatField(db_column='HMGCS2', blank=True, null=True)  # Field name made lowercase.
    ctss = models.FloatField(db_column='CTSS', blank=True, null=True)  # Field name made lowercase.
    s100a12 = models.FloatField(db_column='S100A12', blank=True, null=True)  # Field name made lowercase.
    lmna = models.FloatField(db_column='LMNA', blank=True, null=True)  # Field name made lowercase.
    cd247 = models.FloatField(db_column='CD247', blank=True, null=True)  # Field name made lowercase.
    sele = models.FloatField(db_column='SELE', blank=True, null=True)  # Field name made lowercase.
    fmo3 = models.FloatField(db_column='FMO3', blank=True, null=True)  # Field name made lowercase.
    prdx6 = models.FloatField(db_column='PRDX6', blank=True, null=True)  # Field name made lowercase.
    glul = models.FloatField(db_column='GLUL', blank=True, null=True)  # Field name made lowercase.
    lamc1 = models.FloatField(db_column='LAMC1', blank=True, null=True)  # Field name made lowercase.
    ptgs2 = models.FloatField(db_column='PTGS2', blank=True, null=True)  # Field name made lowercase.
    chi3l1 = models.FloatField(db_column='CHI3L1', blank=True, null=True)  # Field name made lowercase.
    chit1 = models.FloatField(db_column='CHIT1', blank=True, null=True)  # Field name made lowercase.
    fmod = models.FloatField(db_column='FMOD', blank=True, null=True)  # Field name made lowercase.
    il10 = models.FloatField(db_column='IL10', blank=True, null=True)  # Field name made lowercase.
    pfkfb2 = models.FloatField(db_column='PFKFB2', blank=True, null=True)  # Field name made lowercase.
    cd34 = models.FloatField(db_column='CD34', blank=True, null=True)  # Field name made lowercase.
    cog2 = models.FloatField(db_column='COG2', blank=True, null=True)  # Field name made lowercase.
    nlrp3 = models.FloatField(db_column='NLRP3', blank=True, null=True)  # Field name made lowercase.
    rock2 = models.FloatField(db_column='ROCK2', blank=True, null=True)  # Field name made lowercase.
    apob = models.FloatField(db_column='APOB', blank=True, null=True)  # Field name made lowercase.
    pomc = models.FloatField(db_column='POMC', blank=True, null=True)  # Field name made lowercase.
    gckr = models.FloatField(db_column='GCKR', blank=True, null=True)  # Field name made lowercase.
    plekhh2 = models.FloatField(db_column='PLEKHH2', blank=True, null=True)  # Field name made lowercase.
    prkce = models.FloatField(db_column='PRKCE', blank=True, null=True)  # Field name made lowercase.
    pigf = models.FloatField(db_column='PIGF', blank=True, null=True)  # Field name made lowercase.
    msh2 = models.FloatField(db_column='MSH2', blank=True, null=True)  # Field name made lowercase.
    gfpt1 = models.FloatField(db_column='GFPT1', blank=True, null=True)  # Field name made lowercase.
    tacr1 = models.FloatField(db_column='TACR1', blank=True, null=True)  # Field name made lowercase.
    reg1a = models.FloatField(db_column='REG1A', blank=True, null=True)  # Field name made lowercase.
    eif2ak3 = models.FloatField(db_column='EIF2AK3', blank=True, null=True)  # Field name made lowercase.
    adra2b = models.FloatField(db_column='ADRA2B', blank=True, null=True)  # Field name made lowercase.
    il1b = models.FloatField(db_column='IL1B', blank=True, null=True)  # Field name made lowercase.
    proc = models.FloatField(db_column='PROC', blank=True, null=True)  # Field name made lowercase.
    polr2d = models.FloatField(db_column='POLR2D', blank=True, null=True)  # Field name made lowercase.
    zeb2 = models.FloatField(db_column='ZEB2', blank=True, null=True)  # Field name made lowercase.
    acvr1c = models.FloatField(db_column='ACVR1C', blank=True, null=True)  # Field name made lowercase.
    dpp4 = models.FloatField(db_column='DPP4', blank=True, null=True)  # Field name made lowercase.
    nfe2l2 = models.FloatField(db_column='NFE2L2', blank=True, null=True)  # Field name made lowercase.
    igfbp5 = models.FloatField(db_column='IGFBP5', blank=True, null=True)  # Field name made lowercase.
    ccl20 = models.FloatField(db_column='CCL20', blank=True, null=True)  # Field name made lowercase.
    hdac4 = models.FloatField(db_column='HDAC4', blank=True, null=True)  # Field name made lowercase.
    capn10 = models.FloatField(db_column='CAPN10', blank=True, null=True)  # Field name made lowercase.
    ghrl = models.FloatField(db_column='GHRL', blank=True, null=True)  # Field name made lowercase.
    pparg = models.FloatField(db_column='PPARG', blank=True, null=True)  # Field name made lowercase.
    raf1 = models.FloatField(db_column='RAF1', blank=True, null=True)  # Field name made lowercase.
    myd88 = models.FloatField(db_column='MYD88', blank=True, null=True)  # Field name made lowercase.
    cx3cr1 = models.FloatField(db_column='CX3CR1', blank=True, null=True)  # Field name made lowercase.
    cck = models.FloatField(db_column='CCK', blank=True, null=True)  # Field name made lowercase.
    exosc7 = models.FloatField(db_column='EXOSC7', blank=True, null=True)  # Field name made lowercase.
    ccr1 = models.FloatField(db_column='CCR1', blank=True, null=True)  # Field name made lowercase.
    ccr5 = models.FloatField(db_column='CCR5', blank=True, null=True)  # Field name made lowercase.
    gpx1 = models.FloatField(db_column='GPX1', blank=True, null=True)  # Field name made lowercase.
    rhoa = models.FloatField(db_column='RHOA', blank=True, null=True)  # Field name made lowercase.
    cish = models.FloatField(db_column='CISH', blank=True, null=True)  # Field name made lowercase.
    tkt = models.FloatField(db_column='TKT', blank=True, null=True)  # Field name made lowercase.
    appl1 = models.FloatField(db_column='APPL1', blank=True, null=True)  # Field name made lowercase.
    slmap = models.FloatField(db_column='SLMAP', blank=True, null=True)  # Field name made lowercase.
    col8a1 = models.FloatField(db_column='COL8A1', blank=True, null=True)  # Field name made lowercase.
    cd47 = models.FloatField(db_column='CD47', blank=True, null=True)  # Field name made lowercase.
    gap43 = models.FloatField(db_column='GAP43', blank=True, null=True)  # Field name made lowercase.
    cd80 = models.FloatField(db_column='CD80', blank=True, null=True)  # Field name made lowercase.
    rho = models.FloatField(db_column='RHO', blank=True, null=True)  # Field name made lowercase.
    trh = models.FloatField(db_column='TRH', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='TF', blank=True, null=True)  # Field name made lowercase.
    rbp1 = models.FloatField(db_column='RBP1', blank=True, null=True)  # Field name made lowercase.
    trpc1 = models.FloatField(db_column='TRPC1', blank=True, null=True)  # Field name made lowercase.
    agtr1 = models.FloatField(db_column='AGTR1', blank=True, null=True)  # Field name made lowercase.
    sucnr1 = models.FloatField(db_column='SUCNR1', blank=True, null=True)  # Field name made lowercase.
    p2ry1 = models.FloatField(db_column='P2RY1', blank=True, null=True)  # Field name made lowercase.
    mme = models.FloatField(db_column='MME', blank=True, null=True)  # Field name made lowercase.
    slc2a2 = models.FloatField(db_column='SLC2A2', blank=True, null=True)  # Field name made lowercase.
    pik3ca = models.FloatField(db_column='PIK3CA', blank=True, null=True)  # Field name made lowercase.
    parl = models.FloatField(db_column='PARL', blank=True, null=True)  # Field name made lowercase.
    ahsg = models.FloatField(db_column='AHSG', blank=True, null=True)  # Field name made lowercase.
    adipoq = models.FloatField(db_column='ADIPOQ', blank=True, null=True)  # Field name made lowercase.
    spon2 = models.FloatField(db_column='SPON2', blank=True, null=True)  # Field name made lowercase.
    wfs1 = models.FloatField(db_column='WFS1', blank=True, null=True)  # Field name made lowercase.
    cd38 = models.FloatField(db_column='CD38', blank=True, null=True)  # Field name made lowercase.
    prom1 = models.FloatField(db_column='PROM1', blank=True, null=True)  # Field name made lowercase.
    ppargc1a = models.FloatField(db_column='PPARGC1A', blank=True, null=True)  # Field name made lowercase.
    igfbp7 = models.FloatField(db_column='IGFBP7', blank=True, null=True)  # Field name made lowercase.
    cxcl5 = models.FloatField(db_column='CXCL5', blank=True, null=True)  # Field name made lowercase.
    cxcl9 = models.FloatField(db_column='CXCL9', blank=True, null=True)  # Field name made lowercase.
    cxcl10 = models.FloatField(db_column='CXCL10', blank=True, null=True)  # Field name made lowercase.
    cxcl11 = models.FloatField(db_column='CXCL11', blank=True, null=True)  # Field name made lowercase.
    hpse = models.FloatField(db_column='HPSE', blank=True, null=True)  # Field name made lowercase.
    spp1 = models.FloatField(db_column='SPP1', blank=True, null=True)  # Field name made lowercase.
    adh1b = models.FloatField(db_column='ADH1B', blank=True, null=True)  # Field name made lowercase.
    egf = models.FloatField(db_column='EGF', blank=True, null=True)  # Field name made lowercase.
    alpk1 = models.FloatField(db_column='ALPK1', blank=True, null=True)  # Field name made lowercase.
    fabp2 = models.FloatField(db_column='FABP2', blank=True, null=True)  # Field name made lowercase.
    pde5a = models.FloatField(db_column='PDE5A', blank=True, null=True)  # Field name made lowercase.
    setd7 = models.FloatField(db_column='SETD7', blank=True, null=True)  # Field name made lowercase.
    smad1 = models.FloatField(db_column='SMAD1', blank=True, null=True)  # Field name made lowercase.
    ednra = models.FloatField(db_column='EDNRA', blank=True, null=True)  # Field name made lowercase.
    nr3c2 = models.FloatField(db_column='NR3C2', blank=True, null=True)  # Field name made lowercase.
    tlr2 = models.FloatField(db_column='TLR2', blank=True, null=True)  # Field name made lowercase.
    npy5r = models.FloatField(db_column='NPY5R', blank=True, null=True)  # Field name made lowercase.
    fbxo8 = models.FloatField(db_column='FBXO8', blank=True, null=True)  # Field name made lowercase.
    vegfc = models.FloatField(db_column='VEGFC', blank=True, null=True)  # Field name made lowercase.
    acsl1 = models.FloatField(db_column='ACSL1', blank=True, null=True)  # Field name made lowercase.
    sorbs2 = models.FloatField(db_column='SORBS2', blank=True, null=True)  # Field name made lowercase.
    f11 = models.FloatField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    basp1 = models.FloatField(db_column='BASP1', blank=True, null=True)  # Field name made lowercase.
    ptger4 = models.FloatField(db_column='PTGER4', blank=True, null=True)  # Field name made lowercase.
    prkaa1 = models.FloatField(db_column='PRKAA1', blank=True, null=True)  # Field name made lowercase.
    ghr = models.FloatField(db_column='GHR', blank=True, null=True)  # Field name made lowercase.
    itga2 = models.FloatField(db_column='ITGA2', blank=True, null=True)  # Field name made lowercase.
    cdk7 = models.FloatField(db_column='CDK7', blank=True, null=True)  # Field name made lowercase.
    f2r = models.FloatField(db_column='F2R', blank=True, null=True)  # Field name made lowercase.
    erap2 = models.FloatField(db_column='ERAP2', blank=True, null=True)  # Field name made lowercase.
    apc = models.FloatField(db_column='APC', blank=True, null=True)  # Field name made lowercase.
    tnfaip8 = models.FloatField(db_column='TNFAIP8', blank=True, null=True)  # Field name made lowercase.
    vdac1 = models.FloatField(db_column='VDAC1', blank=True, null=True)  # Field name made lowercase.
    pdgfrb = models.FloatField(db_column='PDGFRB', blank=True, null=True)  # Field name made lowercase.
    cd74 = models.FloatField(db_column='CD74', blank=True, null=True)  # Field name made lowercase.
    sparc = models.FloatField(db_column='SPARC', blank=True, null=True)  # Field name made lowercase.
    ebf1 = models.FloatField(db_column='EBF1', blank=True, null=True)  # Field name made lowercase.
    gfpt2 = models.FloatField(db_column='GFPT2', blank=True, null=True)  # Field name made lowercase.
    rreb1 = models.FloatField(db_column='RREB1', blank=True, null=True)  # Field name made lowercase.
    edn1 = models.FloatField(db_column='EDN1', blank=True, null=True)  # Field name made lowercase.
    cdkal1 = models.FloatField(db_column='CDKAL1', blank=True, null=True)  # Field name made lowercase.
    hfe = models.FloatField(db_column='HFE', blank=True, null=True)  # Field name made lowercase.
    hla_a = models.FloatField(db_column='HLA-A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  # Field name made lowercase.
    tnf = models.FloatField(db_column='TNF', blank=True, null=True)  # Field name made lowercase.
    hspa1a = models.FloatField(db_column='HSPA1A', blank=True, null=True)  # Field name made lowercase.
    hspa1b = models.FloatField(db_column='HSPA1B', blank=True, null=True)  # Field name made lowercase.
    hla_dqa1 = models.FloatField(db_column='HLA-DQA1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mapk14 = models.FloatField(db_column='MAPK14', blank=True, null=True)  # Field name made lowercase.
    cdkn1a = models.FloatField(db_column='CDKN1A', blank=True, null=True)  # Field name made lowercase.
    glo1 = models.FloatField(db_column='GLO1', blank=True, null=True)  # Field name made lowercase.
    vegfa = models.FloatField(db_column='VEGFA', blank=True, null=True)  # Field name made lowercase.
    cd2ap = models.FloatField(db_column='CD2AP', blank=True, null=True)  # Field name made lowercase.
    cnr1 = models.FloatField(db_column='CNR1', blank=True, null=True)  # Field name made lowercase.
    enpp1 = models.FloatField(db_column='ENPP1', blank=True, null=True)  # Field name made lowercase.
    ctgf = models.FloatField(db_column='CTGF', blank=True, null=True)  # Field name made lowercase.
    rps12 = models.FloatField(db_column='RPS12', blank=True, null=True)  # Field name made lowercase.
    sgk1 = models.FloatField(db_column='SGK1', blank=True, null=True)  # Field name made lowercase.
    map3k5 = models.FloatField(db_column='MAP3K5', blank=True, null=True)  # Field name made lowercase.
    cited2 = models.FloatField(db_column='CITED2', blank=True, null=True)  # Field name made lowercase.
    utrn = models.FloatField(db_column='UTRN', blank=True, null=True)  # Field name made lowercase.
    mthfd1l = models.FloatField(db_column='MTHFD1L', blank=True, null=True)  # Field name made lowercase.
    vip = models.FloatField(db_column='VIP', blank=True, null=True)  # Field name made lowercase.
    sod2 = models.FloatField(db_column='SOD2', blank=True, null=True)  # Field name made lowercase.
    lpa = models.FloatField(db_column='LPA', blank=True, null=True)  # Field name made lowercase.
    thbs2 = models.FloatField(db_column='THBS2', blank=True, null=True)  # Field name made lowercase.
    pdgfa = models.FloatField(db_column='PDGFA', blank=True, null=True)  # Field name made lowercase.
    il6 = models.FloatField(db_column='IL6', blank=True, null=True)  # Field name made lowercase.
    npy = models.FloatField(db_column='NPY', blank=True, null=True)  # Field name made lowercase.
    jazf1 = models.FloatField(db_column='JAZF1', blank=True, null=True)  # Field name made lowercase.
    cpvl = models.FloatField(db_column='CPVL', blank=True, null=True)  # Field name made lowercase.
    aqp1 = models.FloatField(db_column='AQP1', blank=True, null=True)  # Field name made lowercase.
    elmo1 = models.FloatField(db_column='ELMO1', blank=True, null=True)  # Field name made lowercase.
    igfbp3 = models.FloatField(db_column='IGFBP3', blank=True, null=True)  # Field name made lowercase.
    egfr = models.FloatField(db_column='EGFR', blank=True, null=True)  # Field name made lowercase.
    eln = models.FloatField(db_column='ELN', blank=True, null=True)  # Field name made lowercase.
    ncf1 = models.FloatField(db_column='NCF1', blank=True, null=True)  # Field name made lowercase.
    hspb1 = models.FloatField(db_column='HSPB1', blank=True, null=True)  # Field name made lowercase.
    sema3a = models.FloatField(db_column='SEMA3A', blank=True, null=True)  # Field name made lowercase.
    pon3 = models.FloatField(db_column='PON3', blank=True, null=True)  # Field name made lowercase.
    pon2 = models.FloatField(db_column='PON2', blank=True, null=True)  # Field name made lowercase.
    nampt = models.FloatField(db_column='NAMPT', blank=True, null=True)  # Field name made lowercase.
    cav1 = models.FloatField(db_column='CAV1', blank=True, null=True)  # Field name made lowercase.
    lep = models.FloatField(db_column='LEP', blank=True, null=True)  # Field name made lowercase.
    akr1b1 = models.FloatField(db_column='AKR1B1', blank=True, null=True)  # Field name made lowercase.
    akr1b10 = models.FloatField(db_column='AKR1B10', blank=True, null=True)  # Field name made lowercase.
    pip = models.FloatField(db_column='PIP', blank=True, null=True)  # Field name made lowercase.
    rarres2 = models.FloatField(db_column='RARRES2', blank=True, null=True)  # Field name made lowercase.
    nos3 = models.FloatField(db_column='NOS3', blank=True, null=True)  # Field name made lowercase.
    angpt2 = models.FloatField(db_column='ANGPT2', blank=True, null=True)  # Field name made lowercase.
    defa1 = models.FloatField(db_column='DEFA1', blank=True, null=True)  # Field name made lowercase.
    lpl = models.FloatField(db_column='LPL', blank=True, null=True)  # Field name made lowercase.
    ebf2 = models.FloatField(db_column='EBF2', blank=True, null=True)  # Field name made lowercase.
    adrb3 = models.FloatField(db_column='ADRB3', blank=True, null=True)  # Field name made lowercase.
    eif4ebp1 = models.FloatField(db_column='EIF4EBP1', blank=True, null=True)  # Field name made lowercase.
    fgfr1 = models.FloatField(db_column='FGFR1', blank=True, null=True)  # Field name made lowercase.
    crh = models.FloatField(db_column='CRH', blank=True, null=True)  # Field name made lowercase.
    sgk3 = models.FloatField(db_column='SGK3', blank=True, null=True)  # Field name made lowercase.
    fabp5 = models.FloatField(db_column='FABP5', blank=True, null=True)  # Field name made lowercase.
    fabp4 = models.FloatField(db_column='FABP4', blank=True, null=True)  # Field name made lowercase.
    mmp16 = models.FloatField(db_column='MMP16', blank=True, null=True)  # Field name made lowercase.
    ncald = models.FloatField(db_column='NCALD', blank=True, null=True)  # Field name made lowercase.
    klf10 = models.FloatField(db_column='KLF10', blank=True, null=True)  # Field name made lowercase.
    enpp2 = models.FloatField(db_column='ENPP2', blank=True, null=True)  # Field name made lowercase.
    pvt1 = models.FloatField(db_column='PVT1', blank=True, null=True)  # Field name made lowercase.
    jak2 = models.FloatField(db_column='JAK2', blank=True, null=True)  # Field name made lowercase.
    psip1 = models.FloatField(db_column='PSIP1', blank=True, null=True)  # Field name made lowercase.
    plin2 = models.FloatField(db_column='PLIN2', blank=True, null=True)  # Field name made lowercase.
    rps6 = models.FloatField(db_column='RPS6', blank=True, null=True)  # Field name made lowercase.
    aldh1a1 = models.FloatField(db_column='ALDH1A1', blank=True, null=True)  # Field name made lowercase.
    frmd3 = models.FloatField(db_column='FRMD3', blank=True, null=True)  # Field name made lowercase.
    gas1 = models.FloatField(db_column='GAS1', blank=True, null=True)  # Field name made lowercase.
    baat = models.FloatField(db_column='BAAT', blank=True, null=True)  # Field name made lowercase.
    abca1 = models.FloatField(db_column='ABCA1', blank=True, null=True)  # Field name made lowercase.
    txn = models.FloatField(db_column='TXN', blank=True, null=True)  # Field name made lowercase.
    ambp = models.FloatField(db_column='AMBP', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    hspa5 = models.FloatField(db_column='HSPA5', blank=True, null=True)  # Field name made lowercase.
    angptl2 = models.FloatField(db_column='ANGPTL2', blank=True, null=True)  # Field name made lowercase.
    ptges = models.FloatField(db_column='PTGES', blank=True, null=True)  # Field name made lowercase.
    tsc1 = models.FloatField(db_column='TSC1', blank=True, null=True)  # Field name made lowercase.
    abo = models.FloatField(db_column='ABO', blank=True, null=True)  # Field name made lowercase.
    adamts13 = models.FloatField(db_column='ADAMTS13', blank=True, null=True)  # Field name made lowercase.
    ptgds = models.FloatField(db_column='PTGDS', blank=True, null=True)  # Field name made lowercase.
    klf6 = models.FloatField(db_column='KLF6', blank=True, null=True)  # Field name made lowercase.
    cdc123 = models.FloatField(db_column='CDC123', blank=True, null=True)  # Field name made lowercase.
    bambi = models.FloatField(db_column='BAMBI', blank=True, null=True)  # Field name made lowercase.
    cxcl12 = models.FloatField(db_column='CXCL12', blank=True, null=True)  # Field name made lowercase.
    mbl2 = models.FloatField(db_column='MBL2', blank=True, null=True)  # Field name made lowercase.
    tfam = models.FloatField(db_column='TFAM', blank=True, null=True)  # Field name made lowercase.
    sirt1 = models.FloatField(db_column='SIRT1', blank=True, null=True)  # Field name made lowercase.
    srgn = models.FloatField(db_column='SRGN', blank=True, null=True)  # Field name made lowercase.
    unc5b = models.FloatField(db_column='UNC5B', blank=True, null=True)  # Field name made lowercase.
    adk = models.FloatField(db_column='ADK', blank=True, null=True)  # Field name made lowercase.
    pten = models.FloatField(db_column='PTEN', blank=True, null=True)  # Field name made lowercase.
    rbp4 = models.FloatField(db_column='RBP4', blank=True, null=True)  # Field name made lowercase.
    cyp2c19 = models.FloatField(db_column='CYP2C19', blank=True, null=True)  # Field name made lowercase.
    entpd1 = models.FloatField(db_column='ENTPD1', blank=True, null=True)  # Field name made lowercase.
    tcf7l2 = models.FloatField(db_column='TCF7L2', blank=True, null=True)  # Field name made lowercase.
    bnip3 = models.FloatField(db_column='BNIP3', blank=True, null=True)  # Field name made lowercase.
    igf2 = models.FloatField(db_column='IGF2', blank=True, null=True)  # Field name made lowercase.
    ins = models.FloatField(db_column='INS', blank=True, null=True)  # Field name made lowercase.
    th = models.FloatField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    kcnq1 = models.FloatField(db_column='KCNQ1', blank=True, null=True)  # Field name made lowercase.
    hbg2 = models.FloatField(db_column='HBG2', blank=True, null=True)  # Field name made lowercase.
    smpd1 = models.FloatField(db_column='SMPD1', blank=True, null=True)  # Field name made lowercase.
    ilk = models.FloatField(db_column='ILK', blank=True, null=True)  # Field name made lowercase.
    adm = models.FloatField(db_column='ADM', blank=True, null=True)  # Field name made lowercase.
    pth = models.FloatField(db_column='PTH', blank=True, null=True)  # Field name made lowercase.
    nucb2 = models.FloatField(db_column='NUCB2', blank=True, null=True)  # Field name made lowercase.
    kcnj11 = models.FloatField(db_column='KCNJ11', blank=True, null=True)  # Field name made lowercase.
    saa1 = models.FloatField(db_column='SAA1', blank=True, null=True)  # Field name made lowercase.
    bdnf = models.FloatField(db_column='BDNF', blank=True, null=True)  # Field name made lowercase.
    wt1 = models.FloatField(db_column='WT1', blank=True, null=True)  # Field name made lowercase.
    cd59 = models.FloatField(db_column='CD59', blank=True, null=True)  # Field name made lowercase.
    pdhx = models.FloatField(db_column='PDHX', blank=True, null=True)  # Field name made lowercase.
    traf6 = models.FloatField(db_column='TRAF6', blank=True, null=True)  # Field name made lowercase.
    api5 = models.FloatField(db_column='API5', blank=True, null=True)  # Field name made lowercase.
    nr1h3 = models.FloatField(db_column='NR1H3', blank=True, null=True)  # Field name made lowercase.
    ndufs3 = models.FloatField(db_column='NDUFS3', blank=True, null=True)  # Field name made lowercase.
    folh1 = models.FloatField(db_column='FOLH1', blank=True, null=True)  # Field name made lowercase.
    aplnr = models.FloatField(db_column='APLNR', blank=True, null=True)  # Field name made lowercase.
    p2rx3 = models.FloatField(db_column='P2RX3', blank=True, null=True)  # Field name made lowercase.
    cntf = models.FloatField(db_column='CNTF', blank=True, null=True)  # Field name made lowercase.
    fads1 = models.FloatField(db_column='FADS1', blank=True, null=True)  # Field name made lowercase.
    fads2 = models.FloatField(db_column='FADS2', blank=True, null=True)  # Field name made lowercase.
    fkbp2 = models.FloatField(db_column='FKBP2', blank=True, null=True)  # Field name made lowercase.
    syvn1 = models.FloatField(db_column='SYVN1', blank=True, null=True)  # Field name made lowercase.
    pc = models.FloatField(db_column='PC', blank=True, null=True)  # Field name made lowercase.
    dhcr7 = models.FloatField(db_column='DHCR7', blank=True, null=True)  # Field name made lowercase.
    prcp = models.FloatField(db_column='PRCP', blank=True, null=True)  # Field name made lowercase.
    nox4 = models.FloatField(db_column='NOX4', blank=True, null=True)  # Field name made lowercase.
    pdgfd = models.FloatField(db_column='PDGFD', blank=True, null=True)  # Field name made lowercase.
    atm = models.FloatField(db_column='ATM', blank=True, null=True)  # Field name made lowercase.
    il18 = models.FloatField(db_column='IL18', blank=True, null=True)  # Field name made lowercase.
    apoa1 = models.FloatField(db_column='APOA1', blank=True, null=True)  # Field name made lowercase.
    hyou1 = models.FloatField(db_column='HYOU1', blank=True, null=True)  # Field name made lowercase.
    esam = models.FloatField(db_column='ESAM', blank=True, null=True)  # Field name made lowercase.
    fkbp4 = models.FloatField(db_column='FKBP4', blank=True, null=True)  # Field name made lowercase.
    fgf23 = models.FloatField(db_column='FGF23', blank=True, null=True)  # Field name made lowercase.
    ntf3 = models.FloatField(db_column='NTF3', blank=True, null=True)  # Field name made lowercase.
    vwf = models.FloatField(db_column='VWF', blank=True, null=True)  # Field name made lowercase.
    cd9 = models.FloatField(db_column='CD9', blank=True, null=True)  # Field name made lowercase.
    gapdh = models.FloatField(db_column='GAPDH', blank=True, null=True)  # Field name made lowercase.
    cd4 = models.FloatField(db_column='CD4', blank=True, null=True)  # Field name made lowercase.
    gnb3 = models.FloatField(db_column='GNB3', blank=True, null=True)  # Field name made lowercase.
    cd163 = models.FloatField(db_column='CD163', blank=True, null=True)  # Field name made lowercase.
    slc2a3 = models.FloatField(db_column='SLC2A3', blank=True, null=True)  # Field name made lowercase.
    cd69 = models.FloatField(db_column='CD69', blank=True, null=True)  # Field name made lowercase.
    irak4 = models.FloatField(db_column='IRAK4', blank=True, null=True)  # Field name made lowercase.
    vdr = models.FloatField(db_column='VDR', blank=True, null=True)  # Field name made lowercase.
    aqp5 = models.FloatField(db_column='AQP5', blank=True, null=True)  # Field name made lowercase.
    acvrl1 = models.FloatField(db_column='ACVRL1', blank=True, null=True)  # Field name made lowercase.
    nfe2 = models.FloatField(db_column='NFE2', blank=True, null=True)  # Field name made lowercase.
    cd63 = models.FloatField(db_column='CD63', blank=True, null=True)  # Field name made lowercase.
    erbb3 = models.FloatField(db_column='ERBB3', blank=True, null=True)  # Field name made lowercase.
    ddit3 = models.FloatField(db_column='DDIT3', blank=True, null=True)  # Field name made lowercase.
    ifng = models.FloatField(db_column='IFNG', blank=True, null=True)  # Field name made lowercase.
    nts = models.FloatField(db_column='NTS', blank=True, null=True)  # Field name made lowercase.
    igf1 = models.FloatField(db_column='IGF1', blank=True, null=True)  # Field name made lowercase.
    acacb = models.FloatField(db_column='ACACB', blank=True, null=True)  # Field name made lowercase.
    trpv4 = models.FloatField(db_column='TRPV4', blank=True, null=True)  # Field name made lowercase.
    atp2a2 = models.FloatField(db_column='ATP2A2', blank=True, null=True)  # Field name made lowercase.
    aldh2 = models.FloatField(db_column='ALDH2', blank=True, null=True)  # Field name made lowercase.
    nos1 = models.FloatField(db_column='NOS1', blank=True, null=True)  # Field name made lowercase.
    pebp1 = models.FloatField(db_column='PEBP1', blank=True, null=True)  # Field name made lowercase.
    psmd9 = models.FloatField(db_column='PSMD9', blank=True, null=True)  # Field name made lowercase.
    scarb1 = models.FloatField(db_column='SCARB1', blank=True, null=True)  # Field name made lowercase.
    p2rx2 = models.FloatField(db_column='P2RX2', blank=True, null=True)  # Field name made lowercase.
    alox5ap = models.FloatField(db_column='ALOX5AP', blank=True, null=True)  # Field name made lowercase.
    kl = models.FloatField(db_column='KL', blank=True, null=True)  # Field name made lowercase.
    postn = models.FloatField(db_column='POSTN', blank=True, null=True)  # Field name made lowercase.
    foxo1 = models.FloatField(db_column='FOXO1', blank=True, null=True)  # Field name made lowercase.
    htr2a = models.FloatField(db_column='HTR2A', blank=True, null=True)  # Field name made lowercase.
    gpc5 = models.FloatField(db_column='GPC5', blank=True, null=True)  # Field name made lowercase.
    irs2 = models.FloatField(db_column='IRS2', blank=True, null=True)  # Field name made lowercase.
    gas6 = models.FloatField(db_column='GAS6', blank=True, null=True)  # Field name made lowercase.
    ang = models.FloatField(db_column='ANG', blank=True, null=True)  # Field name made lowercase.
    mmp14 = models.FloatField(db_column='MMP14', blank=True, null=True)  # Field name made lowercase.
    ltb4r2 = models.FloatField(db_column='LTB4R2', blank=True, null=True)  # Field name made lowercase.
    nfkbia = models.FloatField(db_column='NFKBIA', blank=True, null=True)  # Field name made lowercase.
    bmp4 = models.FloatField(db_column='BMP4', blank=True, null=True)  # Field name made lowercase.
    rtn1 = models.FloatField(db_column='RTN1', blank=True, null=True)  # Field name made lowercase.
    pgf = models.FloatField(db_column='PGF', blank=True, null=True)  # Field name made lowercase.
    ngb = models.FloatField(db_column='NGB', blank=True, null=True)  # Field name made lowercase.
    ahsa1 = models.FloatField(db_column='AHSA1', blank=True, null=True)  # Field name made lowercase.
    bdkrb2 = models.FloatField(db_column='BDKRB2', blank=True, null=True)  # Field name made lowercase.
    bdkrb1 = models.FloatField(db_column='BDKRB1', blank=True, null=True)  # Field name made lowercase.
    akt1 = models.FloatField(db_column='AKT1', blank=True, null=True)  # Field name made lowercase.
    grem1 = models.FloatField(db_column='GREM1', blank=True, null=True)  # Field name made lowercase.
    thbs1 = models.FloatField(db_column='THBS1', blank=True, null=True)  # Field name made lowercase.
    pak6 = models.FloatField(db_column='PAK6', blank=True, null=True)  # Field name made lowercase.
    b2m = models.FloatField(db_column='B2M', blank=True, null=True)  # Field name made lowercase.
    myo5c = models.FloatField(db_column='MYO5C', blank=True, null=True)  # Field name made lowercase.
    onecut1 = models.FloatField(db_column='ONECUT1', blank=True, null=True)  # Field name made lowercase.
    adam10 = models.FloatField(db_column='ADAM10', blank=True, null=True)  # Field name made lowercase.
    ctsh = models.FloatField(db_column='CTSH', blank=True, null=True)  # Field name made lowercase.
    plin1 = models.FloatField(db_column='PLIN1', blank=True, null=True)  # Field name made lowercase.
    igf1r = models.FloatField(db_column='IGF1R', blank=True, null=True)  # Field name made lowercase.
    mrpl28 = models.FloatField(db_column='MRPL28', blank=True, null=True)  # Field name made lowercase.
    cacna1h = models.FloatField(db_column='CACNA1H', blank=True, null=True)  # Field name made lowercase.
    pdpk1 = models.FloatField(db_column='PDPK1', blank=True, null=True)  # Field name made lowercase.
    ercc4 = models.FloatField(db_column='ERCC4', blank=True, null=True)  # Field name made lowercase.
    smg1 = models.FloatField(db_column='SMG1', blank=True, null=True)  # Field name made lowercase.
    itgam = models.FloatField(db_column='ITGAM', blank=True, null=True)  # Field name made lowercase.
    fto = models.FloatField(db_column='FTO', blank=True, null=True)  # Field name made lowercase.
    mmp2 = models.FloatField(db_column='MMP2', blank=True, null=True)  # Field name made lowercase.
    slc12a3 = models.FloatField(db_column='SLC12A3', blank=True, null=True)  # Field name made lowercase.
    cetp = models.FloatField(db_column='CETP', blank=True, null=True)  # Field name made lowercase.
    cx3cl1 = models.FloatField(db_column='CX3CL1', blank=True, null=True)  # Field name made lowercase.
    cdh1 = models.FloatField(db_column='CDH1', blank=True, null=True)  # Field name made lowercase.
    nqo1 = models.FloatField(db_column='NQO1', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    znrf1 = models.FloatField(db_column='ZNRF1', blank=True, null=True)  # Field name made lowercase.
    cyba = models.FloatField(db_column='CYBA', blank=True, null=True)  # Field name made lowercase.
    tubb3 = models.FloatField(db_column='TUBB3', blank=True, null=True)  # Field name made lowercase.
    crk = models.FloatField(db_column='CRK', blank=True, null=True)  # Field name made lowercase.
    serpinf2 = models.FloatField(db_column='SERPINF2', blank=True, null=True)  # Field name made lowercase.
    serpinf1 = models.FloatField(db_column='SERPINF1', blank=True, null=True)  # Field name made lowercase.
    trpv3 = models.FloatField(db_column='TRPV3', blank=True, null=True)  # Field name made lowercase.
    cxcl16 = models.FloatField(db_column='CXCL16', blank=True, null=True)  # Field name made lowercase.
    slc2a4 = models.FloatField(db_column='SLC2A4', blank=True, null=True)  # Field name made lowercase.
    cd68 = models.FloatField(db_column='CD68', blank=True, null=True)  # Field name made lowercase.
    shbg = models.FloatField(db_column='SHBG', blank=True, null=True)  # Field name made lowercase.
    pmp22 = models.FloatField(db_column='PMP22', blank=True, null=True)  # Field name made lowercase.
    srebf1 = models.FloatField(db_column='SREBF1', blank=True, null=True)  # Field name made lowercase.
    mapk7 = models.FloatField(db_column='MAPK7', blank=True, null=True)  # Field name made lowercase.
    ccl2 = models.FloatField(db_column='CCL2', blank=True, null=True)  # Field name made lowercase.
    ccl5 = models.FloatField(db_column='CCL5', blank=True, null=True)  # Field name made lowercase.
    hnf1b = models.FloatField(db_column='HNF1B', blank=True, null=True)  # Field name made lowercase.
    erbb2 = models.FloatField(db_column='ERBB2', blank=True, null=True)  # Field name made lowercase.
    fkbp10 = models.FloatField(db_column='FKBP10', blank=True, null=True)  # Field name made lowercase.
    stat5a = models.FloatField(db_column='STAT5A', blank=True, null=True)  # Field name made lowercase.
    stat3 = models.FloatField(db_column='STAT3', blank=True, null=True)  # Field name made lowercase.
    naglu = models.FloatField(db_column='NAGLU', blank=True, null=True)  # Field name made lowercase.
    aoc2 = models.FloatField(db_column='AOC2', blank=True, null=True)  # Field name made lowercase.
    aoc3 = models.FloatField(db_column='AOC3', blank=True, null=True)  # Field name made lowercase.
    ppy = models.FloatField(db_column='PPY', blank=True, null=True)  # Field name made lowercase.
    sth = models.FloatField(db_column='STH', blank=True, null=True)  # Field name made lowercase.
    itgb3 = models.FloatField(db_column='ITGB3', blank=True, null=True)  # Field name made lowercase.
    gip = models.FloatField(db_column='GIP', blank=True, null=True)  # Field name made lowercase.
    mpo = models.FloatField(db_column='MPO', blank=True, null=True)  # Field name made lowercase.
    pecam1 = models.FloatField(db_column='PECAM1', blank=True, null=True)  # Field name made lowercase.
    sox9 = models.FloatField(db_column='SOX9', blank=True, null=True)  # Field name made lowercase.
    timp2 = models.FloatField(db_column='TIMP2', blank=True, null=True)  # Field name made lowercase.
    dcxr = models.FloatField(db_column='DCXR', blank=True, null=True)  # Field name made lowercase.
    fasn = models.FloatField(db_column='FASN', blank=True, null=True)  # Field name made lowercase.
    colec12 = models.FloatField(db_column='COLEC12', blank=True, null=True)  # Field name made lowercase.
    adcyap1 = models.FloatField(db_column='ADCYAP1', blank=True, null=True)  # Field name made lowercase.
    smad7 = models.FloatField(db_column='SMAD7', blank=True, null=True)  # Field name made lowercase.
    nedd4l = models.FloatField(db_column='NEDD4L', blank=True, null=True)  # Field name made lowercase.
    mc4r = models.FloatField(db_column='MC4R', blank=True, null=True)  # Field name made lowercase.
    bcl2 = models.FloatField(db_column='BCL2', blank=True, null=True)  # Field name made lowercase.
    cndp2 = models.FloatField(db_column='CNDP2', blank=True, null=True)  # Field name made lowercase.
    znf236 = models.FloatField(db_column='ZNF236', blank=True, null=True)  # Field name made lowercase.
    stk11 = models.FloatField(db_column='STK11', blank=True, null=True)  # Field name made lowercase.
    sirt6 = models.FloatField(db_column='SIRT6', blank=True, null=True)  # Field name made lowercase.
    uhrf1 = models.FloatField(db_column='UHRF1', blank=True, null=True)  # Field name made lowercase.
    timm44 = models.FloatField(db_column='TIMM44', blank=True, null=True)  # Field name made lowercase.
    angptl4 = models.FloatField(db_column='ANGPTL4', blank=True, null=True)  # Field name made lowercase.
    dnmt1 = models.FloatField(db_column='DNMT1', blank=True, null=True)  # Field name made lowercase.
    icam1 = models.FloatField(db_column='ICAM1', blank=True, null=True)  # Field name made lowercase.
    ldlr = models.FloatField(db_column='LDLR', blank=True, null=True)  # Field name made lowercase.
    epor = models.FloatField(db_column='EPOR', blank=True, null=True)  # Field name made lowercase.
    prdx2 = models.FloatField(db_column='PRDX2', blank=True, null=True)  # Field name made lowercase.
    ptger1 = models.FloatField(db_column='PTGER1', blank=True, null=True)  # Field name made lowercase.
    unc13a = models.FloatField(db_column='UNC13A', blank=True, null=True)  # Field name made lowercase.
    gdf15 = models.FloatField(db_column='GDF15', blank=True, null=True)  # Field name made lowercase.
    fkbp8 = models.FloatField(db_column='FKBP8', blank=True, null=True)  # Field name made lowercase.
    usf2 = models.FloatField(db_column='USF2', blank=True, null=True)  # Field name made lowercase.
    ffar1 = models.FloatField(db_column='FFAR1', blank=True, null=True)  # Field name made lowercase.
    ffar2 = models.FloatField(db_column='FFAR2', blank=True, null=True)  # Field name made lowercase.
    nphs1 = models.FloatField(db_column='NPHS1', blank=True, null=True)  # Field name made lowercase.
    tgfb1 = models.FloatField(db_column='TGFB1', blank=True, null=True)  # Field name made lowercase.
    xrcc1 = models.FloatField(db_column='XRCC1', blank=True, null=True)  # Field name made lowercase.
    ercc1 = models.FloatField(db_column='ERCC1', blank=True, null=True)  # Field name made lowercase.
    gipr = models.FloatField(db_column='GIPR', blank=True, null=True)  # Field name made lowercase.
    fgf21 = models.FloatField(db_column='FGF21', blank=True, null=True)  # Field name made lowercase.
    clec11a = models.FloatField(db_column='CLEC11A', blank=True, null=True)  # Field name made lowercase.
    fpr1 = models.FloatField(db_column='FPR1', blank=True, null=True)  # Field name made lowercase.
    trib3 = models.FloatField(db_column='TRIB3', blank=True, null=True)  # Field name made lowercase.
    bmp2 = models.FloatField(db_column='BMP2', blank=True, null=True)  # Field name made lowercase.
    thbd = models.FloatField(db_column='THBD', blank=True, null=True)  # Field name made lowercase.
    cst3 = models.FloatField(db_column='CST3', blank=True, null=True)  # Field name made lowercase.
    id1 = models.FloatField(db_column='ID1', blank=True, null=True)  # Field name made lowercase.
    src = models.FloatField(db_column='SRC', blank=True, null=True)  # Field name made lowercase.
    mafb = models.FloatField(db_column='MAFB', blank=True, null=True)  # Field name made lowercase.
    sgk2 = models.FloatField(db_column='SGK2', blank=True, null=True)  # Field name made lowercase.
    hnf4a = models.FloatField(db_column='HNF4A', blank=True, null=True)  # Field name made lowercase.
    pltp = models.FloatField(db_column='PLTP', blank=True, null=True)  # Field name made lowercase.
    mmp9 = models.FloatField(db_column='MMP9', blank=True, null=True)  # Field name made lowercase.
    cd40 = models.FloatField(db_column='CD40', blank=True, null=True)  # Field name made lowercase.
    ptpn1 = models.FloatField(db_column='PTPN1', blank=True, null=True)  # Field name made lowercase.
    cyp24a1 = models.FloatField(db_column='CYP24A1', blank=True, null=True)  # Field name made lowercase.
    rcan1 = models.FloatField(db_column='RCAN1', blank=True, null=True)  # Field name made lowercase.
    abcg1 = models.FloatField(db_column='ABCG1', blank=True, null=True)  # Field name made lowercase.
    prmt2 = models.FloatField(db_column='PRMT2', blank=True, null=True)  # Field name made lowercase.
    comt = models.FloatField(db_column='COMT', blank=True, null=True)  # Field name made lowercase.
    mapk1 = models.FloatField(db_column='MAPK1', blank=True, null=True)  # Field name made lowercase.
    mif = models.FloatField(db_column='MIF', blank=True, null=True)  # Field name made lowercase.
    ggt1 = models.FloatField(db_column='GGT1', blank=True, null=True)  # Field name made lowercase.
    xbp1 = models.FloatField(db_column='XBP1', blank=True, null=True)  # Field name made lowercase.
    osm = models.FloatField(db_column='OSM', blank=True, null=True)  # Field name made lowercase.
    limk2 = models.FloatField(db_column='LIMK2', blank=True, null=True)  # Field name made lowercase.
    sfi1 = models.FloatField(db_column='SFI1', blank=True, null=True)  # Field name made lowercase.
    timp3 = models.FloatField(db_column='TIMP3', blank=True, null=True)  # Field name made lowercase.
    hmox1 = models.FloatField(db_column='HMOX1', blank=True, null=True)  # Field name made lowercase.
    apol1 = models.FloatField(db_column='APOL1', blank=True, null=True)  # Field name made lowercase.
    myh9 = models.FloatField(db_column='MYH9', blank=True, null=True)  # Field name made lowercase.
    pdgfb = models.FloatField(db_column='PDGFB', blank=True, null=True)  # Field name made lowercase.
    atf4 = models.FloatField(db_column='ATF4', blank=True, null=True)  # Field name made lowercase.
    tspo = models.FloatField(db_column='TSPO', blank=True, null=True)  # Field name made lowercase.
    miox = models.FloatField(db_column='MIOX', blank=True, null=True)  # Field name made lowercase.
    prdx4 = models.FloatField(db_column='PRDX4', blank=True, null=True)  # Field name made lowercase.
    gk = models.FloatField(db_column='GK', blank=True, null=True)  # Field name made lowercase.
    rgn = models.FloatField(db_column='RGN', blank=True, null=True)  # Field name made lowercase.
    timp1 = models.FloatField(db_column='TIMP1', blank=True, null=True)  # Field name made lowercase.
    clcn5 = models.FloatField(db_column='CLCN5', blank=True, null=True)  # Field name made lowercase.
    ar = models.FloatField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    foxo4 = models.FloatField(db_column='FOXO4', blank=True, null=True)  # Field name made lowercase.
    rps6ka6 = models.FloatField(db_column='RPS6KA6', blank=True, null=True)  # Field name made lowercase.
    nox1 = models.FloatField(db_column='NOX1', blank=True, null=True)  # Field name made lowercase.
    xiap = models.FloatField(db_column='XIAP', blank=True, null=True)  # Field name made lowercase.
    cd40lg = models.FloatField(db_column='CD40LG', blank=True, null=True)  # Field name made lowercase.
    l1cam = models.FloatField(db_column='L1CAM', blank=True, null=True)  # Field name made lowercase.
    irak1 = models.FloatField(db_column='IRAK1', blank=True, null=True)  # Field name made lowercase.
    g6pd = models.FloatField(db_column='G6PD', blank=True, null=True)  # Field name made lowercase.
    f8 = models.FloatField(db_column='F8', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diaco_tissue_adrenal_gland'


class DiacoTissueArteryAorta(models.Model):
    subjid = models.CharField(db_column='SUBJID', max_length=50, primary_key=True)  # Field name made lowercase.
    sampid = models.CharField(db_column='SAMPID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sesso = models.CharField(db_column='Sesso', max_length=1)  # Field name made lowercase.
    eta = models.CharField(db_column='Età', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errfi1 = models.FloatField(db_column='ERRFI1', blank=True, null=True)  # Field name made lowercase.
    mad2l2 = models.FloatField(db_column='MAD2L2', blank=True, null=True)  # Field name made lowercase.
    mthfr = models.FloatField(db_column='MTHFR', blank=True, null=True)  # Field name made lowercase.
    nppa = models.FloatField(db_column='NPPA', blank=True, null=True)  # Field name made lowercase.
    tnfrsf1b = models.FloatField(db_column='TNFRSF1B', blank=True, null=True)  # Field name made lowercase.
    pla2g2a = models.FloatField(db_column='PLA2G2A', blank=True, null=True)  # Field name made lowercase.
    alpl = models.FloatField(db_column='ALPL', blank=True, null=True)  # Field name made lowercase.
    hspg2 = models.FloatField(db_column='HSPG2', blank=True, null=True)  # Field name made lowercase.
    cnr2 = models.FloatField(db_column='CNR2', blank=True, null=True)  # Field name made lowercase.
    slc9a1 = models.FloatField(db_column='SLC9A1', blank=True, null=True)  # Field name made lowercase.
    col8a2 = models.FloatField(db_column='COL8A2', blank=True, null=True)  # Field name made lowercase.
    cap1 = models.FloatField(db_column='CAP1', blank=True, null=True)  # Field name made lowercase.
    slc2a1 = models.FloatField(db_column='SLC2A1', blank=True, null=True)  # Field name made lowercase.
    cyp2j2 = models.FloatField(db_column='CYP2J2', blank=True, null=True)  # Field name made lowercase.
    ddah1 = models.FloatField(db_column='DDAH1', blank=True, null=True)  # Field name made lowercase.
    cyr61 = models.FloatField(db_column='CYR61', blank=True, null=True)  # Field name made lowercase.
    ngf = models.FloatField(db_column='NGF', blank=True, null=True)  # Field name made lowercase.
    hmgcs2 = models.FloatField(db_column='HMGCS2', blank=True, null=True)  # Field name made lowercase.
    ctss = models.FloatField(db_column='CTSS', blank=True, null=True)  # Field name made lowercase.
    s100a12 = models.FloatField(db_column='S100A12', blank=True, null=True)  # Field name made lowercase.
    lmna = models.FloatField(db_column='LMNA', blank=True, null=True)  # Field name made lowercase.
    cd247 = models.FloatField(db_column='CD247', blank=True, null=True)  # Field name made lowercase.
    sele = models.FloatField(db_column='SELE', blank=True, null=True)  # Field name made lowercase.
    fmo3 = models.FloatField(db_column='FMO3', blank=True, null=True)  # Field name made lowercase.
    prdx6 = models.FloatField(db_column='PRDX6', blank=True, null=True)  # Field name made lowercase.
    glul = models.FloatField(db_column='GLUL', blank=True, null=True)  # Field name made lowercase.
    lamc1 = models.FloatField(db_column='LAMC1', blank=True, null=True)  # Field name made lowercase.
    ptgs2 = models.FloatField(db_column='PTGS2', blank=True, null=True)  # Field name made lowercase.
    chi3l1 = models.FloatField(db_column='CHI3L1', blank=True, null=True)  # Field name made lowercase.
    chit1 = models.FloatField(db_column='CHIT1', blank=True, null=True)  # Field name made lowercase.
    fmod = models.FloatField(db_column='FMOD', blank=True, null=True)  # Field name made lowercase.
    il10 = models.FloatField(db_column='IL10', blank=True, null=True)  # Field name made lowercase.
    pfkfb2 = models.FloatField(db_column='PFKFB2', blank=True, null=True)  # Field name made lowercase.
    cd34 = models.FloatField(db_column='CD34', blank=True, null=True)  # Field name made lowercase.
    cog2 = models.FloatField(db_column='COG2', blank=True, null=True)  # Field name made lowercase.
    nlrp3 = models.FloatField(db_column='NLRP3', blank=True, null=True)  # Field name made lowercase.
    rock2 = models.FloatField(db_column='ROCK2', blank=True, null=True)  # Field name made lowercase.
    apob = models.FloatField(db_column='APOB', blank=True, null=True)  # Field name made lowercase.
    pomc = models.FloatField(db_column='POMC', blank=True, null=True)  # Field name made lowercase.
    gckr = models.FloatField(db_column='GCKR', blank=True, null=True)  # Field name made lowercase.
    plekhh2 = models.FloatField(db_column='PLEKHH2', blank=True, null=True)  # Field name made lowercase.
    prkce = models.FloatField(db_column='PRKCE', blank=True, null=True)  # Field name made lowercase.
    pigf = models.FloatField(db_column='PIGF', blank=True, null=True)  # Field name made lowercase.
    msh2 = models.FloatField(db_column='MSH2', blank=True, null=True)  # Field name made lowercase.
    gfpt1 = models.FloatField(db_column='GFPT1', blank=True, null=True)  # Field name made lowercase.
    tacr1 = models.FloatField(db_column='TACR1', blank=True, null=True)  # Field name made lowercase.
    reg1a = models.FloatField(db_column='REG1A', blank=True, null=True)  # Field name made lowercase.
    eif2ak3 = models.FloatField(db_column='EIF2AK3', blank=True, null=True)  # Field name made lowercase.
    adra2b = models.FloatField(db_column='ADRA2B', blank=True, null=True)  # Field name made lowercase.
    il1b = models.FloatField(db_column='IL1B', blank=True, null=True)  # Field name made lowercase.
    proc = models.FloatField(db_column='PROC', blank=True, null=True)  # Field name made lowercase.
    polr2d = models.FloatField(db_column='POLR2D', blank=True, null=True)  # Field name made lowercase.
    zeb2 = models.FloatField(db_column='ZEB2', blank=True, null=True)  # Field name made lowercase.
    acvr1c = models.FloatField(db_column='ACVR1C', blank=True, null=True)  # Field name made lowercase.
    dpp4 = models.FloatField(db_column='DPP4', blank=True, null=True)  # Field name made lowercase.
    nfe2l2 = models.FloatField(db_column='NFE2L2', blank=True, null=True)  # Field name made lowercase.
    igfbp5 = models.FloatField(db_column='IGFBP5', blank=True, null=True)  # Field name made lowercase.
    ccl20 = models.FloatField(db_column='CCL20', blank=True, null=True)  # Field name made lowercase.
    hdac4 = models.FloatField(db_column='HDAC4', blank=True, null=True)  # Field name made lowercase.
    capn10 = models.FloatField(db_column='CAPN10', blank=True, null=True)  # Field name made lowercase.
    ghrl = models.FloatField(db_column='GHRL', blank=True, null=True)  # Field name made lowercase.
    pparg = models.FloatField(db_column='PPARG', blank=True, null=True)  # Field name made lowercase.
    raf1 = models.FloatField(db_column='RAF1', blank=True, null=True)  # Field name made lowercase.
    myd88 = models.FloatField(db_column='MYD88', blank=True, null=True)  # Field name made lowercase.
    cx3cr1 = models.FloatField(db_column='CX3CR1', blank=True, null=True)  # Field name made lowercase.
    cck = models.FloatField(db_column='CCK', blank=True, null=True)  # Field name made lowercase.
    exosc7 = models.FloatField(db_column='EXOSC7', blank=True, null=True)  # Field name made lowercase.
    ccr1 = models.FloatField(db_column='CCR1', blank=True, null=True)  # Field name made lowercase.
    ccr5 = models.FloatField(db_column='CCR5', blank=True, null=True)  # Field name made lowercase.
    gpx1 = models.FloatField(db_column='GPX1', blank=True, null=True)  # Field name made lowercase.
    rhoa = models.FloatField(db_column='RHOA', blank=True, null=True)  # Field name made lowercase.
    cish = models.FloatField(db_column='CISH', blank=True, null=True)  # Field name made lowercase.
    tkt = models.FloatField(db_column='TKT', blank=True, null=True)  # Field name made lowercase.
    appl1 = models.FloatField(db_column='APPL1', blank=True, null=True)  # Field name made lowercase.
    slmap = models.FloatField(db_column='SLMAP', blank=True, null=True)  # Field name made lowercase.
    col8a1 = models.FloatField(db_column='COL8A1', blank=True, null=True)  # Field name made lowercase.
    cd47 = models.FloatField(db_column='CD47', blank=True, null=True)  # Field name made lowercase.
    gap43 = models.FloatField(db_column='GAP43', blank=True, null=True)  # Field name made lowercase.
    cd80 = models.FloatField(db_column='CD80', blank=True, null=True)  # Field name made lowercase.
    rho = models.FloatField(db_column='RHO', blank=True, null=True)  # Field name made lowercase.
    trh = models.FloatField(db_column='TRH', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='TF', blank=True, null=True)  # Field name made lowercase.
    rbp1 = models.FloatField(db_column='RBP1', blank=True, null=True)  # Field name made lowercase.
    trpc1 = models.FloatField(db_column='TRPC1', blank=True, null=True)  # Field name made lowercase.
    agtr1 = models.FloatField(db_column='AGTR1', blank=True, null=True)  # Field name made lowercase.
    sucnr1 = models.FloatField(db_column='SUCNR1', blank=True, null=True)  # Field name made lowercase.
    p2ry1 = models.FloatField(db_column='P2RY1', blank=True, null=True)  # Field name made lowercase.
    mme = models.FloatField(db_column='MME', blank=True, null=True)  # Field name made lowercase.
    slc2a2 = models.FloatField(db_column='SLC2A2', blank=True, null=True)  # Field name made lowercase.
    pik3ca = models.FloatField(db_column='PIK3CA', blank=True, null=True)  # Field name made lowercase.
    parl = models.FloatField(db_column='PARL', blank=True, null=True)  # Field name made lowercase.
    ahsg = models.FloatField(db_column='AHSG', blank=True, null=True)  # Field name made lowercase.
    adipoq = models.FloatField(db_column='ADIPOQ', blank=True, null=True)  # Field name made lowercase.
    spon2 = models.FloatField(db_column='SPON2', blank=True, null=True)  # Field name made lowercase.
    wfs1 = models.FloatField(db_column='WFS1', blank=True, null=True)  # Field name made lowercase.
    cd38 = models.FloatField(db_column='CD38', blank=True, null=True)  # Field name made lowercase.
    prom1 = models.FloatField(db_column='PROM1', blank=True, null=True)  # Field name made lowercase.
    ppargc1a = models.FloatField(db_column='PPARGC1A', blank=True, null=True)  # Field name made lowercase.
    igfbp7 = models.FloatField(db_column='IGFBP7', blank=True, null=True)  # Field name made lowercase.
    cxcl5 = models.FloatField(db_column='CXCL5', blank=True, null=True)  # Field name made lowercase.
    cxcl9 = models.FloatField(db_column='CXCL9', blank=True, null=True)  # Field name made lowercase.
    cxcl10 = models.FloatField(db_column='CXCL10', blank=True, null=True)  # Field name made lowercase.
    cxcl11 = models.FloatField(db_column='CXCL11', blank=True, null=True)  # Field name made lowercase.
    hpse = models.FloatField(db_column='HPSE', blank=True, null=True)  # Field name made lowercase.
    spp1 = models.FloatField(db_column='SPP1', blank=True, null=True)  # Field name made lowercase.
    adh1b = models.FloatField(db_column='ADH1B', blank=True, null=True)  # Field name made lowercase.
    egf = models.FloatField(db_column='EGF', blank=True, null=True)  # Field name made lowercase.
    alpk1 = models.FloatField(db_column='ALPK1', blank=True, null=True)  # Field name made lowercase.
    fabp2 = models.FloatField(db_column='FABP2', blank=True, null=True)  # Field name made lowercase.
    pde5a = models.FloatField(db_column='PDE5A', blank=True, null=True)  # Field name made lowercase.
    setd7 = models.FloatField(db_column='SETD7', blank=True, null=True)  # Field name made lowercase.
    smad1 = models.FloatField(db_column='SMAD1', blank=True, null=True)  # Field name made lowercase.
    ednra = models.FloatField(db_column='EDNRA', blank=True, null=True)  # Field name made lowercase.
    nr3c2 = models.FloatField(db_column='NR3C2', blank=True, null=True)  # Field name made lowercase.
    tlr2 = models.FloatField(db_column='TLR2', blank=True, null=True)  # Field name made lowercase.
    npy5r = models.FloatField(db_column='NPY5R', blank=True, null=True)  # Field name made lowercase.
    fbxo8 = models.FloatField(db_column='FBXO8', blank=True, null=True)  # Field name made lowercase.
    vegfc = models.FloatField(db_column='VEGFC', blank=True, null=True)  # Field name made lowercase.
    acsl1 = models.FloatField(db_column='ACSL1', blank=True, null=True)  # Field name made lowercase.
    sorbs2 = models.FloatField(db_column='SORBS2', blank=True, null=True)  # Field name made lowercase.
    f11 = models.FloatField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    basp1 = models.FloatField(db_column='BASP1', blank=True, null=True)  # Field name made lowercase.
    ptger4 = models.FloatField(db_column='PTGER4', blank=True, null=True)  # Field name made lowercase.
    prkaa1 = models.FloatField(db_column='PRKAA1', blank=True, null=True)  # Field name made lowercase.
    ghr = models.FloatField(db_column='GHR', blank=True, null=True)  # Field name made lowercase.
    itga2 = models.FloatField(db_column='ITGA2', blank=True, null=True)  # Field name made lowercase.
    cdk7 = models.FloatField(db_column='CDK7', blank=True, null=True)  # Field name made lowercase.
    f2r = models.FloatField(db_column='F2R', blank=True, null=True)  # Field name made lowercase.
    erap2 = models.FloatField(db_column='ERAP2', blank=True, null=True)  # Field name made lowercase.
    apc = models.FloatField(db_column='APC', blank=True, null=True)  # Field name made lowercase.
    tnfaip8 = models.FloatField(db_column='TNFAIP8', blank=True, null=True)  # Field name made lowercase.
    vdac1 = models.FloatField(db_column='VDAC1', blank=True, null=True)  # Field name made lowercase.
    pdgfrb = models.FloatField(db_column='PDGFRB', blank=True, null=True)  # Field name made lowercase.
    cd74 = models.FloatField(db_column='CD74', blank=True, null=True)  # Field name made lowercase.
    sparc = models.FloatField(db_column='SPARC', blank=True, null=True)  # Field name made lowercase.
    ebf1 = models.FloatField(db_column='EBF1', blank=True, null=True)  # Field name made lowercase.
    gfpt2 = models.FloatField(db_column='GFPT2', blank=True, null=True)  # Field name made lowercase.
    rreb1 = models.FloatField(db_column='RREB1', blank=True, null=True)  # Field name made lowercase.
    edn1 = models.FloatField(db_column='EDN1', blank=True, null=True)  # Field name made lowercase.
    cdkal1 = models.FloatField(db_column='CDKAL1', blank=True, null=True)  # Field name made lowercase.
    hfe = models.FloatField(db_column='HFE', blank=True, null=True)  # Field name made lowercase.
    hla_a = models.FloatField(db_column='HLA-A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  # Field name made lowercase.
    tnf = models.FloatField(db_column='TNF', blank=True, null=True)  # Field name made lowercase.
    hspa1a = models.FloatField(db_column='HSPA1A', blank=True, null=True)  # Field name made lowercase.
    hspa1b = models.FloatField(db_column='HSPA1B', blank=True, null=True)  # Field name made lowercase.
    hla_dqa1 = models.FloatField(db_column='HLA-DQA1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mapk14 = models.FloatField(db_column='MAPK14', blank=True, null=True)  # Field name made lowercase.
    cdkn1a = models.FloatField(db_column='CDKN1A', blank=True, null=True)  # Field name made lowercase.
    glo1 = models.FloatField(db_column='GLO1', blank=True, null=True)  # Field name made lowercase.
    vegfa = models.FloatField(db_column='VEGFA', blank=True, null=True)  # Field name made lowercase.
    cd2ap = models.FloatField(db_column='CD2AP', blank=True, null=True)  # Field name made lowercase.
    cnr1 = models.FloatField(db_column='CNR1', blank=True, null=True)  # Field name made lowercase.
    enpp1 = models.FloatField(db_column='ENPP1', blank=True, null=True)  # Field name made lowercase.
    ctgf = models.FloatField(db_column='CTGF', blank=True, null=True)  # Field name made lowercase.
    rps12 = models.FloatField(db_column='RPS12', blank=True, null=True)  # Field name made lowercase.
    sgk1 = models.FloatField(db_column='SGK1', blank=True, null=True)  # Field name made lowercase.
    map3k5 = models.FloatField(db_column='MAP3K5', blank=True, null=True)  # Field name made lowercase.
    cited2 = models.FloatField(db_column='CITED2', blank=True, null=True)  # Field name made lowercase.
    utrn = models.FloatField(db_column='UTRN', blank=True, null=True)  # Field name made lowercase.
    mthfd1l = models.FloatField(db_column='MTHFD1L', blank=True, null=True)  # Field name made lowercase.
    vip = models.FloatField(db_column='VIP', blank=True, null=True)  # Field name made lowercase.
    sod2 = models.FloatField(db_column='SOD2', blank=True, null=True)  # Field name made lowercase.
    lpa = models.FloatField(db_column='LPA', blank=True, null=True)  # Field name made lowercase.
    thbs2 = models.FloatField(db_column='THBS2', blank=True, null=True)  # Field name made lowercase.
    pdgfa = models.FloatField(db_column='PDGFA', blank=True, null=True)  # Field name made lowercase.
    il6 = models.FloatField(db_column='IL6', blank=True, null=True)  # Field name made lowercase.
    npy = models.FloatField(db_column='NPY', blank=True, null=True)  # Field name made lowercase.
    jazf1 = models.FloatField(db_column='JAZF1', blank=True, null=True)  # Field name made lowercase.
    cpvl = models.FloatField(db_column='CPVL', blank=True, null=True)  # Field name made lowercase.
    aqp1 = models.FloatField(db_column='AQP1', blank=True, null=True)  # Field name made lowercase.
    elmo1 = models.FloatField(db_column='ELMO1', blank=True, null=True)  # Field name made lowercase.
    igfbp3 = models.FloatField(db_column='IGFBP3', blank=True, null=True)  # Field name made lowercase.
    egfr = models.FloatField(db_column='EGFR', blank=True, null=True)  # Field name made lowercase.
    eln = models.FloatField(db_column='ELN', blank=True, null=True)  # Field name made lowercase.
    ncf1 = models.FloatField(db_column='NCF1', blank=True, null=True)  # Field name made lowercase.
    hspb1 = models.FloatField(db_column='HSPB1', blank=True, null=True)  # Field name made lowercase.
    sema3a = models.FloatField(db_column='SEMA3A', blank=True, null=True)  # Field name made lowercase.
    pon3 = models.FloatField(db_column='PON3', blank=True, null=True)  # Field name made lowercase.
    pon2 = models.FloatField(db_column='PON2', blank=True, null=True)  # Field name made lowercase.
    nampt = models.FloatField(db_column='NAMPT', blank=True, null=True)  # Field name made lowercase.
    cav1 = models.FloatField(db_column='CAV1', blank=True, null=True)  # Field name made lowercase.
    lep = models.FloatField(db_column='LEP', blank=True, null=True)  # Field name made lowercase.
    akr1b1 = models.FloatField(db_column='AKR1B1', blank=True, null=True)  # Field name made lowercase.
    akr1b10 = models.FloatField(db_column='AKR1B10', blank=True, null=True)  # Field name made lowercase.
    pip = models.FloatField(db_column='PIP', blank=True, null=True)  # Field name made lowercase.
    rarres2 = models.FloatField(db_column='RARRES2', blank=True, null=True)  # Field name made lowercase.
    nos3 = models.FloatField(db_column='NOS3', blank=True, null=True)  # Field name made lowercase.
    angpt2 = models.FloatField(db_column='ANGPT2', blank=True, null=True)  # Field name made lowercase.
    defa1 = models.FloatField(db_column='DEFA1', blank=True, null=True)  # Field name made lowercase.
    lpl = models.FloatField(db_column='LPL', blank=True, null=True)  # Field name made lowercase.
    ebf2 = models.FloatField(db_column='EBF2', blank=True, null=True)  # Field name made lowercase.
    adrb3 = models.FloatField(db_column='ADRB3', blank=True, null=True)  # Field name made lowercase.
    eif4ebp1 = models.FloatField(db_column='EIF4EBP1', blank=True, null=True)  # Field name made lowercase.
    fgfr1 = models.FloatField(db_column='FGFR1', blank=True, null=True)  # Field name made lowercase.
    crh = models.FloatField(db_column='CRH', blank=True, null=True)  # Field name made lowercase.
    sgk3 = models.FloatField(db_column='SGK3', blank=True, null=True)  # Field name made lowercase.
    fabp5 = models.FloatField(db_column='FABP5', blank=True, null=True)  # Field name made lowercase.
    fabp4 = models.FloatField(db_column='FABP4', blank=True, null=True)  # Field name made lowercase.
    mmp16 = models.FloatField(db_column='MMP16', blank=True, null=True)  # Field name made lowercase.
    ncald = models.FloatField(db_column='NCALD', blank=True, null=True)  # Field name made lowercase.
    klf10 = models.FloatField(db_column='KLF10', blank=True, null=True)  # Field name made lowercase.
    enpp2 = models.FloatField(db_column='ENPP2', blank=True, null=True)  # Field name made lowercase.
    pvt1 = models.FloatField(db_column='PVT1', blank=True, null=True)  # Field name made lowercase.
    jak2 = models.FloatField(db_column='JAK2', blank=True, null=True)  # Field name made lowercase.
    psip1 = models.FloatField(db_column='PSIP1', blank=True, null=True)  # Field name made lowercase.
    plin2 = models.FloatField(db_column='PLIN2', blank=True, null=True)  # Field name made lowercase.
    rps6 = models.FloatField(db_column='RPS6', blank=True, null=True)  # Field name made lowercase.
    aldh1a1 = models.FloatField(db_column='ALDH1A1', blank=True, null=True)  # Field name made lowercase.
    frmd3 = models.FloatField(db_column='FRMD3', blank=True, null=True)  # Field name made lowercase.
    gas1 = models.FloatField(db_column='GAS1', blank=True, null=True)  # Field name made lowercase.
    baat = models.FloatField(db_column='BAAT', blank=True, null=True)  # Field name made lowercase.
    abca1 = models.FloatField(db_column='ABCA1', blank=True, null=True)  # Field name made lowercase.
    txn = models.FloatField(db_column='TXN', blank=True, null=True)  # Field name made lowercase.
    ambp = models.FloatField(db_column='AMBP', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    hspa5 = models.FloatField(db_column='HSPA5', blank=True, null=True)  # Field name made lowercase.
    angptl2 = models.FloatField(db_column='ANGPTL2', blank=True, null=True)  # Field name made lowercase.
    ptges = models.FloatField(db_column='PTGES', blank=True, null=True)  # Field name made lowercase.
    tsc1 = models.FloatField(db_column='TSC1', blank=True, null=True)  # Field name made lowercase.
    abo = models.FloatField(db_column='ABO', blank=True, null=True)  # Field name made lowercase.
    adamts13 = models.FloatField(db_column='ADAMTS13', blank=True, null=True)  # Field name made lowercase.
    ptgds = models.FloatField(db_column='PTGDS', blank=True, null=True)  # Field name made lowercase.
    klf6 = models.FloatField(db_column='KLF6', blank=True, null=True)  # Field name made lowercase.
    cdc123 = models.FloatField(db_column='CDC123', blank=True, null=True)  # Field name made lowercase.
    bambi = models.FloatField(db_column='BAMBI', blank=True, null=True)  # Field name made lowercase.
    cxcl12 = models.FloatField(db_column='CXCL12', blank=True, null=True)  # Field name made lowercase.
    mbl2 = models.FloatField(db_column='MBL2', blank=True, null=True)  # Field name made lowercase.
    tfam = models.FloatField(db_column='TFAM', blank=True, null=True)  # Field name made lowercase.
    sirt1 = models.FloatField(db_column='SIRT1', blank=True, null=True)  # Field name made lowercase.
    srgn = models.FloatField(db_column='SRGN', blank=True, null=True)  # Field name made lowercase.
    unc5b = models.FloatField(db_column='UNC5B', blank=True, null=True)  # Field name made lowercase.
    adk = models.FloatField(db_column='ADK', blank=True, null=True)  # Field name made lowercase.
    pten = models.FloatField(db_column='PTEN', blank=True, null=True)  # Field name made lowercase.
    rbp4 = models.FloatField(db_column='RBP4', blank=True, null=True)  # Field name made lowercase.
    cyp2c19 = models.FloatField(db_column='CYP2C19', blank=True, null=True)  # Field name made lowercase.
    entpd1 = models.FloatField(db_column='ENTPD1', blank=True, null=True)  # Field name made lowercase.
    tcf7l2 = models.FloatField(db_column='TCF7L2', blank=True, null=True)  # Field name made lowercase.
    bnip3 = models.FloatField(db_column='BNIP3', blank=True, null=True)  # Field name made lowercase.
    igf2 = models.FloatField(db_column='IGF2', blank=True, null=True)  # Field name made lowercase.
    ins = models.FloatField(db_column='INS', blank=True, null=True)  # Field name made lowercase.
    th = models.FloatField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    kcnq1 = models.FloatField(db_column='KCNQ1', blank=True, null=True)  # Field name made lowercase.
    hbg2 = models.FloatField(db_column='HBG2', blank=True, null=True)  # Field name made lowercase.
    smpd1 = models.FloatField(db_column='SMPD1', blank=True, null=True)  # Field name made lowercase.
    ilk = models.FloatField(db_column='ILK', blank=True, null=True)  # Field name made lowercase.
    adm = models.FloatField(db_column='ADM', blank=True, null=True)  # Field name made lowercase.
    pth = models.FloatField(db_column='PTH', blank=True, null=True)  # Field name made lowercase.
    nucb2 = models.FloatField(db_column='NUCB2', blank=True, null=True)  # Field name made lowercase.
    kcnj11 = models.FloatField(db_column='KCNJ11', blank=True, null=True)  # Field name made lowercase.
    saa1 = models.FloatField(db_column='SAA1', blank=True, null=True)  # Field name made lowercase.
    bdnf = models.FloatField(db_column='BDNF', blank=True, null=True)  # Field name made lowercase.
    wt1 = models.FloatField(db_column='WT1', blank=True, null=True)  # Field name made lowercase.
    cd59 = models.FloatField(db_column='CD59', blank=True, null=True)  # Field name made lowercase.
    pdhx = models.FloatField(db_column='PDHX', blank=True, null=True)  # Field name made lowercase.
    traf6 = models.FloatField(db_column='TRAF6', blank=True, null=True)  # Field name made lowercase.
    api5 = models.FloatField(db_column='API5', blank=True, null=True)  # Field name made lowercase.
    nr1h3 = models.FloatField(db_column='NR1H3', blank=True, null=True)  # Field name made lowercase.
    ndufs3 = models.FloatField(db_column='NDUFS3', blank=True, null=True)  # Field name made lowercase.
    folh1 = models.FloatField(db_column='FOLH1', blank=True, null=True)  # Field name made lowercase.
    aplnr = models.FloatField(db_column='APLNR', blank=True, null=True)  # Field name made lowercase.
    p2rx3 = models.FloatField(db_column='P2RX3', blank=True, null=True)  # Field name made lowercase.
    cntf = models.FloatField(db_column='CNTF', blank=True, null=True)  # Field name made lowercase.
    fads1 = models.FloatField(db_column='FADS1', blank=True, null=True)  # Field name made lowercase.
    fads2 = models.FloatField(db_column='FADS2', blank=True, null=True)  # Field name made lowercase.
    fkbp2 = models.FloatField(db_column='FKBP2', blank=True, null=True)  # Field name made lowercase.
    syvn1 = models.FloatField(db_column='SYVN1', blank=True, null=True)  # Field name made lowercase.
    pc = models.FloatField(db_column='PC', blank=True, null=True)  # Field name made lowercase.
    dhcr7 = models.FloatField(db_column='DHCR7', blank=True, null=True)  # Field name made lowercase.
    prcp = models.FloatField(db_column='PRCP', blank=True, null=True)  # Field name made lowercase.
    nox4 = models.FloatField(db_column='NOX4', blank=True, null=True)  # Field name made lowercase.
    pdgfd = models.FloatField(db_column='PDGFD', blank=True, null=True)  # Field name made lowercase.
    atm = models.FloatField(db_column='ATM', blank=True, null=True)  # Field name made lowercase.
    il18 = models.FloatField(db_column='IL18', blank=True, null=True)  # Field name made lowercase.
    apoa1 = models.FloatField(db_column='APOA1', blank=True, null=True)  # Field name made lowercase.
    hyou1 = models.FloatField(db_column='HYOU1', blank=True, null=True)  # Field name made lowercase.
    esam = models.FloatField(db_column='ESAM', blank=True, null=True)  # Field name made lowercase.
    fkbp4 = models.FloatField(db_column='FKBP4', blank=True, null=True)  # Field name made lowercase.
    fgf23 = models.FloatField(db_column='FGF23', blank=True, null=True)  # Field name made lowercase.
    ntf3 = models.FloatField(db_column='NTF3', blank=True, null=True)  # Field name made lowercase.
    vwf = models.FloatField(db_column='VWF', blank=True, null=True)  # Field name made lowercase.
    cd9 = models.FloatField(db_column='CD9', blank=True, null=True)  # Field name made lowercase.
    gapdh = models.FloatField(db_column='GAPDH', blank=True, null=True)  # Field name made lowercase.
    cd4 = models.FloatField(db_column='CD4', blank=True, null=True)  # Field name made lowercase.
    gnb3 = models.FloatField(db_column='GNB3', blank=True, null=True)  # Field name made lowercase.
    cd163 = models.FloatField(db_column='CD163', blank=True, null=True)  # Field name made lowercase.
    slc2a3 = models.FloatField(db_column='SLC2A3', blank=True, null=True)  # Field name made lowercase.
    cd69 = models.FloatField(db_column='CD69', blank=True, null=True)  # Field name made lowercase.
    irak4 = models.FloatField(db_column='IRAK4', blank=True, null=True)  # Field name made lowercase.
    vdr = models.FloatField(db_column='VDR', blank=True, null=True)  # Field name made lowercase.
    aqp5 = models.FloatField(db_column='AQP5', blank=True, null=True)  # Field name made lowercase.
    acvrl1 = models.FloatField(db_column='ACVRL1', blank=True, null=True)  # Field name made lowercase.
    nfe2 = models.FloatField(db_column='NFE2', blank=True, null=True)  # Field name made lowercase.
    cd63 = models.FloatField(db_column='CD63', blank=True, null=True)  # Field name made lowercase.
    erbb3 = models.FloatField(db_column='ERBB3', blank=True, null=True)  # Field name made lowercase.
    ddit3 = models.FloatField(db_column='DDIT3', blank=True, null=True)  # Field name made lowercase.
    ifng = models.FloatField(db_column='IFNG', blank=True, null=True)  # Field name made lowercase.
    nts = models.FloatField(db_column='NTS', blank=True, null=True)  # Field name made lowercase.
    igf1 = models.FloatField(db_column='IGF1', blank=True, null=True)  # Field name made lowercase.
    acacb = models.FloatField(db_column='ACACB', blank=True, null=True)  # Field name made lowercase.
    trpv4 = models.FloatField(db_column='TRPV4', blank=True, null=True)  # Field name made lowercase.
    atp2a2 = models.FloatField(db_column='ATP2A2', blank=True, null=True)  # Field name made lowercase.
    aldh2 = models.FloatField(db_column='ALDH2', blank=True, null=True)  # Field name made lowercase.
    nos1 = models.FloatField(db_column='NOS1', blank=True, null=True)  # Field name made lowercase.
    pebp1 = models.FloatField(db_column='PEBP1', blank=True, null=True)  # Field name made lowercase.
    psmd9 = models.FloatField(db_column='PSMD9', blank=True, null=True)  # Field name made lowercase.
    scarb1 = models.FloatField(db_column='SCARB1', blank=True, null=True)  # Field name made lowercase.
    p2rx2 = models.FloatField(db_column='P2RX2', blank=True, null=True)  # Field name made lowercase.
    alox5ap = models.FloatField(db_column='ALOX5AP', blank=True, null=True)  # Field name made lowercase.
    kl = models.FloatField(db_column='KL', blank=True, null=True)  # Field name made lowercase.
    postn = models.FloatField(db_column='POSTN', blank=True, null=True)  # Field name made lowercase.
    foxo1 = models.FloatField(db_column='FOXO1', blank=True, null=True)  # Field name made lowercase.
    htr2a = models.FloatField(db_column='HTR2A', blank=True, null=True)  # Field name made lowercase.
    gpc5 = models.FloatField(db_column='GPC5', blank=True, null=True)  # Field name made lowercase.
    irs2 = models.FloatField(db_column='IRS2', blank=True, null=True)  # Field name made lowercase.
    gas6 = models.FloatField(db_column='GAS6', blank=True, null=True)  # Field name made lowercase.
    ang = models.FloatField(db_column='ANG', blank=True, null=True)  # Field name made lowercase.
    mmp14 = models.FloatField(db_column='MMP14', blank=True, null=True)  # Field name made lowercase.
    ltb4r2 = models.FloatField(db_column='LTB4R2', blank=True, null=True)  # Field name made lowercase.
    nfkbia = models.FloatField(db_column='NFKBIA', blank=True, null=True)  # Field name made lowercase.
    bmp4 = models.FloatField(db_column='BMP4', blank=True, null=True)  # Field name made lowercase.
    rtn1 = models.FloatField(db_column='RTN1', blank=True, null=True)  # Field name made lowercase.
    pgf = models.FloatField(db_column='PGF', blank=True, null=True)  # Field name made lowercase.
    ngb = models.FloatField(db_column='NGB', blank=True, null=True)  # Field name made lowercase.
    ahsa1 = models.FloatField(db_column='AHSA1', blank=True, null=True)  # Field name made lowercase.
    bdkrb2 = models.FloatField(db_column='BDKRB2', blank=True, null=True)  # Field name made lowercase.
    bdkrb1 = models.FloatField(db_column='BDKRB1', blank=True, null=True)  # Field name made lowercase.
    akt1 = models.FloatField(db_column='AKT1', blank=True, null=True)  # Field name made lowercase.
    grem1 = models.FloatField(db_column='GREM1', blank=True, null=True)  # Field name made lowercase.
    thbs1 = models.FloatField(db_column='THBS1', blank=True, null=True)  # Field name made lowercase.
    pak6 = models.FloatField(db_column='PAK6', blank=True, null=True)  # Field name made lowercase.
    b2m = models.FloatField(db_column='B2M', blank=True, null=True)  # Field name made lowercase.
    myo5c = models.FloatField(db_column='MYO5C', blank=True, null=True)  # Field name made lowercase.
    onecut1 = models.FloatField(db_column='ONECUT1', blank=True, null=True)  # Field name made lowercase.
    adam10 = models.FloatField(db_column='ADAM10', blank=True, null=True)  # Field name made lowercase.
    ctsh = models.FloatField(db_column='CTSH', blank=True, null=True)  # Field name made lowercase.
    plin1 = models.FloatField(db_column='PLIN1', blank=True, null=True)  # Field name made lowercase.
    igf1r = models.FloatField(db_column='IGF1R', blank=True, null=True)  # Field name made lowercase.
    mrpl28 = models.FloatField(db_column='MRPL28', blank=True, null=True)  # Field name made lowercase.
    cacna1h = models.FloatField(db_column='CACNA1H', blank=True, null=True)  # Field name made lowercase.
    pdpk1 = models.FloatField(db_column='PDPK1', blank=True, null=True)  # Field name made lowercase.
    ercc4 = models.FloatField(db_column='ERCC4', blank=True, null=True)  # Field name made lowercase.
    smg1 = models.FloatField(db_column='SMG1', blank=True, null=True)  # Field name made lowercase.
    itgam = models.FloatField(db_column='ITGAM', blank=True, null=True)  # Field name made lowercase.
    fto = models.FloatField(db_column='FTO', blank=True, null=True)  # Field name made lowercase.
    mmp2 = models.FloatField(db_column='MMP2', blank=True, null=True)  # Field name made lowercase.
    slc12a3 = models.FloatField(db_column='SLC12A3', blank=True, null=True)  # Field name made lowercase.
    cetp = models.FloatField(db_column='CETP', blank=True, null=True)  # Field name made lowercase.
    cx3cl1 = models.FloatField(db_column='CX3CL1', blank=True, null=True)  # Field name made lowercase.
    cdh1 = models.FloatField(db_column='CDH1', blank=True, null=True)  # Field name made lowercase.
    nqo1 = models.FloatField(db_column='NQO1', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    znrf1 = models.FloatField(db_column='ZNRF1', blank=True, null=True)  # Field name made lowercase.
    cyba = models.FloatField(db_column='CYBA', blank=True, null=True)  # Field name made lowercase.
    tubb3 = models.FloatField(db_column='TUBB3', blank=True, null=True)  # Field name made lowercase.
    crk = models.FloatField(db_column='CRK', blank=True, null=True)  # Field name made lowercase.
    serpinf2 = models.FloatField(db_column='SERPINF2', blank=True, null=True)  # Field name made lowercase.
    serpinf1 = models.FloatField(db_column='SERPINF1', blank=True, null=True)  # Field name made lowercase.
    trpv3 = models.FloatField(db_column='TRPV3', blank=True, null=True)  # Field name made lowercase.
    cxcl16 = models.FloatField(db_column='CXCL16', blank=True, null=True)  # Field name made lowercase.
    slc2a4 = models.FloatField(db_column='SLC2A4', blank=True, null=True)  # Field name made lowercase.
    cd68 = models.FloatField(db_column='CD68', blank=True, null=True)  # Field name made lowercase.
    shbg = models.FloatField(db_column='SHBG', blank=True, null=True)  # Field name made lowercase.
    pmp22 = models.FloatField(db_column='PMP22', blank=True, null=True)  # Field name made lowercase.
    srebf1 = models.FloatField(db_column='SREBF1', blank=True, null=True)  # Field name made lowercase.
    mapk7 = models.FloatField(db_column='MAPK7', blank=True, null=True)  # Field name made lowercase.
    ccl2 = models.FloatField(db_column='CCL2', blank=True, null=True)  # Field name made lowercase.
    ccl5 = models.FloatField(db_column='CCL5', blank=True, null=True)  # Field name made lowercase.
    hnf1b = models.FloatField(db_column='HNF1B', blank=True, null=True)  # Field name made lowercase.
    erbb2 = models.FloatField(db_column='ERBB2', blank=True, null=True)  # Field name made lowercase.
    fkbp10 = models.FloatField(db_column='FKBP10', blank=True, null=True)  # Field name made lowercase.
    stat5a = models.FloatField(db_column='STAT5A', blank=True, null=True)  # Field name made lowercase.
    stat3 = models.FloatField(db_column='STAT3', blank=True, null=True)  # Field name made lowercase.
    naglu = models.FloatField(db_column='NAGLU', blank=True, null=True)  # Field name made lowercase.
    aoc2 = models.FloatField(db_column='AOC2', blank=True, null=True)  # Field name made lowercase.
    aoc3 = models.FloatField(db_column='AOC3', blank=True, null=True)  # Field name made lowercase.
    ppy = models.FloatField(db_column='PPY', blank=True, null=True)  # Field name made lowercase.
    sth = models.FloatField(db_column='STH', blank=True, null=True)  # Field name made lowercase.
    itgb3 = models.FloatField(db_column='ITGB3', blank=True, null=True)  # Field name made lowercase.
    gip = models.FloatField(db_column='GIP', blank=True, null=True)  # Field name made lowercase.
    mpo = models.FloatField(db_column='MPO', blank=True, null=True)  # Field name made lowercase.
    pecam1 = models.FloatField(db_column='PECAM1', blank=True, null=True)  # Field name made lowercase.
    sox9 = models.FloatField(db_column='SOX9', blank=True, null=True)  # Field name made lowercase.
    timp2 = models.FloatField(db_column='TIMP2', blank=True, null=True)  # Field name made lowercase.
    dcxr = models.FloatField(db_column='DCXR', blank=True, null=True)  # Field name made lowercase.
    fasn = models.FloatField(db_column='FASN', blank=True, null=True)  # Field name made lowercase.
    colec12 = models.FloatField(db_column='COLEC12', blank=True, null=True)  # Field name made lowercase.
    adcyap1 = models.FloatField(db_column='ADCYAP1', blank=True, null=True)  # Field name made lowercase.
    smad7 = models.FloatField(db_column='SMAD7', blank=True, null=True)  # Field name made lowercase.
    nedd4l = models.FloatField(db_column='NEDD4L', blank=True, null=True)  # Field name made lowercase.
    mc4r = models.FloatField(db_column='MC4R', blank=True, null=True)  # Field name made lowercase.
    bcl2 = models.FloatField(db_column='BCL2', blank=True, null=True)  # Field name made lowercase.
    cndp2 = models.FloatField(db_column='CNDP2', blank=True, null=True)  # Field name made lowercase.
    znf236 = models.FloatField(db_column='ZNF236', blank=True, null=True)  # Field name made lowercase.
    stk11 = models.FloatField(db_column='STK11', blank=True, null=True)  # Field name made lowercase.
    sirt6 = models.FloatField(db_column='SIRT6', blank=True, null=True)  # Field name made lowercase.
    uhrf1 = models.FloatField(db_column='UHRF1', blank=True, null=True)  # Field name made lowercase.
    timm44 = models.FloatField(db_column='TIMM44', blank=True, null=True)  # Field name made lowercase.
    angptl4 = models.FloatField(db_column='ANGPTL4', blank=True, null=True)  # Field name made lowercase.
    dnmt1 = models.FloatField(db_column='DNMT1', blank=True, null=True)  # Field name made lowercase.
    icam1 = models.FloatField(db_column='ICAM1', blank=True, null=True)  # Field name made lowercase.
    ldlr = models.FloatField(db_column='LDLR', blank=True, null=True)  # Field name made lowercase.
    epor = models.FloatField(db_column='EPOR', blank=True, null=True)  # Field name made lowercase.
    prdx2 = models.FloatField(db_column='PRDX2', blank=True, null=True)  # Field name made lowercase.
    ptger1 = models.FloatField(db_column='PTGER1', blank=True, null=True)  # Field name made lowercase.
    unc13a = models.FloatField(db_column='UNC13A', blank=True, null=True)  # Field name made lowercase.
    gdf15 = models.FloatField(db_column='GDF15', blank=True, null=True)  # Field name made lowercase.
    fkbp8 = models.FloatField(db_column='FKBP8', blank=True, null=True)  # Field name made lowercase.
    usf2 = models.FloatField(db_column='USF2', blank=True, null=True)  # Field name made lowercase.
    ffar1 = models.FloatField(db_column='FFAR1', blank=True, null=True)  # Field name made lowercase.
    ffar2 = models.FloatField(db_column='FFAR2', blank=True, null=True)  # Field name made lowercase.
    nphs1 = models.FloatField(db_column='NPHS1', blank=True, null=True)  # Field name made lowercase.
    tgfb1 = models.FloatField(db_column='TGFB1', blank=True, null=True)  # Field name made lowercase.
    xrcc1 = models.FloatField(db_column='XRCC1', blank=True, null=True)  # Field name made lowercase.
    ercc1 = models.FloatField(db_column='ERCC1', blank=True, null=True)  # Field name made lowercase.
    gipr = models.FloatField(db_column='GIPR', blank=True, null=True)  # Field name made lowercase.
    fgf21 = models.FloatField(db_column='FGF21', blank=True, null=True)  # Field name made lowercase.
    clec11a = models.FloatField(db_column='CLEC11A', blank=True, null=True)  # Field name made lowercase.
    fpr1 = models.FloatField(db_column='FPR1', blank=True, null=True)  # Field name made lowercase.
    trib3 = models.FloatField(db_column='TRIB3', blank=True, null=True)  # Field name made lowercase.
    bmp2 = models.FloatField(db_column='BMP2', blank=True, null=True)  # Field name made lowercase.
    thbd = models.FloatField(db_column='THBD', blank=True, null=True)  # Field name made lowercase.
    cst3 = models.FloatField(db_column='CST3', blank=True, null=True)  # Field name made lowercase.
    id1 = models.FloatField(db_column='ID1', blank=True, null=True)  # Field name made lowercase.
    src = models.FloatField(db_column='SRC', blank=True, null=True)  # Field name made lowercase.
    mafb = models.FloatField(db_column='MAFB', blank=True, null=True)  # Field name made lowercase.
    sgk2 = models.FloatField(db_column='SGK2', blank=True, null=True)  # Field name made lowercase.
    hnf4a = models.FloatField(db_column='HNF4A', blank=True, null=True)  # Field name made lowercase.
    pltp = models.FloatField(db_column='PLTP', blank=True, null=True)  # Field name made lowercase.
    mmp9 = models.FloatField(db_column='MMP9', blank=True, null=True)  # Field name made lowercase.
    cd40 = models.FloatField(db_column='CD40', blank=True, null=True)  # Field name made lowercase.
    ptpn1 = models.FloatField(db_column='PTPN1', blank=True, null=True)  # Field name made lowercase.
    cyp24a1 = models.FloatField(db_column='CYP24A1', blank=True, null=True)  # Field name made lowercase.
    rcan1 = models.FloatField(db_column='RCAN1', blank=True, null=True)  # Field name made lowercase.
    abcg1 = models.FloatField(db_column='ABCG1', blank=True, null=True)  # Field name made lowercase.
    prmt2 = models.FloatField(db_column='PRMT2', blank=True, null=True)  # Field name made lowercase.
    comt = models.FloatField(db_column='COMT', blank=True, null=True)  # Field name made lowercase.
    mapk1 = models.FloatField(db_column='MAPK1', blank=True, null=True)  # Field name made lowercase.
    mif = models.FloatField(db_column='MIF', blank=True, null=True)  # Field name made lowercase.
    ggt1 = models.FloatField(db_column='GGT1', blank=True, null=True)  # Field name made lowercase.
    xbp1 = models.FloatField(db_column='XBP1', blank=True, null=True)  # Field name made lowercase.
    osm = models.FloatField(db_column='OSM', blank=True, null=True)  # Field name made lowercase.
    limk2 = models.FloatField(db_column='LIMK2', blank=True, null=True)  # Field name made lowercase.
    sfi1 = models.FloatField(db_column='SFI1', blank=True, null=True)  # Field name made lowercase.
    timp3 = models.FloatField(db_column='TIMP3', blank=True, null=True)  # Field name made lowercase.
    hmox1 = models.FloatField(db_column='HMOX1', blank=True, null=True)  # Field name made lowercase.
    apol1 = models.FloatField(db_column='APOL1', blank=True, null=True)  # Field name made lowercase.
    myh9 = models.FloatField(db_column='MYH9', blank=True, null=True)  # Field name made lowercase.
    pdgfb = models.FloatField(db_column='PDGFB', blank=True, null=True)  # Field name made lowercase.
    atf4 = models.FloatField(db_column='ATF4', blank=True, null=True)  # Field name made lowercase.
    tspo = models.FloatField(db_column='TSPO', blank=True, null=True)  # Field name made lowercase.
    miox = models.FloatField(db_column='MIOX', blank=True, null=True)  # Field name made lowercase.
    prdx4 = models.FloatField(db_column='PRDX4', blank=True, null=True)  # Field name made lowercase.
    gk = models.FloatField(db_column='GK', blank=True, null=True)  # Field name made lowercase.
    rgn = models.FloatField(db_column='RGN', blank=True, null=True)  # Field name made lowercase.
    timp1 = models.FloatField(db_column='TIMP1', blank=True, null=True)  # Field name made lowercase.
    clcn5 = models.FloatField(db_column='CLCN5', blank=True, null=True)  # Field name made lowercase.
    ar = models.FloatField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    foxo4 = models.FloatField(db_column='FOXO4', blank=True, null=True)  # Field name made lowercase.
    rps6ka6 = models.FloatField(db_column='RPS6KA6', blank=True, null=True)  # Field name made lowercase.
    nox1 = models.FloatField(db_column='NOX1', blank=True, null=True)  # Field name made lowercase.
    xiap = models.FloatField(db_column='XIAP', blank=True, null=True)  # Field name made lowercase.
    cd40lg = models.FloatField(db_column='CD40LG', blank=True, null=True)  # Field name made lowercase.
    l1cam = models.FloatField(db_column='L1CAM', blank=True, null=True)  # Field name made lowercase.
    irak1 = models.FloatField(db_column='IRAK1', blank=True, null=True)  # Field name made lowercase.
    g6pd = models.FloatField(db_column='G6PD', blank=True, null=True)  # Field name made lowercase.
    f8 = models.FloatField(db_column='F8', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diaco_tissue_artery_aorta'


class DiacoTissueArteryCoronary(models.Model):
    subjid = models.CharField(db_column='SUBJID', max_length=50, primary_key=True)  # Field name made lowercase.
    sampid = models.CharField(db_column='SAMPID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sesso = models.CharField(db_column='Sesso', max_length=1)  # Field name made lowercase.
    eta = models.CharField(db_column='Età', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errfi1 = models.FloatField(db_column='ERRFI1', blank=True, null=True)  # Field name made lowercase.
    mad2l2 = models.FloatField(db_column='MAD2L2', blank=True, null=True)  # Field name made lowercase.
    mthfr = models.FloatField(db_column='MTHFR', blank=True, null=True)  # Field name made lowercase.
    nppa = models.FloatField(db_column='NPPA', blank=True, null=True)  # Field name made lowercase.
    tnfrsf1b = models.FloatField(db_column='TNFRSF1B', blank=True, null=True)  # Field name made lowercase.
    pla2g2a = models.FloatField(db_column='PLA2G2A', blank=True, null=True)  # Field name made lowercase.
    alpl = models.FloatField(db_column='ALPL', blank=True, null=True)  # Field name made lowercase.
    hspg2 = models.FloatField(db_column='HSPG2', blank=True, null=True)  # Field name made lowercase.
    cnr2 = models.FloatField(db_column='CNR2', blank=True, null=True)  # Field name made lowercase.
    slc9a1 = models.FloatField(db_column='SLC9A1', blank=True, null=True)  # Field name made lowercase.
    col8a2 = models.FloatField(db_column='COL8A2', blank=True, null=True)  # Field name made lowercase.
    cap1 = models.FloatField(db_column='CAP1', blank=True, null=True)  # Field name made lowercase.
    slc2a1 = models.FloatField(db_column='SLC2A1', blank=True, null=True)  # Field name made lowercase.
    cyp2j2 = models.FloatField(db_column='CYP2J2', blank=True, null=True)  # Field name made lowercase.
    ddah1 = models.FloatField(db_column='DDAH1', blank=True, null=True)  # Field name made lowercase.
    cyr61 = models.FloatField(db_column='CYR61', blank=True, null=True)  # Field name made lowercase.
    ngf = models.FloatField(db_column='NGF', blank=True, null=True)  # Field name made lowercase.
    hmgcs2 = models.FloatField(db_column='HMGCS2', blank=True, null=True)  # Field name made lowercase.
    ctss = models.FloatField(db_column='CTSS', blank=True, null=True)  # Field name made lowercase.
    s100a12 = models.FloatField(db_column='S100A12', blank=True, null=True)  # Field name made lowercase.
    lmna = models.FloatField(db_column='LMNA', blank=True, null=True)  # Field name made lowercase.
    cd247 = models.FloatField(db_column='CD247', blank=True, null=True)  # Field name made lowercase.
    sele = models.FloatField(db_column='SELE', blank=True, null=True)  # Field name made lowercase.
    fmo3 = models.FloatField(db_column='FMO3', blank=True, null=True)  # Field name made lowercase.
    prdx6 = models.FloatField(db_column='PRDX6', blank=True, null=True)  # Field name made lowercase.
    glul = models.FloatField(db_column='GLUL', blank=True, null=True)  # Field name made lowercase.
    lamc1 = models.FloatField(db_column='LAMC1', blank=True, null=True)  # Field name made lowercase.
    ptgs2 = models.FloatField(db_column='PTGS2', blank=True, null=True)  # Field name made lowercase.
    chi3l1 = models.FloatField(db_column='CHI3L1', blank=True, null=True)  # Field name made lowercase.
    chit1 = models.FloatField(db_column='CHIT1', blank=True, null=True)  # Field name made lowercase.
    fmod = models.FloatField(db_column='FMOD', blank=True, null=True)  # Field name made lowercase.
    il10 = models.FloatField(db_column='IL10', blank=True, null=True)  # Field name made lowercase.
    pfkfb2 = models.FloatField(db_column='PFKFB2', blank=True, null=True)  # Field name made lowercase.
    cd34 = models.FloatField(db_column='CD34', blank=True, null=True)  # Field name made lowercase.
    cog2 = models.FloatField(db_column='COG2', blank=True, null=True)  # Field name made lowercase.
    nlrp3 = models.FloatField(db_column='NLRP3', blank=True, null=True)  # Field name made lowercase.
    rock2 = models.FloatField(db_column='ROCK2', blank=True, null=True)  # Field name made lowercase.
    apob = models.FloatField(db_column='APOB', blank=True, null=True)  # Field name made lowercase.
    pomc = models.FloatField(db_column='POMC', blank=True, null=True)  # Field name made lowercase.
    gckr = models.FloatField(db_column='GCKR', blank=True, null=True)  # Field name made lowercase.
    plekhh2 = models.FloatField(db_column='PLEKHH2', blank=True, null=True)  # Field name made lowercase.
    prkce = models.FloatField(db_column='PRKCE', blank=True, null=True)  # Field name made lowercase.
    pigf = models.FloatField(db_column='PIGF', blank=True, null=True)  # Field name made lowercase.
    msh2 = models.FloatField(db_column='MSH2', blank=True, null=True)  # Field name made lowercase.
    gfpt1 = models.FloatField(db_column='GFPT1', blank=True, null=True)  # Field name made lowercase.
    tacr1 = models.FloatField(db_column='TACR1', blank=True, null=True)  # Field name made lowercase.
    reg1a = models.FloatField(db_column='REG1A', blank=True, null=True)  # Field name made lowercase.
    eif2ak3 = models.FloatField(db_column='EIF2AK3', blank=True, null=True)  # Field name made lowercase.
    adra2b = models.FloatField(db_column='ADRA2B', blank=True, null=True)  # Field name made lowercase.
    il1b = models.FloatField(db_column='IL1B', blank=True, null=True)  # Field name made lowercase.
    proc = models.FloatField(db_column='PROC', blank=True, null=True)  # Field name made lowercase.
    polr2d = models.FloatField(db_column='POLR2D', blank=True, null=True)  # Field name made lowercase.
    zeb2 = models.FloatField(db_column='ZEB2', blank=True, null=True)  # Field name made lowercase.
    acvr1c = models.FloatField(db_column='ACVR1C', blank=True, null=True)  # Field name made lowercase.
    dpp4 = models.FloatField(db_column='DPP4', blank=True, null=True)  # Field name made lowercase.
    nfe2l2 = models.FloatField(db_column='NFE2L2', blank=True, null=True)  # Field name made lowercase.
    igfbp5 = models.FloatField(db_column='IGFBP5', blank=True, null=True)  # Field name made lowercase.
    ccl20 = models.FloatField(db_column='CCL20', blank=True, null=True)  # Field name made lowercase.
    hdac4 = models.FloatField(db_column='HDAC4', blank=True, null=True)  # Field name made lowercase.
    capn10 = models.FloatField(db_column='CAPN10', blank=True, null=True)  # Field name made lowercase.
    ghrl = models.FloatField(db_column='GHRL', blank=True, null=True)  # Field name made lowercase.
    pparg = models.FloatField(db_column='PPARG', blank=True, null=True)  # Field name made lowercase.
    raf1 = models.FloatField(db_column='RAF1', blank=True, null=True)  # Field name made lowercase.
    myd88 = models.FloatField(db_column='MYD88', blank=True, null=True)  # Field name made lowercase.
    cx3cr1 = models.FloatField(db_column='CX3CR1', blank=True, null=True)  # Field name made lowercase.
    cck = models.FloatField(db_column='CCK', blank=True, null=True)  # Field name made lowercase.
    exosc7 = models.FloatField(db_column='EXOSC7', blank=True, null=True)  # Field name made lowercase.
    ccr1 = models.FloatField(db_column='CCR1', blank=True, null=True)  # Field name made lowercase.
    ccr5 = models.FloatField(db_column='CCR5', blank=True, null=True)  # Field name made lowercase.
    gpx1 = models.FloatField(db_column='GPX1', blank=True, null=True)  # Field name made lowercase.
    rhoa = models.FloatField(db_column='RHOA', blank=True, null=True)  # Field name made lowercase.
    cish = models.FloatField(db_column='CISH', blank=True, null=True)  # Field name made lowercase.
    tkt = models.FloatField(db_column='TKT', blank=True, null=True)  # Field name made lowercase.
    appl1 = models.FloatField(db_column='APPL1', blank=True, null=True)  # Field name made lowercase.
    slmap = models.FloatField(db_column='SLMAP', blank=True, null=True)  # Field name made lowercase.
    col8a1 = models.FloatField(db_column='COL8A1', blank=True, null=True)  # Field name made lowercase.
    cd47 = models.FloatField(db_column='CD47', blank=True, null=True)  # Field name made lowercase.
    gap43 = models.FloatField(db_column='GAP43', blank=True, null=True)  # Field name made lowercase.
    cd80 = models.FloatField(db_column='CD80', blank=True, null=True)  # Field name made lowercase.
    rho = models.FloatField(db_column='RHO', blank=True, null=True)  # Field name made lowercase.
    trh = models.FloatField(db_column='TRH', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='TF', blank=True, null=True)  # Field name made lowercase.
    rbp1 = models.FloatField(db_column='RBP1', blank=True, null=True)  # Field name made lowercase.
    trpc1 = models.FloatField(db_column='TRPC1', blank=True, null=True)  # Field name made lowercase.
    agtr1 = models.FloatField(db_column='AGTR1', blank=True, null=True)  # Field name made lowercase.
    sucnr1 = models.FloatField(db_column='SUCNR1', blank=True, null=True)  # Field name made lowercase.
    p2ry1 = models.FloatField(db_column='P2RY1', blank=True, null=True)  # Field name made lowercase.
    mme = models.FloatField(db_column='MME', blank=True, null=True)  # Field name made lowercase.
    slc2a2 = models.FloatField(db_column='SLC2A2', blank=True, null=True)  # Field name made lowercase.
    pik3ca = models.FloatField(db_column='PIK3CA', blank=True, null=True)  # Field name made lowercase.
    parl = models.FloatField(db_column='PARL', blank=True, null=True)  # Field name made lowercase.
    ahsg = models.FloatField(db_column='AHSG', blank=True, null=True)  # Field name made lowercase.
    adipoq = models.FloatField(db_column='ADIPOQ', blank=True, null=True)  # Field name made lowercase.
    spon2 = models.FloatField(db_column='SPON2', blank=True, null=True)  # Field name made lowercase.
    wfs1 = models.FloatField(db_column='WFS1', blank=True, null=True)  # Field name made lowercase.
    cd38 = models.FloatField(db_column='CD38', blank=True, null=True)  # Field name made lowercase.
    prom1 = models.FloatField(db_column='PROM1', blank=True, null=True)  # Field name made lowercase.
    ppargc1a = models.FloatField(db_column='PPARGC1A', blank=True, null=True)  # Field name made lowercase.
    igfbp7 = models.FloatField(db_column='IGFBP7', blank=True, null=True)  # Field name made lowercase.
    cxcl5 = models.FloatField(db_column='CXCL5', blank=True, null=True)  # Field name made lowercase.
    cxcl9 = models.FloatField(db_column='CXCL9', blank=True, null=True)  # Field name made lowercase.
    cxcl10 = models.FloatField(db_column='CXCL10', blank=True, null=True)  # Field name made lowercase.
    cxcl11 = models.FloatField(db_column='CXCL11', blank=True, null=True)  # Field name made lowercase.
    hpse = models.FloatField(db_column='HPSE', blank=True, null=True)  # Field name made lowercase.
    spp1 = models.FloatField(db_column='SPP1', blank=True, null=True)  # Field name made lowercase.
    adh1b = models.FloatField(db_column='ADH1B', blank=True, null=True)  # Field name made lowercase.
    egf = models.FloatField(db_column='EGF', blank=True, null=True)  # Field name made lowercase.
    alpk1 = models.FloatField(db_column='ALPK1', blank=True, null=True)  # Field name made lowercase.
    fabp2 = models.FloatField(db_column='FABP2', blank=True, null=True)  # Field name made lowercase.
    pde5a = models.FloatField(db_column='PDE5A', blank=True, null=True)  # Field name made lowercase.
    setd7 = models.FloatField(db_column='SETD7', blank=True, null=True)  # Field name made lowercase.
    smad1 = models.FloatField(db_column='SMAD1', blank=True, null=True)  # Field name made lowercase.
    ednra = models.FloatField(db_column='EDNRA', blank=True, null=True)  # Field name made lowercase.
    nr3c2 = models.FloatField(db_column='NR3C2', blank=True, null=True)  # Field name made lowercase.
    tlr2 = models.FloatField(db_column='TLR2', blank=True, null=True)  # Field name made lowercase.
    npy5r = models.FloatField(db_column='NPY5R', blank=True, null=True)  # Field name made lowercase.
    fbxo8 = models.FloatField(db_column='FBXO8', blank=True, null=True)  # Field name made lowercase.
    vegfc = models.FloatField(db_column='VEGFC', blank=True, null=True)  # Field name made lowercase.
    acsl1 = models.FloatField(db_column='ACSL1', blank=True, null=True)  # Field name made lowercase.
    sorbs2 = models.FloatField(db_column='SORBS2', blank=True, null=True)  # Field name made lowercase.
    f11 = models.FloatField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    basp1 = models.FloatField(db_column='BASP1', blank=True, null=True)  # Field name made lowercase.
    ptger4 = models.FloatField(db_column='PTGER4', blank=True, null=True)  # Field name made lowercase.
    prkaa1 = models.FloatField(db_column='PRKAA1', blank=True, null=True)  # Field name made lowercase.
    ghr = models.FloatField(db_column='GHR', blank=True, null=True)  # Field name made lowercase.
    itga2 = models.FloatField(db_column='ITGA2', blank=True, null=True)  # Field name made lowercase.
    cdk7 = models.FloatField(db_column='CDK7', blank=True, null=True)  # Field name made lowercase.
    f2r = models.FloatField(db_column='F2R', blank=True, null=True)  # Field name made lowercase.
    erap2 = models.FloatField(db_column='ERAP2', blank=True, null=True)  # Field name made lowercase.
    apc = models.FloatField(db_column='APC', blank=True, null=True)  # Field name made lowercase.
    tnfaip8 = models.FloatField(db_column='TNFAIP8', blank=True, null=True)  # Field name made lowercase.
    vdac1 = models.FloatField(db_column='VDAC1', blank=True, null=True)  # Field name made lowercase.
    pdgfrb = models.FloatField(db_column='PDGFRB', blank=True, null=True)  # Field name made lowercase.
    cd74 = models.FloatField(db_column='CD74', blank=True, null=True)  # Field name made lowercase.
    sparc = models.FloatField(db_column='SPARC', blank=True, null=True)  # Field name made lowercase.
    ebf1 = models.FloatField(db_column='EBF1', blank=True, null=True)  # Field name made lowercase.
    gfpt2 = models.FloatField(db_column='GFPT2', blank=True, null=True)  # Field name made lowercase.
    rreb1 = models.FloatField(db_column='RREB1', blank=True, null=True)  # Field name made lowercase.
    edn1 = models.FloatField(db_column='EDN1', blank=True, null=True)  # Field name made lowercase.
    cdkal1 = models.FloatField(db_column='CDKAL1', blank=True, null=True)  # Field name made lowercase.
    hfe = models.FloatField(db_column='HFE', blank=True, null=True)  # Field name made lowercase.
    hla_a = models.FloatField(db_column='HLA-A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  # Field name made lowercase.
    tnf = models.FloatField(db_column='TNF', blank=True, null=True)  # Field name made lowercase.
    hspa1a = models.FloatField(db_column='HSPA1A', blank=True, null=True)  # Field name made lowercase.
    hspa1b = models.FloatField(db_column='HSPA1B', blank=True, null=True)  # Field name made lowercase.
    hla_dqa1 = models.FloatField(db_column='HLA-DQA1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mapk14 = models.FloatField(db_column='MAPK14', blank=True, null=True)  # Field name made lowercase.
    cdkn1a = models.FloatField(db_column='CDKN1A', blank=True, null=True)  # Field name made lowercase.
    glo1 = models.FloatField(db_column='GLO1', blank=True, null=True)  # Field name made lowercase.
    vegfa = models.FloatField(db_column='VEGFA', blank=True, null=True)  # Field name made lowercase.
    cd2ap = models.FloatField(db_column='CD2AP', blank=True, null=True)  # Field name made lowercase.
    cnr1 = models.FloatField(db_column='CNR1', blank=True, null=True)  # Field name made lowercase.
    enpp1 = models.FloatField(db_column='ENPP1', blank=True, null=True)  # Field name made lowercase.
    ctgf = models.FloatField(db_column='CTGF', blank=True, null=True)  # Field name made lowercase.
    rps12 = models.FloatField(db_column='RPS12', blank=True, null=True)  # Field name made lowercase.
    sgk1 = models.FloatField(db_column='SGK1', blank=True, null=True)  # Field name made lowercase.
    map3k5 = models.FloatField(db_column='MAP3K5', blank=True, null=True)  # Field name made lowercase.
    cited2 = models.FloatField(db_column='CITED2', blank=True, null=True)  # Field name made lowercase.
    utrn = models.FloatField(db_column='UTRN', blank=True, null=True)  # Field name made lowercase.
    mthfd1l = models.FloatField(db_column='MTHFD1L', blank=True, null=True)  # Field name made lowercase.
    vip = models.FloatField(db_column='VIP', blank=True, null=True)  # Field name made lowercase.
    sod2 = models.FloatField(db_column='SOD2', blank=True, null=True)  # Field name made lowercase.
    lpa = models.FloatField(db_column='LPA', blank=True, null=True)  # Field name made lowercase.
    thbs2 = models.FloatField(db_column='THBS2', blank=True, null=True)  # Field name made lowercase.
    pdgfa = models.FloatField(db_column='PDGFA', blank=True, null=True)  # Field name made lowercase.
    il6 = models.FloatField(db_column='IL6', blank=True, null=True)  # Field name made lowercase.
    npy = models.FloatField(db_column='NPY', blank=True, null=True)  # Field name made lowercase.
    jazf1 = models.FloatField(db_column='JAZF1', blank=True, null=True)  # Field name made lowercase.
    cpvl = models.FloatField(db_column='CPVL', blank=True, null=True)  # Field name made lowercase.
    aqp1 = models.FloatField(db_column='AQP1', blank=True, null=True)  # Field name made lowercase.
    elmo1 = models.FloatField(db_column='ELMO1', blank=True, null=True)  # Field name made lowercase.
    igfbp3 = models.FloatField(db_column='IGFBP3', blank=True, null=True)  # Field name made lowercase.
    egfr = models.FloatField(db_column='EGFR', blank=True, null=True)  # Field name made lowercase.
    eln = models.FloatField(db_column='ELN', blank=True, null=True)  # Field name made lowercase.
    ncf1 = models.FloatField(db_column='NCF1', blank=True, null=True)  # Field name made lowercase.
    hspb1 = models.FloatField(db_column='HSPB1', blank=True, null=True)  # Field name made lowercase.
    sema3a = models.FloatField(db_column='SEMA3A', blank=True, null=True)  # Field name made lowercase.
    pon3 = models.FloatField(db_column='PON3', blank=True, null=True)  # Field name made lowercase.
    pon2 = models.FloatField(db_column='PON2', blank=True, null=True)  # Field name made lowercase.
    nampt = models.FloatField(db_column='NAMPT', blank=True, null=True)  # Field name made lowercase.
    cav1 = models.FloatField(db_column='CAV1', blank=True, null=True)  # Field name made lowercase.
    lep = models.FloatField(db_column='LEP', blank=True, null=True)  # Field name made lowercase.
    akr1b1 = models.FloatField(db_column='AKR1B1', blank=True, null=True)  # Field name made lowercase.
    akr1b10 = models.FloatField(db_column='AKR1B10', blank=True, null=True)  # Field name made lowercase.
    pip = models.FloatField(db_column='PIP', blank=True, null=True)  # Field name made lowercase.
    rarres2 = models.FloatField(db_column='RARRES2', blank=True, null=True)  # Field name made lowercase.
    nos3 = models.FloatField(db_column='NOS3', blank=True, null=True)  # Field name made lowercase.
    angpt2 = models.FloatField(db_column='ANGPT2', blank=True, null=True)  # Field name made lowercase.
    defa1 = models.FloatField(db_column='DEFA1', blank=True, null=True)  # Field name made lowercase.
    lpl = models.FloatField(db_column='LPL', blank=True, null=True)  # Field name made lowercase.
    ebf2 = models.FloatField(db_column='EBF2', blank=True, null=True)  # Field name made lowercase.
    adrb3 = models.FloatField(db_column='ADRB3', blank=True, null=True)  # Field name made lowercase.
    eif4ebp1 = models.FloatField(db_column='EIF4EBP1', blank=True, null=True)  # Field name made lowercase.
    fgfr1 = models.FloatField(db_column='FGFR1', blank=True, null=True)  # Field name made lowercase.
    crh = models.FloatField(db_column='CRH', blank=True, null=True)  # Field name made lowercase.
    sgk3 = models.FloatField(db_column='SGK3', blank=True, null=True)  # Field name made lowercase.
    fabp5 = models.FloatField(db_column='FABP5', blank=True, null=True)  # Field name made lowercase.
    fabp4 = models.FloatField(db_column='FABP4', blank=True, null=True)  # Field name made lowercase.
    mmp16 = models.FloatField(db_column='MMP16', blank=True, null=True)  # Field name made lowercase.
    ncald = models.FloatField(db_column='NCALD', blank=True, null=True)  # Field name made lowercase.
    klf10 = models.FloatField(db_column='KLF10', blank=True, null=True)  # Field name made lowercase.
    enpp2 = models.FloatField(db_column='ENPP2', blank=True, null=True)  # Field name made lowercase.
    pvt1 = models.FloatField(db_column='PVT1', blank=True, null=True)  # Field name made lowercase.
    jak2 = models.FloatField(db_column='JAK2', blank=True, null=True)  # Field name made lowercase.
    psip1 = models.FloatField(db_column='PSIP1', blank=True, null=True)  # Field name made lowercase.
    plin2 = models.FloatField(db_column='PLIN2', blank=True, null=True)  # Field name made lowercase.
    rps6 = models.FloatField(db_column='RPS6', blank=True, null=True)  # Field name made lowercase.
    aldh1a1 = models.FloatField(db_column='ALDH1A1', blank=True, null=True)  # Field name made lowercase.
    frmd3 = models.FloatField(db_column='FRMD3', blank=True, null=True)  # Field name made lowercase.
    gas1 = models.FloatField(db_column='GAS1', blank=True, null=True)  # Field name made lowercase.
    baat = models.FloatField(db_column='BAAT', blank=True, null=True)  # Field name made lowercase.
    abca1 = models.FloatField(db_column='ABCA1', blank=True, null=True)  # Field name made lowercase.
    txn = models.FloatField(db_column='TXN', blank=True, null=True)  # Field name made lowercase.
    ambp = models.FloatField(db_column='AMBP', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    hspa5 = models.FloatField(db_column='HSPA5', blank=True, null=True)  # Field name made lowercase.
    angptl2 = models.FloatField(db_column='ANGPTL2', blank=True, null=True)  # Field name made lowercase.
    ptges = models.FloatField(db_column='PTGES', blank=True, null=True)  # Field name made lowercase.
    tsc1 = models.FloatField(db_column='TSC1', blank=True, null=True)  # Field name made lowercase.
    abo = models.FloatField(db_column='ABO', blank=True, null=True)  # Field name made lowercase.
    adamts13 = models.FloatField(db_column='ADAMTS13', blank=True, null=True)  # Field name made lowercase.
    ptgds = models.FloatField(db_column='PTGDS', blank=True, null=True)  # Field name made lowercase.
    klf6 = models.FloatField(db_column='KLF6', blank=True, null=True)  # Field name made lowercase.
    cdc123 = models.FloatField(db_column='CDC123', blank=True, null=True)  # Field name made lowercase.
    bambi = models.FloatField(db_column='BAMBI', blank=True, null=True)  # Field name made lowercase.
    cxcl12 = models.FloatField(db_column='CXCL12', blank=True, null=True)  # Field name made lowercase.
    mbl2 = models.FloatField(db_column='MBL2', blank=True, null=True)  # Field name made lowercase.
    tfam = models.FloatField(db_column='TFAM', blank=True, null=True)  # Field name made lowercase.
    sirt1 = models.FloatField(db_column='SIRT1', blank=True, null=True)  # Field name made lowercase.
    srgn = models.FloatField(db_column='SRGN', blank=True, null=True)  # Field name made lowercase.
    unc5b = models.FloatField(db_column='UNC5B', blank=True, null=True)  # Field name made lowercase.
    adk = models.FloatField(db_column='ADK', blank=True, null=True)  # Field name made lowercase.
    pten = models.FloatField(db_column='PTEN', blank=True, null=True)  # Field name made lowercase.
    rbp4 = models.FloatField(db_column='RBP4', blank=True, null=True)  # Field name made lowercase.
    cyp2c19 = models.FloatField(db_column='CYP2C19', blank=True, null=True)  # Field name made lowercase.
    entpd1 = models.FloatField(db_column='ENTPD1', blank=True, null=True)  # Field name made lowercase.
    tcf7l2 = models.FloatField(db_column='TCF7L2', blank=True, null=True)  # Field name made lowercase.
    bnip3 = models.FloatField(db_column='BNIP3', blank=True, null=True)  # Field name made lowercase.
    igf2 = models.FloatField(db_column='IGF2', blank=True, null=True)  # Field name made lowercase.
    ins = models.FloatField(db_column='INS', blank=True, null=True)  # Field name made lowercase.
    th = models.FloatField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    kcnq1 = models.FloatField(db_column='KCNQ1', blank=True, null=True)  # Field name made lowercase.
    hbg2 = models.FloatField(db_column='HBG2', blank=True, null=True)  # Field name made lowercase.
    smpd1 = models.FloatField(db_column='SMPD1', blank=True, null=True)  # Field name made lowercase.
    ilk = models.FloatField(db_column='ILK', blank=True, null=True)  # Field name made lowercase.
    adm = models.FloatField(db_column='ADM', blank=True, null=True)  # Field name made lowercase.
    pth = models.FloatField(db_column='PTH', blank=True, null=True)  # Field name made lowercase.
    nucb2 = models.FloatField(db_column='NUCB2', blank=True, null=True)  # Field name made lowercase.
    kcnj11 = models.FloatField(db_column='KCNJ11', blank=True, null=True)  # Field name made lowercase.
    saa1 = models.FloatField(db_column='SAA1', blank=True, null=True)  # Field name made lowercase.
    bdnf = models.FloatField(db_column='BDNF', blank=True, null=True)  # Field name made lowercase.
    wt1 = models.FloatField(db_column='WT1', blank=True, null=True)  # Field name made lowercase.
    cd59 = models.FloatField(db_column='CD59', blank=True, null=True)  # Field name made lowercase.
    pdhx = models.FloatField(db_column='PDHX', blank=True, null=True)  # Field name made lowercase.
    traf6 = models.FloatField(db_column='TRAF6', blank=True, null=True)  # Field name made lowercase.
    api5 = models.FloatField(db_column='API5', blank=True, null=True)  # Field name made lowercase.
    nr1h3 = models.FloatField(db_column='NR1H3', blank=True, null=True)  # Field name made lowercase.
    ndufs3 = models.FloatField(db_column='NDUFS3', blank=True, null=True)  # Field name made lowercase.
    folh1 = models.FloatField(db_column='FOLH1', blank=True, null=True)  # Field name made lowercase.
    aplnr = models.FloatField(db_column='APLNR', blank=True, null=True)  # Field name made lowercase.
    p2rx3 = models.FloatField(db_column='P2RX3', blank=True, null=True)  # Field name made lowercase.
    cntf = models.FloatField(db_column='CNTF', blank=True, null=True)  # Field name made lowercase.
    fads1 = models.FloatField(db_column='FADS1', blank=True, null=True)  # Field name made lowercase.
    fads2 = models.FloatField(db_column='FADS2', blank=True, null=True)  # Field name made lowercase.
    fkbp2 = models.FloatField(db_column='FKBP2', blank=True, null=True)  # Field name made lowercase.
    syvn1 = models.FloatField(db_column='SYVN1', blank=True, null=True)  # Field name made lowercase.
    pc = models.FloatField(db_column='PC', blank=True, null=True)  # Field name made lowercase.
    dhcr7 = models.FloatField(db_column='DHCR7', blank=True, null=True)  # Field name made lowercase.
    prcp = models.FloatField(db_column='PRCP', blank=True, null=True)  # Field name made lowercase.
    nox4 = models.FloatField(db_column='NOX4', blank=True, null=True)  # Field name made lowercase.
    pdgfd = models.FloatField(db_column='PDGFD', blank=True, null=True)  # Field name made lowercase.
    atm = models.FloatField(db_column='ATM', blank=True, null=True)  # Field name made lowercase.
    il18 = models.FloatField(db_column='IL18', blank=True, null=True)  # Field name made lowercase.
    apoa1 = models.FloatField(db_column='APOA1', blank=True, null=True)  # Field name made lowercase.
    hyou1 = models.FloatField(db_column='HYOU1', blank=True, null=True)  # Field name made lowercase.
    esam = models.FloatField(db_column='ESAM', blank=True, null=True)  # Field name made lowercase.
    fkbp4 = models.FloatField(db_column='FKBP4', blank=True, null=True)  # Field name made lowercase.
    fgf23 = models.FloatField(db_column='FGF23', blank=True, null=True)  # Field name made lowercase.
    ntf3 = models.FloatField(db_column='NTF3', blank=True, null=True)  # Field name made lowercase.
    vwf = models.FloatField(db_column='VWF', blank=True, null=True)  # Field name made lowercase.
    cd9 = models.FloatField(db_column='CD9', blank=True, null=True)  # Field name made lowercase.
    gapdh = models.FloatField(db_column='GAPDH', blank=True, null=True)  # Field name made lowercase.
    cd4 = models.FloatField(db_column='CD4', blank=True, null=True)  # Field name made lowercase.
    gnb3 = models.FloatField(db_column='GNB3', blank=True, null=True)  # Field name made lowercase.
    cd163 = models.FloatField(db_column='CD163', blank=True, null=True)  # Field name made lowercase.
    slc2a3 = models.FloatField(db_column='SLC2A3', blank=True, null=True)  # Field name made lowercase.
    cd69 = models.FloatField(db_column='CD69', blank=True, null=True)  # Field name made lowercase.
    irak4 = models.FloatField(db_column='IRAK4', blank=True, null=True)  # Field name made lowercase.
    vdr = models.FloatField(db_column='VDR', blank=True, null=True)  # Field name made lowercase.
    aqp5 = models.FloatField(db_column='AQP5', blank=True, null=True)  # Field name made lowercase.
    acvrl1 = models.FloatField(db_column='ACVRL1', blank=True, null=True)  # Field name made lowercase.
    nfe2 = models.FloatField(db_column='NFE2', blank=True, null=True)  # Field name made lowercase.
    cd63 = models.FloatField(db_column='CD63', blank=True, null=True)  # Field name made lowercase.
    erbb3 = models.FloatField(db_column='ERBB3', blank=True, null=True)  # Field name made lowercase.
    ddit3 = models.FloatField(db_column='DDIT3', blank=True, null=True)  # Field name made lowercase.
    ifng = models.FloatField(db_column='IFNG', blank=True, null=True)  # Field name made lowercase.
    nts = models.FloatField(db_column='NTS', blank=True, null=True)  # Field name made lowercase.
    igf1 = models.FloatField(db_column='IGF1', blank=True, null=True)  # Field name made lowercase.
    acacb = models.FloatField(db_column='ACACB', blank=True, null=True)  # Field name made lowercase.
    trpv4 = models.FloatField(db_column='TRPV4', blank=True, null=True)  # Field name made lowercase.
    atp2a2 = models.FloatField(db_column='ATP2A2', blank=True, null=True)  # Field name made lowercase.
    aldh2 = models.FloatField(db_column='ALDH2', blank=True, null=True)  # Field name made lowercase.
    nos1 = models.FloatField(db_column='NOS1', blank=True, null=True)  # Field name made lowercase.
    pebp1 = models.FloatField(db_column='PEBP1', blank=True, null=True)  # Field name made lowercase.
    psmd9 = models.FloatField(db_column='PSMD9', blank=True, null=True)  # Field name made lowercase.
    scarb1 = models.FloatField(db_column='SCARB1', blank=True, null=True)  # Field name made lowercase.
    p2rx2 = models.FloatField(db_column='P2RX2', blank=True, null=True)  # Field name made lowercase.
    alox5ap = models.FloatField(db_column='ALOX5AP', blank=True, null=True)  # Field name made lowercase.
    kl = models.FloatField(db_column='KL', blank=True, null=True)  # Field name made lowercase.
    postn = models.FloatField(db_column='POSTN', blank=True, null=True)  # Field name made lowercase.
    foxo1 = models.FloatField(db_column='FOXO1', blank=True, null=True)  # Field name made lowercase.
    htr2a = models.FloatField(db_column='HTR2A', blank=True, null=True)  # Field name made lowercase.
    gpc5 = models.FloatField(db_column='GPC5', blank=True, null=True)  # Field name made lowercase.
    irs2 = models.FloatField(db_column='IRS2', blank=True, null=True)  # Field name made lowercase.
    gas6 = models.FloatField(db_column='GAS6', blank=True, null=True)  # Field name made lowercase.
    ang = models.FloatField(db_column='ANG', blank=True, null=True)  # Field name made lowercase.
    mmp14 = models.FloatField(db_column='MMP14', blank=True, null=True)  # Field name made lowercase.
    ltb4r2 = models.FloatField(db_column='LTB4R2', blank=True, null=True)  # Field name made lowercase.
    nfkbia = models.FloatField(db_column='NFKBIA', blank=True, null=True)  # Field name made lowercase.
    bmp4 = models.FloatField(db_column='BMP4', blank=True, null=True)  # Field name made lowercase.
    rtn1 = models.FloatField(db_column='RTN1', blank=True, null=True)  # Field name made lowercase.
    pgf = models.FloatField(db_column='PGF', blank=True, null=True)  # Field name made lowercase.
    ngb = models.FloatField(db_column='NGB', blank=True, null=True)  # Field name made lowercase.
    ahsa1 = models.FloatField(db_column='AHSA1', blank=True, null=True)  # Field name made lowercase.
    bdkrb2 = models.FloatField(db_column='BDKRB2', blank=True, null=True)  # Field name made lowercase.
    bdkrb1 = models.FloatField(db_column='BDKRB1', blank=True, null=True)  # Field name made lowercase.
    akt1 = models.FloatField(db_column='AKT1', blank=True, null=True)  # Field name made lowercase.
    grem1 = models.FloatField(db_column='GREM1', blank=True, null=True)  # Field name made lowercase.
    thbs1 = models.FloatField(db_column='THBS1', blank=True, null=True)  # Field name made lowercase.
    pak6 = models.FloatField(db_column='PAK6', blank=True, null=True)  # Field name made lowercase.
    b2m = models.FloatField(db_column='B2M', blank=True, null=True)  # Field name made lowercase.
    myo5c = models.FloatField(db_column='MYO5C', blank=True, null=True)  # Field name made lowercase.
    onecut1 = models.FloatField(db_column='ONECUT1', blank=True, null=True)  # Field name made lowercase.
    adam10 = models.FloatField(db_column='ADAM10', blank=True, null=True)  # Field name made lowercase.
    ctsh = models.FloatField(db_column='CTSH', blank=True, null=True)  # Field name made lowercase.
    plin1 = models.FloatField(db_column='PLIN1', blank=True, null=True)  # Field name made lowercase.
    igf1r = models.FloatField(db_column='IGF1R', blank=True, null=True)  # Field name made lowercase.
    mrpl28 = models.FloatField(db_column='MRPL28', blank=True, null=True)  # Field name made lowercase.
    cacna1h = models.FloatField(db_column='CACNA1H', blank=True, null=True)  # Field name made lowercase.
    pdpk1 = models.FloatField(db_column='PDPK1', blank=True, null=True)  # Field name made lowercase.
    ercc4 = models.FloatField(db_column='ERCC4', blank=True, null=True)  # Field name made lowercase.
    smg1 = models.FloatField(db_column='SMG1', blank=True, null=True)  # Field name made lowercase.
    itgam = models.FloatField(db_column='ITGAM', blank=True, null=True)  # Field name made lowercase.
    fto = models.FloatField(db_column='FTO', blank=True, null=True)  # Field name made lowercase.
    mmp2 = models.FloatField(db_column='MMP2', blank=True, null=True)  # Field name made lowercase.
    slc12a3 = models.FloatField(db_column='SLC12A3', blank=True, null=True)  # Field name made lowercase.
    cetp = models.FloatField(db_column='CETP', blank=True, null=True)  # Field name made lowercase.
    cx3cl1 = models.FloatField(db_column='CX3CL1', blank=True, null=True)  # Field name made lowercase.
    cdh1 = models.FloatField(db_column='CDH1', blank=True, null=True)  # Field name made lowercase.
    nqo1 = models.FloatField(db_column='NQO1', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    znrf1 = models.FloatField(db_column='ZNRF1', blank=True, null=True)  # Field name made lowercase.
    cyba = models.FloatField(db_column='CYBA', blank=True, null=True)  # Field name made lowercase.
    tubb3 = models.FloatField(db_column='TUBB3', blank=True, null=True)  # Field name made lowercase.
    crk = models.FloatField(db_column='CRK', blank=True, null=True)  # Field name made lowercase.
    serpinf2 = models.FloatField(db_column='SERPINF2', blank=True, null=True)  # Field name made lowercase.
    serpinf1 = models.FloatField(db_column='SERPINF1', blank=True, null=True)  # Field name made lowercase.
    trpv3 = models.FloatField(db_column='TRPV3', blank=True, null=True)  # Field name made lowercase.
    cxcl16 = models.FloatField(db_column='CXCL16', blank=True, null=True)  # Field name made lowercase.
    slc2a4 = models.FloatField(db_column='SLC2A4', blank=True, null=True)  # Field name made lowercase.
    cd68 = models.FloatField(db_column='CD68', blank=True, null=True)  # Field name made lowercase.
    shbg = models.FloatField(db_column='SHBG', blank=True, null=True)  # Field name made lowercase.
    pmp22 = models.FloatField(db_column='PMP22', blank=True, null=True)  # Field name made lowercase.
    srebf1 = models.FloatField(db_column='SREBF1', blank=True, null=True)  # Field name made lowercase.
    mapk7 = models.FloatField(db_column='MAPK7', blank=True, null=True)  # Field name made lowercase.
    ccl2 = models.FloatField(db_column='CCL2', blank=True, null=True)  # Field name made lowercase.
    ccl5 = models.FloatField(db_column='CCL5', blank=True, null=True)  # Field name made lowercase.
    hnf1b = models.FloatField(db_column='HNF1B', blank=True, null=True)  # Field name made lowercase.
    erbb2 = models.FloatField(db_column='ERBB2', blank=True, null=True)  # Field name made lowercase.
    fkbp10 = models.FloatField(db_column='FKBP10', blank=True, null=True)  # Field name made lowercase.
    stat5a = models.FloatField(db_column='STAT5A', blank=True, null=True)  # Field name made lowercase.
    stat3 = models.FloatField(db_column='STAT3', blank=True, null=True)  # Field name made lowercase.
    naglu = models.FloatField(db_column='NAGLU', blank=True, null=True)  # Field name made lowercase.
    aoc2 = models.FloatField(db_column='AOC2', blank=True, null=True)  # Field name made lowercase.
    aoc3 = models.FloatField(db_column='AOC3', blank=True, null=True)  # Field name made lowercase.
    ppy = models.FloatField(db_column='PPY', blank=True, null=True)  # Field name made lowercase.
    sth = models.FloatField(db_column='STH', blank=True, null=True)  # Field name made lowercase.
    itgb3 = models.FloatField(db_column='ITGB3', blank=True, null=True)  # Field name made lowercase.
    gip = models.FloatField(db_column='GIP', blank=True, null=True)  # Field name made lowercase.
    mpo = models.FloatField(db_column='MPO', blank=True, null=True)  # Field name made lowercase.
    pecam1 = models.FloatField(db_column='PECAM1', blank=True, null=True)  # Field name made lowercase.
    sox9 = models.FloatField(db_column='SOX9', blank=True, null=True)  # Field name made lowercase.
    timp2 = models.FloatField(db_column='TIMP2', blank=True, null=True)  # Field name made lowercase.
    dcxr = models.FloatField(db_column='DCXR', blank=True, null=True)  # Field name made lowercase.
    fasn = models.FloatField(db_column='FASN', blank=True, null=True)  # Field name made lowercase.
    colec12 = models.FloatField(db_column='COLEC12', blank=True, null=True)  # Field name made lowercase.
    adcyap1 = models.FloatField(db_column='ADCYAP1', blank=True, null=True)  # Field name made lowercase.
    smad7 = models.FloatField(db_column='SMAD7', blank=True, null=True)  # Field name made lowercase.
    nedd4l = models.FloatField(db_column='NEDD4L', blank=True, null=True)  # Field name made lowercase.
    mc4r = models.FloatField(db_column='MC4R', blank=True, null=True)  # Field name made lowercase.
    bcl2 = models.FloatField(db_column='BCL2', blank=True, null=True)  # Field name made lowercase.
    cndp2 = models.FloatField(db_column='CNDP2', blank=True, null=True)  # Field name made lowercase.
    znf236 = models.FloatField(db_column='ZNF236', blank=True, null=True)  # Field name made lowercase.
    stk11 = models.FloatField(db_column='STK11', blank=True, null=True)  # Field name made lowercase.
    sirt6 = models.FloatField(db_column='SIRT6', blank=True, null=True)  # Field name made lowercase.
    uhrf1 = models.FloatField(db_column='UHRF1', blank=True, null=True)  # Field name made lowercase.
    timm44 = models.FloatField(db_column='TIMM44', blank=True, null=True)  # Field name made lowercase.
    angptl4 = models.FloatField(db_column='ANGPTL4', blank=True, null=True)  # Field name made lowercase.
    dnmt1 = models.FloatField(db_column='DNMT1', blank=True, null=True)  # Field name made lowercase.
    icam1 = models.FloatField(db_column='ICAM1', blank=True, null=True)  # Field name made lowercase.
    ldlr = models.FloatField(db_column='LDLR', blank=True, null=True)  # Field name made lowercase.
    epor = models.FloatField(db_column='EPOR', blank=True, null=True)  # Field name made lowercase.
    prdx2 = models.FloatField(db_column='PRDX2', blank=True, null=True)  # Field name made lowercase.
    ptger1 = models.FloatField(db_column='PTGER1', blank=True, null=True)  # Field name made lowercase.
    unc13a = models.FloatField(db_column='UNC13A', blank=True, null=True)  # Field name made lowercase.
    gdf15 = models.FloatField(db_column='GDF15', blank=True, null=True)  # Field name made lowercase.
    fkbp8 = models.FloatField(db_column='FKBP8', blank=True, null=True)  # Field name made lowercase.
    usf2 = models.FloatField(db_column='USF2', blank=True, null=True)  # Field name made lowercase.
    ffar1 = models.FloatField(db_column='FFAR1', blank=True, null=True)  # Field name made lowercase.
    ffar2 = models.FloatField(db_column='FFAR2', blank=True, null=True)  # Field name made lowercase.
    nphs1 = models.FloatField(db_column='NPHS1', blank=True, null=True)  # Field name made lowercase.
    tgfb1 = models.FloatField(db_column='TGFB1', blank=True, null=True)  # Field name made lowercase.
    xrcc1 = models.FloatField(db_column='XRCC1', blank=True, null=True)  # Field name made lowercase.
    ercc1 = models.FloatField(db_column='ERCC1', blank=True, null=True)  # Field name made lowercase.
    gipr = models.FloatField(db_column='GIPR', blank=True, null=True)  # Field name made lowercase.
    fgf21 = models.FloatField(db_column='FGF21', blank=True, null=True)  # Field name made lowercase.
    clec11a = models.FloatField(db_column='CLEC11A', blank=True, null=True)  # Field name made lowercase.
    fpr1 = models.FloatField(db_column='FPR1', blank=True, null=True)  # Field name made lowercase.
    trib3 = models.FloatField(db_column='TRIB3', blank=True, null=True)  # Field name made lowercase.
    bmp2 = models.FloatField(db_column='BMP2', blank=True, null=True)  # Field name made lowercase.
    thbd = models.FloatField(db_column='THBD', blank=True, null=True)  # Field name made lowercase.
    cst3 = models.FloatField(db_column='CST3', blank=True, null=True)  # Field name made lowercase.
    id1 = models.FloatField(db_column='ID1', blank=True, null=True)  # Field name made lowercase.
    src = models.FloatField(db_column='SRC', blank=True, null=True)  # Field name made lowercase.
    mafb = models.FloatField(db_column='MAFB', blank=True, null=True)  # Field name made lowercase.
    sgk2 = models.FloatField(db_column='SGK2', blank=True, null=True)  # Field name made lowercase.
    hnf4a = models.FloatField(db_column='HNF4A', blank=True, null=True)  # Field name made lowercase.
    pltp = models.FloatField(db_column='PLTP', blank=True, null=True)  # Field name made lowercase.
    mmp9 = models.FloatField(db_column='MMP9', blank=True, null=True)  # Field name made lowercase.
    cd40 = models.FloatField(db_column='CD40', blank=True, null=True)  # Field name made lowercase.
    ptpn1 = models.FloatField(db_column='PTPN1', blank=True, null=True)  # Field name made lowercase.
    cyp24a1 = models.FloatField(db_column='CYP24A1', blank=True, null=True)  # Field name made lowercase.
    rcan1 = models.FloatField(db_column='RCAN1', blank=True, null=True)  # Field name made lowercase.
    abcg1 = models.FloatField(db_column='ABCG1', blank=True, null=True)  # Field name made lowercase.
    prmt2 = models.FloatField(db_column='PRMT2', blank=True, null=True)  # Field name made lowercase.
    comt = models.FloatField(db_column='COMT', blank=True, null=True)  # Field name made lowercase.
    mapk1 = models.FloatField(db_column='MAPK1', blank=True, null=True)  # Field name made lowercase.
    mif = models.FloatField(db_column='MIF', blank=True, null=True)  # Field name made lowercase.
    ggt1 = models.FloatField(db_column='GGT1', blank=True, null=True)  # Field name made lowercase.
    xbp1 = models.FloatField(db_column='XBP1', blank=True, null=True)  # Field name made lowercase.
    osm = models.FloatField(db_column='OSM', blank=True, null=True)  # Field name made lowercase.
    limk2 = models.FloatField(db_column='LIMK2', blank=True, null=True)  # Field name made lowercase.
    sfi1 = models.FloatField(db_column='SFI1', blank=True, null=True)  # Field name made lowercase.
    timp3 = models.FloatField(db_column='TIMP3', blank=True, null=True)  # Field name made lowercase.
    hmox1 = models.FloatField(db_column='HMOX1', blank=True, null=True)  # Field name made lowercase.
    apol1 = models.FloatField(db_column='APOL1', blank=True, null=True)  # Field name made lowercase.
    myh9 = models.FloatField(db_column='MYH9', blank=True, null=True)  # Field name made lowercase.
    pdgfb = models.FloatField(db_column='PDGFB', blank=True, null=True)  # Field name made lowercase.
    atf4 = models.FloatField(db_column='ATF4', blank=True, null=True)  # Field name made lowercase.
    tspo = models.FloatField(db_column='TSPO', blank=True, null=True)  # Field name made lowercase.
    miox = models.FloatField(db_column='MIOX', blank=True, null=True)  # Field name made lowercase.
    prdx4 = models.FloatField(db_column='PRDX4', blank=True, null=True)  # Field name made lowercase.
    gk = models.FloatField(db_column='GK', blank=True, null=True)  # Field name made lowercase.
    rgn = models.FloatField(db_column='RGN', blank=True, null=True)  # Field name made lowercase.
    timp1 = models.FloatField(db_column='TIMP1', blank=True, null=True)  # Field name made lowercase.
    clcn5 = models.FloatField(db_column='CLCN5', blank=True, null=True)  # Field name made lowercase.
    ar = models.FloatField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    foxo4 = models.FloatField(db_column='FOXO4', blank=True, null=True)  # Field name made lowercase.
    rps6ka6 = models.FloatField(db_column='RPS6KA6', blank=True, null=True)  # Field name made lowercase.
    nox1 = models.FloatField(db_column='NOX1', blank=True, null=True)  # Field name made lowercase.
    xiap = models.FloatField(db_column='XIAP', blank=True, null=True)  # Field name made lowercase.
    cd40lg = models.FloatField(db_column='CD40LG', blank=True, null=True)  # Field name made lowercase.
    l1cam = models.FloatField(db_column='L1CAM', blank=True, null=True)  # Field name made lowercase.
    irak1 = models.FloatField(db_column='IRAK1', blank=True, null=True)  # Field name made lowercase.
    g6pd = models.FloatField(db_column='G6PD', blank=True, null=True)  # Field name made lowercase.
    f8 = models.FloatField(db_column='F8', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diaco_tissue_artery_coronary'


class DiacoTissueBladder(models.Model):
    subjid = models.CharField(db_column='SUBJID', max_length=50, primary_key=True)  # Field name made lowercase.
    sampid = models.CharField(db_column='SAMPID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sesso = models.CharField(db_column='Sesso', max_length=1)  # Field name made lowercase.
    eta = models.CharField(db_column='Età', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errfi1 = models.FloatField(db_column='ERRFI1', blank=True, null=True)  # Field name made lowercase.
    mad2l2 = models.FloatField(db_column='MAD2L2', blank=True, null=True)  # Field name made lowercase.
    mthfr = models.FloatField(db_column='MTHFR', blank=True, null=True)  # Field name made lowercase.
    nppa = models.FloatField(db_column='NPPA', blank=True, null=True)  # Field name made lowercase.
    tnfrsf1b = models.FloatField(db_column='TNFRSF1B', blank=True, null=True)  # Field name made lowercase.
    pla2g2a = models.FloatField(db_column='PLA2G2A', blank=True, null=True)  # Field name made lowercase.
    alpl = models.FloatField(db_column='ALPL', blank=True, null=True)  # Field name made lowercase.
    hspg2 = models.FloatField(db_column='HSPG2', blank=True, null=True)  # Field name made lowercase.
    cnr2 = models.FloatField(db_column='CNR2', blank=True, null=True)  # Field name made lowercase.
    slc9a1 = models.FloatField(db_column='SLC9A1', blank=True, null=True)  # Field name made lowercase.
    col8a2 = models.FloatField(db_column='COL8A2', blank=True, null=True)  # Field name made lowercase.
    cap1 = models.FloatField(db_column='CAP1', blank=True, null=True)  # Field name made lowercase.
    slc2a1 = models.FloatField(db_column='SLC2A1', blank=True, null=True)  # Field name made lowercase.
    cyp2j2 = models.FloatField(db_column='CYP2J2', blank=True, null=True)  # Field name made lowercase.
    ddah1 = models.FloatField(db_column='DDAH1', blank=True, null=True)  # Field name made lowercase.
    cyr61 = models.FloatField(db_column='CYR61', blank=True, null=True)  # Field name made lowercase.
    ngf = models.FloatField(db_column='NGF', blank=True, null=True)  # Field name made lowercase.
    hmgcs2 = models.FloatField(db_column='HMGCS2', blank=True, null=True)  # Field name made lowercase.
    ctss = models.FloatField(db_column='CTSS', blank=True, null=True)  # Field name made lowercase.
    s100a12 = models.FloatField(db_column='S100A12', blank=True, null=True)  # Field name made lowercase.
    lmna = models.FloatField(db_column='LMNA', blank=True, null=True)  # Field name made lowercase.
    cd247 = models.FloatField(db_column='CD247', blank=True, null=True)  # Field name made lowercase.
    sele = models.FloatField(db_column='SELE', blank=True, null=True)  # Field name made lowercase.
    fmo3 = models.FloatField(db_column='FMO3', blank=True, null=True)  # Field name made lowercase.
    prdx6 = models.FloatField(db_column='PRDX6', blank=True, null=True)  # Field name made lowercase.
    glul = models.FloatField(db_column='GLUL', blank=True, null=True)  # Field name made lowercase.
    lamc1 = models.FloatField(db_column='LAMC1', blank=True, null=True)  # Field name made lowercase.
    ptgs2 = models.FloatField(db_column='PTGS2', blank=True, null=True)  # Field name made lowercase.
    chi3l1 = models.FloatField(db_column='CHI3L1', blank=True, null=True)  # Field name made lowercase.
    chit1 = models.FloatField(db_column='CHIT1', blank=True, null=True)  # Field name made lowercase.
    fmod = models.FloatField(db_column='FMOD', blank=True, null=True)  # Field name made lowercase.
    il10 = models.FloatField(db_column='IL10', blank=True, null=True)  # Field name made lowercase.
    pfkfb2 = models.FloatField(db_column='PFKFB2', blank=True, null=True)  # Field name made lowercase.
    cd34 = models.FloatField(db_column='CD34', blank=True, null=True)  # Field name made lowercase.
    cog2 = models.FloatField(db_column='COG2', blank=True, null=True)  # Field name made lowercase.
    nlrp3 = models.FloatField(db_column='NLRP3', blank=True, null=True)  # Field name made lowercase.
    rock2 = models.FloatField(db_column='ROCK2', blank=True, null=True)  # Field name made lowercase.
    apob = models.FloatField(db_column='APOB', blank=True, null=True)  # Field name made lowercase.
    pomc = models.FloatField(db_column='POMC', blank=True, null=True)  # Field name made lowercase.
    gckr = models.FloatField(db_column='GCKR', blank=True, null=True)  # Field name made lowercase.
    plekhh2 = models.FloatField(db_column='PLEKHH2', blank=True, null=True)  # Field name made lowercase.
    prkce = models.FloatField(db_column='PRKCE', blank=True, null=True)  # Field name made lowercase.
    pigf = models.FloatField(db_column='PIGF', blank=True, null=True)  # Field name made lowercase.
    msh2 = models.FloatField(db_column='MSH2', blank=True, null=True)  # Field name made lowercase.
    gfpt1 = models.FloatField(db_column='GFPT1', blank=True, null=True)  # Field name made lowercase.
    tacr1 = models.FloatField(db_column='TACR1', blank=True, null=True)  # Field name made lowercase.
    reg1a = models.FloatField(db_column='REG1A', blank=True, null=True)  # Field name made lowercase.
    eif2ak3 = models.FloatField(db_column='EIF2AK3', blank=True, null=True)  # Field name made lowercase.
    adra2b = models.FloatField(db_column='ADRA2B', blank=True, null=True)  # Field name made lowercase.
    il1b = models.FloatField(db_column='IL1B', blank=True, null=True)  # Field name made lowercase.
    proc = models.FloatField(db_column='PROC', blank=True, null=True)  # Field name made lowercase.
    polr2d = models.FloatField(db_column='POLR2D', blank=True, null=True)  # Field name made lowercase.
    zeb2 = models.FloatField(db_column='ZEB2', blank=True, null=True)  # Field name made lowercase.
    acvr1c = models.FloatField(db_column='ACVR1C', blank=True, null=True)  # Field name made lowercase.
    dpp4 = models.FloatField(db_column='DPP4', blank=True, null=True)  # Field name made lowercase.
    nfe2l2 = models.FloatField(db_column='NFE2L2', blank=True, null=True)  # Field name made lowercase.
    igfbp5 = models.FloatField(db_column='IGFBP5', blank=True, null=True)  # Field name made lowercase.
    ccl20 = models.FloatField(db_column='CCL20', blank=True, null=True)  # Field name made lowercase.
    hdac4 = models.FloatField(db_column='HDAC4', blank=True, null=True)  # Field name made lowercase.
    capn10 = models.FloatField(db_column='CAPN10', blank=True, null=True)  # Field name made lowercase.
    ghrl = models.FloatField(db_column='GHRL', blank=True, null=True)  # Field name made lowercase.
    pparg = models.FloatField(db_column='PPARG', blank=True, null=True)  # Field name made lowercase.
    raf1 = models.FloatField(db_column='RAF1', blank=True, null=True)  # Field name made lowercase.
    myd88 = models.FloatField(db_column='MYD88', blank=True, null=True)  # Field name made lowercase.
    cx3cr1 = models.FloatField(db_column='CX3CR1', blank=True, null=True)  # Field name made lowercase.
    cck = models.FloatField(db_column='CCK', blank=True, null=True)  # Field name made lowercase.
    exosc7 = models.FloatField(db_column='EXOSC7', blank=True, null=True)  # Field name made lowercase.
    ccr1 = models.FloatField(db_column='CCR1', blank=True, null=True)  # Field name made lowercase.
    ccr5 = models.FloatField(db_column='CCR5', blank=True, null=True)  # Field name made lowercase.
    gpx1 = models.FloatField(db_column='GPX1', blank=True, null=True)  # Field name made lowercase.
    rhoa = models.FloatField(db_column='RHOA', blank=True, null=True)  # Field name made lowercase.
    cish = models.FloatField(db_column='CISH', blank=True, null=True)  # Field name made lowercase.
    tkt = models.FloatField(db_column='TKT', blank=True, null=True)  # Field name made lowercase.
    appl1 = models.FloatField(db_column='APPL1', blank=True, null=True)  # Field name made lowercase.
    slmap = models.FloatField(db_column='SLMAP', blank=True, null=True)  # Field name made lowercase.
    col8a1 = models.FloatField(db_column='COL8A1', blank=True, null=True)  # Field name made lowercase.
    cd47 = models.FloatField(db_column='CD47', blank=True, null=True)  # Field name made lowercase.
    gap43 = models.FloatField(db_column='GAP43', blank=True, null=True)  # Field name made lowercase.
    cd80 = models.FloatField(db_column='CD80', blank=True, null=True)  # Field name made lowercase.
    rho = models.FloatField(db_column='RHO', blank=True, null=True)  # Field name made lowercase.
    trh = models.FloatField(db_column='TRH', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='TF', blank=True, null=True)  # Field name made lowercase.
    rbp1 = models.FloatField(db_column='RBP1', blank=True, null=True)  # Field name made lowercase.
    trpc1 = models.FloatField(db_column='TRPC1', blank=True, null=True)  # Field name made lowercase.
    agtr1 = models.FloatField(db_column='AGTR1', blank=True, null=True)  # Field name made lowercase.
    sucnr1 = models.FloatField(db_column='SUCNR1', blank=True, null=True)  # Field name made lowercase.
    p2ry1 = models.FloatField(db_column='P2RY1', blank=True, null=True)  # Field name made lowercase.
    mme = models.FloatField(db_column='MME', blank=True, null=True)  # Field name made lowercase.
    slc2a2 = models.FloatField(db_column='SLC2A2', blank=True, null=True)  # Field name made lowercase.
    pik3ca = models.FloatField(db_column='PIK3CA', blank=True, null=True)  # Field name made lowercase.
    parl = models.FloatField(db_column='PARL', blank=True, null=True)  # Field name made lowercase.
    ahsg = models.FloatField(db_column='AHSG', blank=True, null=True)  # Field name made lowercase.
    adipoq = models.FloatField(db_column='ADIPOQ', blank=True, null=True)  # Field name made lowercase.
    spon2 = models.FloatField(db_column='SPON2', blank=True, null=True)  # Field name made lowercase.
    wfs1 = models.FloatField(db_column='WFS1', blank=True, null=True)  # Field name made lowercase.
    cd38 = models.FloatField(db_column='CD38', blank=True, null=True)  # Field name made lowercase.
    prom1 = models.FloatField(db_column='PROM1', blank=True, null=True)  # Field name made lowercase.
    ppargc1a = models.FloatField(db_column='PPARGC1A', blank=True, null=True)  # Field name made lowercase.
    igfbp7 = models.FloatField(db_column='IGFBP7', blank=True, null=True)  # Field name made lowercase.
    cxcl5 = models.FloatField(db_column='CXCL5', blank=True, null=True)  # Field name made lowercase.
    cxcl9 = models.FloatField(db_column='CXCL9', blank=True, null=True)  # Field name made lowercase.
    cxcl10 = models.FloatField(db_column='CXCL10', blank=True, null=True)  # Field name made lowercase.
    cxcl11 = models.FloatField(db_column='CXCL11', blank=True, null=True)  # Field name made lowercase.
    hpse = models.FloatField(db_column='HPSE', blank=True, null=True)  # Field name made lowercase.
    spp1 = models.FloatField(db_column='SPP1', blank=True, null=True)  # Field name made lowercase.
    adh1b = models.FloatField(db_column='ADH1B', blank=True, null=True)  # Field name made lowercase.
    egf = models.FloatField(db_column='EGF', blank=True, null=True)  # Field name made lowercase.
    alpk1 = models.FloatField(db_column='ALPK1', blank=True, null=True)  # Field name made lowercase.
    fabp2 = models.FloatField(db_column='FABP2', blank=True, null=True)  # Field name made lowercase.
    pde5a = models.FloatField(db_column='PDE5A', blank=True, null=True)  # Field name made lowercase.
    setd7 = models.FloatField(db_column='SETD7', blank=True, null=True)  # Field name made lowercase.
    smad1 = models.FloatField(db_column='SMAD1', blank=True, null=True)  # Field name made lowercase.
    ednra = models.FloatField(db_column='EDNRA', blank=True, null=True)  # Field name made lowercase.
    nr3c2 = models.FloatField(db_column='NR3C2', blank=True, null=True)  # Field name made lowercase.
    tlr2 = models.FloatField(db_column='TLR2', blank=True, null=True)  # Field name made lowercase.
    npy5r = models.FloatField(db_column='NPY5R', blank=True, null=True)  # Field name made lowercase.
    fbxo8 = models.FloatField(db_column='FBXO8', blank=True, null=True)  # Field name made lowercase.
    vegfc = models.FloatField(db_column='VEGFC', blank=True, null=True)  # Field name made lowercase.
    acsl1 = models.FloatField(db_column='ACSL1', blank=True, null=True)  # Field name made lowercase.
    sorbs2 = models.FloatField(db_column='SORBS2', blank=True, null=True)  # Field name made lowercase.
    f11 = models.FloatField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    basp1 = models.FloatField(db_column='BASP1', blank=True, null=True)  # Field name made lowercase.
    ptger4 = models.FloatField(db_column='PTGER4', blank=True, null=True)  # Field name made lowercase.
    prkaa1 = models.FloatField(db_column='PRKAA1', blank=True, null=True)  # Field name made lowercase.
    ghr = models.FloatField(db_column='GHR', blank=True, null=True)  # Field name made lowercase.
    itga2 = models.FloatField(db_column='ITGA2', blank=True, null=True)  # Field name made lowercase.
    cdk7 = models.FloatField(db_column='CDK7', blank=True, null=True)  # Field name made lowercase.
    f2r = models.FloatField(db_column='F2R', blank=True, null=True)  # Field name made lowercase.
    erap2 = models.FloatField(db_column='ERAP2', blank=True, null=True)  # Field name made lowercase.
    apc = models.FloatField(db_column='APC', blank=True, null=True)  # Field name made lowercase.
    tnfaip8 = models.FloatField(db_column='TNFAIP8', blank=True, null=True)  # Field name made lowercase.
    vdac1 = models.FloatField(db_column='VDAC1', blank=True, null=True)  # Field name made lowercase.
    pdgfrb = models.FloatField(db_column='PDGFRB', blank=True, null=True)  # Field name made lowercase.
    cd74 = models.FloatField(db_column='CD74', blank=True, null=True)  # Field name made lowercase.
    sparc = models.FloatField(db_column='SPARC', blank=True, null=True)  # Field name made lowercase.
    ebf1 = models.FloatField(db_column='EBF1', blank=True, null=True)  # Field name made lowercase.
    gfpt2 = models.FloatField(db_column='GFPT2', blank=True, null=True)  # Field name made lowercase.
    rreb1 = models.FloatField(db_column='RREB1', blank=True, null=True)  # Field name made lowercase.
    edn1 = models.FloatField(db_column='EDN1', blank=True, null=True)  # Field name made lowercase.
    cdkal1 = models.FloatField(db_column='CDKAL1', blank=True, null=True)  # Field name made lowercase.
    hfe = models.FloatField(db_column='HFE', blank=True, null=True)  # Field name made lowercase.
    hla_a = models.FloatField(db_column='HLA-A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  # Field name made lowercase.
    tnf = models.FloatField(db_column='TNF', blank=True, null=True)  # Field name made lowercase.
    hspa1a = models.FloatField(db_column='HSPA1A', blank=True, null=True)  # Field name made lowercase.
    hspa1b = models.FloatField(db_column='HSPA1B', blank=True, null=True)  # Field name made lowercase.
    hla_dqa1 = models.FloatField(db_column='HLA-DQA1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mapk14 = models.FloatField(db_column='MAPK14', blank=True, null=True)  # Field name made lowercase.
    cdkn1a = models.FloatField(db_column='CDKN1A', blank=True, null=True)  # Field name made lowercase.
    glo1 = models.FloatField(db_column='GLO1', blank=True, null=True)  # Field name made lowercase.
    vegfa = models.FloatField(db_column='VEGFA', blank=True, null=True)  # Field name made lowercase.
    cd2ap = models.FloatField(db_column='CD2AP', blank=True, null=True)  # Field name made lowercase.
    cnr1 = models.FloatField(db_column='CNR1', blank=True, null=True)  # Field name made lowercase.
    enpp1 = models.FloatField(db_column='ENPP1', blank=True, null=True)  # Field name made lowercase.
    ctgf = models.FloatField(db_column='CTGF', blank=True, null=True)  # Field name made lowercase.
    rps12 = models.FloatField(db_column='RPS12', blank=True, null=True)  # Field name made lowercase.
    sgk1 = models.FloatField(db_column='SGK1', blank=True, null=True)  # Field name made lowercase.
    map3k5 = models.FloatField(db_column='MAP3K5', blank=True, null=True)  # Field name made lowercase.
    cited2 = models.FloatField(db_column='CITED2', blank=True, null=True)  # Field name made lowercase.
    utrn = models.FloatField(db_column='UTRN', blank=True, null=True)  # Field name made lowercase.
    mthfd1l = models.FloatField(db_column='MTHFD1L', blank=True, null=True)  # Field name made lowercase.
    vip = models.FloatField(db_column='VIP', blank=True, null=True)  # Field name made lowercase.
    sod2 = models.FloatField(db_column='SOD2', blank=True, null=True)  # Field name made lowercase.
    lpa = models.FloatField(db_column='LPA', blank=True, null=True)  # Field name made lowercase.
    thbs2 = models.FloatField(db_column='THBS2', blank=True, null=True)  # Field name made lowercase.
    pdgfa = models.FloatField(db_column='PDGFA', blank=True, null=True)  # Field name made lowercase.
    il6 = models.FloatField(db_column='IL6', blank=True, null=True)  # Field name made lowercase.
    npy = models.FloatField(db_column='NPY', blank=True, null=True)  # Field name made lowercase.
    jazf1 = models.FloatField(db_column='JAZF1', blank=True, null=True)  # Field name made lowercase.
    cpvl = models.FloatField(db_column='CPVL', blank=True, null=True)  # Field name made lowercase.
    aqp1 = models.FloatField(db_column='AQP1', blank=True, null=True)  # Field name made lowercase.
    elmo1 = models.FloatField(db_column='ELMO1', blank=True, null=True)  # Field name made lowercase.
    igfbp3 = models.FloatField(db_column='IGFBP3', blank=True, null=True)  # Field name made lowercase.
    egfr = models.FloatField(db_column='EGFR', blank=True, null=True)  # Field name made lowercase.
    eln = models.FloatField(db_column='ELN', blank=True, null=True)  # Field name made lowercase.
    ncf1 = models.FloatField(db_column='NCF1', blank=True, null=True)  # Field name made lowercase.
    hspb1 = models.FloatField(db_column='HSPB1', blank=True, null=True)  # Field name made lowercase.
    sema3a = models.FloatField(db_column='SEMA3A', blank=True, null=True)  # Field name made lowercase.
    pon3 = models.FloatField(db_column='PON3', blank=True, null=True)  # Field name made lowercase.
    pon2 = models.FloatField(db_column='PON2', blank=True, null=True)  # Field name made lowercase.
    nampt = models.FloatField(db_column='NAMPT', blank=True, null=True)  # Field name made lowercase.
    cav1 = models.FloatField(db_column='CAV1', blank=True, null=True)  # Field name made lowercase.
    lep = models.FloatField(db_column='LEP', blank=True, null=True)  # Field name made lowercase.
    akr1b1 = models.FloatField(db_column='AKR1B1', blank=True, null=True)  # Field name made lowercase.
    akr1b10 = models.FloatField(db_column='AKR1B10', blank=True, null=True)  # Field name made lowercase.
    pip = models.FloatField(db_column='PIP', blank=True, null=True)  # Field name made lowercase.
    rarres2 = models.FloatField(db_column='RARRES2', blank=True, null=True)  # Field name made lowercase.
    nos3 = models.FloatField(db_column='NOS3', blank=True, null=True)  # Field name made lowercase.
    angpt2 = models.FloatField(db_column='ANGPT2', blank=True, null=True)  # Field name made lowercase.
    defa1 = models.FloatField(db_column='DEFA1', blank=True, null=True)  # Field name made lowercase.
    lpl = models.FloatField(db_column='LPL', blank=True, null=True)  # Field name made lowercase.
    ebf2 = models.FloatField(db_column='EBF2', blank=True, null=True)  # Field name made lowercase.
    adrb3 = models.FloatField(db_column='ADRB3', blank=True, null=True)  # Field name made lowercase.
    eif4ebp1 = models.FloatField(db_column='EIF4EBP1', blank=True, null=True)  # Field name made lowercase.
    fgfr1 = models.FloatField(db_column='FGFR1', blank=True, null=True)  # Field name made lowercase.
    crh = models.FloatField(db_column='CRH', blank=True, null=True)  # Field name made lowercase.
    sgk3 = models.FloatField(db_column='SGK3', blank=True, null=True)  # Field name made lowercase.
    fabp5 = models.FloatField(db_column='FABP5', blank=True, null=True)  # Field name made lowercase.
    fabp4 = models.FloatField(db_column='FABP4', blank=True, null=True)  # Field name made lowercase.
    mmp16 = models.FloatField(db_column='MMP16', blank=True, null=True)  # Field name made lowercase.
    ncald = models.FloatField(db_column='NCALD', blank=True, null=True)  # Field name made lowercase.
    klf10 = models.FloatField(db_column='KLF10', blank=True, null=True)  # Field name made lowercase.
    enpp2 = models.FloatField(db_column='ENPP2', blank=True, null=True)  # Field name made lowercase.
    pvt1 = models.FloatField(db_column='PVT1', blank=True, null=True)  # Field name made lowercase.
    jak2 = models.FloatField(db_column='JAK2', blank=True, null=True)  # Field name made lowercase.
    psip1 = models.FloatField(db_column='PSIP1', blank=True, null=True)  # Field name made lowercase.
    plin2 = models.FloatField(db_column='PLIN2', blank=True, null=True)  # Field name made lowercase.
    rps6 = models.FloatField(db_column='RPS6', blank=True, null=True)  # Field name made lowercase.
    aldh1a1 = models.FloatField(db_column='ALDH1A1', blank=True, null=True)  # Field name made lowercase.
    frmd3 = models.FloatField(db_column='FRMD3', blank=True, null=True)  # Field name made lowercase.
    gas1 = models.FloatField(db_column='GAS1', blank=True, null=True)  # Field name made lowercase.
    baat = models.FloatField(db_column='BAAT', blank=True, null=True)  # Field name made lowercase.
    abca1 = models.FloatField(db_column='ABCA1', blank=True, null=True)  # Field name made lowercase.
    txn = models.FloatField(db_column='TXN', blank=True, null=True)  # Field name made lowercase.
    ambp = models.FloatField(db_column='AMBP', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    hspa5 = models.FloatField(db_column='HSPA5', blank=True, null=True)  # Field name made lowercase.
    angptl2 = models.FloatField(db_column='ANGPTL2', blank=True, null=True)  # Field name made lowercase.
    ptges = models.FloatField(db_column='PTGES', blank=True, null=True)  # Field name made lowercase.
    tsc1 = models.FloatField(db_column='TSC1', blank=True, null=True)  # Field name made lowercase.
    abo = models.FloatField(db_column='ABO', blank=True, null=True)  # Field name made lowercase.
    adamts13 = models.FloatField(db_column='ADAMTS13', blank=True, null=True)  # Field name made lowercase.
    ptgds = models.FloatField(db_column='PTGDS', blank=True, null=True)  # Field name made lowercase.
    klf6 = models.FloatField(db_column='KLF6', blank=True, null=True)  # Field name made lowercase.
    cdc123 = models.FloatField(db_column='CDC123', blank=True, null=True)  # Field name made lowercase.
    bambi = models.FloatField(db_column='BAMBI', blank=True, null=True)  # Field name made lowercase.
    cxcl12 = models.FloatField(db_column='CXCL12', blank=True, null=True)  # Field name made lowercase.
    mbl2 = models.FloatField(db_column='MBL2', blank=True, null=True)  # Field name made lowercase.
    tfam = models.FloatField(db_column='TFAM', blank=True, null=True)  # Field name made lowercase.
    sirt1 = models.FloatField(db_column='SIRT1', blank=True, null=True)  # Field name made lowercase.
    srgn = models.FloatField(db_column='SRGN', blank=True, null=True)  # Field name made lowercase.
    unc5b = models.FloatField(db_column='UNC5B', blank=True, null=True)  # Field name made lowercase.
    adk = models.FloatField(db_column='ADK', blank=True, null=True)  # Field name made lowercase.
    pten = models.FloatField(db_column='PTEN', blank=True, null=True)  # Field name made lowercase.
    rbp4 = models.FloatField(db_column='RBP4', blank=True, null=True)  # Field name made lowercase.
    cyp2c19 = models.FloatField(db_column='CYP2C19', blank=True, null=True)  # Field name made lowercase.
    entpd1 = models.FloatField(db_column='ENTPD1', blank=True, null=True)  # Field name made lowercase.
    tcf7l2 = models.FloatField(db_column='TCF7L2', blank=True, null=True)  # Field name made lowercase.
    bnip3 = models.FloatField(db_column='BNIP3', blank=True, null=True)  # Field name made lowercase.
    igf2 = models.FloatField(db_column='IGF2', blank=True, null=True)  # Field name made lowercase.
    ins = models.FloatField(db_column='INS', blank=True, null=True)  # Field name made lowercase.
    th = models.FloatField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    kcnq1 = models.FloatField(db_column='KCNQ1', blank=True, null=True)  # Field name made lowercase.
    hbg2 = models.FloatField(db_column='HBG2', blank=True, null=True)  # Field name made lowercase.
    smpd1 = models.FloatField(db_column='SMPD1', blank=True, null=True)  # Field name made lowercase.
    ilk = models.FloatField(db_column='ILK', blank=True, null=True)  # Field name made lowercase.
    adm = models.FloatField(db_column='ADM', blank=True, null=True)  # Field name made lowercase.
    pth = models.FloatField(db_column='PTH', blank=True, null=True)  # Field name made lowercase.
    nucb2 = models.FloatField(db_column='NUCB2', blank=True, null=True)  # Field name made lowercase.
    kcnj11 = models.FloatField(db_column='KCNJ11', blank=True, null=True)  # Field name made lowercase.
    saa1 = models.FloatField(db_column='SAA1', blank=True, null=True)  # Field name made lowercase.
    bdnf = models.FloatField(db_column='BDNF', blank=True, null=True)  # Field name made lowercase.
    wt1 = models.FloatField(db_column='WT1', blank=True, null=True)  # Field name made lowercase.
    cd59 = models.FloatField(db_column='CD59', blank=True, null=True)  # Field name made lowercase.
    pdhx = models.FloatField(db_column='PDHX', blank=True, null=True)  # Field name made lowercase.
    traf6 = models.FloatField(db_column='TRAF6', blank=True, null=True)  # Field name made lowercase.
    api5 = models.FloatField(db_column='API5', blank=True, null=True)  # Field name made lowercase.
    nr1h3 = models.FloatField(db_column='NR1H3', blank=True, null=True)  # Field name made lowercase.
    ndufs3 = models.FloatField(db_column='NDUFS3', blank=True, null=True)  # Field name made lowercase.
    folh1 = models.FloatField(db_column='FOLH1', blank=True, null=True)  # Field name made lowercase.
    aplnr = models.FloatField(db_column='APLNR', blank=True, null=True)  # Field name made lowercase.
    p2rx3 = models.FloatField(db_column='P2RX3', blank=True, null=True)  # Field name made lowercase.
    cntf = models.FloatField(db_column='CNTF', blank=True, null=True)  # Field name made lowercase.
    fads1 = models.FloatField(db_column='FADS1', blank=True, null=True)  # Field name made lowercase.
    fads2 = models.FloatField(db_column='FADS2', blank=True, null=True)  # Field name made lowercase.
    fkbp2 = models.FloatField(db_column='FKBP2', blank=True, null=True)  # Field name made lowercase.
    syvn1 = models.FloatField(db_column='SYVN1', blank=True, null=True)  # Field name made lowercase.
    pc = models.FloatField(db_column='PC', blank=True, null=True)  # Field name made lowercase.
    dhcr7 = models.FloatField(db_column='DHCR7', blank=True, null=True)  # Field name made lowercase.
    prcp = models.FloatField(db_column='PRCP', blank=True, null=True)  # Field name made lowercase.
    nox4 = models.FloatField(db_column='NOX4', blank=True, null=True)  # Field name made lowercase.
    pdgfd = models.FloatField(db_column='PDGFD', blank=True, null=True)  # Field name made lowercase.
    atm = models.FloatField(db_column='ATM', blank=True, null=True)  # Field name made lowercase.
    il18 = models.FloatField(db_column='IL18', blank=True, null=True)  # Field name made lowercase.
    apoa1 = models.FloatField(db_column='APOA1', blank=True, null=True)  # Field name made lowercase.
    hyou1 = models.FloatField(db_column='HYOU1', blank=True, null=True)  # Field name made lowercase.
    esam = models.FloatField(db_column='ESAM', blank=True, null=True)  # Field name made lowercase.
    fkbp4 = models.FloatField(db_column='FKBP4', blank=True, null=True)  # Field name made lowercase.
    fgf23 = models.FloatField(db_column='FGF23', blank=True, null=True)  # Field name made lowercase.
    ntf3 = models.FloatField(db_column='NTF3', blank=True, null=True)  # Field name made lowercase.
    vwf = models.FloatField(db_column='VWF', blank=True, null=True)  # Field name made lowercase.
    cd9 = models.FloatField(db_column='CD9', blank=True, null=True)  # Field name made lowercase.
    gapdh = models.FloatField(db_column='GAPDH', blank=True, null=True)  # Field name made lowercase.
    cd4 = models.FloatField(db_column='CD4', blank=True, null=True)  # Field name made lowercase.
    gnb3 = models.FloatField(db_column='GNB3', blank=True, null=True)  # Field name made lowercase.
    cd163 = models.FloatField(db_column='CD163', blank=True, null=True)  # Field name made lowercase.
    slc2a3 = models.FloatField(db_column='SLC2A3', blank=True, null=True)  # Field name made lowercase.
    cd69 = models.FloatField(db_column='CD69', blank=True, null=True)  # Field name made lowercase.
    irak4 = models.FloatField(db_column='IRAK4', blank=True, null=True)  # Field name made lowercase.
    vdr = models.FloatField(db_column='VDR', blank=True, null=True)  # Field name made lowercase.
    aqp5 = models.FloatField(db_column='AQP5', blank=True, null=True)  # Field name made lowercase.
    acvrl1 = models.FloatField(db_column='ACVRL1', blank=True, null=True)  # Field name made lowercase.
    nfe2 = models.FloatField(db_column='NFE2', blank=True, null=True)  # Field name made lowercase.
    cd63 = models.FloatField(db_column='CD63', blank=True, null=True)  # Field name made lowercase.
    erbb3 = models.FloatField(db_column='ERBB3', blank=True, null=True)  # Field name made lowercase.
    ddit3 = models.FloatField(db_column='DDIT3', blank=True, null=True)  # Field name made lowercase.
    ifng = models.FloatField(db_column='IFNG', blank=True, null=True)  # Field name made lowercase.
    nts = models.FloatField(db_column='NTS', blank=True, null=True)  # Field name made lowercase.
    igf1 = models.FloatField(db_column='IGF1', blank=True, null=True)  # Field name made lowercase.
    acacb = models.FloatField(db_column='ACACB', blank=True, null=True)  # Field name made lowercase.
    trpv4 = models.FloatField(db_column='TRPV4', blank=True, null=True)  # Field name made lowercase.
    atp2a2 = models.FloatField(db_column='ATP2A2', blank=True, null=True)  # Field name made lowercase.
    aldh2 = models.FloatField(db_column='ALDH2', blank=True, null=True)  # Field name made lowercase.
    nos1 = models.FloatField(db_column='NOS1', blank=True, null=True)  # Field name made lowercase.
    pebp1 = models.FloatField(db_column='PEBP1', blank=True, null=True)  # Field name made lowercase.
    psmd9 = models.FloatField(db_column='PSMD9', blank=True, null=True)  # Field name made lowercase.
    scarb1 = models.FloatField(db_column='SCARB1', blank=True, null=True)  # Field name made lowercase.
    p2rx2 = models.FloatField(db_column='P2RX2', blank=True, null=True)  # Field name made lowercase.
    alox5ap = models.FloatField(db_column='ALOX5AP', blank=True, null=True)  # Field name made lowercase.
    kl = models.FloatField(db_column='KL', blank=True, null=True)  # Field name made lowercase.
    postn = models.FloatField(db_column='POSTN', blank=True, null=True)  # Field name made lowercase.
    foxo1 = models.FloatField(db_column='FOXO1', blank=True, null=True)  # Field name made lowercase.
    htr2a = models.FloatField(db_column='HTR2A', blank=True, null=True)  # Field name made lowercase.
    gpc5 = models.FloatField(db_column='GPC5', blank=True, null=True)  # Field name made lowercase.
    irs2 = models.FloatField(db_column='IRS2', blank=True, null=True)  # Field name made lowercase.
    gas6 = models.FloatField(db_column='GAS6', blank=True, null=True)  # Field name made lowercase.
    ang = models.FloatField(db_column='ANG', blank=True, null=True)  # Field name made lowercase.
    mmp14 = models.FloatField(db_column='MMP14', blank=True, null=True)  # Field name made lowercase.
    ltb4r2 = models.FloatField(db_column='LTB4R2', blank=True, null=True)  # Field name made lowercase.
    nfkbia = models.FloatField(db_column='NFKBIA', blank=True, null=True)  # Field name made lowercase.
    bmp4 = models.FloatField(db_column='BMP4', blank=True, null=True)  # Field name made lowercase.
    rtn1 = models.FloatField(db_column='RTN1', blank=True, null=True)  # Field name made lowercase.
    pgf = models.FloatField(db_column='PGF', blank=True, null=True)  # Field name made lowercase.
    ngb = models.FloatField(db_column='NGB', blank=True, null=True)  # Field name made lowercase.
    ahsa1 = models.FloatField(db_column='AHSA1', blank=True, null=True)  # Field name made lowercase.
    bdkrb2 = models.FloatField(db_column='BDKRB2', blank=True, null=True)  # Field name made lowercase.
    bdkrb1 = models.FloatField(db_column='BDKRB1', blank=True, null=True)  # Field name made lowercase.
    akt1 = models.FloatField(db_column='AKT1', blank=True, null=True)  # Field name made lowercase.
    grem1 = models.FloatField(db_column='GREM1', blank=True, null=True)  # Field name made lowercase.
    thbs1 = models.FloatField(db_column='THBS1', blank=True, null=True)  # Field name made lowercase.
    pak6 = models.FloatField(db_column='PAK6', blank=True, null=True)  # Field name made lowercase.
    b2m = models.FloatField(db_column='B2M', blank=True, null=True)  # Field name made lowercase.
    myo5c = models.FloatField(db_column='MYO5C', blank=True, null=True)  # Field name made lowercase.
    onecut1 = models.FloatField(db_column='ONECUT1', blank=True, null=True)  # Field name made lowercase.
    adam10 = models.FloatField(db_column='ADAM10', blank=True, null=True)  # Field name made lowercase.
    ctsh = models.FloatField(db_column='CTSH', blank=True, null=True)  # Field name made lowercase.
    plin1 = models.FloatField(db_column='PLIN1', blank=True, null=True)  # Field name made lowercase.
    igf1r = models.FloatField(db_column='IGF1R', blank=True, null=True)  # Field name made lowercase.
    mrpl28 = models.FloatField(db_column='MRPL28', blank=True, null=True)  # Field name made lowercase.
    cacna1h = models.FloatField(db_column='CACNA1H', blank=True, null=True)  # Field name made lowercase.
    pdpk1 = models.FloatField(db_column='PDPK1', blank=True, null=True)  # Field name made lowercase.
    ercc4 = models.FloatField(db_column='ERCC4', blank=True, null=True)  # Field name made lowercase.
    smg1 = models.FloatField(db_column='SMG1', blank=True, null=True)  # Field name made lowercase.
    itgam = models.FloatField(db_column='ITGAM', blank=True, null=True)  # Field name made lowercase.
    fto = models.FloatField(db_column='FTO', blank=True, null=True)  # Field name made lowercase.
    mmp2 = models.FloatField(db_column='MMP2', blank=True, null=True)  # Field name made lowercase.
    slc12a3 = models.FloatField(db_column='SLC12A3', blank=True, null=True)  # Field name made lowercase.
    cetp = models.FloatField(db_column='CETP', blank=True, null=True)  # Field name made lowercase.
    cx3cl1 = models.FloatField(db_column='CX3CL1', blank=True, null=True)  # Field name made lowercase.
    cdh1 = models.FloatField(db_column='CDH1', blank=True, null=True)  # Field name made lowercase.
    nqo1 = models.FloatField(db_column='NQO1', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    znrf1 = models.FloatField(db_column='ZNRF1', blank=True, null=True)  # Field name made lowercase.
    cyba = models.FloatField(db_column='CYBA', blank=True, null=True)  # Field name made lowercase.
    tubb3 = models.FloatField(db_column='TUBB3', blank=True, null=True)  # Field name made lowercase.
    crk = models.FloatField(db_column='CRK', blank=True, null=True)  # Field name made lowercase.
    serpinf2 = models.FloatField(db_column='SERPINF2', blank=True, null=True)  # Field name made lowercase.
    serpinf1 = models.FloatField(db_column='SERPINF1', blank=True, null=True)  # Field name made lowercase.
    trpv3 = models.FloatField(db_column='TRPV3', blank=True, null=True)  # Field name made lowercase.
    cxcl16 = models.FloatField(db_column='CXCL16', blank=True, null=True)  # Field name made lowercase.
    slc2a4 = models.FloatField(db_column='SLC2A4', blank=True, null=True)  # Field name made lowercase.
    cd68 = models.FloatField(db_column='CD68', blank=True, null=True)  # Field name made lowercase.
    shbg = models.FloatField(db_column='SHBG', blank=True, null=True)  # Field name made lowercase.
    pmp22 = models.FloatField(db_column='PMP22', blank=True, null=True)  # Field name made lowercase.
    srebf1 = models.FloatField(db_column='SREBF1', blank=True, null=True)  # Field name made lowercase.
    mapk7 = models.FloatField(db_column='MAPK7', blank=True, null=True)  # Field name made lowercase.
    ccl2 = models.FloatField(db_column='CCL2', blank=True, null=True)  # Field name made lowercase.
    ccl5 = models.FloatField(db_column='CCL5', blank=True, null=True)  # Field name made lowercase.
    hnf1b = models.FloatField(db_column='HNF1B', blank=True, null=True)  # Field name made lowercase.
    erbb2 = models.FloatField(db_column='ERBB2', blank=True, null=True)  # Field name made lowercase.
    fkbp10 = models.FloatField(db_column='FKBP10', blank=True, null=True)  # Field name made lowercase.
    stat5a = models.FloatField(db_column='STAT5A', blank=True, null=True)  # Field name made lowercase.
    stat3 = models.FloatField(db_column='STAT3', blank=True, null=True)  # Field name made lowercase.
    naglu = models.FloatField(db_column='NAGLU', blank=True, null=True)  # Field name made lowercase.
    aoc2 = models.FloatField(db_column='AOC2', blank=True, null=True)  # Field name made lowercase.
    aoc3 = models.FloatField(db_column='AOC3', blank=True, null=True)  # Field name made lowercase.
    ppy = models.FloatField(db_column='PPY', blank=True, null=True)  # Field name made lowercase.
    sth = models.FloatField(db_column='STH', blank=True, null=True)  # Field name made lowercase.
    itgb3 = models.FloatField(db_column='ITGB3', blank=True, null=True)  # Field name made lowercase.
    gip = models.FloatField(db_column='GIP', blank=True, null=True)  # Field name made lowercase.
    mpo = models.FloatField(db_column='MPO', blank=True, null=True)  # Field name made lowercase.
    pecam1 = models.FloatField(db_column='PECAM1', blank=True, null=True)  # Field name made lowercase.
    sox9 = models.FloatField(db_column='SOX9', blank=True, null=True)  # Field name made lowercase.
    timp2 = models.FloatField(db_column='TIMP2', blank=True, null=True)  # Field name made lowercase.
    dcxr = models.FloatField(db_column='DCXR', blank=True, null=True)  # Field name made lowercase.
    fasn = models.FloatField(db_column='FASN', blank=True, null=True)  # Field name made lowercase.
    colec12 = models.FloatField(db_column='COLEC12', blank=True, null=True)  # Field name made lowercase.
    adcyap1 = models.FloatField(db_column='ADCYAP1', blank=True, null=True)  # Field name made lowercase.
    smad7 = models.FloatField(db_column='SMAD7', blank=True, null=True)  # Field name made lowercase.
    nedd4l = models.FloatField(db_column='NEDD4L', blank=True, null=True)  # Field name made lowercase.
    mc4r = models.FloatField(db_column='MC4R', blank=True, null=True)  # Field name made lowercase.
    bcl2 = models.FloatField(db_column='BCL2', blank=True, null=True)  # Field name made lowercase.
    cndp2 = models.FloatField(db_column='CNDP2', blank=True, null=True)  # Field name made lowercase.
    znf236 = models.FloatField(db_column='ZNF236', blank=True, null=True)  # Field name made lowercase.
    stk11 = models.FloatField(db_column='STK11', blank=True, null=True)  # Field name made lowercase.
    sirt6 = models.FloatField(db_column='SIRT6', blank=True, null=True)  # Field name made lowercase.
    uhrf1 = models.FloatField(db_column='UHRF1', blank=True, null=True)  # Field name made lowercase.
    timm44 = models.FloatField(db_column='TIMM44', blank=True, null=True)  # Field name made lowercase.
    angptl4 = models.FloatField(db_column='ANGPTL4', blank=True, null=True)  # Field name made lowercase.
    dnmt1 = models.FloatField(db_column='DNMT1', blank=True, null=True)  # Field name made lowercase.
    icam1 = models.FloatField(db_column='ICAM1', blank=True, null=True)  # Field name made lowercase.
    ldlr = models.FloatField(db_column='LDLR', blank=True, null=True)  # Field name made lowercase.
    epor = models.FloatField(db_column='EPOR', blank=True, null=True)  # Field name made lowercase.
    prdx2 = models.FloatField(db_column='PRDX2', blank=True, null=True)  # Field name made lowercase.
    ptger1 = models.FloatField(db_column='PTGER1', blank=True, null=True)  # Field name made lowercase.
    unc13a = models.FloatField(db_column='UNC13A', blank=True, null=True)  # Field name made lowercase.
    gdf15 = models.FloatField(db_column='GDF15', blank=True, null=True)  # Field name made lowercase.
    fkbp8 = models.FloatField(db_column='FKBP8', blank=True, null=True)  # Field name made lowercase.
    usf2 = models.FloatField(db_column='USF2', blank=True, null=True)  # Field name made lowercase.
    ffar1 = models.FloatField(db_column='FFAR1', blank=True, null=True)  # Field name made lowercase.
    ffar2 = models.FloatField(db_column='FFAR2', blank=True, null=True)  # Field name made lowercase.
    nphs1 = models.FloatField(db_column='NPHS1', blank=True, null=True)  # Field name made lowercase.
    tgfb1 = models.FloatField(db_column='TGFB1', blank=True, null=True)  # Field name made lowercase.
    xrcc1 = models.FloatField(db_column='XRCC1', blank=True, null=True)  # Field name made lowercase.
    ercc1 = models.FloatField(db_column='ERCC1', blank=True, null=True)  # Field name made lowercase.
    gipr = models.FloatField(db_column='GIPR', blank=True, null=True)  # Field name made lowercase.
    fgf21 = models.FloatField(db_column='FGF21', blank=True, null=True)  # Field name made lowercase.
    clec11a = models.FloatField(db_column='CLEC11A', blank=True, null=True)  # Field name made lowercase.
    fpr1 = models.FloatField(db_column='FPR1', blank=True, null=True)  # Field name made lowercase.
    trib3 = models.FloatField(db_column='TRIB3', blank=True, null=True)  # Field name made lowercase.
    bmp2 = models.FloatField(db_column='BMP2', blank=True, null=True)  # Field name made lowercase.
    thbd = models.FloatField(db_column='THBD', blank=True, null=True)  # Field name made lowercase.
    cst3 = models.FloatField(db_column='CST3', blank=True, null=True)  # Field name made lowercase.
    id1 = models.FloatField(db_column='ID1', blank=True, null=True)  # Field name made lowercase.
    src = models.FloatField(db_column='SRC', blank=True, null=True)  # Field name made lowercase.
    mafb = models.FloatField(db_column='MAFB', blank=True, null=True)  # Field name made lowercase.
    sgk2 = models.FloatField(db_column='SGK2', blank=True, null=True)  # Field name made lowercase.
    hnf4a = models.FloatField(db_column='HNF4A', blank=True, null=True)  # Field name made lowercase.
    pltp = models.FloatField(db_column='PLTP', blank=True, null=True)  # Field name made lowercase.
    mmp9 = models.FloatField(db_column='MMP9', blank=True, null=True)  # Field name made lowercase.
    cd40 = models.FloatField(db_column='CD40', blank=True, null=True)  # Field name made lowercase.
    ptpn1 = models.FloatField(db_column='PTPN1', blank=True, null=True)  # Field name made lowercase.
    cyp24a1 = models.FloatField(db_column='CYP24A1', blank=True, null=True)  # Field name made lowercase.
    rcan1 = models.FloatField(db_column='RCAN1', blank=True, null=True)  # Field name made lowercase.
    abcg1 = models.FloatField(db_column='ABCG1', blank=True, null=True)  # Field name made lowercase.
    prmt2 = models.FloatField(db_column='PRMT2', blank=True, null=True)  # Field name made lowercase.
    comt = models.FloatField(db_column='COMT', blank=True, null=True)  # Field name made lowercase.
    mapk1 = models.FloatField(db_column='MAPK1', blank=True, null=True)  # Field name made lowercase.
    mif = models.FloatField(db_column='MIF', blank=True, null=True)  # Field name made lowercase.
    ggt1 = models.FloatField(db_column='GGT1', blank=True, null=True)  # Field name made lowercase.
    xbp1 = models.FloatField(db_column='XBP1', blank=True, null=True)  # Field name made lowercase.
    osm = models.FloatField(db_column='OSM', blank=True, null=True)  # Field name made lowercase.
    limk2 = models.FloatField(db_column='LIMK2', blank=True, null=True)  # Field name made lowercase.
    sfi1 = models.FloatField(db_column='SFI1', blank=True, null=True)  # Field name made lowercase.
    timp3 = models.FloatField(db_column='TIMP3', blank=True, null=True)  # Field name made lowercase.
    hmox1 = models.FloatField(db_column='HMOX1', blank=True, null=True)  # Field name made lowercase.
    apol1 = models.FloatField(db_column='APOL1', blank=True, null=True)  # Field name made lowercase.
    myh9 = models.FloatField(db_column='MYH9', blank=True, null=True)  # Field name made lowercase.
    pdgfb = models.FloatField(db_column='PDGFB', blank=True, null=True)  # Field name made lowercase.
    atf4 = models.FloatField(db_column='ATF4', blank=True, null=True)  # Field name made lowercase.
    tspo = models.FloatField(db_column='TSPO', blank=True, null=True)  # Field name made lowercase.
    miox = models.FloatField(db_column='MIOX', blank=True, null=True)  # Field name made lowercase.
    prdx4 = models.FloatField(db_column='PRDX4', blank=True, null=True)  # Field name made lowercase.
    gk = models.FloatField(db_column='GK', blank=True, null=True)  # Field name made lowercase.
    rgn = models.FloatField(db_column='RGN', blank=True, null=True)  # Field name made lowercase.
    timp1 = models.FloatField(db_column='TIMP1', blank=True, null=True)  # Field name made lowercase.
    clcn5 = models.FloatField(db_column='CLCN5', blank=True, null=True)  # Field name made lowercase.
    ar = models.FloatField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    foxo4 = models.FloatField(db_column='FOXO4', blank=True, null=True)  # Field name made lowercase.
    rps6ka6 = models.FloatField(db_column='RPS6KA6', blank=True, null=True)  # Field name made lowercase.
    nox1 = models.FloatField(db_column='NOX1', blank=True, null=True)  # Field name made lowercase.
    xiap = models.FloatField(db_column='XIAP', blank=True, null=True)  # Field name made lowercase.
    cd40lg = models.FloatField(db_column='CD40LG', blank=True, null=True)  # Field name made lowercase.
    l1cam = models.FloatField(db_column='L1CAM', blank=True, null=True)  # Field name made lowercase.
    irak1 = models.FloatField(db_column='IRAK1', blank=True, null=True)  # Field name made lowercase.
    g6pd = models.FloatField(db_column='G6PD', blank=True, null=True)  # Field name made lowercase.
    f8 = models.FloatField(db_column='F8', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diaco_tissue_bladder'


class DiacoTissueBrainAmygdala(models.Model):
    subjid = models.CharField(db_column='SUBJID', max_length=50, primary_key=True)  # Field name made lowercase.
    sampid = models.CharField(db_column='SAMPID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sesso = models.CharField(db_column='Sesso', max_length=1)  # Field name made lowercase.
    eta = models.CharField(db_column='Età', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errfi1 = models.FloatField(db_column='ERRFI1', blank=True, null=True)  # Field name made lowercase.
    mad2l2 = models.FloatField(db_column='MAD2L2', blank=True, null=True)  # Field name made lowercase.
    mthfr = models.FloatField(db_column='MTHFR', blank=True, null=True)  # Field name made lowercase.
    nppa = models.FloatField(db_column='NPPA', blank=True, null=True)  # Field name made lowercase.
    tnfrsf1b = models.FloatField(db_column='TNFRSF1B', blank=True, null=True)  # Field name made lowercase.
    pla2g2a = models.FloatField(db_column='PLA2G2A', blank=True, null=True)  # Field name made lowercase.
    alpl = models.FloatField(db_column='ALPL', blank=True, null=True)  # Field name made lowercase.
    hspg2 = models.FloatField(db_column='HSPG2', blank=True, null=True)  # Field name made lowercase.
    cnr2 = models.FloatField(db_column='CNR2', blank=True, null=True)  # Field name made lowercase.
    slc9a1 = models.FloatField(db_column='SLC9A1', blank=True, null=True)  # Field name made lowercase.
    col8a2 = models.FloatField(db_column='COL8A2', blank=True, null=True)  # Field name made lowercase.
    cap1 = models.FloatField(db_column='CAP1', blank=True, null=True)  # Field name made lowercase.
    slc2a1 = models.FloatField(db_column='SLC2A1', blank=True, null=True)  # Field name made lowercase.
    cyp2j2 = models.FloatField(db_column='CYP2J2', blank=True, null=True)  # Field name made lowercase.
    ddah1 = models.FloatField(db_column='DDAH1', blank=True, null=True)  # Field name made lowercase.
    cyr61 = models.FloatField(db_column='CYR61', blank=True, null=True)  # Field name made lowercase.
    ngf = models.FloatField(db_column='NGF', blank=True, null=True)  # Field name made lowercase.
    hmgcs2 = models.FloatField(db_column='HMGCS2', blank=True, null=True)  # Field name made lowercase.
    ctss = models.FloatField(db_column='CTSS', blank=True, null=True)  # Field name made lowercase.
    s100a12 = models.FloatField(db_column='S100A12', blank=True, null=True)  # Field name made lowercase.
    lmna = models.FloatField(db_column='LMNA', blank=True, null=True)  # Field name made lowercase.
    cd247 = models.FloatField(db_column='CD247', blank=True, null=True)  # Field name made lowercase.
    sele = models.FloatField(db_column='SELE', blank=True, null=True)  # Field name made lowercase.
    fmo3 = models.FloatField(db_column='FMO3', blank=True, null=True)  # Field name made lowercase.
    prdx6 = models.FloatField(db_column='PRDX6', blank=True, null=True)  # Field name made lowercase.
    glul = models.FloatField(db_column='GLUL', blank=True, null=True)  # Field name made lowercase.
    lamc1 = models.FloatField(db_column='LAMC1', blank=True, null=True)  # Field name made lowercase.
    ptgs2 = models.FloatField(db_column='PTGS2', blank=True, null=True)  # Field name made lowercase.
    chi3l1 = models.FloatField(db_column='CHI3L1', blank=True, null=True)  # Field name made lowercase.
    chit1 = models.FloatField(db_column='CHIT1', blank=True, null=True)  # Field name made lowercase.
    fmod = models.FloatField(db_column='FMOD', blank=True, null=True)  # Field name made lowercase.
    il10 = models.FloatField(db_column='IL10', blank=True, null=True)  # Field name made lowercase.
    pfkfb2 = models.FloatField(db_column='PFKFB2', blank=True, null=True)  # Field name made lowercase.
    cd34 = models.FloatField(db_column='CD34', blank=True, null=True)  # Field name made lowercase.
    cog2 = models.FloatField(db_column='COG2', blank=True, null=True)  # Field name made lowercase.
    nlrp3 = models.FloatField(db_column='NLRP3', blank=True, null=True)  # Field name made lowercase.
    rock2 = models.FloatField(db_column='ROCK2', blank=True, null=True)  # Field name made lowercase.
    apob = models.FloatField(db_column='APOB', blank=True, null=True)  # Field name made lowercase.
    pomc = models.FloatField(db_column='POMC', blank=True, null=True)  # Field name made lowercase.
    gckr = models.FloatField(db_column='GCKR', blank=True, null=True)  # Field name made lowercase.
    plekhh2 = models.FloatField(db_column='PLEKHH2', blank=True, null=True)  # Field name made lowercase.
    prkce = models.FloatField(db_column='PRKCE', blank=True, null=True)  # Field name made lowercase.
    pigf = models.FloatField(db_column='PIGF', blank=True, null=True)  # Field name made lowercase.
    msh2 = models.FloatField(db_column='MSH2', blank=True, null=True)  # Field name made lowercase.
    gfpt1 = models.FloatField(db_column='GFPT1', blank=True, null=True)  # Field name made lowercase.
    tacr1 = models.FloatField(db_column='TACR1', blank=True, null=True)  # Field name made lowercase.
    reg1a = models.FloatField(db_column='REG1A', blank=True, null=True)  # Field name made lowercase.
    eif2ak3 = models.FloatField(db_column='EIF2AK3', blank=True, null=True)  # Field name made lowercase.
    adra2b = models.FloatField(db_column='ADRA2B', blank=True, null=True)  # Field name made lowercase.
    il1b = models.FloatField(db_column='IL1B', blank=True, null=True)  # Field name made lowercase.
    proc = models.FloatField(db_column='PROC', blank=True, null=True)  # Field name made lowercase.
    polr2d = models.FloatField(db_column='POLR2D', blank=True, null=True)  # Field name made lowercase.
    zeb2 = models.FloatField(db_column='ZEB2', blank=True, null=True)  # Field name made lowercase.
    acvr1c = models.FloatField(db_column='ACVR1C', blank=True, null=True)  # Field name made lowercase.
    dpp4 = models.FloatField(db_column='DPP4', blank=True, null=True)  # Field name made lowercase.
    nfe2l2 = models.FloatField(db_column='NFE2L2', blank=True, null=True)  # Field name made lowercase.
    igfbp5 = models.FloatField(db_column='IGFBP5', blank=True, null=True)  # Field name made lowercase.
    ccl20 = models.FloatField(db_column='CCL20', blank=True, null=True)  # Field name made lowercase.
    hdac4 = models.FloatField(db_column='HDAC4', blank=True, null=True)  # Field name made lowercase.
    capn10 = models.FloatField(db_column='CAPN10', blank=True, null=True)  # Field name made lowercase.
    ghrl = models.FloatField(db_column='GHRL', blank=True, null=True)  # Field name made lowercase.
    pparg = models.FloatField(db_column='PPARG', blank=True, null=True)  # Field name made lowercase.
    raf1 = models.FloatField(db_column='RAF1', blank=True, null=True)  # Field name made lowercase.
    myd88 = models.FloatField(db_column='MYD88', blank=True, null=True)  # Field name made lowercase.
    cx3cr1 = models.FloatField(db_column='CX3CR1', blank=True, null=True)  # Field name made lowercase.
    cck = models.FloatField(db_column='CCK', blank=True, null=True)  # Field name made lowercase.
    exosc7 = models.FloatField(db_column='EXOSC7', blank=True, null=True)  # Field name made lowercase.
    ccr1 = models.FloatField(db_column='CCR1', blank=True, null=True)  # Field name made lowercase.
    ccr5 = models.FloatField(db_column='CCR5', blank=True, null=True)  # Field name made lowercase.
    gpx1 = models.FloatField(db_column='GPX1', blank=True, null=True)  # Field name made lowercase.
    rhoa = models.FloatField(db_column='RHOA', blank=True, null=True)  # Field name made lowercase.
    cish = models.FloatField(db_column='CISH', blank=True, null=True)  # Field name made lowercase.
    tkt = models.FloatField(db_column='TKT', blank=True, null=True)  # Field name made lowercase.
    appl1 = models.FloatField(db_column='APPL1', blank=True, null=True)  # Field name made lowercase.
    slmap = models.FloatField(db_column='SLMAP', blank=True, null=True)  # Field name made lowercase.
    col8a1 = models.FloatField(db_column='COL8A1', blank=True, null=True)  # Field name made lowercase.
    cd47 = models.FloatField(db_column='CD47', blank=True, null=True)  # Field name made lowercase.
    gap43 = models.FloatField(db_column='GAP43', blank=True, null=True)  # Field name made lowercase.
    cd80 = models.FloatField(db_column='CD80', blank=True, null=True)  # Field name made lowercase.
    rho = models.FloatField(db_column='RHO', blank=True, null=True)  # Field name made lowercase.
    trh = models.FloatField(db_column='TRH', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='TF', blank=True, null=True)  # Field name made lowercase.
    rbp1 = models.FloatField(db_column='RBP1', blank=True, null=True)  # Field name made lowercase.
    trpc1 = models.FloatField(db_column='TRPC1', blank=True, null=True)  # Field name made lowercase.
    agtr1 = models.FloatField(db_column='AGTR1', blank=True, null=True)  # Field name made lowercase.
    sucnr1 = models.FloatField(db_column='SUCNR1', blank=True, null=True)  # Field name made lowercase.
    p2ry1 = models.FloatField(db_column='P2RY1', blank=True, null=True)  # Field name made lowercase.
    mme = models.FloatField(db_column='MME', blank=True, null=True)  # Field name made lowercase.
    slc2a2 = models.FloatField(db_column='SLC2A2', blank=True, null=True)  # Field name made lowercase.
    pik3ca = models.FloatField(db_column='PIK3CA', blank=True, null=True)  # Field name made lowercase.
    parl = models.FloatField(db_column='PARL', blank=True, null=True)  # Field name made lowercase.
    ahsg = models.FloatField(db_column='AHSG', blank=True, null=True)  # Field name made lowercase.
    adipoq = models.FloatField(db_column='ADIPOQ', blank=True, null=True)  # Field name made lowercase.
    spon2 = models.FloatField(db_column='SPON2', blank=True, null=True)  # Field name made lowercase.
    wfs1 = models.FloatField(db_column='WFS1', blank=True, null=True)  # Field name made lowercase.
    cd38 = models.FloatField(db_column='CD38', blank=True, null=True)  # Field name made lowercase.
    prom1 = models.FloatField(db_column='PROM1', blank=True, null=True)  # Field name made lowercase.
    ppargc1a = models.FloatField(db_column='PPARGC1A', blank=True, null=True)  # Field name made lowercase.
    igfbp7 = models.FloatField(db_column='IGFBP7', blank=True, null=True)  # Field name made lowercase.
    cxcl5 = models.FloatField(db_column='CXCL5', blank=True, null=True)  # Field name made lowercase.
    cxcl9 = models.FloatField(db_column='CXCL9', blank=True, null=True)  # Field name made lowercase.
    cxcl10 = models.FloatField(db_column='CXCL10', blank=True, null=True)  # Field name made lowercase.
    cxcl11 = models.FloatField(db_column='CXCL11', blank=True, null=True)  # Field name made lowercase.
    hpse = models.FloatField(db_column='HPSE', blank=True, null=True)  # Field name made lowercase.
    spp1 = models.FloatField(db_column='SPP1', blank=True, null=True)  # Field name made lowercase.
    adh1b = models.FloatField(db_column='ADH1B', blank=True, null=True)  # Field name made lowercase.
    egf = models.FloatField(db_column='EGF', blank=True, null=True)  # Field name made lowercase.
    alpk1 = models.FloatField(db_column='ALPK1', blank=True, null=True)  # Field name made lowercase.
    fabp2 = models.FloatField(db_column='FABP2', blank=True, null=True)  # Field name made lowercase.
    pde5a = models.FloatField(db_column='PDE5A', blank=True, null=True)  # Field name made lowercase.
    setd7 = models.FloatField(db_column='SETD7', blank=True, null=True)  # Field name made lowercase.
    smad1 = models.FloatField(db_column='SMAD1', blank=True, null=True)  # Field name made lowercase.
    ednra = models.FloatField(db_column='EDNRA', blank=True, null=True)  # Field name made lowercase.
    nr3c2 = models.FloatField(db_column='NR3C2', blank=True, null=True)  # Field name made lowercase.
    tlr2 = models.FloatField(db_column='TLR2', blank=True, null=True)  # Field name made lowercase.
    npy5r = models.FloatField(db_column='NPY5R', blank=True, null=True)  # Field name made lowercase.
    fbxo8 = models.FloatField(db_column='FBXO8', blank=True, null=True)  # Field name made lowercase.
    vegfc = models.FloatField(db_column='VEGFC', blank=True, null=True)  # Field name made lowercase.
    acsl1 = models.FloatField(db_column='ACSL1', blank=True, null=True)  # Field name made lowercase.
    sorbs2 = models.FloatField(db_column='SORBS2', blank=True, null=True)  # Field name made lowercase.
    f11 = models.FloatField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    basp1 = models.FloatField(db_column='BASP1', blank=True, null=True)  # Field name made lowercase.
    ptger4 = models.FloatField(db_column='PTGER4', blank=True, null=True)  # Field name made lowercase.
    prkaa1 = models.FloatField(db_column='PRKAA1', blank=True, null=True)  # Field name made lowercase.
    ghr = models.FloatField(db_column='GHR', blank=True, null=True)  # Field name made lowercase.
    itga2 = models.FloatField(db_column='ITGA2', blank=True, null=True)  # Field name made lowercase.
    cdk7 = models.FloatField(db_column='CDK7', blank=True, null=True)  # Field name made lowercase.
    f2r = models.FloatField(db_column='F2R', blank=True, null=True)  # Field name made lowercase.
    erap2 = models.FloatField(db_column='ERAP2', blank=True, null=True)  # Field name made lowercase.
    apc = models.FloatField(db_column='APC', blank=True, null=True)  # Field name made lowercase.
    tnfaip8 = models.FloatField(db_column='TNFAIP8', blank=True, null=True)  # Field name made lowercase.
    vdac1 = models.FloatField(db_column='VDAC1', blank=True, null=True)  # Field name made lowercase.
    pdgfrb = models.FloatField(db_column='PDGFRB', blank=True, null=True)  # Field name made lowercase.
    cd74 = models.FloatField(db_column='CD74', blank=True, null=True)  # Field name made lowercase.
    sparc = models.FloatField(db_column='SPARC', blank=True, null=True)  # Field name made lowercase.
    ebf1 = models.FloatField(db_column='EBF1', blank=True, null=True)  # Field name made lowercase.
    gfpt2 = models.FloatField(db_column='GFPT2', blank=True, null=True)  # Field name made lowercase.
    rreb1 = models.FloatField(db_column='RREB1', blank=True, null=True)  # Field name made lowercase.
    edn1 = models.FloatField(db_column='EDN1', blank=True, null=True)  # Field name made lowercase.
    cdkal1 = models.FloatField(db_column='CDKAL1', blank=True, null=True)  # Field name made lowercase.
    hfe = models.FloatField(db_column='HFE', blank=True, null=True)  # Field name made lowercase.
    hla_a = models.FloatField(db_column='HLA-A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  # Field name made lowercase.
    tnf = models.FloatField(db_column='TNF', blank=True, null=True)  # Field name made lowercase.
    hspa1a = models.FloatField(db_column='HSPA1A', blank=True, null=True)  # Field name made lowercase.
    hspa1b = models.FloatField(db_column='HSPA1B', blank=True, null=True)  # Field name made lowercase.
    hla_dqa1 = models.FloatField(db_column='HLA-DQA1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mapk14 = models.FloatField(db_column='MAPK14', blank=True, null=True)  # Field name made lowercase.
    cdkn1a = models.FloatField(db_column='CDKN1A', blank=True, null=True)  # Field name made lowercase.
    glo1 = models.FloatField(db_column='GLO1', blank=True, null=True)  # Field name made lowercase.
    vegfa = models.FloatField(db_column='VEGFA', blank=True, null=True)  # Field name made lowercase.
    cd2ap = models.FloatField(db_column='CD2AP', blank=True, null=True)  # Field name made lowercase.
    cnr1 = models.FloatField(db_column='CNR1', blank=True, null=True)  # Field name made lowercase.
    enpp1 = models.FloatField(db_column='ENPP1', blank=True, null=True)  # Field name made lowercase.
    ctgf = models.FloatField(db_column='CTGF', blank=True, null=True)  # Field name made lowercase.
    rps12 = models.FloatField(db_column='RPS12', blank=True, null=True)  # Field name made lowercase.
    sgk1 = models.FloatField(db_column='SGK1', blank=True, null=True)  # Field name made lowercase.
    map3k5 = models.FloatField(db_column='MAP3K5', blank=True, null=True)  # Field name made lowercase.
    cited2 = models.FloatField(db_column='CITED2', blank=True, null=True)  # Field name made lowercase.
    utrn = models.FloatField(db_column='UTRN', blank=True, null=True)  # Field name made lowercase.
    mthfd1l = models.FloatField(db_column='MTHFD1L', blank=True, null=True)  # Field name made lowercase.
    vip = models.FloatField(db_column='VIP', blank=True, null=True)  # Field name made lowercase.
    sod2 = models.FloatField(db_column='SOD2', blank=True, null=True)  # Field name made lowercase.
    lpa = models.FloatField(db_column='LPA', blank=True, null=True)  # Field name made lowercase.
    thbs2 = models.FloatField(db_column='THBS2', blank=True, null=True)  # Field name made lowercase.
    pdgfa = models.FloatField(db_column='PDGFA', blank=True, null=True)  # Field name made lowercase.
    il6 = models.FloatField(db_column='IL6', blank=True, null=True)  # Field name made lowercase.
    npy = models.FloatField(db_column='NPY', blank=True, null=True)  # Field name made lowercase.
    jazf1 = models.FloatField(db_column='JAZF1', blank=True, null=True)  # Field name made lowercase.
    cpvl = models.FloatField(db_column='CPVL', blank=True, null=True)  # Field name made lowercase.
    aqp1 = models.FloatField(db_column='AQP1', blank=True, null=True)  # Field name made lowercase.
    elmo1 = models.FloatField(db_column='ELMO1', blank=True, null=True)  # Field name made lowercase.
    igfbp3 = models.FloatField(db_column='IGFBP3', blank=True, null=True)  # Field name made lowercase.
    egfr = models.FloatField(db_column='EGFR', blank=True, null=True)  # Field name made lowercase.
    eln = models.FloatField(db_column='ELN', blank=True, null=True)  # Field name made lowercase.
    ncf1 = models.FloatField(db_column='NCF1', blank=True, null=True)  # Field name made lowercase.
    hspb1 = models.FloatField(db_column='HSPB1', blank=True, null=True)  # Field name made lowercase.
    sema3a = models.FloatField(db_column='SEMA3A', blank=True, null=True)  # Field name made lowercase.
    pon3 = models.FloatField(db_column='PON3', blank=True, null=True)  # Field name made lowercase.
    pon2 = models.FloatField(db_column='PON2', blank=True, null=True)  # Field name made lowercase.
    nampt = models.FloatField(db_column='NAMPT', blank=True, null=True)  # Field name made lowercase.
    cav1 = models.FloatField(db_column='CAV1', blank=True, null=True)  # Field name made lowercase.
    lep = models.FloatField(db_column='LEP', blank=True, null=True)  # Field name made lowercase.
    akr1b1 = models.FloatField(db_column='AKR1B1', blank=True, null=True)  # Field name made lowercase.
    akr1b10 = models.FloatField(db_column='AKR1B10', blank=True, null=True)  # Field name made lowercase.
    pip = models.FloatField(db_column='PIP', blank=True, null=True)  # Field name made lowercase.
    rarres2 = models.FloatField(db_column='RARRES2', blank=True, null=True)  # Field name made lowercase.
    nos3 = models.FloatField(db_column='NOS3', blank=True, null=True)  # Field name made lowercase.
    angpt2 = models.FloatField(db_column='ANGPT2', blank=True, null=True)  # Field name made lowercase.
    defa1 = models.FloatField(db_column='DEFA1', blank=True, null=True)  # Field name made lowercase.
    lpl = models.FloatField(db_column='LPL', blank=True, null=True)  # Field name made lowercase.
    ebf2 = models.FloatField(db_column='EBF2', blank=True, null=True)  # Field name made lowercase.
    adrb3 = models.FloatField(db_column='ADRB3', blank=True, null=True)  # Field name made lowercase.
    eif4ebp1 = models.FloatField(db_column='EIF4EBP1', blank=True, null=True)  # Field name made lowercase.
    fgfr1 = models.FloatField(db_column='FGFR1', blank=True, null=True)  # Field name made lowercase.
    crh = models.FloatField(db_column='CRH', blank=True, null=True)  # Field name made lowercase.
    sgk3 = models.FloatField(db_column='SGK3', blank=True, null=True)  # Field name made lowercase.
    fabp5 = models.FloatField(db_column='FABP5', blank=True, null=True)  # Field name made lowercase.
    fabp4 = models.FloatField(db_column='FABP4', blank=True, null=True)  # Field name made lowercase.
    mmp16 = models.FloatField(db_column='MMP16', blank=True, null=True)  # Field name made lowercase.
    ncald = models.FloatField(db_column='NCALD', blank=True, null=True)  # Field name made lowercase.
    klf10 = models.FloatField(db_column='KLF10', blank=True, null=True)  # Field name made lowercase.
    enpp2 = models.FloatField(db_column='ENPP2', blank=True, null=True)  # Field name made lowercase.
    pvt1 = models.FloatField(db_column='PVT1', blank=True, null=True)  # Field name made lowercase.
    jak2 = models.FloatField(db_column='JAK2', blank=True, null=True)  # Field name made lowercase.
    psip1 = models.FloatField(db_column='PSIP1', blank=True, null=True)  # Field name made lowercase.
    plin2 = models.FloatField(db_column='PLIN2', blank=True, null=True)  # Field name made lowercase.
    rps6 = models.FloatField(db_column='RPS6', blank=True, null=True)  # Field name made lowercase.
    aldh1a1 = models.FloatField(db_column='ALDH1A1', blank=True, null=True)  # Field name made lowercase.
    frmd3 = models.FloatField(db_column='FRMD3', blank=True, null=True)  # Field name made lowercase.
    gas1 = models.FloatField(db_column='GAS1', blank=True, null=True)  # Field name made lowercase.
    baat = models.FloatField(db_column='BAAT', blank=True, null=True)  # Field name made lowercase.
    abca1 = models.FloatField(db_column='ABCA1', blank=True, null=True)  # Field name made lowercase.
    txn = models.FloatField(db_column='TXN', blank=True, null=True)  # Field name made lowercase.
    ambp = models.FloatField(db_column='AMBP', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    hspa5 = models.FloatField(db_column='HSPA5', blank=True, null=True)  # Field name made lowercase.
    angptl2 = models.FloatField(db_column='ANGPTL2', blank=True, null=True)  # Field name made lowercase.
    ptges = models.FloatField(db_column='PTGES', blank=True, null=True)  # Field name made lowercase.
    tsc1 = models.FloatField(db_column='TSC1', blank=True, null=True)  # Field name made lowercase.
    abo = models.FloatField(db_column='ABO', blank=True, null=True)  # Field name made lowercase.
    adamts13 = models.FloatField(db_column='ADAMTS13', blank=True, null=True)  # Field name made lowercase.
    ptgds = models.FloatField(db_column='PTGDS', blank=True, null=True)  # Field name made lowercase.
    klf6 = models.FloatField(db_column='KLF6', blank=True, null=True)  # Field name made lowercase.
    cdc123 = models.FloatField(db_column='CDC123', blank=True, null=True)  # Field name made lowercase.
    bambi = models.FloatField(db_column='BAMBI', blank=True, null=True)  # Field name made lowercase.
    cxcl12 = models.FloatField(db_column='CXCL12', blank=True, null=True)  # Field name made lowercase.
    mbl2 = models.FloatField(db_column='MBL2', blank=True, null=True)  # Field name made lowercase.
    tfam = models.FloatField(db_column='TFAM', blank=True, null=True)  # Field name made lowercase.
    sirt1 = models.FloatField(db_column='SIRT1', blank=True, null=True)  # Field name made lowercase.
    srgn = models.FloatField(db_column='SRGN', blank=True, null=True)  # Field name made lowercase.
    unc5b = models.FloatField(db_column='UNC5B', blank=True, null=True)  # Field name made lowercase.
    adk = models.FloatField(db_column='ADK', blank=True, null=True)  # Field name made lowercase.
    pten = models.FloatField(db_column='PTEN', blank=True, null=True)  # Field name made lowercase.
    rbp4 = models.FloatField(db_column='RBP4', blank=True, null=True)  # Field name made lowercase.
    cyp2c19 = models.FloatField(db_column='CYP2C19', blank=True, null=True)  # Field name made lowercase.
    entpd1 = models.FloatField(db_column='ENTPD1', blank=True, null=True)  # Field name made lowercase.
    tcf7l2 = models.FloatField(db_column='TCF7L2', blank=True, null=True)  # Field name made lowercase.
    bnip3 = models.FloatField(db_column='BNIP3', blank=True, null=True)  # Field name made lowercase.
    igf2 = models.FloatField(db_column='IGF2', blank=True, null=True)  # Field name made lowercase.
    ins = models.FloatField(db_column='INS', blank=True, null=True)  # Field name made lowercase.
    th = models.FloatField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    kcnq1 = models.FloatField(db_column='KCNQ1', blank=True, null=True)  # Field name made lowercase.
    hbg2 = models.FloatField(db_column='HBG2', blank=True, null=True)  # Field name made lowercase.
    smpd1 = models.FloatField(db_column='SMPD1', blank=True, null=True)  # Field name made lowercase.
    ilk = models.FloatField(db_column='ILK', blank=True, null=True)  # Field name made lowercase.
    adm = models.FloatField(db_column='ADM', blank=True, null=True)  # Field name made lowercase.
    pth = models.FloatField(db_column='PTH', blank=True, null=True)  # Field name made lowercase.
    nucb2 = models.FloatField(db_column='NUCB2', blank=True, null=True)  # Field name made lowercase.
    kcnj11 = models.FloatField(db_column='KCNJ11', blank=True, null=True)  # Field name made lowercase.
    saa1 = models.FloatField(db_column='SAA1', blank=True, null=True)  # Field name made lowercase.
    bdnf = models.FloatField(db_column='BDNF', blank=True, null=True)  # Field name made lowercase.
    wt1 = models.FloatField(db_column='WT1', blank=True, null=True)  # Field name made lowercase.
    cd59 = models.FloatField(db_column='CD59', blank=True, null=True)  # Field name made lowercase.
    pdhx = models.FloatField(db_column='PDHX', blank=True, null=True)  # Field name made lowercase.
    traf6 = models.FloatField(db_column='TRAF6', blank=True, null=True)  # Field name made lowercase.
    api5 = models.FloatField(db_column='API5', blank=True, null=True)  # Field name made lowercase.
    nr1h3 = models.FloatField(db_column='NR1H3', blank=True, null=True)  # Field name made lowercase.
    ndufs3 = models.FloatField(db_column='NDUFS3', blank=True, null=True)  # Field name made lowercase.
    folh1 = models.FloatField(db_column='FOLH1', blank=True, null=True)  # Field name made lowercase.
    aplnr = models.FloatField(db_column='APLNR', blank=True, null=True)  # Field name made lowercase.
    p2rx3 = models.FloatField(db_column='P2RX3', blank=True, null=True)  # Field name made lowercase.
    cntf = models.FloatField(db_column='CNTF', blank=True, null=True)  # Field name made lowercase.
    fads1 = models.FloatField(db_column='FADS1', blank=True, null=True)  # Field name made lowercase.
    fads2 = models.FloatField(db_column='FADS2', blank=True, null=True)  # Field name made lowercase.
    fkbp2 = models.FloatField(db_column='FKBP2', blank=True, null=True)  # Field name made lowercase.
    syvn1 = models.FloatField(db_column='SYVN1', blank=True, null=True)  # Field name made lowercase.
    pc = models.FloatField(db_column='PC', blank=True, null=True)  # Field name made lowercase.
    dhcr7 = models.FloatField(db_column='DHCR7', blank=True, null=True)  # Field name made lowercase.
    prcp = models.FloatField(db_column='PRCP', blank=True, null=True)  # Field name made lowercase.
    nox4 = models.FloatField(db_column='NOX4', blank=True, null=True)  # Field name made lowercase.
    pdgfd = models.FloatField(db_column='PDGFD', blank=True, null=True)  # Field name made lowercase.
    atm = models.FloatField(db_column='ATM', blank=True, null=True)  # Field name made lowercase.
    il18 = models.FloatField(db_column='IL18', blank=True, null=True)  # Field name made lowercase.
    apoa1 = models.FloatField(db_column='APOA1', blank=True, null=True)  # Field name made lowercase.
    hyou1 = models.FloatField(db_column='HYOU1', blank=True, null=True)  # Field name made lowercase.
    esam = models.FloatField(db_column='ESAM', blank=True, null=True)  # Field name made lowercase.
    fkbp4 = models.FloatField(db_column='FKBP4', blank=True, null=True)  # Field name made lowercase.
    fgf23 = models.FloatField(db_column='FGF23', blank=True, null=True)  # Field name made lowercase.
    ntf3 = models.FloatField(db_column='NTF3', blank=True, null=True)  # Field name made lowercase.
    vwf = models.FloatField(db_column='VWF', blank=True, null=True)  # Field name made lowercase.
    cd9 = models.FloatField(db_column='CD9', blank=True, null=True)  # Field name made lowercase.
    gapdh = models.FloatField(db_column='GAPDH', blank=True, null=True)  # Field name made lowercase.
    cd4 = models.FloatField(db_column='CD4', blank=True, null=True)  # Field name made lowercase.
    gnb3 = models.FloatField(db_column='GNB3', blank=True, null=True)  # Field name made lowercase.
    cd163 = models.FloatField(db_column='CD163', blank=True, null=True)  # Field name made lowercase.
    slc2a3 = models.FloatField(db_column='SLC2A3', blank=True, null=True)  # Field name made lowercase.
    cd69 = models.FloatField(db_column='CD69', blank=True, null=True)  # Field name made lowercase.
    irak4 = models.FloatField(db_column='IRAK4', blank=True, null=True)  # Field name made lowercase.
    vdr = models.FloatField(db_column='VDR', blank=True, null=True)  # Field name made lowercase.
    aqp5 = models.FloatField(db_column='AQP5', blank=True, null=True)  # Field name made lowercase.
    acvrl1 = models.FloatField(db_column='ACVRL1', blank=True, null=True)  # Field name made lowercase.
    nfe2 = models.FloatField(db_column='NFE2', blank=True, null=True)  # Field name made lowercase.
    cd63 = models.FloatField(db_column='CD63', blank=True, null=True)  # Field name made lowercase.
    erbb3 = models.FloatField(db_column='ERBB3', blank=True, null=True)  # Field name made lowercase.
    ddit3 = models.FloatField(db_column='DDIT3', blank=True, null=True)  # Field name made lowercase.
    ifng = models.FloatField(db_column='IFNG', blank=True, null=True)  # Field name made lowercase.
    nts = models.FloatField(db_column='NTS', blank=True, null=True)  # Field name made lowercase.
    igf1 = models.FloatField(db_column='IGF1', blank=True, null=True)  # Field name made lowercase.
    acacb = models.FloatField(db_column='ACACB', blank=True, null=True)  # Field name made lowercase.
    trpv4 = models.FloatField(db_column='TRPV4', blank=True, null=True)  # Field name made lowercase.
    atp2a2 = models.FloatField(db_column='ATP2A2', blank=True, null=True)  # Field name made lowercase.
    aldh2 = models.FloatField(db_column='ALDH2', blank=True, null=True)  # Field name made lowercase.
    nos1 = models.FloatField(db_column='NOS1', blank=True, null=True)  # Field name made lowercase.
    pebp1 = models.FloatField(db_column='PEBP1', blank=True, null=True)  # Field name made lowercase.
    psmd9 = models.FloatField(db_column='PSMD9', blank=True, null=True)  # Field name made lowercase.
    scarb1 = models.FloatField(db_column='SCARB1', blank=True, null=True)  # Field name made lowercase.
    p2rx2 = models.FloatField(db_column='P2RX2', blank=True, null=True)  # Field name made lowercase.
    alox5ap = models.FloatField(db_column='ALOX5AP', blank=True, null=True)  # Field name made lowercase.
    kl = models.FloatField(db_column='KL', blank=True, null=True)  # Field name made lowercase.
    postn = models.FloatField(db_column='POSTN', blank=True, null=True)  # Field name made lowercase.
    foxo1 = models.FloatField(db_column='FOXO1', blank=True, null=True)  # Field name made lowercase.
    htr2a = models.FloatField(db_column='HTR2A', blank=True, null=True)  # Field name made lowercase.
    gpc5 = models.FloatField(db_column='GPC5', blank=True, null=True)  # Field name made lowercase.
    irs2 = models.FloatField(db_column='IRS2', blank=True, null=True)  # Field name made lowercase.
    gas6 = models.FloatField(db_column='GAS6', blank=True, null=True)  # Field name made lowercase.
    ang = models.FloatField(db_column='ANG', blank=True, null=True)  # Field name made lowercase.
    mmp14 = models.FloatField(db_column='MMP14', blank=True, null=True)  # Field name made lowercase.
    ltb4r2 = models.FloatField(db_column='LTB4R2', blank=True, null=True)  # Field name made lowercase.
    nfkbia = models.FloatField(db_column='NFKBIA', blank=True, null=True)  # Field name made lowercase.
    bmp4 = models.FloatField(db_column='BMP4', blank=True, null=True)  # Field name made lowercase.
    rtn1 = models.FloatField(db_column='RTN1', blank=True, null=True)  # Field name made lowercase.
    pgf = models.FloatField(db_column='PGF', blank=True, null=True)  # Field name made lowercase.
    ngb = models.FloatField(db_column='NGB', blank=True, null=True)  # Field name made lowercase.
    ahsa1 = models.FloatField(db_column='AHSA1', blank=True, null=True)  # Field name made lowercase.
    bdkrb2 = models.FloatField(db_column='BDKRB2', blank=True, null=True)  # Field name made lowercase.
    bdkrb1 = models.FloatField(db_column='BDKRB1', blank=True, null=True)  # Field name made lowercase.
    akt1 = models.FloatField(db_column='AKT1', blank=True, null=True)  # Field name made lowercase.
    grem1 = models.FloatField(db_column='GREM1', blank=True, null=True)  # Field name made lowercase.
    thbs1 = models.FloatField(db_column='THBS1', blank=True, null=True)  # Field name made lowercase.
    pak6 = models.FloatField(db_column='PAK6', blank=True, null=True)  # Field name made lowercase.
    b2m = models.FloatField(db_column='B2M', blank=True, null=True)  # Field name made lowercase.
    myo5c = models.FloatField(db_column='MYO5C', blank=True, null=True)  # Field name made lowercase.
    onecut1 = models.FloatField(db_column='ONECUT1', blank=True, null=True)  # Field name made lowercase.
    adam10 = models.FloatField(db_column='ADAM10', blank=True, null=True)  # Field name made lowercase.
    ctsh = models.FloatField(db_column='CTSH', blank=True, null=True)  # Field name made lowercase.
    plin1 = models.FloatField(db_column='PLIN1', blank=True, null=True)  # Field name made lowercase.
    igf1r = models.FloatField(db_column='IGF1R', blank=True, null=True)  # Field name made lowercase.
    mrpl28 = models.FloatField(db_column='MRPL28', blank=True, null=True)  # Field name made lowercase.
    cacna1h = models.FloatField(db_column='CACNA1H', blank=True, null=True)  # Field name made lowercase.
    pdpk1 = models.FloatField(db_column='PDPK1', blank=True, null=True)  # Field name made lowercase.
    ercc4 = models.FloatField(db_column='ERCC4', blank=True, null=True)  # Field name made lowercase.
    smg1 = models.FloatField(db_column='SMG1', blank=True, null=True)  # Field name made lowercase.
    itgam = models.FloatField(db_column='ITGAM', blank=True, null=True)  # Field name made lowercase.
    fto = models.FloatField(db_column='FTO', blank=True, null=True)  # Field name made lowercase.
    mmp2 = models.FloatField(db_column='MMP2', blank=True, null=True)  # Field name made lowercase.
    slc12a3 = models.FloatField(db_column='SLC12A3', blank=True, null=True)  # Field name made lowercase.
    cetp = models.FloatField(db_column='CETP', blank=True, null=True)  # Field name made lowercase.
    cx3cl1 = models.FloatField(db_column='CX3CL1', blank=True, null=True)  # Field name made lowercase.
    cdh1 = models.FloatField(db_column='CDH1', blank=True, null=True)  # Field name made lowercase.
    nqo1 = models.FloatField(db_column='NQO1', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    znrf1 = models.FloatField(db_column='ZNRF1', blank=True, null=True)  # Field name made lowercase.
    cyba = models.FloatField(db_column='CYBA', blank=True, null=True)  # Field name made lowercase.
    tubb3 = models.FloatField(db_column='TUBB3', blank=True, null=True)  # Field name made lowercase.
    crk = models.FloatField(db_column='CRK', blank=True, null=True)  # Field name made lowercase.
    serpinf2 = models.FloatField(db_column='SERPINF2', blank=True, null=True)  # Field name made lowercase.
    serpinf1 = models.FloatField(db_column='SERPINF1', blank=True, null=True)  # Field name made lowercase.
    trpv3 = models.FloatField(db_column='TRPV3', blank=True, null=True)  # Field name made lowercase.
    cxcl16 = models.FloatField(db_column='CXCL16', blank=True, null=True)  # Field name made lowercase.
    slc2a4 = models.FloatField(db_column='SLC2A4', blank=True, null=True)  # Field name made lowercase.
    cd68 = models.FloatField(db_column='CD68', blank=True, null=True)  # Field name made lowercase.
    shbg = models.FloatField(db_column='SHBG', blank=True, null=True)  # Field name made lowercase.
    pmp22 = models.FloatField(db_column='PMP22', blank=True, null=True)  # Field name made lowercase.
    srebf1 = models.FloatField(db_column='SREBF1', blank=True, null=True)  # Field name made lowercase.
    mapk7 = models.FloatField(db_column='MAPK7', blank=True, null=True)  # Field name made lowercase.
    ccl2 = models.FloatField(db_column='CCL2', blank=True, null=True)  # Field name made lowercase.
    ccl5 = models.FloatField(db_column='CCL5', blank=True, null=True)  # Field name made lowercase.
    hnf1b = models.FloatField(db_column='HNF1B', blank=True, null=True)  # Field name made lowercase.
    erbb2 = models.FloatField(db_column='ERBB2', blank=True, null=True)  # Field name made lowercase.
    fkbp10 = models.FloatField(db_column='FKBP10', blank=True, null=True)  # Field name made lowercase.
    stat5a = models.FloatField(db_column='STAT5A', blank=True, null=True)  # Field name made lowercase.
    stat3 = models.FloatField(db_column='STAT3', blank=True, null=True)  # Field name made lowercase.
    naglu = models.FloatField(db_column='NAGLU', blank=True, null=True)  # Field name made lowercase.
    aoc2 = models.FloatField(db_column='AOC2', blank=True, null=True)  # Field name made lowercase.
    aoc3 = models.FloatField(db_column='AOC3', blank=True, null=True)  # Field name made lowercase.
    ppy = models.FloatField(db_column='PPY', blank=True, null=True)  # Field name made lowercase.
    sth = models.FloatField(db_column='STH', blank=True, null=True)  # Field name made lowercase.
    itgb3 = models.FloatField(db_column='ITGB3', blank=True, null=True)  # Field name made lowercase.
    gip = models.FloatField(db_column='GIP', blank=True, null=True)  # Field name made lowercase.
    mpo = models.FloatField(db_column='MPO', blank=True, null=True)  # Field name made lowercase.
    pecam1 = models.FloatField(db_column='PECAM1', blank=True, null=True)  # Field name made lowercase.
    sox9 = models.FloatField(db_column='SOX9', blank=True, null=True)  # Field name made lowercase.
    timp2 = models.FloatField(db_column='TIMP2', blank=True, null=True)  # Field name made lowercase.
    dcxr = models.FloatField(db_column='DCXR', blank=True, null=True)  # Field name made lowercase.
    fasn = models.FloatField(db_column='FASN', blank=True, null=True)  # Field name made lowercase.
    colec12 = models.FloatField(db_column='COLEC12', blank=True, null=True)  # Field name made lowercase.
    adcyap1 = models.FloatField(db_column='ADCYAP1', blank=True, null=True)  # Field name made lowercase.
    smad7 = models.FloatField(db_column='SMAD7', blank=True, null=True)  # Field name made lowercase.
    nedd4l = models.FloatField(db_column='NEDD4L', blank=True, null=True)  # Field name made lowercase.
    mc4r = models.FloatField(db_column='MC4R', blank=True, null=True)  # Field name made lowercase.
    bcl2 = models.FloatField(db_column='BCL2', blank=True, null=True)  # Field name made lowercase.
    cndp2 = models.FloatField(db_column='CNDP2', blank=True, null=True)  # Field name made lowercase.
    znf236 = models.FloatField(db_column='ZNF236', blank=True, null=True)  # Field name made lowercase.
    stk11 = models.FloatField(db_column='STK11', blank=True, null=True)  # Field name made lowercase.
    sirt6 = models.FloatField(db_column='SIRT6', blank=True, null=True)  # Field name made lowercase.
    uhrf1 = models.FloatField(db_column='UHRF1', blank=True, null=True)  # Field name made lowercase.
    timm44 = models.FloatField(db_column='TIMM44', blank=True, null=True)  # Field name made lowercase.
    angptl4 = models.FloatField(db_column='ANGPTL4', blank=True, null=True)  # Field name made lowercase.
    dnmt1 = models.FloatField(db_column='DNMT1', blank=True, null=True)  # Field name made lowercase.
    icam1 = models.FloatField(db_column='ICAM1', blank=True, null=True)  # Field name made lowercase.
    ldlr = models.FloatField(db_column='LDLR', blank=True, null=True)  # Field name made lowercase.
    epor = models.FloatField(db_column='EPOR', blank=True, null=True)  # Field name made lowercase.
    prdx2 = models.FloatField(db_column='PRDX2', blank=True, null=True)  # Field name made lowercase.
    ptger1 = models.FloatField(db_column='PTGER1', blank=True, null=True)  # Field name made lowercase.
    unc13a = models.FloatField(db_column='UNC13A', blank=True, null=True)  # Field name made lowercase.
    gdf15 = models.FloatField(db_column='GDF15', blank=True, null=True)  # Field name made lowercase.
    fkbp8 = models.FloatField(db_column='FKBP8', blank=True, null=True)  # Field name made lowercase.
    usf2 = models.FloatField(db_column='USF2', blank=True, null=True)  # Field name made lowercase.
    ffar1 = models.FloatField(db_column='FFAR1', blank=True, null=True)  # Field name made lowercase.
    ffar2 = models.FloatField(db_column='FFAR2', blank=True, null=True)  # Field name made lowercase.
    nphs1 = models.FloatField(db_column='NPHS1', blank=True, null=True)  # Field name made lowercase.
    tgfb1 = models.FloatField(db_column='TGFB1', blank=True, null=True)  # Field name made lowercase.
    xrcc1 = models.FloatField(db_column='XRCC1', blank=True, null=True)  # Field name made lowercase.
    ercc1 = models.FloatField(db_column='ERCC1', blank=True, null=True)  # Field name made lowercase.
    gipr = models.FloatField(db_column='GIPR', blank=True, null=True)  # Field name made lowercase.
    fgf21 = models.FloatField(db_column='FGF21', blank=True, null=True)  # Field name made lowercase.
    clec11a = models.FloatField(db_column='CLEC11A', blank=True, null=True)  # Field name made lowercase.
    fpr1 = models.FloatField(db_column='FPR1', blank=True, null=True)  # Field name made lowercase.
    trib3 = models.FloatField(db_column='TRIB3', blank=True, null=True)  # Field name made lowercase.
    bmp2 = models.FloatField(db_column='BMP2', blank=True, null=True)  # Field name made lowercase.
    thbd = models.FloatField(db_column='THBD', blank=True, null=True)  # Field name made lowercase.
    cst3 = models.FloatField(db_column='CST3', blank=True, null=True)  # Field name made lowercase.
    id1 = models.FloatField(db_column='ID1', blank=True, null=True)  # Field name made lowercase.
    src = models.FloatField(db_column='SRC', blank=True, null=True)  # Field name made lowercase.
    mafb = models.FloatField(db_column='MAFB', blank=True, null=True)  # Field name made lowercase.
    sgk2 = models.FloatField(db_column='SGK2', blank=True, null=True)  # Field name made lowercase.
    hnf4a = models.FloatField(db_column='HNF4A', blank=True, null=True)  # Field name made lowercase.
    pltp = models.FloatField(db_column='PLTP', blank=True, null=True)  # Field name made lowercase.
    mmp9 = models.FloatField(db_column='MMP9', blank=True, null=True)  # Field name made lowercase.
    cd40 = models.FloatField(db_column='CD40', blank=True, null=True)  # Field name made lowercase.
    ptpn1 = models.FloatField(db_column='PTPN1', blank=True, null=True)  # Field name made lowercase.
    cyp24a1 = models.FloatField(db_column='CYP24A1', blank=True, null=True)  # Field name made lowercase.
    rcan1 = models.FloatField(db_column='RCAN1', blank=True, null=True)  # Field name made lowercase.
    abcg1 = models.FloatField(db_column='ABCG1', blank=True, null=True)  # Field name made lowercase.
    prmt2 = models.FloatField(db_column='PRMT2', blank=True, null=True)  # Field name made lowercase.
    comt = models.FloatField(db_column='COMT', blank=True, null=True)  # Field name made lowercase.
    mapk1 = models.FloatField(db_column='MAPK1', blank=True, null=True)  # Field name made lowercase.
    mif = models.FloatField(db_column='MIF', blank=True, null=True)  # Field name made lowercase.
    ggt1 = models.FloatField(db_column='GGT1', blank=True, null=True)  # Field name made lowercase.
    xbp1 = models.FloatField(db_column='XBP1', blank=True, null=True)  # Field name made lowercase.
    osm = models.FloatField(db_column='OSM', blank=True, null=True)  # Field name made lowercase.
    limk2 = models.FloatField(db_column='LIMK2', blank=True, null=True)  # Field name made lowercase.
    sfi1 = models.FloatField(db_column='SFI1', blank=True, null=True)  # Field name made lowercase.
    timp3 = models.FloatField(db_column='TIMP3', blank=True, null=True)  # Field name made lowercase.
    hmox1 = models.FloatField(db_column='HMOX1', blank=True, null=True)  # Field name made lowercase.
    apol1 = models.FloatField(db_column='APOL1', blank=True, null=True)  # Field name made lowercase.
    myh9 = models.FloatField(db_column='MYH9', blank=True, null=True)  # Field name made lowercase.
    pdgfb = models.FloatField(db_column='PDGFB', blank=True, null=True)  # Field name made lowercase.
    atf4 = models.FloatField(db_column='ATF4', blank=True, null=True)  # Field name made lowercase.
    tspo = models.FloatField(db_column='TSPO', blank=True, null=True)  # Field name made lowercase.
    miox = models.FloatField(db_column='MIOX', blank=True, null=True)  # Field name made lowercase.
    prdx4 = models.FloatField(db_column='PRDX4', blank=True, null=True)  # Field name made lowercase.
    gk = models.FloatField(db_column='GK', blank=True, null=True)  # Field name made lowercase.
    rgn = models.FloatField(db_column='RGN', blank=True, null=True)  # Field name made lowercase.
    timp1 = models.FloatField(db_column='TIMP1', blank=True, null=True)  # Field name made lowercase.
    clcn5 = models.FloatField(db_column='CLCN5', blank=True, null=True)  # Field name made lowercase.
    ar = models.FloatField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    foxo4 = models.FloatField(db_column='FOXO4', blank=True, null=True)  # Field name made lowercase.
    rps6ka6 = models.FloatField(db_column='RPS6KA6', blank=True, null=True)  # Field name made lowercase.
    nox1 = models.FloatField(db_column='NOX1', blank=True, null=True)  # Field name made lowercase.
    xiap = models.FloatField(db_column='XIAP', blank=True, null=True)  # Field name made lowercase.
    cd40lg = models.FloatField(db_column='CD40LG', blank=True, null=True)  # Field name made lowercase.
    l1cam = models.FloatField(db_column='L1CAM', blank=True, null=True)  # Field name made lowercase.
    irak1 = models.FloatField(db_column='IRAK1', blank=True, null=True)  # Field name made lowercase.
    g6pd = models.FloatField(db_column='G6PD', blank=True, null=True)  # Field name made lowercase.
    f8 = models.FloatField(db_column='F8', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diaco_tissue_brain_amygdala'


class DiacoTissueBrainAnteriorCcBa24(models.Model):
    subjid = models.CharField(db_column='SUBJID', max_length=50, primary_key=True)  # Field name made lowercase.
    sampid = models.CharField(db_column='SAMPID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sesso = models.CharField(db_column='Sesso', max_length=1)  # Field name made lowercase.
    eta = models.CharField(db_column='Età', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errfi1 = models.FloatField(db_column='ERRFI1', blank=True, null=True)  # Field name made lowercase.
    mad2l2 = models.FloatField(db_column='MAD2L2', blank=True, null=True)  # Field name made lowercase.
    mthfr = models.FloatField(db_column='MTHFR', blank=True, null=True)  # Field name made lowercase.
    nppa = models.FloatField(db_column='NPPA', blank=True, null=True)  # Field name made lowercase.
    tnfrsf1b = models.FloatField(db_column='TNFRSF1B', blank=True, null=True)  # Field name made lowercase.
    pla2g2a = models.FloatField(db_column='PLA2G2A', blank=True, null=True)  # Field name made lowercase.
    alpl = models.FloatField(db_column='ALPL', blank=True, null=True)  # Field name made lowercase.
    hspg2 = models.FloatField(db_column='HSPG2', blank=True, null=True)  # Field name made lowercase.
    cnr2 = models.FloatField(db_column='CNR2', blank=True, null=True)  # Field name made lowercase.
    slc9a1 = models.FloatField(db_column='SLC9A1', blank=True, null=True)  # Field name made lowercase.
    col8a2 = models.FloatField(db_column='COL8A2', blank=True, null=True)  # Field name made lowercase.
    cap1 = models.FloatField(db_column='CAP1', blank=True, null=True)  # Field name made lowercase.
    slc2a1 = models.FloatField(db_column='SLC2A1', blank=True, null=True)  # Field name made lowercase.
    cyp2j2 = models.FloatField(db_column='CYP2J2', blank=True, null=True)  # Field name made lowercase.
    ddah1 = models.FloatField(db_column='DDAH1', blank=True, null=True)  # Field name made lowercase.
    cyr61 = models.FloatField(db_column='CYR61', blank=True, null=True)  # Field name made lowercase.
    ngf = models.FloatField(db_column='NGF', blank=True, null=True)  # Field name made lowercase.
    hmgcs2 = models.FloatField(db_column='HMGCS2', blank=True, null=True)  # Field name made lowercase.
    ctss = models.FloatField(db_column='CTSS', blank=True, null=True)  # Field name made lowercase.
    s100a12 = models.FloatField(db_column='S100A12', blank=True, null=True)  # Field name made lowercase.
    lmna = models.FloatField(db_column='LMNA', blank=True, null=True)  # Field name made lowercase.
    cd247 = models.FloatField(db_column='CD247', blank=True, null=True)  # Field name made lowercase.
    sele = models.FloatField(db_column='SELE', blank=True, null=True)  # Field name made lowercase.
    fmo3 = models.FloatField(db_column='FMO3', blank=True, null=True)  # Field name made lowercase.
    prdx6 = models.FloatField(db_column='PRDX6', blank=True, null=True)  # Field name made lowercase.
    glul = models.FloatField(db_column='GLUL', blank=True, null=True)  # Field name made lowercase.
    lamc1 = models.FloatField(db_column='LAMC1', blank=True, null=True)  # Field name made lowercase.
    ptgs2 = models.FloatField(db_column='PTGS2', blank=True, null=True)  # Field name made lowercase.
    chi3l1 = models.FloatField(db_column='CHI3L1', blank=True, null=True)  # Field name made lowercase.
    chit1 = models.FloatField(db_column='CHIT1', blank=True, null=True)  # Field name made lowercase.
    fmod = models.FloatField(db_column='FMOD', blank=True, null=True)  # Field name made lowercase.
    il10 = models.FloatField(db_column='IL10', blank=True, null=True)  # Field name made lowercase.
    pfkfb2 = models.FloatField(db_column='PFKFB2', blank=True, null=True)  # Field name made lowercase.
    cd34 = models.FloatField(db_column='CD34', blank=True, null=True)  # Field name made lowercase.
    cog2 = models.FloatField(db_column='COG2', blank=True, null=True)  # Field name made lowercase.
    nlrp3 = models.FloatField(db_column='NLRP3', blank=True, null=True)  # Field name made lowercase.
    rock2 = models.FloatField(db_column='ROCK2', blank=True, null=True)  # Field name made lowercase.
    apob = models.FloatField(db_column='APOB', blank=True, null=True)  # Field name made lowercase.
    pomc = models.FloatField(db_column='POMC', blank=True, null=True)  # Field name made lowercase.
    gckr = models.FloatField(db_column='GCKR', blank=True, null=True)  # Field name made lowercase.
    plekhh2 = models.FloatField(db_column='PLEKHH2', blank=True, null=True)  # Field name made lowercase.
    prkce = models.FloatField(db_column='PRKCE', blank=True, null=True)  # Field name made lowercase.
    pigf = models.FloatField(db_column='PIGF', blank=True, null=True)  # Field name made lowercase.
    msh2 = models.FloatField(db_column='MSH2', blank=True, null=True)  # Field name made lowercase.
    gfpt1 = models.FloatField(db_column='GFPT1', blank=True, null=True)  # Field name made lowercase.
    tacr1 = models.FloatField(db_column='TACR1', blank=True, null=True)  # Field name made lowercase.
    reg1a = models.FloatField(db_column='REG1A', blank=True, null=True)  # Field name made lowercase.
    eif2ak3 = models.FloatField(db_column='EIF2AK3', blank=True, null=True)  # Field name made lowercase.
    adra2b = models.FloatField(db_column='ADRA2B', blank=True, null=True)  # Field name made lowercase.
    il1b = models.FloatField(db_column='IL1B', blank=True, null=True)  # Field name made lowercase.
    proc = models.FloatField(db_column='PROC', blank=True, null=True)  # Field name made lowercase.
    polr2d = models.FloatField(db_column='POLR2D', blank=True, null=True)  # Field name made lowercase.
    zeb2 = models.FloatField(db_column='ZEB2', blank=True, null=True)  # Field name made lowercase.
    acvr1c = models.FloatField(db_column='ACVR1C', blank=True, null=True)  # Field name made lowercase.
    dpp4 = models.FloatField(db_column='DPP4', blank=True, null=True)  # Field name made lowercase.
    nfe2l2 = models.FloatField(db_column='NFE2L2', blank=True, null=True)  # Field name made lowercase.
    igfbp5 = models.FloatField(db_column='IGFBP5', blank=True, null=True)  # Field name made lowercase.
    ccl20 = models.FloatField(db_column='CCL20', blank=True, null=True)  # Field name made lowercase.
    hdac4 = models.FloatField(db_column='HDAC4', blank=True, null=True)  # Field name made lowercase.
    capn10 = models.FloatField(db_column='CAPN10', blank=True, null=True)  # Field name made lowercase.
    ghrl = models.FloatField(db_column='GHRL', blank=True, null=True)  # Field name made lowercase.
    pparg = models.FloatField(db_column='PPARG', blank=True, null=True)  # Field name made lowercase.
    raf1 = models.FloatField(db_column='RAF1', blank=True, null=True)  # Field name made lowercase.
    myd88 = models.FloatField(db_column='MYD88', blank=True, null=True)  # Field name made lowercase.
    cx3cr1 = models.FloatField(db_column='CX3CR1', blank=True, null=True)  # Field name made lowercase.
    cck = models.FloatField(db_column='CCK', blank=True, null=True)  # Field name made lowercase.
    exosc7 = models.FloatField(db_column='EXOSC7', blank=True, null=True)  # Field name made lowercase.
    ccr1 = models.FloatField(db_column='CCR1', blank=True, null=True)  # Field name made lowercase.
    ccr5 = models.FloatField(db_column='CCR5', blank=True, null=True)  # Field name made lowercase.
    gpx1 = models.FloatField(db_column='GPX1', blank=True, null=True)  # Field name made lowercase.
    rhoa = models.FloatField(db_column='RHOA', blank=True, null=True)  # Field name made lowercase.
    cish = models.FloatField(db_column='CISH', blank=True, null=True)  # Field name made lowercase.
    tkt = models.FloatField(db_column='TKT', blank=True, null=True)  # Field name made lowercase.
    appl1 = models.FloatField(db_column='APPL1', blank=True, null=True)  # Field name made lowercase.
    slmap = models.FloatField(db_column='SLMAP', blank=True, null=True)  # Field name made lowercase.
    col8a1 = models.FloatField(db_column='COL8A1', blank=True, null=True)  # Field name made lowercase.
    cd47 = models.FloatField(db_column='CD47', blank=True, null=True)  # Field name made lowercase.
    gap43 = models.FloatField(db_column='GAP43', blank=True, null=True)  # Field name made lowercase.
    cd80 = models.FloatField(db_column='CD80', blank=True, null=True)  # Field name made lowercase.
    rho = models.FloatField(db_column='RHO', blank=True, null=True)  # Field name made lowercase.
    trh = models.FloatField(db_column='TRH', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='TF', blank=True, null=True)  # Field name made lowercase.
    rbp1 = models.FloatField(db_column='RBP1', blank=True, null=True)  # Field name made lowercase.
    trpc1 = models.FloatField(db_column='TRPC1', blank=True, null=True)  # Field name made lowercase.
    agtr1 = models.FloatField(db_column='AGTR1', blank=True, null=True)  # Field name made lowercase.
    sucnr1 = models.FloatField(db_column='SUCNR1', blank=True, null=True)  # Field name made lowercase.
    p2ry1 = models.FloatField(db_column='P2RY1', blank=True, null=True)  # Field name made lowercase.
    mme = models.FloatField(db_column='MME', blank=True, null=True)  # Field name made lowercase.
    slc2a2 = models.FloatField(db_column='SLC2A2', blank=True, null=True)  # Field name made lowercase.
    pik3ca = models.FloatField(db_column='PIK3CA', blank=True, null=True)  # Field name made lowercase.
    parl = models.FloatField(db_column='PARL', blank=True, null=True)  # Field name made lowercase.
    ahsg = models.FloatField(db_column='AHSG', blank=True, null=True)  # Field name made lowercase.
    adipoq = models.FloatField(db_column='ADIPOQ', blank=True, null=True)  # Field name made lowercase.
    spon2 = models.FloatField(db_column='SPON2', blank=True, null=True)  # Field name made lowercase.
    wfs1 = models.FloatField(db_column='WFS1', blank=True, null=True)  # Field name made lowercase.
    cd38 = models.FloatField(db_column='CD38', blank=True, null=True)  # Field name made lowercase.
    prom1 = models.FloatField(db_column='PROM1', blank=True, null=True)  # Field name made lowercase.
    ppargc1a = models.FloatField(db_column='PPARGC1A', blank=True, null=True)  # Field name made lowercase.
    igfbp7 = models.FloatField(db_column='IGFBP7', blank=True, null=True)  # Field name made lowercase.
    cxcl5 = models.FloatField(db_column='CXCL5', blank=True, null=True)  # Field name made lowercase.
    cxcl9 = models.FloatField(db_column='CXCL9', blank=True, null=True)  # Field name made lowercase.
    cxcl10 = models.FloatField(db_column='CXCL10', blank=True, null=True)  # Field name made lowercase.
    cxcl11 = models.FloatField(db_column='CXCL11', blank=True, null=True)  # Field name made lowercase.
    hpse = models.FloatField(db_column='HPSE', blank=True, null=True)  # Field name made lowercase.
    spp1 = models.FloatField(db_column='SPP1', blank=True, null=True)  # Field name made lowercase.
    adh1b = models.FloatField(db_column='ADH1B', blank=True, null=True)  # Field name made lowercase.
    egf = models.FloatField(db_column='EGF', blank=True, null=True)  # Field name made lowercase.
    alpk1 = models.FloatField(db_column='ALPK1', blank=True, null=True)  # Field name made lowercase.
    fabp2 = models.FloatField(db_column='FABP2', blank=True, null=True)  # Field name made lowercase.
    pde5a = models.FloatField(db_column='PDE5A', blank=True, null=True)  # Field name made lowercase.
    setd7 = models.FloatField(db_column='SETD7', blank=True, null=True)  # Field name made lowercase.
    smad1 = models.FloatField(db_column='SMAD1', blank=True, null=True)  # Field name made lowercase.
    ednra = models.FloatField(db_column='EDNRA', blank=True, null=True)  # Field name made lowercase.
    nr3c2 = models.FloatField(db_column='NR3C2', blank=True, null=True)  # Field name made lowercase.
    tlr2 = models.FloatField(db_column='TLR2', blank=True, null=True)  # Field name made lowercase.
    npy5r = models.FloatField(db_column='NPY5R', blank=True, null=True)  # Field name made lowercase.
    fbxo8 = models.FloatField(db_column='FBXO8', blank=True, null=True)  # Field name made lowercase.
    vegfc = models.FloatField(db_column='VEGFC', blank=True, null=True)  # Field name made lowercase.
    acsl1 = models.FloatField(db_column='ACSL1', blank=True, null=True)  # Field name made lowercase.
    sorbs2 = models.FloatField(db_column='SORBS2', blank=True, null=True)  # Field name made lowercase.
    f11 = models.FloatField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    basp1 = models.FloatField(db_column='BASP1', blank=True, null=True)  # Field name made lowercase.
    ptger4 = models.FloatField(db_column='PTGER4', blank=True, null=True)  # Field name made lowercase.
    prkaa1 = models.FloatField(db_column='PRKAA1', blank=True, null=True)  # Field name made lowercase.
    ghr = models.FloatField(db_column='GHR', blank=True, null=True)  # Field name made lowercase.
    itga2 = models.FloatField(db_column='ITGA2', blank=True, null=True)  # Field name made lowercase.
    cdk7 = models.FloatField(db_column='CDK7', blank=True, null=True)  # Field name made lowercase.
    f2r = models.FloatField(db_column='F2R', blank=True, null=True)  # Field name made lowercase.
    erap2 = models.FloatField(db_column='ERAP2', blank=True, null=True)  # Field name made lowercase.
    apc = models.FloatField(db_column='APC', blank=True, null=True)  # Field name made lowercase.
    tnfaip8 = models.FloatField(db_column='TNFAIP8', blank=True, null=True)  # Field name made lowercase.
    vdac1 = models.FloatField(db_column='VDAC1', blank=True, null=True)  # Field name made lowercase.
    pdgfrb = models.FloatField(db_column='PDGFRB', blank=True, null=True)  # Field name made lowercase.
    cd74 = models.FloatField(db_column='CD74', blank=True, null=True)  # Field name made lowercase.
    sparc = models.FloatField(db_column='SPARC', blank=True, null=True)  # Field name made lowercase.
    ebf1 = models.FloatField(db_column='EBF1', blank=True, null=True)  # Field name made lowercase.
    gfpt2 = models.FloatField(db_column='GFPT2', blank=True, null=True)  # Field name made lowercase.
    rreb1 = models.FloatField(db_column='RREB1', blank=True, null=True)  # Field name made lowercase.
    edn1 = models.FloatField(db_column='EDN1', blank=True, null=True)  # Field name made lowercase.
    cdkal1 = models.FloatField(db_column='CDKAL1', blank=True, null=True)  # Field name made lowercase.
    hfe = models.FloatField(db_column='HFE', blank=True, null=True)  # Field name made lowercase.
    hla_a = models.FloatField(db_column='HLA-A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  # Field name made lowercase.
    tnf = models.FloatField(db_column='TNF', blank=True, null=True)  # Field name made lowercase.
    hspa1a = models.FloatField(db_column='HSPA1A', blank=True, null=True)  # Field name made lowercase.
    hspa1b = models.FloatField(db_column='HSPA1B', blank=True, null=True)  # Field name made lowercase.
    hla_dqa1 = models.FloatField(db_column='HLA-DQA1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mapk14 = models.FloatField(db_column='MAPK14', blank=True, null=True)  # Field name made lowercase.
    cdkn1a = models.FloatField(db_column='CDKN1A', blank=True, null=True)  # Field name made lowercase.
    glo1 = models.FloatField(db_column='GLO1', blank=True, null=True)  # Field name made lowercase.
    vegfa = models.FloatField(db_column='VEGFA', blank=True, null=True)  # Field name made lowercase.
    cd2ap = models.FloatField(db_column='CD2AP', blank=True, null=True)  # Field name made lowercase.
    cnr1 = models.FloatField(db_column='CNR1', blank=True, null=True)  # Field name made lowercase.
    enpp1 = models.FloatField(db_column='ENPP1', blank=True, null=True)  # Field name made lowercase.
    ctgf = models.FloatField(db_column='CTGF', blank=True, null=True)  # Field name made lowercase.
    rps12 = models.FloatField(db_column='RPS12', blank=True, null=True)  # Field name made lowercase.
    sgk1 = models.FloatField(db_column='SGK1', blank=True, null=True)  # Field name made lowercase.
    map3k5 = models.FloatField(db_column='MAP3K5', blank=True, null=True)  # Field name made lowercase.
    cited2 = models.FloatField(db_column='CITED2', blank=True, null=True)  # Field name made lowercase.
    utrn = models.FloatField(db_column='UTRN', blank=True, null=True)  # Field name made lowercase.
    mthfd1l = models.FloatField(db_column='MTHFD1L', blank=True, null=True)  # Field name made lowercase.
    vip = models.FloatField(db_column='VIP', blank=True, null=True)  # Field name made lowercase.
    sod2 = models.FloatField(db_column='SOD2', blank=True, null=True)  # Field name made lowercase.
    lpa = models.FloatField(db_column='LPA', blank=True, null=True)  # Field name made lowercase.
    thbs2 = models.FloatField(db_column='THBS2', blank=True, null=True)  # Field name made lowercase.
    pdgfa = models.FloatField(db_column='PDGFA', blank=True, null=True)  # Field name made lowercase.
    il6 = models.FloatField(db_column='IL6', blank=True, null=True)  # Field name made lowercase.
    npy = models.FloatField(db_column='NPY', blank=True, null=True)  # Field name made lowercase.
    jazf1 = models.FloatField(db_column='JAZF1', blank=True, null=True)  # Field name made lowercase.
    cpvl = models.FloatField(db_column='CPVL', blank=True, null=True)  # Field name made lowercase.
    aqp1 = models.FloatField(db_column='AQP1', blank=True, null=True)  # Field name made lowercase.
    elmo1 = models.FloatField(db_column='ELMO1', blank=True, null=True)  # Field name made lowercase.
    igfbp3 = models.FloatField(db_column='IGFBP3', blank=True, null=True)  # Field name made lowercase.
    egfr = models.FloatField(db_column='EGFR', blank=True, null=True)  # Field name made lowercase.
    eln = models.FloatField(db_column='ELN', blank=True, null=True)  # Field name made lowercase.
    ncf1 = models.FloatField(db_column='NCF1', blank=True, null=True)  # Field name made lowercase.
    hspb1 = models.FloatField(db_column='HSPB1', blank=True, null=True)  # Field name made lowercase.
    sema3a = models.FloatField(db_column='SEMA3A', blank=True, null=True)  # Field name made lowercase.
    pon3 = models.FloatField(db_column='PON3', blank=True, null=True)  # Field name made lowercase.
    pon2 = models.FloatField(db_column='PON2', blank=True, null=True)  # Field name made lowercase.
    nampt = models.FloatField(db_column='NAMPT', blank=True, null=True)  # Field name made lowercase.
    cav1 = models.FloatField(db_column='CAV1', blank=True, null=True)  # Field name made lowercase.
    lep = models.FloatField(db_column='LEP', blank=True, null=True)  # Field name made lowercase.
    akr1b1 = models.FloatField(db_column='AKR1B1', blank=True, null=True)  # Field name made lowercase.
    akr1b10 = models.FloatField(db_column='AKR1B10', blank=True, null=True)  # Field name made lowercase.
    pip = models.FloatField(db_column='PIP', blank=True, null=True)  # Field name made lowercase.
    rarres2 = models.FloatField(db_column='RARRES2', blank=True, null=True)  # Field name made lowercase.
    nos3 = models.FloatField(db_column='NOS3', blank=True, null=True)  # Field name made lowercase.
    angpt2 = models.FloatField(db_column='ANGPT2', blank=True, null=True)  # Field name made lowercase.
    defa1 = models.FloatField(db_column='DEFA1', blank=True, null=True)  # Field name made lowercase.
    lpl = models.FloatField(db_column='LPL', blank=True, null=True)  # Field name made lowercase.
    ebf2 = models.FloatField(db_column='EBF2', blank=True, null=True)  # Field name made lowercase.
    adrb3 = models.FloatField(db_column='ADRB3', blank=True, null=True)  # Field name made lowercase.
    eif4ebp1 = models.FloatField(db_column='EIF4EBP1', blank=True, null=True)  # Field name made lowercase.
    fgfr1 = models.FloatField(db_column='FGFR1', blank=True, null=True)  # Field name made lowercase.
    crh = models.FloatField(db_column='CRH', blank=True, null=True)  # Field name made lowercase.
    sgk3 = models.FloatField(db_column='SGK3', blank=True, null=True)  # Field name made lowercase.
    fabp5 = models.FloatField(db_column='FABP5', blank=True, null=True)  # Field name made lowercase.
    fabp4 = models.FloatField(db_column='FABP4', blank=True, null=True)  # Field name made lowercase.
    mmp16 = models.FloatField(db_column='MMP16', blank=True, null=True)  # Field name made lowercase.
    ncald = models.FloatField(db_column='NCALD', blank=True, null=True)  # Field name made lowercase.
    klf10 = models.FloatField(db_column='KLF10', blank=True, null=True)  # Field name made lowercase.
    enpp2 = models.FloatField(db_column='ENPP2', blank=True, null=True)  # Field name made lowercase.
    pvt1 = models.FloatField(db_column='PVT1', blank=True, null=True)  # Field name made lowercase.
    jak2 = models.FloatField(db_column='JAK2', blank=True, null=True)  # Field name made lowercase.
    psip1 = models.FloatField(db_column='PSIP1', blank=True, null=True)  # Field name made lowercase.
    plin2 = models.FloatField(db_column='PLIN2', blank=True, null=True)  # Field name made lowercase.
    rps6 = models.FloatField(db_column='RPS6', blank=True, null=True)  # Field name made lowercase.
    aldh1a1 = models.FloatField(db_column='ALDH1A1', blank=True, null=True)  # Field name made lowercase.
    frmd3 = models.FloatField(db_column='FRMD3', blank=True, null=True)  # Field name made lowercase.
    gas1 = models.FloatField(db_column='GAS1', blank=True, null=True)  # Field name made lowercase.
    baat = models.FloatField(db_column='BAAT', blank=True, null=True)  # Field name made lowercase.
    abca1 = models.FloatField(db_column='ABCA1', blank=True, null=True)  # Field name made lowercase.
    txn = models.FloatField(db_column='TXN', blank=True, null=True)  # Field name made lowercase.
    ambp = models.FloatField(db_column='AMBP', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    hspa5 = models.FloatField(db_column='HSPA5', blank=True, null=True)  # Field name made lowercase.
    angptl2 = models.FloatField(db_column='ANGPTL2', blank=True, null=True)  # Field name made lowercase.
    ptges = models.FloatField(db_column='PTGES', blank=True, null=True)  # Field name made lowercase.
    tsc1 = models.FloatField(db_column='TSC1', blank=True, null=True)  # Field name made lowercase.
    abo = models.FloatField(db_column='ABO', blank=True, null=True)  # Field name made lowercase.
    adamts13 = models.FloatField(db_column='ADAMTS13', blank=True, null=True)  # Field name made lowercase.
    ptgds = models.FloatField(db_column='PTGDS', blank=True, null=True)  # Field name made lowercase.
    klf6 = models.FloatField(db_column='KLF6', blank=True, null=True)  # Field name made lowercase.
    cdc123 = models.FloatField(db_column='CDC123', blank=True, null=True)  # Field name made lowercase.
    bambi = models.FloatField(db_column='BAMBI', blank=True, null=True)  # Field name made lowercase.
    cxcl12 = models.FloatField(db_column='CXCL12', blank=True, null=True)  # Field name made lowercase.
    mbl2 = models.FloatField(db_column='MBL2', blank=True, null=True)  # Field name made lowercase.
    tfam = models.FloatField(db_column='TFAM', blank=True, null=True)  # Field name made lowercase.
    sirt1 = models.FloatField(db_column='SIRT1', blank=True, null=True)  # Field name made lowercase.
    srgn = models.FloatField(db_column='SRGN', blank=True, null=True)  # Field name made lowercase.
    unc5b = models.FloatField(db_column='UNC5B', blank=True, null=True)  # Field name made lowercase.
    adk = models.FloatField(db_column='ADK', blank=True, null=True)  # Field name made lowercase.
    pten = models.FloatField(db_column='PTEN', blank=True, null=True)  # Field name made lowercase.
    rbp4 = models.FloatField(db_column='RBP4', blank=True, null=True)  # Field name made lowercase.
    cyp2c19 = models.FloatField(db_column='CYP2C19', blank=True, null=True)  # Field name made lowercase.
    entpd1 = models.FloatField(db_column='ENTPD1', blank=True, null=True)  # Field name made lowercase.
    tcf7l2 = models.FloatField(db_column='TCF7L2', blank=True, null=True)  # Field name made lowercase.
    bnip3 = models.FloatField(db_column='BNIP3', blank=True, null=True)  # Field name made lowercase.
    igf2 = models.FloatField(db_column='IGF2', blank=True, null=True)  # Field name made lowercase.
    ins = models.FloatField(db_column='INS', blank=True, null=True)  # Field name made lowercase.
    th = models.FloatField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    kcnq1 = models.FloatField(db_column='KCNQ1', blank=True, null=True)  # Field name made lowercase.
    hbg2 = models.FloatField(db_column='HBG2', blank=True, null=True)  # Field name made lowercase.
    smpd1 = models.FloatField(db_column='SMPD1', blank=True, null=True)  # Field name made lowercase.
    ilk = models.FloatField(db_column='ILK', blank=True, null=True)  # Field name made lowercase.
    adm = models.FloatField(db_column='ADM', blank=True, null=True)  # Field name made lowercase.
    pth = models.FloatField(db_column='PTH', blank=True, null=True)  # Field name made lowercase.
    nucb2 = models.FloatField(db_column='NUCB2', blank=True, null=True)  # Field name made lowercase.
    kcnj11 = models.FloatField(db_column='KCNJ11', blank=True, null=True)  # Field name made lowercase.
    saa1 = models.FloatField(db_column='SAA1', blank=True, null=True)  # Field name made lowercase.
    bdnf = models.FloatField(db_column='BDNF', blank=True, null=True)  # Field name made lowercase.
    wt1 = models.FloatField(db_column='WT1', blank=True, null=True)  # Field name made lowercase.
    cd59 = models.FloatField(db_column='CD59', blank=True, null=True)  # Field name made lowercase.
    pdhx = models.FloatField(db_column='PDHX', blank=True, null=True)  # Field name made lowercase.
    traf6 = models.FloatField(db_column='TRAF6', blank=True, null=True)  # Field name made lowercase.
    api5 = models.FloatField(db_column='API5', blank=True, null=True)  # Field name made lowercase.
    nr1h3 = models.FloatField(db_column='NR1H3', blank=True, null=True)  # Field name made lowercase.
    ndufs3 = models.FloatField(db_column='NDUFS3', blank=True, null=True)  # Field name made lowercase.
    folh1 = models.FloatField(db_column='FOLH1', blank=True, null=True)  # Field name made lowercase.
    aplnr = models.FloatField(db_column='APLNR', blank=True, null=True)  # Field name made lowercase.
    p2rx3 = models.FloatField(db_column='P2RX3', blank=True, null=True)  # Field name made lowercase.
    cntf = models.FloatField(db_column='CNTF', blank=True, null=True)  # Field name made lowercase.
    fads1 = models.FloatField(db_column='FADS1', blank=True, null=True)  # Field name made lowercase.
    fads2 = models.FloatField(db_column='FADS2', blank=True, null=True)  # Field name made lowercase.
    fkbp2 = models.FloatField(db_column='FKBP2', blank=True, null=True)  # Field name made lowercase.
    syvn1 = models.FloatField(db_column='SYVN1', blank=True, null=True)  # Field name made lowercase.
    pc = models.FloatField(db_column='PC', blank=True, null=True)  # Field name made lowercase.
    dhcr7 = models.FloatField(db_column='DHCR7', blank=True, null=True)  # Field name made lowercase.
    prcp = models.FloatField(db_column='PRCP', blank=True, null=True)  # Field name made lowercase.
    nox4 = models.FloatField(db_column='NOX4', blank=True, null=True)  # Field name made lowercase.
    pdgfd = models.FloatField(db_column='PDGFD', blank=True, null=True)  # Field name made lowercase.
    atm = models.FloatField(db_column='ATM', blank=True, null=True)  # Field name made lowercase.
    il18 = models.FloatField(db_column='IL18', blank=True, null=True)  # Field name made lowercase.
    apoa1 = models.FloatField(db_column='APOA1', blank=True, null=True)  # Field name made lowercase.
    hyou1 = models.FloatField(db_column='HYOU1', blank=True, null=True)  # Field name made lowercase.
    esam = models.FloatField(db_column='ESAM', blank=True, null=True)  # Field name made lowercase.
    fkbp4 = models.FloatField(db_column='FKBP4', blank=True, null=True)  # Field name made lowercase.
    fgf23 = models.FloatField(db_column='FGF23', blank=True, null=True)  # Field name made lowercase.
    ntf3 = models.FloatField(db_column='NTF3', blank=True, null=True)  # Field name made lowercase.
    vwf = models.FloatField(db_column='VWF', blank=True, null=True)  # Field name made lowercase.
    cd9 = models.FloatField(db_column='CD9', blank=True, null=True)  # Field name made lowercase.
    gapdh = models.FloatField(db_column='GAPDH', blank=True, null=True)  # Field name made lowercase.
    cd4 = models.FloatField(db_column='CD4', blank=True, null=True)  # Field name made lowercase.
    gnb3 = models.FloatField(db_column='GNB3', blank=True, null=True)  # Field name made lowercase.
    cd163 = models.FloatField(db_column='CD163', blank=True, null=True)  # Field name made lowercase.
    slc2a3 = models.FloatField(db_column='SLC2A3', blank=True, null=True)  # Field name made lowercase.
    cd69 = models.FloatField(db_column='CD69', blank=True, null=True)  # Field name made lowercase.
    irak4 = models.FloatField(db_column='IRAK4', blank=True, null=True)  # Field name made lowercase.
    vdr = models.FloatField(db_column='VDR', blank=True, null=True)  # Field name made lowercase.
    aqp5 = models.FloatField(db_column='AQP5', blank=True, null=True)  # Field name made lowercase.
    acvrl1 = models.FloatField(db_column='ACVRL1', blank=True, null=True)  # Field name made lowercase.
    nfe2 = models.FloatField(db_column='NFE2', blank=True, null=True)  # Field name made lowercase.
    cd63 = models.FloatField(db_column='CD63', blank=True, null=True)  # Field name made lowercase.
    erbb3 = models.FloatField(db_column='ERBB3', blank=True, null=True)  # Field name made lowercase.
    ddit3 = models.FloatField(db_column='DDIT3', blank=True, null=True)  # Field name made lowercase.
    ifng = models.FloatField(db_column='IFNG', blank=True, null=True)  # Field name made lowercase.
    nts = models.FloatField(db_column='NTS', blank=True, null=True)  # Field name made lowercase.
    igf1 = models.FloatField(db_column='IGF1', blank=True, null=True)  # Field name made lowercase.
    acacb = models.FloatField(db_column='ACACB', blank=True, null=True)  # Field name made lowercase.
    trpv4 = models.FloatField(db_column='TRPV4', blank=True, null=True)  # Field name made lowercase.
    atp2a2 = models.FloatField(db_column='ATP2A2', blank=True, null=True)  # Field name made lowercase.
    aldh2 = models.FloatField(db_column='ALDH2', blank=True, null=True)  # Field name made lowercase.
    nos1 = models.FloatField(db_column='NOS1', blank=True, null=True)  # Field name made lowercase.
    pebp1 = models.FloatField(db_column='PEBP1', blank=True, null=True)  # Field name made lowercase.
    psmd9 = models.FloatField(db_column='PSMD9', blank=True, null=True)  # Field name made lowercase.
    scarb1 = models.FloatField(db_column='SCARB1', blank=True, null=True)  # Field name made lowercase.
    p2rx2 = models.FloatField(db_column='P2RX2', blank=True, null=True)  # Field name made lowercase.
    alox5ap = models.FloatField(db_column='ALOX5AP', blank=True, null=True)  # Field name made lowercase.
    kl = models.FloatField(db_column='KL', blank=True, null=True)  # Field name made lowercase.
    postn = models.FloatField(db_column='POSTN', blank=True, null=True)  # Field name made lowercase.
    foxo1 = models.FloatField(db_column='FOXO1', blank=True, null=True)  # Field name made lowercase.
    htr2a = models.FloatField(db_column='HTR2A', blank=True, null=True)  # Field name made lowercase.
    gpc5 = models.FloatField(db_column='GPC5', blank=True, null=True)  # Field name made lowercase.
    irs2 = models.FloatField(db_column='IRS2', blank=True, null=True)  # Field name made lowercase.
    gas6 = models.FloatField(db_column='GAS6', blank=True, null=True)  # Field name made lowercase.
    ang = models.FloatField(db_column='ANG', blank=True, null=True)  # Field name made lowercase.
    mmp14 = models.FloatField(db_column='MMP14', blank=True, null=True)  # Field name made lowercase.
    ltb4r2 = models.FloatField(db_column='LTB4R2', blank=True, null=True)  # Field name made lowercase.
    nfkbia = models.FloatField(db_column='NFKBIA', blank=True, null=True)  # Field name made lowercase.
    bmp4 = models.FloatField(db_column='BMP4', blank=True, null=True)  # Field name made lowercase.
    rtn1 = models.FloatField(db_column='RTN1', blank=True, null=True)  # Field name made lowercase.
    pgf = models.FloatField(db_column='PGF', blank=True, null=True)  # Field name made lowercase.
    ngb = models.FloatField(db_column='NGB', blank=True, null=True)  # Field name made lowercase.
    ahsa1 = models.FloatField(db_column='AHSA1', blank=True, null=True)  # Field name made lowercase.
    bdkrb2 = models.FloatField(db_column='BDKRB2', blank=True, null=True)  # Field name made lowercase.
    bdkrb1 = models.FloatField(db_column='BDKRB1', blank=True, null=True)  # Field name made lowercase.
    akt1 = models.FloatField(db_column='AKT1', blank=True, null=True)  # Field name made lowercase.
    grem1 = models.FloatField(db_column='GREM1', blank=True, null=True)  # Field name made lowercase.
    thbs1 = models.FloatField(db_column='THBS1', blank=True, null=True)  # Field name made lowercase.
    pak6 = models.FloatField(db_column='PAK6', blank=True, null=True)  # Field name made lowercase.
    b2m = models.FloatField(db_column='B2M', blank=True, null=True)  # Field name made lowercase.
    myo5c = models.FloatField(db_column='MYO5C', blank=True, null=True)  # Field name made lowercase.
    onecut1 = models.FloatField(db_column='ONECUT1', blank=True, null=True)  # Field name made lowercase.
    adam10 = models.FloatField(db_column='ADAM10', blank=True, null=True)  # Field name made lowercase.
    ctsh = models.FloatField(db_column='CTSH', blank=True, null=True)  # Field name made lowercase.
    plin1 = models.FloatField(db_column='PLIN1', blank=True, null=True)  # Field name made lowercase.
    igf1r = models.FloatField(db_column='IGF1R', blank=True, null=True)  # Field name made lowercase.
    mrpl28 = models.FloatField(db_column='MRPL28', blank=True, null=True)  # Field name made lowercase.
    cacna1h = models.FloatField(db_column='CACNA1H', blank=True, null=True)  # Field name made lowercase.
    pdpk1 = models.FloatField(db_column='PDPK1', blank=True, null=True)  # Field name made lowercase.
    ercc4 = models.FloatField(db_column='ERCC4', blank=True, null=True)  # Field name made lowercase.
    smg1 = models.FloatField(db_column='SMG1', blank=True, null=True)  # Field name made lowercase.
    itgam = models.FloatField(db_column='ITGAM', blank=True, null=True)  # Field name made lowercase.
    fto = models.FloatField(db_column='FTO', blank=True, null=True)  # Field name made lowercase.
    mmp2 = models.FloatField(db_column='MMP2', blank=True, null=True)  # Field name made lowercase.
    slc12a3 = models.FloatField(db_column='SLC12A3', blank=True, null=True)  # Field name made lowercase.
    cetp = models.FloatField(db_column='CETP', blank=True, null=True)  # Field name made lowercase.
    cx3cl1 = models.FloatField(db_column='CX3CL1', blank=True, null=True)  # Field name made lowercase.
    cdh1 = models.FloatField(db_column='CDH1', blank=True, null=True)  # Field name made lowercase.
    nqo1 = models.FloatField(db_column='NQO1', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    znrf1 = models.FloatField(db_column='ZNRF1', blank=True, null=True)  # Field name made lowercase.
    cyba = models.FloatField(db_column='CYBA', blank=True, null=True)  # Field name made lowercase.
    tubb3 = models.FloatField(db_column='TUBB3', blank=True, null=True)  # Field name made lowercase.
    crk = models.FloatField(db_column='CRK', blank=True, null=True)  # Field name made lowercase.
    serpinf2 = models.FloatField(db_column='SERPINF2', blank=True, null=True)  # Field name made lowercase.
    serpinf1 = models.FloatField(db_column='SERPINF1', blank=True, null=True)  # Field name made lowercase.
    trpv3 = models.FloatField(db_column='TRPV3', blank=True, null=True)  # Field name made lowercase.
    cxcl16 = models.FloatField(db_column='CXCL16', blank=True, null=True)  # Field name made lowercase.
    slc2a4 = models.FloatField(db_column='SLC2A4', blank=True, null=True)  # Field name made lowercase.
    cd68 = models.FloatField(db_column='CD68', blank=True, null=True)  # Field name made lowercase.
    shbg = models.FloatField(db_column='SHBG', blank=True, null=True)  # Field name made lowercase.
    pmp22 = models.FloatField(db_column='PMP22', blank=True, null=True)  # Field name made lowercase.
    srebf1 = models.FloatField(db_column='SREBF1', blank=True, null=True)  # Field name made lowercase.
    mapk7 = models.FloatField(db_column='MAPK7', blank=True, null=True)  # Field name made lowercase.
    ccl2 = models.FloatField(db_column='CCL2', blank=True, null=True)  # Field name made lowercase.
    ccl5 = models.FloatField(db_column='CCL5', blank=True, null=True)  # Field name made lowercase.
    hnf1b = models.FloatField(db_column='HNF1B', blank=True, null=True)  # Field name made lowercase.
    erbb2 = models.FloatField(db_column='ERBB2', blank=True, null=True)  # Field name made lowercase.
    fkbp10 = models.FloatField(db_column='FKBP10', blank=True, null=True)  # Field name made lowercase.
    stat5a = models.FloatField(db_column='STAT5A', blank=True, null=True)  # Field name made lowercase.
    stat3 = models.FloatField(db_column='STAT3', blank=True, null=True)  # Field name made lowercase.
    naglu = models.FloatField(db_column='NAGLU', blank=True, null=True)  # Field name made lowercase.
    aoc2 = models.FloatField(db_column='AOC2', blank=True, null=True)  # Field name made lowercase.
    aoc3 = models.FloatField(db_column='AOC3', blank=True, null=True)  # Field name made lowercase.
    ppy = models.FloatField(db_column='PPY', blank=True, null=True)  # Field name made lowercase.
    sth = models.FloatField(db_column='STH', blank=True, null=True)  # Field name made lowercase.
    itgb3 = models.FloatField(db_column='ITGB3', blank=True, null=True)  # Field name made lowercase.
    gip = models.FloatField(db_column='GIP', blank=True, null=True)  # Field name made lowercase.
    mpo = models.FloatField(db_column='MPO', blank=True, null=True)  # Field name made lowercase.
    pecam1 = models.FloatField(db_column='PECAM1', blank=True, null=True)  # Field name made lowercase.
    sox9 = models.FloatField(db_column='SOX9', blank=True, null=True)  # Field name made lowercase.
    timp2 = models.FloatField(db_column='TIMP2', blank=True, null=True)  # Field name made lowercase.
    dcxr = models.FloatField(db_column='DCXR', blank=True, null=True)  # Field name made lowercase.
    fasn = models.FloatField(db_column='FASN', blank=True, null=True)  # Field name made lowercase.
    colec12 = models.FloatField(db_column='COLEC12', blank=True, null=True)  # Field name made lowercase.
    adcyap1 = models.FloatField(db_column='ADCYAP1', blank=True, null=True)  # Field name made lowercase.
    smad7 = models.FloatField(db_column='SMAD7', blank=True, null=True)  # Field name made lowercase.
    nedd4l = models.FloatField(db_column='NEDD4L', blank=True, null=True)  # Field name made lowercase.
    mc4r = models.FloatField(db_column='MC4R', blank=True, null=True)  # Field name made lowercase.
    bcl2 = models.FloatField(db_column='BCL2', blank=True, null=True)  # Field name made lowercase.
    cndp2 = models.FloatField(db_column='CNDP2', blank=True, null=True)  # Field name made lowercase.
    znf236 = models.FloatField(db_column='ZNF236', blank=True, null=True)  # Field name made lowercase.
    stk11 = models.FloatField(db_column='STK11', blank=True, null=True)  # Field name made lowercase.
    sirt6 = models.FloatField(db_column='SIRT6', blank=True, null=True)  # Field name made lowercase.
    uhrf1 = models.FloatField(db_column='UHRF1', blank=True, null=True)  # Field name made lowercase.
    timm44 = models.FloatField(db_column='TIMM44', blank=True, null=True)  # Field name made lowercase.
    angptl4 = models.FloatField(db_column='ANGPTL4', blank=True, null=True)  # Field name made lowercase.
    dnmt1 = models.FloatField(db_column='DNMT1', blank=True, null=True)  # Field name made lowercase.
    icam1 = models.FloatField(db_column='ICAM1', blank=True, null=True)  # Field name made lowercase.
    ldlr = models.FloatField(db_column='LDLR', blank=True, null=True)  # Field name made lowercase.
    epor = models.FloatField(db_column='EPOR', blank=True, null=True)  # Field name made lowercase.
    prdx2 = models.FloatField(db_column='PRDX2', blank=True, null=True)  # Field name made lowercase.
    ptger1 = models.FloatField(db_column='PTGER1', blank=True, null=True)  # Field name made lowercase.
    unc13a = models.FloatField(db_column='UNC13A', blank=True, null=True)  # Field name made lowercase.
    gdf15 = models.FloatField(db_column='GDF15', blank=True, null=True)  # Field name made lowercase.
    fkbp8 = models.FloatField(db_column='FKBP8', blank=True, null=True)  # Field name made lowercase.
    usf2 = models.FloatField(db_column='USF2', blank=True, null=True)  # Field name made lowercase.
    ffar1 = models.FloatField(db_column='FFAR1', blank=True, null=True)  # Field name made lowercase.
    ffar2 = models.FloatField(db_column='FFAR2', blank=True, null=True)  # Field name made lowercase.
    nphs1 = models.FloatField(db_column='NPHS1', blank=True, null=True)  # Field name made lowercase.
    tgfb1 = models.FloatField(db_column='TGFB1', blank=True, null=True)  # Field name made lowercase.
    xrcc1 = models.FloatField(db_column='XRCC1', blank=True, null=True)  # Field name made lowercase.
    ercc1 = models.FloatField(db_column='ERCC1', blank=True, null=True)  # Field name made lowercase.
    gipr = models.FloatField(db_column='GIPR', blank=True, null=True)  # Field name made lowercase.
    fgf21 = models.FloatField(db_column='FGF21', blank=True, null=True)  # Field name made lowercase.
    clec11a = models.FloatField(db_column='CLEC11A', blank=True, null=True)  # Field name made lowercase.
    fpr1 = models.FloatField(db_column='FPR1', blank=True, null=True)  # Field name made lowercase.
    trib3 = models.FloatField(db_column='TRIB3', blank=True, null=True)  # Field name made lowercase.
    bmp2 = models.FloatField(db_column='BMP2', blank=True, null=True)  # Field name made lowercase.
    thbd = models.FloatField(db_column='THBD', blank=True, null=True)  # Field name made lowercase.
    cst3 = models.FloatField(db_column='CST3', blank=True, null=True)  # Field name made lowercase.
    id1 = models.FloatField(db_column='ID1', blank=True, null=True)  # Field name made lowercase.
    src = models.FloatField(db_column='SRC', blank=True, null=True)  # Field name made lowercase.
    mafb = models.FloatField(db_column='MAFB', blank=True, null=True)  # Field name made lowercase.
    sgk2 = models.FloatField(db_column='SGK2', blank=True, null=True)  # Field name made lowercase.
    hnf4a = models.FloatField(db_column='HNF4A', blank=True, null=True)  # Field name made lowercase.
    pltp = models.FloatField(db_column='PLTP', blank=True, null=True)  # Field name made lowercase.
    mmp9 = models.FloatField(db_column='MMP9', blank=True, null=True)  # Field name made lowercase.
    cd40 = models.FloatField(db_column='CD40', blank=True, null=True)  # Field name made lowercase.
    ptpn1 = models.FloatField(db_column='PTPN1', blank=True, null=True)  # Field name made lowercase.
    cyp24a1 = models.FloatField(db_column='CYP24A1', blank=True, null=True)  # Field name made lowercase.
    rcan1 = models.FloatField(db_column='RCAN1', blank=True, null=True)  # Field name made lowercase.
    abcg1 = models.FloatField(db_column='ABCG1', blank=True, null=True)  # Field name made lowercase.
    prmt2 = models.FloatField(db_column='PRMT2', blank=True, null=True)  # Field name made lowercase.
    comt = models.FloatField(db_column='COMT', blank=True, null=True)  # Field name made lowercase.
    mapk1 = models.FloatField(db_column='MAPK1', blank=True, null=True)  # Field name made lowercase.
    mif = models.FloatField(db_column='MIF', blank=True, null=True)  # Field name made lowercase.
    ggt1 = models.FloatField(db_column='GGT1', blank=True, null=True)  # Field name made lowercase.
    xbp1 = models.FloatField(db_column='XBP1', blank=True, null=True)  # Field name made lowercase.
    osm = models.FloatField(db_column='OSM', blank=True, null=True)  # Field name made lowercase.
    limk2 = models.FloatField(db_column='LIMK2', blank=True, null=True)  # Field name made lowercase.
    sfi1 = models.FloatField(db_column='SFI1', blank=True, null=True)  # Field name made lowercase.
    timp3 = models.FloatField(db_column='TIMP3', blank=True, null=True)  # Field name made lowercase.
    hmox1 = models.FloatField(db_column='HMOX1', blank=True, null=True)  # Field name made lowercase.
    apol1 = models.FloatField(db_column='APOL1', blank=True, null=True)  # Field name made lowercase.
    myh9 = models.FloatField(db_column='MYH9', blank=True, null=True)  # Field name made lowercase.
    pdgfb = models.FloatField(db_column='PDGFB', blank=True, null=True)  # Field name made lowercase.
    atf4 = models.FloatField(db_column='ATF4', blank=True, null=True)  # Field name made lowercase.
    tspo = models.FloatField(db_column='TSPO', blank=True, null=True)  # Field name made lowercase.
    miox = models.FloatField(db_column='MIOX', blank=True, null=True)  # Field name made lowercase.
    prdx4 = models.FloatField(db_column='PRDX4', blank=True, null=True)  # Field name made lowercase.
    gk = models.FloatField(db_column='GK', blank=True, null=True)  # Field name made lowercase.
    rgn = models.FloatField(db_column='RGN', blank=True, null=True)  # Field name made lowercase.
    timp1 = models.FloatField(db_column='TIMP1', blank=True, null=True)  # Field name made lowercase.
    clcn5 = models.FloatField(db_column='CLCN5', blank=True, null=True)  # Field name made lowercase.
    ar = models.FloatField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    foxo4 = models.FloatField(db_column='FOXO4', blank=True, null=True)  # Field name made lowercase.
    rps6ka6 = models.FloatField(db_column='RPS6KA6', blank=True, null=True)  # Field name made lowercase.
    nox1 = models.FloatField(db_column='NOX1', blank=True, null=True)  # Field name made lowercase.
    xiap = models.FloatField(db_column='XIAP', blank=True, null=True)  # Field name made lowercase.
    cd40lg = models.FloatField(db_column='CD40LG', blank=True, null=True)  # Field name made lowercase.
    l1cam = models.FloatField(db_column='L1CAM', blank=True, null=True)  # Field name made lowercase.
    irak1 = models.FloatField(db_column='IRAK1', blank=True, null=True)  # Field name made lowercase.
    g6pd = models.FloatField(db_column='G6PD', blank=True, null=True)  # Field name made lowercase.
    f8 = models.FloatField(db_column='F8', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diaco_tissue_brain_anterior_cc_ba24'


class DiacoTissueBrainCaudateBg(models.Model):
    subjid = models.CharField(db_column='SUBJID', max_length=50, primary_key=True)  # Field name made lowercase.
    sampid = models.CharField(db_column='SAMPID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sesso = models.CharField(db_column='Sesso', max_length=1)  # Field name made lowercase.
    eta = models.CharField(db_column='Età', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errfi1 = models.FloatField(db_column='ERRFI1', blank=True, null=True)  # Field name made lowercase.
    mad2l2 = models.FloatField(db_column='MAD2L2', blank=True, null=True)  # Field name made lowercase.
    mthfr = models.FloatField(db_column='MTHFR', blank=True, null=True)  # Field name made lowercase.
    nppa = models.FloatField(db_column='NPPA', blank=True, null=True)  # Field name made lowercase.
    tnfrsf1b = models.FloatField(db_column='TNFRSF1B', blank=True, null=True)  # Field name made lowercase.
    pla2g2a = models.FloatField(db_column='PLA2G2A', blank=True, null=True)  # Field name made lowercase.
    alpl = models.FloatField(db_column='ALPL', blank=True, null=True)  # Field name made lowercase.
    hspg2 = models.FloatField(db_column='HSPG2', blank=True, null=True)  # Field name made lowercase.
    cnr2 = models.FloatField(db_column='CNR2', blank=True, null=True)  # Field name made lowercase.
    slc9a1 = models.FloatField(db_column='SLC9A1', blank=True, null=True)  # Field name made lowercase.
    col8a2 = models.FloatField(db_column='COL8A2', blank=True, null=True)  # Field name made lowercase.
    cap1 = models.FloatField(db_column='CAP1', blank=True, null=True)  # Field name made lowercase.
    slc2a1 = models.FloatField(db_column='SLC2A1', blank=True, null=True)  # Field name made lowercase.
    cyp2j2 = models.FloatField(db_column='CYP2J2', blank=True, null=True)  # Field name made lowercase.
    ddah1 = models.FloatField(db_column='DDAH1', blank=True, null=True)  # Field name made lowercase.
    cyr61 = models.FloatField(db_column='CYR61', blank=True, null=True)  # Field name made lowercase.
    ngf = models.FloatField(db_column='NGF', blank=True, null=True)  # Field name made lowercase.
    hmgcs2 = models.FloatField(db_column='HMGCS2', blank=True, null=True)  # Field name made lowercase.
    ctss = models.FloatField(db_column='CTSS', blank=True, null=True)  # Field name made lowercase.
    s100a12 = models.FloatField(db_column='S100A12', blank=True, null=True)  # Field name made lowercase.
    lmna = models.FloatField(db_column='LMNA', blank=True, null=True)  # Field name made lowercase.
    cd247 = models.FloatField(db_column='CD247', blank=True, null=True)  # Field name made lowercase.
    sele = models.FloatField(db_column='SELE', blank=True, null=True)  # Field name made lowercase.
    fmo3 = models.FloatField(db_column='FMO3', blank=True, null=True)  # Field name made lowercase.
    prdx6 = models.FloatField(db_column='PRDX6', blank=True, null=True)  # Field name made lowercase.
    glul = models.FloatField(db_column='GLUL', blank=True, null=True)  # Field name made lowercase.
    lamc1 = models.FloatField(db_column='LAMC1', blank=True, null=True)  # Field name made lowercase.
    ptgs2 = models.FloatField(db_column='PTGS2', blank=True, null=True)  # Field name made lowercase.
    chi3l1 = models.FloatField(db_column='CHI3L1', blank=True, null=True)  # Field name made lowercase.
    chit1 = models.FloatField(db_column='CHIT1', blank=True, null=True)  # Field name made lowercase.
    fmod = models.FloatField(db_column='FMOD', blank=True, null=True)  # Field name made lowercase.
    il10 = models.FloatField(db_column='IL10', blank=True, null=True)  # Field name made lowercase.
    pfkfb2 = models.FloatField(db_column='PFKFB2', blank=True, null=True)  # Field name made lowercase.
    cd34 = models.FloatField(db_column='CD34', blank=True, null=True)  # Field name made lowercase.
    cog2 = models.FloatField(db_column='COG2', blank=True, null=True)  # Field name made lowercase.
    nlrp3 = models.FloatField(db_column='NLRP3', blank=True, null=True)  # Field name made lowercase.
    rock2 = models.FloatField(db_column='ROCK2', blank=True, null=True)  # Field name made lowercase.
    apob = models.FloatField(db_column='APOB', blank=True, null=True)  # Field name made lowercase.
    pomc = models.FloatField(db_column='POMC', blank=True, null=True)  # Field name made lowercase.
    gckr = models.FloatField(db_column='GCKR', blank=True, null=True)  # Field name made lowercase.
    plekhh2 = models.FloatField(db_column='PLEKHH2', blank=True, null=True)  # Field name made lowercase.
    prkce = models.FloatField(db_column='PRKCE', blank=True, null=True)  # Field name made lowercase.
    pigf = models.FloatField(db_column='PIGF', blank=True, null=True)  # Field name made lowercase.
    msh2 = models.FloatField(db_column='MSH2', blank=True, null=True)  # Field name made lowercase.
    gfpt1 = models.FloatField(db_column='GFPT1', blank=True, null=True)  # Field name made lowercase.
    tacr1 = models.FloatField(db_column='TACR1', blank=True, null=True)  # Field name made lowercase.
    reg1a = models.FloatField(db_column='REG1A', blank=True, null=True)  # Field name made lowercase.
    eif2ak3 = models.FloatField(db_column='EIF2AK3', blank=True, null=True)  # Field name made lowercase.
    adra2b = models.FloatField(db_column='ADRA2B', blank=True, null=True)  # Field name made lowercase.
    il1b = models.FloatField(db_column='IL1B', blank=True, null=True)  # Field name made lowercase.
    proc = models.FloatField(db_column='PROC', blank=True, null=True)  # Field name made lowercase.
    polr2d = models.FloatField(db_column='POLR2D', blank=True, null=True)  # Field name made lowercase.
    zeb2 = models.FloatField(db_column='ZEB2', blank=True, null=True)  # Field name made lowercase.
    acvr1c = models.FloatField(db_column='ACVR1C', blank=True, null=True)  # Field name made lowercase.
    dpp4 = models.FloatField(db_column='DPP4', blank=True, null=True)  # Field name made lowercase.
    nfe2l2 = models.FloatField(db_column='NFE2L2', blank=True, null=True)  # Field name made lowercase.
    igfbp5 = models.FloatField(db_column='IGFBP5', blank=True, null=True)  # Field name made lowercase.
    ccl20 = models.FloatField(db_column='CCL20', blank=True, null=True)  # Field name made lowercase.
    hdac4 = models.FloatField(db_column='HDAC4', blank=True, null=True)  # Field name made lowercase.
    capn10 = models.FloatField(db_column='CAPN10', blank=True, null=True)  # Field name made lowercase.
    ghrl = models.FloatField(db_column='GHRL', blank=True, null=True)  # Field name made lowercase.
    pparg = models.FloatField(db_column='PPARG', blank=True, null=True)  # Field name made lowercase.
    raf1 = models.FloatField(db_column='RAF1', blank=True, null=True)  # Field name made lowercase.
    myd88 = models.FloatField(db_column='MYD88', blank=True, null=True)  # Field name made lowercase.
    cx3cr1 = models.FloatField(db_column='CX3CR1', blank=True, null=True)  # Field name made lowercase.
    cck = models.FloatField(db_column='CCK', blank=True, null=True)  # Field name made lowercase.
    exosc7 = models.FloatField(db_column='EXOSC7', blank=True, null=True)  # Field name made lowercase.
    ccr1 = models.FloatField(db_column='CCR1', blank=True, null=True)  # Field name made lowercase.
    ccr5 = models.FloatField(db_column='CCR5', blank=True, null=True)  # Field name made lowercase.
    gpx1 = models.FloatField(db_column='GPX1', blank=True, null=True)  # Field name made lowercase.
    rhoa = models.FloatField(db_column='RHOA', blank=True, null=True)  # Field name made lowercase.
    cish = models.FloatField(db_column='CISH', blank=True, null=True)  # Field name made lowercase.
    tkt = models.FloatField(db_column='TKT', blank=True, null=True)  # Field name made lowercase.
    appl1 = models.FloatField(db_column='APPL1', blank=True, null=True)  # Field name made lowercase.
    slmap = models.FloatField(db_column='SLMAP', blank=True, null=True)  # Field name made lowercase.
    col8a1 = models.FloatField(db_column='COL8A1', blank=True, null=True)  # Field name made lowercase.
    cd47 = models.FloatField(db_column='CD47', blank=True, null=True)  # Field name made lowercase.
    gap43 = models.FloatField(db_column='GAP43', blank=True, null=True)  # Field name made lowercase.
    cd80 = models.FloatField(db_column='CD80', blank=True, null=True)  # Field name made lowercase.
    rho = models.FloatField(db_column='RHO', blank=True, null=True)  # Field name made lowercase.
    trh = models.FloatField(db_column='TRH', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='TF', blank=True, null=True)  # Field name made lowercase.
    rbp1 = models.FloatField(db_column='RBP1', blank=True, null=True)  # Field name made lowercase.
    trpc1 = models.FloatField(db_column='TRPC1', blank=True, null=True)  # Field name made lowercase.
    agtr1 = models.FloatField(db_column='AGTR1', blank=True, null=True)  # Field name made lowercase.
    sucnr1 = models.FloatField(db_column='SUCNR1', blank=True, null=True)  # Field name made lowercase.
    p2ry1 = models.FloatField(db_column='P2RY1', blank=True, null=True)  # Field name made lowercase.
    mme = models.FloatField(db_column='MME', blank=True, null=True)  # Field name made lowercase.
    slc2a2 = models.FloatField(db_column='SLC2A2', blank=True, null=True)  # Field name made lowercase.
    pik3ca = models.FloatField(db_column='PIK3CA', blank=True, null=True)  # Field name made lowercase.
    parl = models.FloatField(db_column='PARL', blank=True, null=True)  # Field name made lowercase.
    ahsg = models.FloatField(db_column='AHSG', blank=True, null=True)  # Field name made lowercase.
    adipoq = models.FloatField(db_column='ADIPOQ', blank=True, null=True)  # Field name made lowercase.
    spon2 = models.FloatField(db_column='SPON2', blank=True, null=True)  # Field name made lowercase.
    wfs1 = models.FloatField(db_column='WFS1', blank=True, null=True)  # Field name made lowercase.
    cd38 = models.FloatField(db_column='CD38', blank=True, null=True)  # Field name made lowercase.
    prom1 = models.FloatField(db_column='PROM1', blank=True, null=True)  # Field name made lowercase.
    ppargc1a = models.FloatField(db_column='PPARGC1A', blank=True, null=True)  # Field name made lowercase.
    igfbp7 = models.FloatField(db_column='IGFBP7', blank=True, null=True)  # Field name made lowercase.
    cxcl5 = models.FloatField(db_column='CXCL5', blank=True, null=True)  # Field name made lowercase.
    cxcl9 = models.FloatField(db_column='CXCL9', blank=True, null=True)  # Field name made lowercase.
    cxcl10 = models.FloatField(db_column='CXCL10', blank=True, null=True)  # Field name made lowercase.
    cxcl11 = models.FloatField(db_column='CXCL11', blank=True, null=True)  # Field name made lowercase.
    hpse = models.FloatField(db_column='HPSE', blank=True, null=True)  # Field name made lowercase.
    spp1 = models.FloatField(db_column='SPP1', blank=True, null=True)  # Field name made lowercase.
    adh1b = models.FloatField(db_column='ADH1B', blank=True, null=True)  # Field name made lowercase.
    egf = models.FloatField(db_column='EGF', blank=True, null=True)  # Field name made lowercase.
    alpk1 = models.FloatField(db_column='ALPK1', blank=True, null=True)  # Field name made lowercase.
    fabp2 = models.FloatField(db_column='FABP2', blank=True, null=True)  # Field name made lowercase.
    pde5a = models.FloatField(db_column='PDE5A', blank=True, null=True)  # Field name made lowercase.
    setd7 = models.FloatField(db_column='SETD7', blank=True, null=True)  # Field name made lowercase.
    smad1 = models.FloatField(db_column='SMAD1', blank=True, null=True)  # Field name made lowercase.
    ednra = models.FloatField(db_column='EDNRA', blank=True, null=True)  # Field name made lowercase.
    nr3c2 = models.FloatField(db_column='NR3C2', blank=True, null=True)  # Field name made lowercase.
    tlr2 = models.FloatField(db_column='TLR2', blank=True, null=True)  # Field name made lowercase.
    npy5r = models.FloatField(db_column='NPY5R', blank=True, null=True)  # Field name made lowercase.
    fbxo8 = models.FloatField(db_column='FBXO8', blank=True, null=True)  # Field name made lowercase.
    vegfc = models.FloatField(db_column='VEGFC', blank=True, null=True)  # Field name made lowercase.
    acsl1 = models.FloatField(db_column='ACSL1', blank=True, null=True)  # Field name made lowercase.
    sorbs2 = models.FloatField(db_column='SORBS2', blank=True, null=True)  # Field name made lowercase.
    f11 = models.FloatField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    basp1 = models.FloatField(db_column='BASP1', blank=True, null=True)  # Field name made lowercase.
    ptger4 = models.FloatField(db_column='PTGER4', blank=True, null=True)  # Field name made lowercase.
    prkaa1 = models.FloatField(db_column='PRKAA1', blank=True, null=True)  # Field name made lowercase.
    ghr = models.FloatField(db_column='GHR', blank=True, null=True)  # Field name made lowercase.
    itga2 = models.FloatField(db_column='ITGA2', blank=True, null=True)  # Field name made lowercase.
    cdk7 = models.FloatField(db_column='CDK7', blank=True, null=True)  # Field name made lowercase.
    f2r = models.FloatField(db_column='F2R', blank=True, null=True)  # Field name made lowercase.
    erap2 = models.FloatField(db_column='ERAP2', blank=True, null=True)  # Field name made lowercase.
    apc = models.FloatField(db_column='APC', blank=True, null=True)  # Field name made lowercase.
    tnfaip8 = models.FloatField(db_column='TNFAIP8', blank=True, null=True)  # Field name made lowercase.
    vdac1 = models.FloatField(db_column='VDAC1', blank=True, null=True)  # Field name made lowercase.
    pdgfrb = models.FloatField(db_column='PDGFRB', blank=True, null=True)  # Field name made lowercase.
    cd74 = models.FloatField(db_column='CD74', blank=True, null=True)  # Field name made lowercase.
    sparc = models.FloatField(db_column='SPARC', blank=True, null=True)  # Field name made lowercase.
    ebf1 = models.FloatField(db_column='EBF1', blank=True, null=True)  # Field name made lowercase.
    gfpt2 = models.FloatField(db_column='GFPT2', blank=True, null=True)  # Field name made lowercase.
    rreb1 = models.FloatField(db_column='RREB1', blank=True, null=True)  # Field name made lowercase.
    edn1 = models.FloatField(db_column='EDN1', blank=True, null=True)  # Field name made lowercase.
    cdkal1 = models.FloatField(db_column='CDKAL1', blank=True, null=True)  # Field name made lowercase.
    hfe = models.FloatField(db_column='HFE', blank=True, null=True)  # Field name made lowercase.
    hla_a = models.FloatField(db_column='HLA-A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  # Field name made lowercase.
    tnf = models.FloatField(db_column='TNF', blank=True, null=True)  # Field name made lowercase.
    hspa1a = models.FloatField(db_column='HSPA1A', blank=True, null=True)  # Field name made lowercase.
    hspa1b = models.FloatField(db_column='HSPA1B', blank=True, null=True)  # Field name made lowercase.
    hla_dqa1 = models.FloatField(db_column='HLA-DQA1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mapk14 = models.FloatField(db_column='MAPK14', blank=True, null=True)  # Field name made lowercase.
    cdkn1a = models.FloatField(db_column='CDKN1A', blank=True, null=True)  # Field name made lowercase.
    glo1 = models.FloatField(db_column='GLO1', blank=True, null=True)  # Field name made lowercase.
    vegfa = models.FloatField(db_column='VEGFA', blank=True, null=True)  # Field name made lowercase.
    cd2ap = models.FloatField(db_column='CD2AP', blank=True, null=True)  # Field name made lowercase.
    cnr1 = models.FloatField(db_column='CNR1', blank=True, null=True)  # Field name made lowercase.
    enpp1 = models.FloatField(db_column='ENPP1', blank=True, null=True)  # Field name made lowercase.
    ctgf = models.FloatField(db_column='CTGF', blank=True, null=True)  # Field name made lowercase.
    rps12 = models.FloatField(db_column='RPS12', blank=True, null=True)  # Field name made lowercase.
    sgk1 = models.FloatField(db_column='SGK1', blank=True, null=True)  # Field name made lowercase.
    map3k5 = models.FloatField(db_column='MAP3K5', blank=True, null=True)  # Field name made lowercase.
    cited2 = models.FloatField(db_column='CITED2', blank=True, null=True)  # Field name made lowercase.
    utrn = models.FloatField(db_column='UTRN', blank=True, null=True)  # Field name made lowercase.
    mthfd1l = models.FloatField(db_column='MTHFD1L', blank=True, null=True)  # Field name made lowercase.
    vip = models.FloatField(db_column='VIP', blank=True, null=True)  # Field name made lowercase.
    sod2 = models.FloatField(db_column='SOD2', blank=True, null=True)  # Field name made lowercase.
    lpa = models.FloatField(db_column='LPA', blank=True, null=True)  # Field name made lowercase.
    thbs2 = models.FloatField(db_column='THBS2', blank=True, null=True)  # Field name made lowercase.
    pdgfa = models.FloatField(db_column='PDGFA', blank=True, null=True)  # Field name made lowercase.
    il6 = models.FloatField(db_column='IL6', blank=True, null=True)  # Field name made lowercase.
    npy = models.FloatField(db_column='NPY', blank=True, null=True)  # Field name made lowercase.
    jazf1 = models.FloatField(db_column='JAZF1', blank=True, null=True)  # Field name made lowercase.
    cpvl = models.FloatField(db_column='CPVL', blank=True, null=True)  # Field name made lowercase.
    aqp1 = models.FloatField(db_column='AQP1', blank=True, null=True)  # Field name made lowercase.
    elmo1 = models.FloatField(db_column='ELMO1', blank=True, null=True)  # Field name made lowercase.
    igfbp3 = models.FloatField(db_column='IGFBP3', blank=True, null=True)  # Field name made lowercase.
    egfr = models.FloatField(db_column='EGFR', blank=True, null=True)  # Field name made lowercase.
    eln = models.FloatField(db_column='ELN', blank=True, null=True)  # Field name made lowercase.
    ncf1 = models.FloatField(db_column='NCF1', blank=True, null=True)  # Field name made lowercase.
    hspb1 = models.FloatField(db_column='HSPB1', blank=True, null=True)  # Field name made lowercase.
    sema3a = models.FloatField(db_column='SEMA3A', blank=True, null=True)  # Field name made lowercase.
    pon3 = models.FloatField(db_column='PON3', blank=True, null=True)  # Field name made lowercase.
    pon2 = models.FloatField(db_column='PON2', blank=True, null=True)  # Field name made lowercase.
    nampt = models.FloatField(db_column='NAMPT', blank=True, null=True)  # Field name made lowercase.
    cav1 = models.FloatField(db_column='CAV1', blank=True, null=True)  # Field name made lowercase.
    lep = models.FloatField(db_column='LEP', blank=True, null=True)  # Field name made lowercase.
    akr1b1 = models.FloatField(db_column='AKR1B1', blank=True, null=True)  # Field name made lowercase.
    akr1b10 = models.FloatField(db_column='AKR1B10', blank=True, null=True)  # Field name made lowercase.
    pip = models.FloatField(db_column='PIP', blank=True, null=True)  # Field name made lowercase.
    rarres2 = models.FloatField(db_column='RARRES2', blank=True, null=True)  # Field name made lowercase.
    nos3 = models.FloatField(db_column='NOS3', blank=True, null=True)  # Field name made lowercase.
    angpt2 = models.FloatField(db_column='ANGPT2', blank=True, null=True)  # Field name made lowercase.
    defa1 = models.FloatField(db_column='DEFA1', blank=True, null=True)  # Field name made lowercase.
    lpl = models.FloatField(db_column='LPL', blank=True, null=True)  # Field name made lowercase.
    ebf2 = models.FloatField(db_column='EBF2', blank=True, null=True)  # Field name made lowercase.
    adrb3 = models.FloatField(db_column='ADRB3', blank=True, null=True)  # Field name made lowercase.
    eif4ebp1 = models.FloatField(db_column='EIF4EBP1', blank=True, null=True)  # Field name made lowercase.
    fgfr1 = models.FloatField(db_column='FGFR1', blank=True, null=True)  # Field name made lowercase.
    crh = models.FloatField(db_column='CRH', blank=True, null=True)  # Field name made lowercase.
    sgk3 = models.FloatField(db_column='SGK3', blank=True, null=True)  # Field name made lowercase.
    fabp5 = models.FloatField(db_column='FABP5', blank=True, null=True)  # Field name made lowercase.
    fabp4 = models.FloatField(db_column='FABP4', blank=True, null=True)  # Field name made lowercase.
    mmp16 = models.FloatField(db_column='MMP16', blank=True, null=True)  # Field name made lowercase.
    ncald = models.FloatField(db_column='NCALD', blank=True, null=True)  # Field name made lowercase.
    klf10 = models.FloatField(db_column='KLF10', blank=True, null=True)  # Field name made lowercase.
    enpp2 = models.FloatField(db_column='ENPP2', blank=True, null=True)  # Field name made lowercase.
    pvt1 = models.FloatField(db_column='PVT1', blank=True, null=True)  # Field name made lowercase.
    jak2 = models.FloatField(db_column='JAK2', blank=True, null=True)  # Field name made lowercase.
    psip1 = models.FloatField(db_column='PSIP1', blank=True, null=True)  # Field name made lowercase.
    plin2 = models.FloatField(db_column='PLIN2', blank=True, null=True)  # Field name made lowercase.
    rps6 = models.FloatField(db_column='RPS6', blank=True, null=True)  # Field name made lowercase.
    aldh1a1 = models.FloatField(db_column='ALDH1A1', blank=True, null=True)  # Field name made lowercase.
    frmd3 = models.FloatField(db_column='FRMD3', blank=True, null=True)  # Field name made lowercase.
    gas1 = models.FloatField(db_column='GAS1', blank=True, null=True)  # Field name made lowercase.
    baat = models.FloatField(db_column='BAAT', blank=True, null=True)  # Field name made lowercase.
    abca1 = models.FloatField(db_column='ABCA1', blank=True, null=True)  # Field name made lowercase.
    txn = models.FloatField(db_column='TXN', blank=True, null=True)  # Field name made lowercase.
    ambp = models.FloatField(db_column='AMBP', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    hspa5 = models.FloatField(db_column='HSPA5', blank=True, null=True)  # Field name made lowercase.
    angptl2 = models.FloatField(db_column='ANGPTL2', blank=True, null=True)  # Field name made lowercase.
    ptges = models.FloatField(db_column='PTGES', blank=True, null=True)  # Field name made lowercase.
    tsc1 = models.FloatField(db_column='TSC1', blank=True, null=True)  # Field name made lowercase.
    abo = models.FloatField(db_column='ABO', blank=True, null=True)  # Field name made lowercase.
    adamts13 = models.FloatField(db_column='ADAMTS13', blank=True, null=True)  # Field name made lowercase.
    ptgds = models.FloatField(db_column='PTGDS', blank=True, null=True)  # Field name made lowercase.
    klf6 = models.FloatField(db_column='KLF6', blank=True, null=True)  # Field name made lowercase.
    cdc123 = models.FloatField(db_column='CDC123', blank=True, null=True)  # Field name made lowercase.
    bambi = models.FloatField(db_column='BAMBI', blank=True, null=True)  # Field name made lowercase.
    cxcl12 = models.FloatField(db_column='CXCL12', blank=True, null=True)  # Field name made lowercase.
    mbl2 = models.FloatField(db_column='MBL2', blank=True, null=True)  # Field name made lowercase.
    tfam = models.FloatField(db_column='TFAM', blank=True, null=True)  # Field name made lowercase.
    sirt1 = models.FloatField(db_column='SIRT1', blank=True, null=True)  # Field name made lowercase.
    srgn = models.FloatField(db_column='SRGN', blank=True, null=True)  # Field name made lowercase.
    unc5b = models.FloatField(db_column='UNC5B', blank=True, null=True)  # Field name made lowercase.
    adk = models.FloatField(db_column='ADK', blank=True, null=True)  # Field name made lowercase.
    pten = models.FloatField(db_column='PTEN', blank=True, null=True)  # Field name made lowercase.
    rbp4 = models.FloatField(db_column='RBP4', blank=True, null=True)  # Field name made lowercase.
    cyp2c19 = models.FloatField(db_column='CYP2C19', blank=True, null=True)  # Field name made lowercase.
    entpd1 = models.FloatField(db_column='ENTPD1', blank=True, null=True)  # Field name made lowercase.
    tcf7l2 = models.FloatField(db_column='TCF7L2', blank=True, null=True)  # Field name made lowercase.
    bnip3 = models.FloatField(db_column='BNIP3', blank=True, null=True)  # Field name made lowercase.
    igf2 = models.FloatField(db_column='IGF2', blank=True, null=True)  # Field name made lowercase.
    ins = models.FloatField(db_column='INS', blank=True, null=True)  # Field name made lowercase.
    th = models.FloatField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    kcnq1 = models.FloatField(db_column='KCNQ1', blank=True, null=True)  # Field name made lowercase.
    hbg2 = models.FloatField(db_column='HBG2', blank=True, null=True)  # Field name made lowercase.
    smpd1 = models.FloatField(db_column='SMPD1', blank=True, null=True)  # Field name made lowercase.
    ilk = models.FloatField(db_column='ILK', blank=True, null=True)  # Field name made lowercase.
    adm = models.FloatField(db_column='ADM', blank=True, null=True)  # Field name made lowercase.
    pth = models.FloatField(db_column='PTH', blank=True, null=True)  # Field name made lowercase.
    nucb2 = models.FloatField(db_column='NUCB2', blank=True, null=True)  # Field name made lowercase.
    kcnj11 = models.FloatField(db_column='KCNJ11', blank=True, null=True)  # Field name made lowercase.
    saa1 = models.FloatField(db_column='SAA1', blank=True, null=True)  # Field name made lowercase.
    bdnf = models.FloatField(db_column='BDNF', blank=True, null=True)  # Field name made lowercase.
    wt1 = models.FloatField(db_column='WT1', blank=True, null=True)  # Field name made lowercase.
    cd59 = models.FloatField(db_column='CD59', blank=True, null=True)  # Field name made lowercase.
    pdhx = models.FloatField(db_column='PDHX', blank=True, null=True)  # Field name made lowercase.
    traf6 = models.FloatField(db_column='TRAF6', blank=True, null=True)  # Field name made lowercase.
    api5 = models.FloatField(db_column='API5', blank=True, null=True)  # Field name made lowercase.
    nr1h3 = models.FloatField(db_column='NR1H3', blank=True, null=True)  # Field name made lowercase.
    ndufs3 = models.FloatField(db_column='NDUFS3', blank=True, null=True)  # Field name made lowercase.
    folh1 = models.FloatField(db_column='FOLH1', blank=True, null=True)  # Field name made lowercase.
    aplnr = models.FloatField(db_column='APLNR', blank=True, null=True)  # Field name made lowercase.
    p2rx3 = models.FloatField(db_column='P2RX3', blank=True, null=True)  # Field name made lowercase.
    cntf = models.FloatField(db_column='CNTF', blank=True, null=True)  # Field name made lowercase.
    fads1 = models.FloatField(db_column='FADS1', blank=True, null=True)  # Field name made lowercase.
    fads2 = models.FloatField(db_column='FADS2', blank=True, null=True)  # Field name made lowercase.
    fkbp2 = models.FloatField(db_column='FKBP2', blank=True, null=True)  # Field name made lowercase.
    syvn1 = models.FloatField(db_column='SYVN1', blank=True, null=True)  # Field name made lowercase.
    pc = models.FloatField(db_column='PC', blank=True, null=True)  # Field name made lowercase.
    dhcr7 = models.FloatField(db_column='DHCR7', blank=True, null=True)  # Field name made lowercase.
    prcp = models.FloatField(db_column='PRCP', blank=True, null=True)  # Field name made lowercase.
    nox4 = models.FloatField(db_column='NOX4', blank=True, null=True)  # Field name made lowercase.
    pdgfd = models.FloatField(db_column='PDGFD', blank=True, null=True)  # Field name made lowercase.
    atm = models.FloatField(db_column='ATM', blank=True, null=True)  # Field name made lowercase.
    il18 = models.FloatField(db_column='IL18', blank=True, null=True)  # Field name made lowercase.
    apoa1 = models.FloatField(db_column='APOA1', blank=True, null=True)  # Field name made lowercase.
    hyou1 = models.FloatField(db_column='HYOU1', blank=True, null=True)  # Field name made lowercase.
    esam = models.FloatField(db_column='ESAM', blank=True, null=True)  # Field name made lowercase.
    fkbp4 = models.FloatField(db_column='FKBP4', blank=True, null=True)  # Field name made lowercase.
    fgf23 = models.FloatField(db_column='FGF23', blank=True, null=True)  # Field name made lowercase.
    ntf3 = models.FloatField(db_column='NTF3', blank=True, null=True)  # Field name made lowercase.
    vwf = models.FloatField(db_column='VWF', blank=True, null=True)  # Field name made lowercase.
    cd9 = models.FloatField(db_column='CD9', blank=True, null=True)  # Field name made lowercase.
    gapdh = models.FloatField(db_column='GAPDH', blank=True, null=True)  # Field name made lowercase.
    cd4 = models.FloatField(db_column='CD4', blank=True, null=True)  # Field name made lowercase.
    gnb3 = models.FloatField(db_column='GNB3', blank=True, null=True)  # Field name made lowercase.
    cd163 = models.FloatField(db_column='CD163', blank=True, null=True)  # Field name made lowercase.
    slc2a3 = models.FloatField(db_column='SLC2A3', blank=True, null=True)  # Field name made lowercase.
    cd69 = models.FloatField(db_column='CD69', blank=True, null=True)  # Field name made lowercase.
    irak4 = models.FloatField(db_column='IRAK4', blank=True, null=True)  # Field name made lowercase.
    vdr = models.FloatField(db_column='VDR', blank=True, null=True)  # Field name made lowercase.
    aqp5 = models.FloatField(db_column='AQP5', blank=True, null=True)  # Field name made lowercase.
    acvrl1 = models.FloatField(db_column='ACVRL1', blank=True, null=True)  # Field name made lowercase.
    nfe2 = models.FloatField(db_column='NFE2', blank=True, null=True)  # Field name made lowercase.
    cd63 = models.FloatField(db_column='CD63', blank=True, null=True)  # Field name made lowercase.
    erbb3 = models.FloatField(db_column='ERBB3', blank=True, null=True)  # Field name made lowercase.
    ddit3 = models.FloatField(db_column='DDIT3', blank=True, null=True)  # Field name made lowercase.
    ifng = models.FloatField(db_column='IFNG', blank=True, null=True)  # Field name made lowercase.
    nts = models.FloatField(db_column='NTS', blank=True, null=True)  # Field name made lowercase.
    igf1 = models.FloatField(db_column='IGF1', blank=True, null=True)  # Field name made lowercase.
    acacb = models.FloatField(db_column='ACACB', blank=True, null=True)  # Field name made lowercase.
    trpv4 = models.FloatField(db_column='TRPV4', blank=True, null=True)  # Field name made lowercase.
    atp2a2 = models.FloatField(db_column='ATP2A2', blank=True, null=True)  # Field name made lowercase.
    aldh2 = models.FloatField(db_column='ALDH2', blank=True, null=True)  # Field name made lowercase.
    nos1 = models.FloatField(db_column='NOS1', blank=True, null=True)  # Field name made lowercase.
    pebp1 = models.FloatField(db_column='PEBP1', blank=True, null=True)  # Field name made lowercase.
    psmd9 = models.FloatField(db_column='PSMD9', blank=True, null=True)  # Field name made lowercase.
    scarb1 = models.FloatField(db_column='SCARB1', blank=True, null=True)  # Field name made lowercase.
    p2rx2 = models.FloatField(db_column='P2RX2', blank=True, null=True)  # Field name made lowercase.
    alox5ap = models.FloatField(db_column='ALOX5AP', blank=True, null=True)  # Field name made lowercase.
    kl = models.FloatField(db_column='KL', blank=True, null=True)  # Field name made lowercase.
    postn = models.FloatField(db_column='POSTN', blank=True, null=True)  # Field name made lowercase.
    foxo1 = models.FloatField(db_column='FOXO1', blank=True, null=True)  # Field name made lowercase.
    htr2a = models.FloatField(db_column='HTR2A', blank=True, null=True)  # Field name made lowercase.
    gpc5 = models.FloatField(db_column='GPC5', blank=True, null=True)  # Field name made lowercase.
    irs2 = models.FloatField(db_column='IRS2', blank=True, null=True)  # Field name made lowercase.
    gas6 = models.FloatField(db_column='GAS6', blank=True, null=True)  # Field name made lowercase.
    ang = models.FloatField(db_column='ANG', blank=True, null=True)  # Field name made lowercase.
    mmp14 = models.FloatField(db_column='MMP14', blank=True, null=True)  # Field name made lowercase.
    ltb4r2 = models.FloatField(db_column='LTB4R2', blank=True, null=True)  # Field name made lowercase.
    nfkbia = models.FloatField(db_column='NFKBIA', blank=True, null=True)  # Field name made lowercase.
    bmp4 = models.FloatField(db_column='BMP4', blank=True, null=True)  # Field name made lowercase.
    rtn1 = models.FloatField(db_column='RTN1', blank=True, null=True)  # Field name made lowercase.
    pgf = models.FloatField(db_column='PGF', blank=True, null=True)  # Field name made lowercase.
    ngb = models.FloatField(db_column='NGB', blank=True, null=True)  # Field name made lowercase.
    ahsa1 = models.FloatField(db_column='AHSA1', blank=True, null=True)  # Field name made lowercase.
    bdkrb2 = models.FloatField(db_column='BDKRB2', blank=True, null=True)  # Field name made lowercase.
    bdkrb1 = models.FloatField(db_column='BDKRB1', blank=True, null=True)  # Field name made lowercase.
    akt1 = models.FloatField(db_column='AKT1', blank=True, null=True)  # Field name made lowercase.
    grem1 = models.FloatField(db_column='GREM1', blank=True, null=True)  # Field name made lowercase.
    thbs1 = models.FloatField(db_column='THBS1', blank=True, null=True)  # Field name made lowercase.
    pak6 = models.FloatField(db_column='PAK6', blank=True, null=True)  # Field name made lowercase.
    b2m = models.FloatField(db_column='B2M', blank=True, null=True)  # Field name made lowercase.
    myo5c = models.FloatField(db_column='MYO5C', blank=True, null=True)  # Field name made lowercase.
    onecut1 = models.FloatField(db_column='ONECUT1', blank=True, null=True)  # Field name made lowercase.
    adam10 = models.FloatField(db_column='ADAM10', blank=True, null=True)  # Field name made lowercase.
    ctsh = models.FloatField(db_column='CTSH', blank=True, null=True)  # Field name made lowercase.
    plin1 = models.FloatField(db_column='PLIN1', blank=True, null=True)  # Field name made lowercase.
    igf1r = models.FloatField(db_column='IGF1R', blank=True, null=True)  # Field name made lowercase.
    mrpl28 = models.FloatField(db_column='MRPL28', blank=True, null=True)  # Field name made lowercase.
    cacna1h = models.FloatField(db_column='CACNA1H', blank=True, null=True)  # Field name made lowercase.
    pdpk1 = models.FloatField(db_column='PDPK1', blank=True, null=True)  # Field name made lowercase.
    ercc4 = models.FloatField(db_column='ERCC4', blank=True, null=True)  # Field name made lowercase.
    smg1 = models.FloatField(db_column='SMG1', blank=True, null=True)  # Field name made lowercase.
    itgam = models.FloatField(db_column='ITGAM', blank=True, null=True)  # Field name made lowercase.
    fto = models.FloatField(db_column='FTO', blank=True, null=True)  # Field name made lowercase.
    mmp2 = models.FloatField(db_column='MMP2', blank=True, null=True)  # Field name made lowercase.
    slc12a3 = models.FloatField(db_column='SLC12A3', blank=True, null=True)  # Field name made lowercase.
    cetp = models.FloatField(db_column='CETP', blank=True, null=True)  # Field name made lowercase.
    cx3cl1 = models.FloatField(db_column='CX3CL1', blank=True, null=True)  # Field name made lowercase.
    cdh1 = models.FloatField(db_column='CDH1', blank=True, null=True)  # Field name made lowercase.
    nqo1 = models.FloatField(db_column='NQO1', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    znrf1 = models.FloatField(db_column='ZNRF1', blank=True, null=True)  # Field name made lowercase.
    cyba = models.FloatField(db_column='CYBA', blank=True, null=True)  # Field name made lowercase.
    tubb3 = models.FloatField(db_column='TUBB3', blank=True, null=True)  # Field name made lowercase.
    crk = models.FloatField(db_column='CRK', blank=True, null=True)  # Field name made lowercase.
    serpinf2 = models.FloatField(db_column='SERPINF2', blank=True, null=True)  # Field name made lowercase.
    serpinf1 = models.FloatField(db_column='SERPINF1', blank=True, null=True)  # Field name made lowercase.
    trpv3 = models.FloatField(db_column='TRPV3', blank=True, null=True)  # Field name made lowercase.
    cxcl16 = models.FloatField(db_column='CXCL16', blank=True, null=True)  # Field name made lowercase.
    slc2a4 = models.FloatField(db_column='SLC2A4', blank=True, null=True)  # Field name made lowercase.
    cd68 = models.FloatField(db_column='CD68', blank=True, null=True)  # Field name made lowercase.
    shbg = models.FloatField(db_column='SHBG', blank=True, null=True)  # Field name made lowercase.
    pmp22 = models.FloatField(db_column='PMP22', blank=True, null=True)  # Field name made lowercase.
    srebf1 = models.FloatField(db_column='SREBF1', blank=True, null=True)  # Field name made lowercase.
    mapk7 = models.FloatField(db_column='MAPK7', blank=True, null=True)  # Field name made lowercase.
    ccl2 = models.FloatField(db_column='CCL2', blank=True, null=True)  # Field name made lowercase.
    ccl5 = models.FloatField(db_column='CCL5', blank=True, null=True)  # Field name made lowercase.
    hnf1b = models.FloatField(db_column='HNF1B', blank=True, null=True)  # Field name made lowercase.
    erbb2 = models.FloatField(db_column='ERBB2', blank=True, null=True)  # Field name made lowercase.
    fkbp10 = models.FloatField(db_column='FKBP10', blank=True, null=True)  # Field name made lowercase.
    stat5a = models.FloatField(db_column='STAT5A', blank=True, null=True)  # Field name made lowercase.
    stat3 = models.FloatField(db_column='STAT3', blank=True, null=True)  # Field name made lowercase.
    naglu = models.FloatField(db_column='NAGLU', blank=True, null=True)  # Field name made lowercase.
    aoc2 = models.FloatField(db_column='AOC2', blank=True, null=True)  # Field name made lowercase.
    aoc3 = models.FloatField(db_column='AOC3', blank=True, null=True)  # Field name made lowercase.
    ppy = models.FloatField(db_column='PPY', blank=True, null=True)  # Field name made lowercase.
    sth = models.FloatField(db_column='STH', blank=True, null=True)  # Field name made lowercase.
    itgb3 = models.FloatField(db_column='ITGB3', blank=True, null=True)  # Field name made lowercase.
    gip = models.FloatField(db_column='GIP', blank=True, null=True)  # Field name made lowercase.
    mpo = models.FloatField(db_column='MPO', blank=True, null=True)  # Field name made lowercase.
    pecam1 = models.FloatField(db_column='PECAM1', blank=True, null=True)  # Field name made lowercase.
    sox9 = models.FloatField(db_column='SOX9', blank=True, null=True)  # Field name made lowercase.
    timp2 = models.FloatField(db_column='TIMP2', blank=True, null=True)  # Field name made lowercase.
    dcxr = models.FloatField(db_column='DCXR', blank=True, null=True)  # Field name made lowercase.
    fasn = models.FloatField(db_column='FASN', blank=True, null=True)  # Field name made lowercase.
    colec12 = models.FloatField(db_column='COLEC12', blank=True, null=True)  # Field name made lowercase.
    adcyap1 = models.FloatField(db_column='ADCYAP1', blank=True, null=True)  # Field name made lowercase.
    smad7 = models.FloatField(db_column='SMAD7', blank=True, null=True)  # Field name made lowercase.
    nedd4l = models.FloatField(db_column='NEDD4L', blank=True, null=True)  # Field name made lowercase.
    mc4r = models.FloatField(db_column='MC4R', blank=True, null=True)  # Field name made lowercase.
    bcl2 = models.FloatField(db_column='BCL2', blank=True, null=True)  # Field name made lowercase.
    cndp2 = models.FloatField(db_column='CNDP2', blank=True, null=True)  # Field name made lowercase.
    znf236 = models.FloatField(db_column='ZNF236', blank=True, null=True)  # Field name made lowercase.
    stk11 = models.FloatField(db_column='STK11', blank=True, null=True)  # Field name made lowercase.
    sirt6 = models.FloatField(db_column='SIRT6', blank=True, null=True)  # Field name made lowercase.
    uhrf1 = models.FloatField(db_column='UHRF1', blank=True, null=True)  # Field name made lowercase.
    timm44 = models.FloatField(db_column='TIMM44', blank=True, null=True)  # Field name made lowercase.
    angptl4 = models.FloatField(db_column='ANGPTL4', blank=True, null=True)  # Field name made lowercase.
    dnmt1 = models.FloatField(db_column='DNMT1', blank=True, null=True)  # Field name made lowercase.
    icam1 = models.FloatField(db_column='ICAM1', blank=True, null=True)  # Field name made lowercase.
    ldlr = models.FloatField(db_column='LDLR', blank=True, null=True)  # Field name made lowercase.
    epor = models.FloatField(db_column='EPOR', blank=True, null=True)  # Field name made lowercase.
    prdx2 = models.FloatField(db_column='PRDX2', blank=True, null=True)  # Field name made lowercase.
    ptger1 = models.FloatField(db_column='PTGER1', blank=True, null=True)  # Field name made lowercase.
    unc13a = models.FloatField(db_column='UNC13A', blank=True, null=True)  # Field name made lowercase.
    gdf15 = models.FloatField(db_column='GDF15', blank=True, null=True)  # Field name made lowercase.
    fkbp8 = models.FloatField(db_column='FKBP8', blank=True, null=True)  # Field name made lowercase.
    usf2 = models.FloatField(db_column='USF2', blank=True, null=True)  # Field name made lowercase.
    ffar1 = models.FloatField(db_column='FFAR1', blank=True, null=True)  # Field name made lowercase.
    ffar2 = models.FloatField(db_column='FFAR2', blank=True, null=True)  # Field name made lowercase.
    nphs1 = models.FloatField(db_column='NPHS1', blank=True, null=True)  # Field name made lowercase.
    tgfb1 = models.FloatField(db_column='TGFB1', blank=True, null=True)  # Field name made lowercase.
    xrcc1 = models.FloatField(db_column='XRCC1', blank=True, null=True)  # Field name made lowercase.
    ercc1 = models.FloatField(db_column='ERCC1', blank=True, null=True)  # Field name made lowercase.
    gipr = models.FloatField(db_column='GIPR', blank=True, null=True)  # Field name made lowercase.
    fgf21 = models.FloatField(db_column='FGF21', blank=True, null=True)  # Field name made lowercase.
    clec11a = models.FloatField(db_column='CLEC11A', blank=True, null=True)  # Field name made lowercase.
    fpr1 = models.FloatField(db_column='FPR1', blank=True, null=True)  # Field name made lowercase.
    trib3 = models.FloatField(db_column='TRIB3', blank=True, null=True)  # Field name made lowercase.
    bmp2 = models.FloatField(db_column='BMP2', blank=True, null=True)  # Field name made lowercase.
    thbd = models.FloatField(db_column='THBD', blank=True, null=True)  # Field name made lowercase.
    cst3 = models.FloatField(db_column='CST3', blank=True, null=True)  # Field name made lowercase.
    id1 = models.FloatField(db_column='ID1', blank=True, null=True)  # Field name made lowercase.
    src = models.FloatField(db_column='SRC', blank=True, null=True)  # Field name made lowercase.
    mafb = models.FloatField(db_column='MAFB', blank=True, null=True)  # Field name made lowercase.
    sgk2 = models.FloatField(db_column='SGK2', blank=True, null=True)  # Field name made lowercase.
    hnf4a = models.FloatField(db_column='HNF4A', blank=True, null=True)  # Field name made lowercase.
    pltp = models.FloatField(db_column='PLTP', blank=True, null=True)  # Field name made lowercase.
    mmp9 = models.FloatField(db_column='MMP9', blank=True, null=True)  # Field name made lowercase.
    cd40 = models.FloatField(db_column='CD40', blank=True, null=True)  # Field name made lowercase.
    ptpn1 = models.FloatField(db_column='PTPN1', blank=True, null=True)  # Field name made lowercase.
    cyp24a1 = models.FloatField(db_column='CYP24A1', blank=True, null=True)  # Field name made lowercase.
    rcan1 = models.FloatField(db_column='RCAN1', blank=True, null=True)  # Field name made lowercase.
    abcg1 = models.FloatField(db_column='ABCG1', blank=True, null=True)  # Field name made lowercase.
    prmt2 = models.FloatField(db_column='PRMT2', blank=True, null=True)  # Field name made lowercase.
    comt = models.FloatField(db_column='COMT', blank=True, null=True)  # Field name made lowercase.
    mapk1 = models.FloatField(db_column='MAPK1', blank=True, null=True)  # Field name made lowercase.
    mif = models.FloatField(db_column='MIF', blank=True, null=True)  # Field name made lowercase.
    ggt1 = models.FloatField(db_column='GGT1', blank=True, null=True)  # Field name made lowercase.
    xbp1 = models.FloatField(db_column='XBP1', blank=True, null=True)  # Field name made lowercase.
    osm = models.FloatField(db_column='OSM', blank=True, null=True)  # Field name made lowercase.
    limk2 = models.FloatField(db_column='LIMK2', blank=True, null=True)  # Field name made lowercase.
    sfi1 = models.FloatField(db_column='SFI1', blank=True, null=True)  # Field name made lowercase.
    timp3 = models.FloatField(db_column='TIMP3', blank=True, null=True)  # Field name made lowercase.
    hmox1 = models.FloatField(db_column='HMOX1', blank=True, null=True)  # Field name made lowercase.
    apol1 = models.FloatField(db_column='APOL1', blank=True, null=True)  # Field name made lowercase.
    myh9 = models.FloatField(db_column='MYH9', blank=True, null=True)  # Field name made lowercase.
    pdgfb = models.FloatField(db_column='PDGFB', blank=True, null=True)  # Field name made lowercase.
    atf4 = models.FloatField(db_column='ATF4', blank=True, null=True)  # Field name made lowercase.
    tspo = models.FloatField(db_column='TSPO', blank=True, null=True)  # Field name made lowercase.
    miox = models.FloatField(db_column='MIOX', blank=True, null=True)  # Field name made lowercase.
    prdx4 = models.FloatField(db_column='PRDX4', blank=True, null=True)  # Field name made lowercase.
    gk = models.FloatField(db_column='GK', blank=True, null=True)  # Field name made lowercase.
    rgn = models.FloatField(db_column='RGN', blank=True, null=True)  # Field name made lowercase.
    timp1 = models.FloatField(db_column='TIMP1', blank=True, null=True)  # Field name made lowercase.
    clcn5 = models.FloatField(db_column='CLCN5', blank=True, null=True)  # Field name made lowercase.
    ar = models.FloatField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    foxo4 = models.FloatField(db_column='FOXO4', blank=True, null=True)  # Field name made lowercase.
    rps6ka6 = models.FloatField(db_column='RPS6KA6', blank=True, null=True)  # Field name made lowercase.
    nox1 = models.FloatField(db_column='NOX1', blank=True, null=True)  # Field name made lowercase.
    xiap = models.FloatField(db_column='XIAP', blank=True, null=True)  # Field name made lowercase.
    cd40lg = models.FloatField(db_column='CD40LG', blank=True, null=True)  # Field name made lowercase.
    l1cam = models.FloatField(db_column='L1CAM', blank=True, null=True)  # Field name made lowercase.
    irak1 = models.FloatField(db_column='IRAK1', blank=True, null=True)  # Field name made lowercase.
    g6pd = models.FloatField(db_column='G6PD', blank=True, null=True)  # Field name made lowercase.
    f8 = models.FloatField(db_column='F8', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diaco_tissue_brain_caudate_bg'


class DiacoTissueBrainCerebellarHs(models.Model):
    subjid = models.CharField(db_column='SUBJID', max_length=50, primary_key=True)  # Field name made lowercase.
    sampid = models.CharField(db_column='SAMPID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sesso = models.CharField(db_column='Sesso', max_length=1)  # Field name made lowercase.
    eta = models.CharField(db_column='Età', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errfi1 = models.FloatField(db_column='ERRFI1', blank=True, null=True)  # Field name made lowercase.
    mad2l2 = models.FloatField(db_column='MAD2L2', blank=True, null=True)  # Field name made lowercase.
    mthfr = models.FloatField(db_column='MTHFR', blank=True, null=True)  # Field name made lowercase.
    nppa = models.FloatField(db_column='NPPA', blank=True, null=True)  # Field name made lowercase.
    tnfrsf1b = models.FloatField(db_column='TNFRSF1B', blank=True, null=True)  # Field name made lowercase.
    pla2g2a = models.FloatField(db_column='PLA2G2A', blank=True, null=True)  # Field name made lowercase.
    alpl = models.FloatField(db_column='ALPL', blank=True, null=True)  # Field name made lowercase.
    hspg2 = models.FloatField(db_column='HSPG2', blank=True, null=True)  # Field name made lowercase.
    cnr2 = models.FloatField(db_column='CNR2', blank=True, null=True)  # Field name made lowercase.
    slc9a1 = models.FloatField(db_column='SLC9A1', blank=True, null=True)  # Field name made lowercase.
    col8a2 = models.FloatField(db_column='COL8A2', blank=True, null=True)  # Field name made lowercase.
    cap1 = models.FloatField(db_column='CAP1', blank=True, null=True)  # Field name made lowercase.
    slc2a1 = models.FloatField(db_column='SLC2A1', blank=True, null=True)  # Field name made lowercase.
    cyp2j2 = models.FloatField(db_column='CYP2J2', blank=True, null=True)  # Field name made lowercase.
    ddah1 = models.FloatField(db_column='DDAH1', blank=True, null=True)  # Field name made lowercase.
    cyr61 = models.FloatField(db_column='CYR61', blank=True, null=True)  # Field name made lowercase.
    ngf = models.FloatField(db_column='NGF', blank=True, null=True)  # Field name made lowercase.
    hmgcs2 = models.FloatField(db_column='HMGCS2', blank=True, null=True)  # Field name made lowercase.
    ctss = models.FloatField(db_column='CTSS', blank=True, null=True)  # Field name made lowercase.
    s100a12 = models.FloatField(db_column='S100A12', blank=True, null=True)  # Field name made lowercase.
    lmna = models.FloatField(db_column='LMNA', blank=True, null=True)  # Field name made lowercase.
    cd247 = models.FloatField(db_column='CD247', blank=True, null=True)  # Field name made lowercase.
    sele = models.FloatField(db_column='SELE', blank=True, null=True)  # Field name made lowercase.
    fmo3 = models.FloatField(db_column='FMO3', blank=True, null=True)  # Field name made lowercase.
    prdx6 = models.FloatField(db_column='PRDX6', blank=True, null=True)  # Field name made lowercase.
    glul = models.FloatField(db_column='GLUL', blank=True, null=True)  # Field name made lowercase.
    lamc1 = models.FloatField(db_column='LAMC1', blank=True, null=True)  # Field name made lowercase.
    ptgs2 = models.FloatField(db_column='PTGS2', blank=True, null=True)  # Field name made lowercase.
    chi3l1 = models.FloatField(db_column='CHI3L1', blank=True, null=True)  # Field name made lowercase.
    chit1 = models.FloatField(db_column='CHIT1', blank=True, null=True)  # Field name made lowercase.
    fmod = models.FloatField(db_column='FMOD', blank=True, null=True)  # Field name made lowercase.
    il10 = models.FloatField(db_column='IL10', blank=True, null=True)  # Field name made lowercase.
    pfkfb2 = models.FloatField(db_column='PFKFB2', blank=True, null=True)  # Field name made lowercase.
    cd34 = models.FloatField(db_column='CD34', blank=True, null=True)  # Field name made lowercase.
    cog2 = models.FloatField(db_column='COG2', blank=True, null=True)  # Field name made lowercase.
    nlrp3 = models.FloatField(db_column='NLRP3', blank=True, null=True)  # Field name made lowercase.
    rock2 = models.FloatField(db_column='ROCK2', blank=True, null=True)  # Field name made lowercase.
    apob = models.FloatField(db_column='APOB', blank=True, null=True)  # Field name made lowercase.
    pomc = models.FloatField(db_column='POMC', blank=True, null=True)  # Field name made lowercase.
    gckr = models.FloatField(db_column='GCKR', blank=True, null=True)  # Field name made lowercase.
    plekhh2 = models.FloatField(db_column='PLEKHH2', blank=True, null=True)  # Field name made lowercase.
    prkce = models.FloatField(db_column='PRKCE', blank=True, null=True)  # Field name made lowercase.
    pigf = models.FloatField(db_column='PIGF', blank=True, null=True)  # Field name made lowercase.
    msh2 = models.FloatField(db_column='MSH2', blank=True, null=True)  # Field name made lowercase.
    gfpt1 = models.FloatField(db_column='GFPT1', blank=True, null=True)  # Field name made lowercase.
    tacr1 = models.FloatField(db_column='TACR1', blank=True, null=True)  # Field name made lowercase.
    reg1a = models.FloatField(db_column='REG1A', blank=True, null=True)  # Field name made lowercase.
    eif2ak3 = models.FloatField(db_column='EIF2AK3', blank=True, null=True)  # Field name made lowercase.
    adra2b = models.FloatField(db_column='ADRA2B', blank=True, null=True)  # Field name made lowercase.
    il1b = models.FloatField(db_column='IL1B', blank=True, null=True)  # Field name made lowercase.
    proc = models.FloatField(db_column='PROC', blank=True, null=True)  # Field name made lowercase.
    polr2d = models.FloatField(db_column='POLR2D', blank=True, null=True)  # Field name made lowercase.
    zeb2 = models.FloatField(db_column='ZEB2', blank=True, null=True)  # Field name made lowercase.
    acvr1c = models.FloatField(db_column='ACVR1C', blank=True, null=True)  # Field name made lowercase.
    dpp4 = models.FloatField(db_column='DPP4', blank=True, null=True)  # Field name made lowercase.
    nfe2l2 = models.FloatField(db_column='NFE2L2', blank=True, null=True)  # Field name made lowercase.
    igfbp5 = models.FloatField(db_column='IGFBP5', blank=True, null=True)  # Field name made lowercase.
    ccl20 = models.FloatField(db_column='CCL20', blank=True, null=True)  # Field name made lowercase.
    hdac4 = models.FloatField(db_column='HDAC4', blank=True, null=True)  # Field name made lowercase.
    capn10 = models.FloatField(db_column='CAPN10', blank=True, null=True)  # Field name made lowercase.
    ghrl = models.FloatField(db_column='GHRL', blank=True, null=True)  # Field name made lowercase.
    pparg = models.FloatField(db_column='PPARG', blank=True, null=True)  # Field name made lowercase.
    raf1 = models.FloatField(db_column='RAF1', blank=True, null=True)  # Field name made lowercase.
    myd88 = models.FloatField(db_column='MYD88', blank=True, null=True)  # Field name made lowercase.
    cx3cr1 = models.FloatField(db_column='CX3CR1', blank=True, null=True)  # Field name made lowercase.
    cck = models.FloatField(db_column='CCK', blank=True, null=True)  # Field name made lowercase.
    exosc7 = models.FloatField(db_column='EXOSC7', blank=True, null=True)  # Field name made lowercase.
    ccr1 = models.FloatField(db_column='CCR1', blank=True, null=True)  # Field name made lowercase.
    ccr5 = models.FloatField(db_column='CCR5', blank=True, null=True)  # Field name made lowercase.
    gpx1 = models.FloatField(db_column='GPX1', blank=True, null=True)  # Field name made lowercase.
    rhoa = models.FloatField(db_column='RHOA', blank=True, null=True)  # Field name made lowercase.
    cish = models.FloatField(db_column='CISH', blank=True, null=True)  # Field name made lowercase.
    tkt = models.FloatField(db_column='TKT', blank=True, null=True)  # Field name made lowercase.
    appl1 = models.FloatField(db_column='APPL1', blank=True, null=True)  # Field name made lowercase.
    slmap = models.FloatField(db_column='SLMAP', blank=True, null=True)  # Field name made lowercase.
    col8a1 = models.FloatField(db_column='COL8A1', blank=True, null=True)  # Field name made lowercase.
    cd47 = models.FloatField(db_column='CD47', blank=True, null=True)  # Field name made lowercase.
    gap43 = models.FloatField(db_column='GAP43', blank=True, null=True)  # Field name made lowercase.
    cd80 = models.FloatField(db_column='CD80', blank=True, null=True)  # Field name made lowercase.
    rho = models.FloatField(db_column='RHO', blank=True, null=True)  # Field name made lowercase.
    trh = models.FloatField(db_column='TRH', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='TF', blank=True, null=True)  # Field name made lowercase.
    rbp1 = models.FloatField(db_column='RBP1', blank=True, null=True)  # Field name made lowercase.
    trpc1 = models.FloatField(db_column='TRPC1', blank=True, null=True)  # Field name made lowercase.
    agtr1 = models.FloatField(db_column='AGTR1', blank=True, null=True)  # Field name made lowercase.
    sucnr1 = models.FloatField(db_column='SUCNR1', blank=True, null=True)  # Field name made lowercase.
    p2ry1 = models.FloatField(db_column='P2RY1', blank=True, null=True)  # Field name made lowercase.
    mme = models.FloatField(db_column='MME', blank=True, null=True)  # Field name made lowercase.
    slc2a2 = models.FloatField(db_column='SLC2A2', blank=True, null=True)  # Field name made lowercase.
    pik3ca = models.FloatField(db_column='PIK3CA', blank=True, null=True)  # Field name made lowercase.
    parl = models.FloatField(db_column='PARL', blank=True, null=True)  # Field name made lowercase.
    ahsg = models.FloatField(db_column='AHSG', blank=True, null=True)  # Field name made lowercase.
    adipoq = models.FloatField(db_column='ADIPOQ', blank=True, null=True)  # Field name made lowercase.
    spon2 = models.FloatField(db_column='SPON2', blank=True, null=True)  # Field name made lowercase.
    wfs1 = models.FloatField(db_column='WFS1', blank=True, null=True)  # Field name made lowercase.
    cd38 = models.FloatField(db_column='CD38', blank=True, null=True)  # Field name made lowercase.
    prom1 = models.FloatField(db_column='PROM1', blank=True, null=True)  # Field name made lowercase.
    ppargc1a = models.FloatField(db_column='PPARGC1A', blank=True, null=True)  # Field name made lowercase.
    igfbp7 = models.FloatField(db_column='IGFBP7', blank=True, null=True)  # Field name made lowercase.
    cxcl5 = models.FloatField(db_column='CXCL5', blank=True, null=True)  # Field name made lowercase.
    cxcl9 = models.FloatField(db_column='CXCL9', blank=True, null=True)  # Field name made lowercase.
    cxcl10 = models.FloatField(db_column='CXCL10', blank=True, null=True)  # Field name made lowercase.
    cxcl11 = models.FloatField(db_column='CXCL11', blank=True, null=True)  # Field name made lowercase.
    hpse = models.FloatField(db_column='HPSE', blank=True, null=True)  # Field name made lowercase.
    spp1 = models.FloatField(db_column='SPP1', blank=True, null=True)  # Field name made lowercase.
    adh1b = models.FloatField(db_column='ADH1B', blank=True, null=True)  # Field name made lowercase.
    egf = models.FloatField(db_column='EGF', blank=True, null=True)  # Field name made lowercase.
    alpk1 = models.FloatField(db_column='ALPK1', blank=True, null=True)  # Field name made lowercase.
    fabp2 = models.FloatField(db_column='FABP2', blank=True, null=True)  # Field name made lowercase.
    pde5a = models.FloatField(db_column='PDE5A', blank=True, null=True)  # Field name made lowercase.
    setd7 = models.FloatField(db_column='SETD7', blank=True, null=True)  # Field name made lowercase.
    smad1 = models.FloatField(db_column='SMAD1', blank=True, null=True)  # Field name made lowercase.
    ednra = models.FloatField(db_column='EDNRA', blank=True, null=True)  # Field name made lowercase.
    nr3c2 = models.FloatField(db_column='NR3C2', blank=True, null=True)  # Field name made lowercase.
    tlr2 = models.FloatField(db_column='TLR2', blank=True, null=True)  # Field name made lowercase.
    npy5r = models.FloatField(db_column='NPY5R', blank=True, null=True)  # Field name made lowercase.
    fbxo8 = models.FloatField(db_column='FBXO8', blank=True, null=True)  # Field name made lowercase.
    vegfc = models.FloatField(db_column='VEGFC', blank=True, null=True)  # Field name made lowercase.
    acsl1 = models.FloatField(db_column='ACSL1', blank=True, null=True)  # Field name made lowercase.
    sorbs2 = models.FloatField(db_column='SORBS2', blank=True, null=True)  # Field name made lowercase.
    f11 = models.FloatField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    basp1 = models.FloatField(db_column='BASP1', blank=True, null=True)  # Field name made lowercase.
    ptger4 = models.FloatField(db_column='PTGER4', blank=True, null=True)  # Field name made lowercase.
    prkaa1 = models.FloatField(db_column='PRKAA1', blank=True, null=True)  # Field name made lowercase.
    ghr = models.FloatField(db_column='GHR', blank=True, null=True)  # Field name made lowercase.
    itga2 = models.FloatField(db_column='ITGA2', blank=True, null=True)  # Field name made lowercase.
    cdk7 = models.FloatField(db_column='CDK7', blank=True, null=True)  # Field name made lowercase.
    f2r = models.FloatField(db_column='F2R', blank=True, null=True)  # Field name made lowercase.
    erap2 = models.FloatField(db_column='ERAP2', blank=True, null=True)  # Field name made lowercase.
    apc = models.FloatField(db_column='APC', blank=True, null=True)  # Field name made lowercase.
    tnfaip8 = models.FloatField(db_column='TNFAIP8', blank=True, null=True)  # Field name made lowercase.
    vdac1 = models.FloatField(db_column='VDAC1', blank=True, null=True)  # Field name made lowercase.
    pdgfrb = models.FloatField(db_column='PDGFRB', blank=True, null=True)  # Field name made lowercase.
    cd74 = models.FloatField(db_column='CD74', blank=True, null=True)  # Field name made lowercase.
    sparc = models.FloatField(db_column='SPARC', blank=True, null=True)  # Field name made lowercase.
    ebf1 = models.FloatField(db_column='EBF1', blank=True, null=True)  # Field name made lowercase.
    gfpt2 = models.FloatField(db_column='GFPT2', blank=True, null=True)  # Field name made lowercase.
    rreb1 = models.FloatField(db_column='RREB1', blank=True, null=True)  # Field name made lowercase.
    edn1 = models.FloatField(db_column='EDN1', blank=True, null=True)  # Field name made lowercase.
    cdkal1 = models.FloatField(db_column='CDKAL1', blank=True, null=True)  # Field name made lowercase.
    hfe = models.FloatField(db_column='HFE', blank=True, null=True)  # Field name made lowercase.
    hla_a = models.FloatField(db_column='HLA-A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  # Field name made lowercase.
    tnf = models.FloatField(db_column='TNF', blank=True, null=True)  # Field name made lowercase.
    hspa1a = models.FloatField(db_column='HSPA1A', blank=True, null=True)  # Field name made lowercase.
    hspa1b = models.FloatField(db_column='HSPA1B', blank=True, null=True)  # Field name made lowercase.
    hla_dqa1 = models.FloatField(db_column='HLA-DQA1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mapk14 = models.FloatField(db_column='MAPK14', blank=True, null=True)  # Field name made lowercase.
    cdkn1a = models.FloatField(db_column='CDKN1A', blank=True, null=True)  # Field name made lowercase.
    glo1 = models.FloatField(db_column='GLO1', blank=True, null=True)  # Field name made lowercase.
    vegfa = models.FloatField(db_column='VEGFA', blank=True, null=True)  # Field name made lowercase.
    cd2ap = models.FloatField(db_column='CD2AP', blank=True, null=True)  # Field name made lowercase.
    cnr1 = models.FloatField(db_column='CNR1', blank=True, null=True)  # Field name made lowercase.
    enpp1 = models.FloatField(db_column='ENPP1', blank=True, null=True)  # Field name made lowercase.
    ctgf = models.FloatField(db_column='CTGF', blank=True, null=True)  # Field name made lowercase.
    rps12 = models.FloatField(db_column='RPS12', blank=True, null=True)  # Field name made lowercase.
    sgk1 = models.FloatField(db_column='SGK1', blank=True, null=True)  # Field name made lowercase.
    map3k5 = models.FloatField(db_column='MAP3K5', blank=True, null=True)  # Field name made lowercase.
    cited2 = models.FloatField(db_column='CITED2', blank=True, null=True)  # Field name made lowercase.
    utrn = models.FloatField(db_column='UTRN', blank=True, null=True)  # Field name made lowercase.
    mthfd1l = models.FloatField(db_column='MTHFD1L', blank=True, null=True)  # Field name made lowercase.
    vip = models.FloatField(db_column='VIP', blank=True, null=True)  # Field name made lowercase.
    sod2 = models.FloatField(db_column='SOD2', blank=True, null=True)  # Field name made lowercase.
    lpa = models.FloatField(db_column='LPA', blank=True, null=True)  # Field name made lowercase.
    thbs2 = models.FloatField(db_column='THBS2', blank=True, null=True)  # Field name made lowercase.
    pdgfa = models.FloatField(db_column='PDGFA', blank=True, null=True)  # Field name made lowercase.
    il6 = models.FloatField(db_column='IL6', blank=True, null=True)  # Field name made lowercase.
    npy = models.FloatField(db_column='NPY', blank=True, null=True)  # Field name made lowercase.
    jazf1 = models.FloatField(db_column='JAZF1', blank=True, null=True)  # Field name made lowercase.
    cpvl = models.FloatField(db_column='CPVL', blank=True, null=True)  # Field name made lowercase.
    aqp1 = models.FloatField(db_column='AQP1', blank=True, null=True)  # Field name made lowercase.
    elmo1 = models.FloatField(db_column='ELMO1', blank=True, null=True)  # Field name made lowercase.
    igfbp3 = models.FloatField(db_column='IGFBP3', blank=True, null=True)  # Field name made lowercase.
    egfr = models.FloatField(db_column='EGFR', blank=True, null=True)  # Field name made lowercase.
    eln = models.FloatField(db_column='ELN', blank=True, null=True)  # Field name made lowercase.
    ncf1 = models.FloatField(db_column='NCF1', blank=True, null=True)  # Field name made lowercase.
    hspb1 = models.FloatField(db_column='HSPB1', blank=True, null=True)  # Field name made lowercase.
    sema3a = models.FloatField(db_column='SEMA3A', blank=True, null=True)  # Field name made lowercase.
    pon3 = models.FloatField(db_column='PON3', blank=True, null=True)  # Field name made lowercase.
    pon2 = models.FloatField(db_column='PON2', blank=True, null=True)  # Field name made lowercase.
    nampt = models.FloatField(db_column='NAMPT', blank=True, null=True)  # Field name made lowercase.
    cav1 = models.FloatField(db_column='CAV1', blank=True, null=True)  # Field name made lowercase.
    lep = models.FloatField(db_column='LEP', blank=True, null=True)  # Field name made lowercase.
    akr1b1 = models.FloatField(db_column='AKR1B1', blank=True, null=True)  # Field name made lowercase.
    akr1b10 = models.FloatField(db_column='AKR1B10', blank=True, null=True)  # Field name made lowercase.
    pip = models.FloatField(db_column='PIP', blank=True, null=True)  # Field name made lowercase.
    rarres2 = models.FloatField(db_column='RARRES2', blank=True, null=True)  # Field name made lowercase.
    nos3 = models.FloatField(db_column='NOS3', blank=True, null=True)  # Field name made lowercase.
    angpt2 = models.FloatField(db_column='ANGPT2', blank=True, null=True)  # Field name made lowercase.
    defa1 = models.FloatField(db_column='DEFA1', blank=True, null=True)  # Field name made lowercase.
    lpl = models.FloatField(db_column='LPL', blank=True, null=True)  # Field name made lowercase.
    ebf2 = models.FloatField(db_column='EBF2', blank=True, null=True)  # Field name made lowercase.
    adrb3 = models.FloatField(db_column='ADRB3', blank=True, null=True)  # Field name made lowercase.
    eif4ebp1 = models.FloatField(db_column='EIF4EBP1', blank=True, null=True)  # Field name made lowercase.
    fgfr1 = models.FloatField(db_column='FGFR1', blank=True, null=True)  # Field name made lowercase.
    crh = models.FloatField(db_column='CRH', blank=True, null=True)  # Field name made lowercase.
    sgk3 = models.FloatField(db_column='SGK3', blank=True, null=True)  # Field name made lowercase.
    fabp5 = models.FloatField(db_column='FABP5', blank=True, null=True)  # Field name made lowercase.
    fabp4 = models.FloatField(db_column='FABP4', blank=True, null=True)  # Field name made lowercase.
    mmp16 = models.FloatField(db_column='MMP16', blank=True, null=True)  # Field name made lowercase.
    ncald = models.FloatField(db_column='NCALD', blank=True, null=True)  # Field name made lowercase.
    klf10 = models.FloatField(db_column='KLF10', blank=True, null=True)  # Field name made lowercase.
    enpp2 = models.FloatField(db_column='ENPP2', blank=True, null=True)  # Field name made lowercase.
    pvt1 = models.FloatField(db_column='PVT1', blank=True, null=True)  # Field name made lowercase.
    jak2 = models.FloatField(db_column='JAK2', blank=True, null=True)  # Field name made lowercase.
    psip1 = models.FloatField(db_column='PSIP1', blank=True, null=True)  # Field name made lowercase.
    plin2 = models.FloatField(db_column='PLIN2', blank=True, null=True)  # Field name made lowercase.
    rps6 = models.FloatField(db_column='RPS6', blank=True, null=True)  # Field name made lowercase.
    aldh1a1 = models.FloatField(db_column='ALDH1A1', blank=True, null=True)  # Field name made lowercase.
    frmd3 = models.FloatField(db_column='FRMD3', blank=True, null=True)  # Field name made lowercase.
    gas1 = models.FloatField(db_column='GAS1', blank=True, null=True)  # Field name made lowercase.
    baat = models.FloatField(db_column='BAAT', blank=True, null=True)  # Field name made lowercase.
    abca1 = models.FloatField(db_column='ABCA1', blank=True, null=True)  # Field name made lowercase.
    txn = models.FloatField(db_column='TXN', blank=True, null=True)  # Field name made lowercase.
    ambp = models.FloatField(db_column='AMBP', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    hspa5 = models.FloatField(db_column='HSPA5', blank=True, null=True)  # Field name made lowercase.
    angptl2 = models.FloatField(db_column='ANGPTL2', blank=True, null=True)  # Field name made lowercase.
    ptges = models.FloatField(db_column='PTGES', blank=True, null=True)  # Field name made lowercase.
    tsc1 = models.FloatField(db_column='TSC1', blank=True, null=True)  # Field name made lowercase.
    abo = models.FloatField(db_column='ABO', blank=True, null=True)  # Field name made lowercase.
    adamts13 = models.FloatField(db_column='ADAMTS13', blank=True, null=True)  # Field name made lowercase.
    ptgds = models.FloatField(db_column='PTGDS', blank=True, null=True)  # Field name made lowercase.
    klf6 = models.FloatField(db_column='KLF6', blank=True, null=True)  # Field name made lowercase.
    cdc123 = models.FloatField(db_column='CDC123', blank=True, null=True)  # Field name made lowercase.
    bambi = models.FloatField(db_column='BAMBI', blank=True, null=True)  # Field name made lowercase.
    cxcl12 = models.FloatField(db_column='CXCL12', blank=True, null=True)  # Field name made lowercase.
    mbl2 = models.FloatField(db_column='MBL2', blank=True, null=True)  # Field name made lowercase.
    tfam = models.FloatField(db_column='TFAM', blank=True, null=True)  # Field name made lowercase.
    sirt1 = models.FloatField(db_column='SIRT1', blank=True, null=True)  # Field name made lowercase.
    srgn = models.FloatField(db_column='SRGN', blank=True, null=True)  # Field name made lowercase.
    unc5b = models.FloatField(db_column='UNC5B', blank=True, null=True)  # Field name made lowercase.
    adk = models.FloatField(db_column='ADK', blank=True, null=True)  # Field name made lowercase.
    pten = models.FloatField(db_column='PTEN', blank=True, null=True)  # Field name made lowercase.
    rbp4 = models.FloatField(db_column='RBP4', blank=True, null=True)  # Field name made lowercase.
    cyp2c19 = models.FloatField(db_column='CYP2C19', blank=True, null=True)  # Field name made lowercase.
    entpd1 = models.FloatField(db_column='ENTPD1', blank=True, null=True)  # Field name made lowercase.
    tcf7l2 = models.FloatField(db_column='TCF7L2', blank=True, null=True)  # Field name made lowercase.
    bnip3 = models.FloatField(db_column='BNIP3', blank=True, null=True)  # Field name made lowercase.
    igf2 = models.FloatField(db_column='IGF2', blank=True, null=True)  # Field name made lowercase.
    ins = models.FloatField(db_column='INS', blank=True, null=True)  # Field name made lowercase.
    th = models.FloatField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    kcnq1 = models.FloatField(db_column='KCNQ1', blank=True, null=True)  # Field name made lowercase.
    hbg2 = models.FloatField(db_column='HBG2', blank=True, null=True)  # Field name made lowercase.
    smpd1 = models.FloatField(db_column='SMPD1', blank=True, null=True)  # Field name made lowercase.
    ilk = models.FloatField(db_column='ILK', blank=True, null=True)  # Field name made lowercase.
    adm = models.FloatField(db_column='ADM', blank=True, null=True)  # Field name made lowercase.
    pth = models.FloatField(db_column='PTH', blank=True, null=True)  # Field name made lowercase.
    nucb2 = models.FloatField(db_column='NUCB2', blank=True, null=True)  # Field name made lowercase.
    kcnj11 = models.FloatField(db_column='KCNJ11', blank=True, null=True)  # Field name made lowercase.
    saa1 = models.FloatField(db_column='SAA1', blank=True, null=True)  # Field name made lowercase.
    bdnf = models.FloatField(db_column='BDNF', blank=True, null=True)  # Field name made lowercase.
    wt1 = models.FloatField(db_column='WT1', blank=True, null=True)  # Field name made lowercase.
    cd59 = models.FloatField(db_column='CD59', blank=True, null=True)  # Field name made lowercase.
    pdhx = models.FloatField(db_column='PDHX', blank=True, null=True)  # Field name made lowercase.
    traf6 = models.FloatField(db_column='TRAF6', blank=True, null=True)  # Field name made lowercase.
    api5 = models.FloatField(db_column='API5', blank=True, null=True)  # Field name made lowercase.
    nr1h3 = models.FloatField(db_column='NR1H3', blank=True, null=True)  # Field name made lowercase.
    ndufs3 = models.FloatField(db_column='NDUFS3', blank=True, null=True)  # Field name made lowercase.
    folh1 = models.FloatField(db_column='FOLH1', blank=True, null=True)  # Field name made lowercase.
    aplnr = models.FloatField(db_column='APLNR', blank=True, null=True)  # Field name made lowercase.
    p2rx3 = models.FloatField(db_column='P2RX3', blank=True, null=True)  # Field name made lowercase.
    cntf = models.FloatField(db_column='CNTF', blank=True, null=True)  # Field name made lowercase.
    fads1 = models.FloatField(db_column='FADS1', blank=True, null=True)  # Field name made lowercase.
    fads2 = models.FloatField(db_column='FADS2', blank=True, null=True)  # Field name made lowercase.
    fkbp2 = models.FloatField(db_column='FKBP2', blank=True, null=True)  # Field name made lowercase.
    syvn1 = models.FloatField(db_column='SYVN1', blank=True, null=True)  # Field name made lowercase.
    pc = models.FloatField(db_column='PC', blank=True, null=True)  # Field name made lowercase.
    dhcr7 = models.FloatField(db_column='DHCR7', blank=True, null=True)  # Field name made lowercase.
    prcp = models.FloatField(db_column='PRCP', blank=True, null=True)  # Field name made lowercase.
    nox4 = models.FloatField(db_column='NOX4', blank=True, null=True)  # Field name made lowercase.
    pdgfd = models.FloatField(db_column='PDGFD', blank=True, null=True)  # Field name made lowercase.
    atm = models.FloatField(db_column='ATM', blank=True, null=True)  # Field name made lowercase.
    il18 = models.FloatField(db_column='IL18', blank=True, null=True)  # Field name made lowercase.
    apoa1 = models.FloatField(db_column='APOA1', blank=True, null=True)  # Field name made lowercase.
    hyou1 = models.FloatField(db_column='HYOU1', blank=True, null=True)  # Field name made lowercase.
    esam = models.FloatField(db_column='ESAM', blank=True, null=True)  # Field name made lowercase.
    fkbp4 = models.FloatField(db_column='FKBP4', blank=True, null=True)  # Field name made lowercase.
    fgf23 = models.FloatField(db_column='FGF23', blank=True, null=True)  # Field name made lowercase.
    ntf3 = models.FloatField(db_column='NTF3', blank=True, null=True)  # Field name made lowercase.
    vwf = models.FloatField(db_column='VWF', blank=True, null=True)  # Field name made lowercase.
    cd9 = models.FloatField(db_column='CD9', blank=True, null=True)  # Field name made lowercase.
    gapdh = models.FloatField(db_column='GAPDH', blank=True, null=True)  # Field name made lowercase.
    cd4 = models.FloatField(db_column='CD4', blank=True, null=True)  # Field name made lowercase.
    gnb3 = models.FloatField(db_column='GNB3', blank=True, null=True)  # Field name made lowercase.
    cd163 = models.FloatField(db_column='CD163', blank=True, null=True)  # Field name made lowercase.
    slc2a3 = models.FloatField(db_column='SLC2A3', blank=True, null=True)  # Field name made lowercase.
    cd69 = models.FloatField(db_column='CD69', blank=True, null=True)  # Field name made lowercase.
    irak4 = models.FloatField(db_column='IRAK4', blank=True, null=True)  # Field name made lowercase.
    vdr = models.FloatField(db_column='VDR', blank=True, null=True)  # Field name made lowercase.
    aqp5 = models.FloatField(db_column='AQP5', blank=True, null=True)  # Field name made lowercase.
    acvrl1 = models.FloatField(db_column='ACVRL1', blank=True, null=True)  # Field name made lowercase.
    nfe2 = models.FloatField(db_column='NFE2', blank=True, null=True)  # Field name made lowercase.
    cd63 = models.FloatField(db_column='CD63', blank=True, null=True)  # Field name made lowercase.
    erbb3 = models.FloatField(db_column='ERBB3', blank=True, null=True)  # Field name made lowercase.
    ddit3 = models.FloatField(db_column='DDIT3', blank=True, null=True)  # Field name made lowercase.
    ifng = models.FloatField(db_column='IFNG', blank=True, null=True)  # Field name made lowercase.
    nts = models.FloatField(db_column='NTS', blank=True, null=True)  # Field name made lowercase.
    igf1 = models.FloatField(db_column='IGF1', blank=True, null=True)  # Field name made lowercase.
    acacb = models.FloatField(db_column='ACACB', blank=True, null=True)  # Field name made lowercase.
    trpv4 = models.FloatField(db_column='TRPV4', blank=True, null=True)  # Field name made lowercase.
    atp2a2 = models.FloatField(db_column='ATP2A2', blank=True, null=True)  # Field name made lowercase.
    aldh2 = models.FloatField(db_column='ALDH2', blank=True, null=True)  # Field name made lowercase.
    nos1 = models.FloatField(db_column='NOS1', blank=True, null=True)  # Field name made lowercase.
    pebp1 = models.FloatField(db_column='PEBP1', blank=True, null=True)  # Field name made lowercase.
    psmd9 = models.FloatField(db_column='PSMD9', blank=True, null=True)  # Field name made lowercase.
    scarb1 = models.FloatField(db_column='SCARB1', blank=True, null=True)  # Field name made lowercase.
    p2rx2 = models.FloatField(db_column='P2RX2', blank=True, null=True)  # Field name made lowercase.
    alox5ap = models.FloatField(db_column='ALOX5AP', blank=True, null=True)  # Field name made lowercase.
    kl = models.FloatField(db_column='KL', blank=True, null=True)  # Field name made lowercase.
    postn = models.FloatField(db_column='POSTN', blank=True, null=True)  # Field name made lowercase.
    foxo1 = models.FloatField(db_column='FOXO1', blank=True, null=True)  # Field name made lowercase.
    htr2a = models.FloatField(db_column='HTR2A', blank=True, null=True)  # Field name made lowercase.
    gpc5 = models.FloatField(db_column='GPC5', blank=True, null=True)  # Field name made lowercase.
    irs2 = models.FloatField(db_column='IRS2', blank=True, null=True)  # Field name made lowercase.
    gas6 = models.FloatField(db_column='GAS6', blank=True, null=True)  # Field name made lowercase.
    ang = models.FloatField(db_column='ANG', blank=True, null=True)  # Field name made lowercase.
    mmp14 = models.FloatField(db_column='MMP14', blank=True, null=True)  # Field name made lowercase.
    ltb4r2 = models.FloatField(db_column='LTB4R2', blank=True, null=True)  # Field name made lowercase.
    nfkbia = models.FloatField(db_column='NFKBIA', blank=True, null=True)  # Field name made lowercase.
    bmp4 = models.FloatField(db_column='BMP4', blank=True, null=True)  # Field name made lowercase.
    rtn1 = models.FloatField(db_column='RTN1', blank=True, null=True)  # Field name made lowercase.
    pgf = models.FloatField(db_column='PGF', blank=True, null=True)  # Field name made lowercase.
    ngb = models.FloatField(db_column='NGB', blank=True, null=True)  # Field name made lowercase.
    ahsa1 = models.FloatField(db_column='AHSA1', blank=True, null=True)  # Field name made lowercase.
    bdkrb2 = models.FloatField(db_column='BDKRB2', blank=True, null=True)  # Field name made lowercase.
    bdkrb1 = models.FloatField(db_column='BDKRB1', blank=True, null=True)  # Field name made lowercase.
    akt1 = models.FloatField(db_column='AKT1', blank=True, null=True)  # Field name made lowercase.
    grem1 = models.FloatField(db_column='GREM1', blank=True, null=True)  # Field name made lowercase.
    thbs1 = models.FloatField(db_column='THBS1', blank=True, null=True)  # Field name made lowercase.
    pak6 = models.FloatField(db_column='PAK6', blank=True, null=True)  # Field name made lowercase.
    b2m = models.FloatField(db_column='B2M', blank=True, null=True)  # Field name made lowercase.
    myo5c = models.FloatField(db_column='MYO5C', blank=True, null=True)  # Field name made lowercase.
    onecut1 = models.FloatField(db_column='ONECUT1', blank=True, null=True)  # Field name made lowercase.
    adam10 = models.FloatField(db_column='ADAM10', blank=True, null=True)  # Field name made lowercase.
    ctsh = models.FloatField(db_column='CTSH', blank=True, null=True)  # Field name made lowercase.
    plin1 = models.FloatField(db_column='PLIN1', blank=True, null=True)  # Field name made lowercase.
    igf1r = models.FloatField(db_column='IGF1R', blank=True, null=True)  # Field name made lowercase.
    mrpl28 = models.FloatField(db_column='MRPL28', blank=True, null=True)  # Field name made lowercase.
    cacna1h = models.FloatField(db_column='CACNA1H', blank=True, null=True)  # Field name made lowercase.
    pdpk1 = models.FloatField(db_column='PDPK1', blank=True, null=True)  # Field name made lowercase.
    ercc4 = models.FloatField(db_column='ERCC4', blank=True, null=True)  # Field name made lowercase.
    smg1 = models.FloatField(db_column='SMG1', blank=True, null=True)  # Field name made lowercase.
    itgam = models.FloatField(db_column='ITGAM', blank=True, null=True)  # Field name made lowercase.
    fto = models.FloatField(db_column='FTO', blank=True, null=True)  # Field name made lowercase.
    mmp2 = models.FloatField(db_column='MMP2', blank=True, null=True)  # Field name made lowercase.
    slc12a3 = models.FloatField(db_column='SLC12A3', blank=True, null=True)  # Field name made lowercase.
    cetp = models.FloatField(db_column='CETP', blank=True, null=True)  # Field name made lowercase.
    cx3cl1 = models.FloatField(db_column='CX3CL1', blank=True, null=True)  # Field name made lowercase.
    cdh1 = models.FloatField(db_column='CDH1', blank=True, null=True)  # Field name made lowercase.
    nqo1 = models.FloatField(db_column='NQO1', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    znrf1 = models.FloatField(db_column='ZNRF1', blank=True, null=True)  # Field name made lowercase.
    cyba = models.FloatField(db_column='CYBA', blank=True, null=True)  # Field name made lowercase.
    tubb3 = models.FloatField(db_column='TUBB3', blank=True, null=True)  # Field name made lowercase.
    crk = models.FloatField(db_column='CRK', blank=True, null=True)  # Field name made lowercase.
    serpinf2 = models.FloatField(db_column='SERPINF2', blank=True, null=True)  # Field name made lowercase.
    serpinf1 = models.FloatField(db_column='SERPINF1', blank=True, null=True)  # Field name made lowercase.
    trpv3 = models.FloatField(db_column='TRPV3', blank=True, null=True)  # Field name made lowercase.
    cxcl16 = models.FloatField(db_column='CXCL16', blank=True, null=True)  # Field name made lowercase.
    slc2a4 = models.FloatField(db_column='SLC2A4', blank=True, null=True)  # Field name made lowercase.
    cd68 = models.FloatField(db_column='CD68', blank=True, null=True)  # Field name made lowercase.
    shbg = models.FloatField(db_column='SHBG', blank=True, null=True)  # Field name made lowercase.
    pmp22 = models.FloatField(db_column='PMP22', blank=True, null=True)  # Field name made lowercase.
    srebf1 = models.FloatField(db_column='SREBF1', blank=True, null=True)  # Field name made lowercase.
    mapk7 = models.FloatField(db_column='MAPK7', blank=True, null=True)  # Field name made lowercase.
    ccl2 = models.FloatField(db_column='CCL2', blank=True, null=True)  # Field name made lowercase.
    ccl5 = models.FloatField(db_column='CCL5', blank=True, null=True)  # Field name made lowercase.
    hnf1b = models.FloatField(db_column='HNF1B', blank=True, null=True)  # Field name made lowercase.
    erbb2 = models.FloatField(db_column='ERBB2', blank=True, null=True)  # Field name made lowercase.
    fkbp10 = models.FloatField(db_column='FKBP10', blank=True, null=True)  # Field name made lowercase.
    stat5a = models.FloatField(db_column='STAT5A', blank=True, null=True)  # Field name made lowercase.
    stat3 = models.FloatField(db_column='STAT3', blank=True, null=True)  # Field name made lowercase.
    naglu = models.FloatField(db_column='NAGLU', blank=True, null=True)  # Field name made lowercase.
    aoc2 = models.FloatField(db_column='AOC2', blank=True, null=True)  # Field name made lowercase.
    aoc3 = models.FloatField(db_column='AOC3', blank=True, null=True)  # Field name made lowercase.
    ppy = models.FloatField(db_column='PPY', blank=True, null=True)  # Field name made lowercase.
    sth = models.FloatField(db_column='STH', blank=True, null=True)  # Field name made lowercase.
    itgb3 = models.FloatField(db_column='ITGB3', blank=True, null=True)  # Field name made lowercase.
    gip = models.FloatField(db_column='GIP', blank=True, null=True)  # Field name made lowercase.
    mpo = models.FloatField(db_column='MPO', blank=True, null=True)  # Field name made lowercase.
    pecam1 = models.FloatField(db_column='PECAM1', blank=True, null=True)  # Field name made lowercase.
    sox9 = models.FloatField(db_column='SOX9', blank=True, null=True)  # Field name made lowercase.
    timp2 = models.FloatField(db_column='TIMP2', blank=True, null=True)  # Field name made lowercase.
    dcxr = models.FloatField(db_column='DCXR', blank=True, null=True)  # Field name made lowercase.
    fasn = models.FloatField(db_column='FASN', blank=True, null=True)  # Field name made lowercase.
    colec12 = models.FloatField(db_column='COLEC12', blank=True, null=True)  # Field name made lowercase.
    adcyap1 = models.FloatField(db_column='ADCYAP1', blank=True, null=True)  # Field name made lowercase.
    smad7 = models.FloatField(db_column='SMAD7', blank=True, null=True)  # Field name made lowercase.
    nedd4l = models.FloatField(db_column='NEDD4L', blank=True, null=True)  # Field name made lowercase.
    mc4r = models.FloatField(db_column='MC4R', blank=True, null=True)  # Field name made lowercase.
    bcl2 = models.FloatField(db_column='BCL2', blank=True, null=True)  # Field name made lowercase.
    cndp2 = models.FloatField(db_column='CNDP2', blank=True, null=True)  # Field name made lowercase.
    znf236 = models.FloatField(db_column='ZNF236', blank=True, null=True)  # Field name made lowercase.
    stk11 = models.FloatField(db_column='STK11', blank=True, null=True)  # Field name made lowercase.
    sirt6 = models.FloatField(db_column='SIRT6', blank=True, null=True)  # Field name made lowercase.
    uhrf1 = models.FloatField(db_column='UHRF1', blank=True, null=True)  # Field name made lowercase.
    timm44 = models.FloatField(db_column='TIMM44', blank=True, null=True)  # Field name made lowercase.
    angptl4 = models.FloatField(db_column='ANGPTL4', blank=True, null=True)  # Field name made lowercase.
    dnmt1 = models.FloatField(db_column='DNMT1', blank=True, null=True)  # Field name made lowercase.
    icam1 = models.FloatField(db_column='ICAM1', blank=True, null=True)  # Field name made lowercase.
    ldlr = models.FloatField(db_column='LDLR', blank=True, null=True)  # Field name made lowercase.
    epor = models.FloatField(db_column='EPOR', blank=True, null=True)  # Field name made lowercase.
    prdx2 = models.FloatField(db_column='PRDX2', blank=True, null=True)  # Field name made lowercase.
    ptger1 = models.FloatField(db_column='PTGER1', blank=True, null=True)  # Field name made lowercase.
    unc13a = models.FloatField(db_column='UNC13A', blank=True, null=True)  # Field name made lowercase.
    gdf15 = models.FloatField(db_column='GDF15', blank=True, null=True)  # Field name made lowercase.
    fkbp8 = models.FloatField(db_column='FKBP8', blank=True, null=True)  # Field name made lowercase.
    usf2 = models.FloatField(db_column='USF2', blank=True, null=True)  # Field name made lowercase.
    ffar1 = models.FloatField(db_column='FFAR1', blank=True, null=True)  # Field name made lowercase.
    ffar2 = models.FloatField(db_column='FFAR2', blank=True, null=True)  # Field name made lowercase.
    nphs1 = models.FloatField(db_column='NPHS1', blank=True, null=True)  # Field name made lowercase.
    tgfb1 = models.FloatField(db_column='TGFB1', blank=True, null=True)  # Field name made lowercase.
    xrcc1 = models.FloatField(db_column='XRCC1', blank=True, null=True)  # Field name made lowercase.
    ercc1 = models.FloatField(db_column='ERCC1', blank=True, null=True)  # Field name made lowercase.
    gipr = models.FloatField(db_column='GIPR', blank=True, null=True)  # Field name made lowercase.
    fgf21 = models.FloatField(db_column='FGF21', blank=True, null=True)  # Field name made lowercase.
    clec11a = models.FloatField(db_column='CLEC11A', blank=True, null=True)  # Field name made lowercase.
    fpr1 = models.FloatField(db_column='FPR1', blank=True, null=True)  # Field name made lowercase.
    trib3 = models.FloatField(db_column='TRIB3', blank=True, null=True)  # Field name made lowercase.
    bmp2 = models.FloatField(db_column='BMP2', blank=True, null=True)  # Field name made lowercase.
    thbd = models.FloatField(db_column='THBD', blank=True, null=True)  # Field name made lowercase.
    cst3 = models.FloatField(db_column='CST3', blank=True, null=True)  # Field name made lowercase.
    id1 = models.FloatField(db_column='ID1', blank=True, null=True)  # Field name made lowercase.
    src = models.FloatField(db_column='SRC', blank=True, null=True)  # Field name made lowercase.
    mafb = models.FloatField(db_column='MAFB', blank=True, null=True)  # Field name made lowercase.
    sgk2 = models.FloatField(db_column='SGK2', blank=True, null=True)  # Field name made lowercase.
    hnf4a = models.FloatField(db_column='HNF4A', blank=True, null=True)  # Field name made lowercase.
    pltp = models.FloatField(db_column='PLTP', blank=True, null=True)  # Field name made lowercase.
    mmp9 = models.FloatField(db_column='MMP9', blank=True, null=True)  # Field name made lowercase.
    cd40 = models.FloatField(db_column='CD40', blank=True, null=True)  # Field name made lowercase.
    ptpn1 = models.FloatField(db_column='PTPN1', blank=True, null=True)  # Field name made lowercase.
    cyp24a1 = models.FloatField(db_column='CYP24A1', blank=True, null=True)  # Field name made lowercase.
    rcan1 = models.FloatField(db_column='RCAN1', blank=True, null=True)  # Field name made lowercase.
    abcg1 = models.FloatField(db_column='ABCG1', blank=True, null=True)  # Field name made lowercase.
    prmt2 = models.FloatField(db_column='PRMT2', blank=True, null=True)  # Field name made lowercase.
    comt = models.FloatField(db_column='COMT', blank=True, null=True)  # Field name made lowercase.
    mapk1 = models.FloatField(db_column='MAPK1', blank=True, null=True)  # Field name made lowercase.
    mif = models.FloatField(db_column='MIF', blank=True, null=True)  # Field name made lowercase.
    ggt1 = models.FloatField(db_column='GGT1', blank=True, null=True)  # Field name made lowercase.
    xbp1 = models.FloatField(db_column='XBP1', blank=True, null=True)  # Field name made lowercase.
    osm = models.FloatField(db_column='OSM', blank=True, null=True)  # Field name made lowercase.
    limk2 = models.FloatField(db_column='LIMK2', blank=True, null=True)  # Field name made lowercase.
    sfi1 = models.FloatField(db_column='SFI1', blank=True, null=True)  # Field name made lowercase.
    timp3 = models.FloatField(db_column='TIMP3', blank=True, null=True)  # Field name made lowercase.
    hmox1 = models.FloatField(db_column='HMOX1', blank=True, null=True)  # Field name made lowercase.
    apol1 = models.FloatField(db_column='APOL1', blank=True, null=True)  # Field name made lowercase.
    myh9 = models.FloatField(db_column='MYH9', blank=True, null=True)  # Field name made lowercase.
    pdgfb = models.FloatField(db_column='PDGFB', blank=True, null=True)  # Field name made lowercase.
    atf4 = models.FloatField(db_column='ATF4', blank=True, null=True)  # Field name made lowercase.
    tspo = models.FloatField(db_column='TSPO', blank=True, null=True)  # Field name made lowercase.
    miox = models.FloatField(db_column='MIOX', blank=True, null=True)  # Field name made lowercase.
    prdx4 = models.FloatField(db_column='PRDX4', blank=True, null=True)  # Field name made lowercase.
    gk = models.FloatField(db_column='GK', blank=True, null=True)  # Field name made lowercase.
    rgn = models.FloatField(db_column='RGN', blank=True, null=True)  # Field name made lowercase.
    timp1 = models.FloatField(db_column='TIMP1', blank=True, null=True)  # Field name made lowercase.
    clcn5 = models.FloatField(db_column='CLCN5', blank=True, null=True)  # Field name made lowercase.
    ar = models.FloatField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    foxo4 = models.FloatField(db_column='FOXO4', blank=True, null=True)  # Field name made lowercase.
    rps6ka6 = models.FloatField(db_column='RPS6KA6', blank=True, null=True)  # Field name made lowercase.
    nox1 = models.FloatField(db_column='NOX1', blank=True, null=True)  # Field name made lowercase.
    xiap = models.FloatField(db_column='XIAP', blank=True, null=True)  # Field name made lowercase.
    cd40lg = models.FloatField(db_column='CD40LG', blank=True, null=True)  # Field name made lowercase.
    l1cam = models.FloatField(db_column='L1CAM', blank=True, null=True)  # Field name made lowercase.
    irak1 = models.FloatField(db_column='IRAK1', blank=True, null=True)  # Field name made lowercase.
    g6pd = models.FloatField(db_column='G6PD', blank=True, null=True)  # Field name made lowercase.
    f8 = models.FloatField(db_column='F8', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diaco_tissue_brain_cerebellar_hs'


class DiacoTissueBrainCerebellum(models.Model):
    subjid = models.CharField(db_column='SUBJID', max_length=50, primary_key=True)  # Field name made lowercase.
    sampid = models.CharField(db_column='SAMPID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sesso = models.CharField(db_column='Sesso', max_length=1)  # Field name made lowercase.
    eta = models.CharField(db_column='Età', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errfi1 = models.FloatField(db_column='ERRFI1', blank=True, null=True)  # Field name made lowercase.
    mad2l2 = models.FloatField(db_column='MAD2L2', blank=True, null=True)  # Field name made lowercase.
    mthfr = models.FloatField(db_column='MTHFR', blank=True, null=True)  # Field name made lowercase.
    nppa = models.FloatField(db_column='NPPA', blank=True, null=True)  # Field name made lowercase.
    tnfrsf1b = models.FloatField(db_column='TNFRSF1B', blank=True, null=True)  # Field name made lowercase.
    pla2g2a = models.FloatField(db_column='PLA2G2A', blank=True, null=True)  # Field name made lowercase.
    alpl = models.FloatField(db_column='ALPL', blank=True, null=True)  # Field name made lowercase.
    hspg2 = models.FloatField(db_column='HSPG2', blank=True, null=True)  # Field name made lowercase.
    cnr2 = models.FloatField(db_column='CNR2', blank=True, null=True)  # Field name made lowercase.
    slc9a1 = models.FloatField(db_column='SLC9A1', blank=True, null=True)  # Field name made lowercase.
    col8a2 = models.FloatField(db_column='COL8A2', blank=True, null=True)  # Field name made lowercase.
    cap1 = models.FloatField(db_column='CAP1', blank=True, null=True)  # Field name made lowercase.
    slc2a1 = models.FloatField(db_column='SLC2A1', blank=True, null=True)  # Field name made lowercase.
    cyp2j2 = models.FloatField(db_column='CYP2J2', blank=True, null=True)  # Field name made lowercase.
    ddah1 = models.FloatField(db_column='DDAH1', blank=True, null=True)  # Field name made lowercase.
    cyr61 = models.FloatField(db_column='CYR61', blank=True, null=True)  # Field name made lowercase.
    ngf = models.FloatField(db_column='NGF', blank=True, null=True)  # Field name made lowercase.
    hmgcs2 = models.FloatField(db_column='HMGCS2', blank=True, null=True)  # Field name made lowercase.
    ctss = models.FloatField(db_column='CTSS', blank=True, null=True)  # Field name made lowercase.
    s100a12 = models.FloatField(db_column='S100A12', blank=True, null=True)  # Field name made lowercase.
    lmna = models.FloatField(db_column='LMNA', blank=True, null=True)  # Field name made lowercase.
    cd247 = models.FloatField(db_column='CD247', blank=True, null=True)  # Field name made lowercase.
    sele = models.FloatField(db_column='SELE', blank=True, null=True)  # Field name made lowercase.
    fmo3 = models.FloatField(db_column='FMO3', blank=True, null=True)  # Field name made lowercase.
    prdx6 = models.FloatField(db_column='PRDX6', blank=True, null=True)  # Field name made lowercase.
    glul = models.FloatField(db_column='GLUL', blank=True, null=True)  # Field name made lowercase.
    lamc1 = models.FloatField(db_column='LAMC1', blank=True, null=True)  # Field name made lowercase.
    ptgs2 = models.FloatField(db_column='PTGS2', blank=True, null=True)  # Field name made lowercase.
    chi3l1 = models.FloatField(db_column='CHI3L1', blank=True, null=True)  # Field name made lowercase.
    chit1 = models.FloatField(db_column='CHIT1', blank=True, null=True)  # Field name made lowercase.
    fmod = models.FloatField(db_column='FMOD', blank=True, null=True)  # Field name made lowercase.
    il10 = models.FloatField(db_column='IL10', blank=True, null=True)  # Field name made lowercase.
    pfkfb2 = models.FloatField(db_column='PFKFB2', blank=True, null=True)  # Field name made lowercase.
    cd34 = models.FloatField(db_column='CD34', blank=True, null=True)  # Field name made lowercase.
    cog2 = models.FloatField(db_column='COG2', blank=True, null=True)  # Field name made lowercase.
    nlrp3 = models.FloatField(db_column='NLRP3', blank=True, null=True)  # Field name made lowercase.
    rock2 = models.FloatField(db_column='ROCK2', blank=True, null=True)  # Field name made lowercase.
    apob = models.FloatField(db_column='APOB', blank=True, null=True)  # Field name made lowercase.
    pomc = models.FloatField(db_column='POMC', blank=True, null=True)  # Field name made lowercase.
    gckr = models.FloatField(db_column='GCKR', blank=True, null=True)  # Field name made lowercase.
    plekhh2 = models.FloatField(db_column='PLEKHH2', blank=True, null=True)  # Field name made lowercase.
    prkce = models.FloatField(db_column='PRKCE', blank=True, null=True)  # Field name made lowercase.
    pigf = models.FloatField(db_column='PIGF', blank=True, null=True)  # Field name made lowercase.
    msh2 = models.FloatField(db_column='MSH2', blank=True, null=True)  # Field name made lowercase.
    gfpt1 = models.FloatField(db_column='GFPT1', blank=True, null=True)  # Field name made lowercase.
    tacr1 = models.FloatField(db_column='TACR1', blank=True, null=True)  # Field name made lowercase.
    reg1a = models.FloatField(db_column='REG1A', blank=True, null=True)  # Field name made lowercase.
    eif2ak3 = models.FloatField(db_column='EIF2AK3', blank=True, null=True)  # Field name made lowercase.
    adra2b = models.FloatField(db_column='ADRA2B', blank=True, null=True)  # Field name made lowercase.
    il1b = models.FloatField(db_column='IL1B', blank=True, null=True)  # Field name made lowercase.
    proc = models.FloatField(db_column='PROC', blank=True, null=True)  # Field name made lowercase.
    polr2d = models.FloatField(db_column='POLR2D', blank=True, null=True)  # Field name made lowercase.
    zeb2 = models.FloatField(db_column='ZEB2', blank=True, null=True)  # Field name made lowercase.
    acvr1c = models.FloatField(db_column='ACVR1C', blank=True, null=True)  # Field name made lowercase.
    dpp4 = models.FloatField(db_column='DPP4', blank=True, null=True)  # Field name made lowercase.
    nfe2l2 = models.FloatField(db_column='NFE2L2', blank=True, null=True)  # Field name made lowercase.
    igfbp5 = models.FloatField(db_column='IGFBP5', blank=True, null=True)  # Field name made lowercase.
    ccl20 = models.FloatField(db_column='CCL20', blank=True, null=True)  # Field name made lowercase.
    hdac4 = models.FloatField(db_column='HDAC4', blank=True, null=True)  # Field name made lowercase.
    capn10 = models.FloatField(db_column='CAPN10', blank=True, null=True)  # Field name made lowercase.
    ghrl = models.FloatField(db_column='GHRL', blank=True, null=True)  # Field name made lowercase.
    pparg = models.FloatField(db_column='PPARG', blank=True, null=True)  # Field name made lowercase.
    raf1 = models.FloatField(db_column='RAF1', blank=True, null=True)  # Field name made lowercase.
    myd88 = models.FloatField(db_column='MYD88', blank=True, null=True)  # Field name made lowercase.
    cx3cr1 = models.FloatField(db_column='CX3CR1', blank=True, null=True)  # Field name made lowercase.
    cck = models.FloatField(db_column='CCK', blank=True, null=True)  # Field name made lowercase.
    exosc7 = models.FloatField(db_column='EXOSC7', blank=True, null=True)  # Field name made lowercase.
    ccr1 = models.FloatField(db_column='CCR1', blank=True, null=True)  # Field name made lowercase.
    ccr5 = models.FloatField(db_column='CCR5', blank=True, null=True)  # Field name made lowercase.
    gpx1 = models.FloatField(db_column='GPX1', blank=True, null=True)  # Field name made lowercase.
    rhoa = models.FloatField(db_column='RHOA', blank=True, null=True)  # Field name made lowercase.
    cish = models.FloatField(db_column='CISH', blank=True, null=True)  # Field name made lowercase.
    tkt = models.FloatField(db_column='TKT', blank=True, null=True)  # Field name made lowercase.
    appl1 = models.FloatField(db_column='APPL1', blank=True, null=True)  # Field name made lowercase.
    slmap = models.FloatField(db_column='SLMAP', blank=True, null=True)  # Field name made lowercase.
    col8a1 = models.FloatField(db_column='COL8A1', blank=True, null=True)  # Field name made lowercase.
    cd47 = models.FloatField(db_column='CD47', blank=True, null=True)  # Field name made lowercase.
    gap43 = models.FloatField(db_column='GAP43', blank=True, null=True)  # Field name made lowercase.
    cd80 = models.FloatField(db_column='CD80', blank=True, null=True)  # Field name made lowercase.
    rho = models.FloatField(db_column='RHO', blank=True, null=True)  # Field name made lowercase.
    trh = models.FloatField(db_column='TRH', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='TF', blank=True, null=True)  # Field name made lowercase.
    rbp1 = models.FloatField(db_column='RBP1', blank=True, null=True)  # Field name made lowercase.
    trpc1 = models.FloatField(db_column='TRPC1', blank=True, null=True)  # Field name made lowercase.
    agtr1 = models.FloatField(db_column='AGTR1', blank=True, null=True)  # Field name made lowercase.
    sucnr1 = models.FloatField(db_column='SUCNR1', blank=True, null=True)  # Field name made lowercase.
    p2ry1 = models.FloatField(db_column='P2RY1', blank=True, null=True)  # Field name made lowercase.
    mme = models.FloatField(db_column='MME', blank=True, null=True)  # Field name made lowercase.
    slc2a2 = models.FloatField(db_column='SLC2A2', blank=True, null=True)  # Field name made lowercase.
    pik3ca = models.FloatField(db_column='PIK3CA', blank=True, null=True)  # Field name made lowercase.
    parl = models.FloatField(db_column='PARL', blank=True, null=True)  # Field name made lowercase.
    ahsg = models.FloatField(db_column='AHSG', blank=True, null=True)  # Field name made lowercase.
    adipoq = models.FloatField(db_column='ADIPOQ', blank=True, null=True)  # Field name made lowercase.
    spon2 = models.FloatField(db_column='SPON2', blank=True, null=True)  # Field name made lowercase.
    wfs1 = models.FloatField(db_column='WFS1', blank=True, null=True)  # Field name made lowercase.
    cd38 = models.FloatField(db_column='CD38', blank=True, null=True)  # Field name made lowercase.
    prom1 = models.FloatField(db_column='PROM1', blank=True, null=True)  # Field name made lowercase.
    ppargc1a = models.FloatField(db_column='PPARGC1A', blank=True, null=True)  # Field name made lowercase.
    igfbp7 = models.FloatField(db_column='IGFBP7', blank=True, null=True)  # Field name made lowercase.
    cxcl5 = models.FloatField(db_column='CXCL5', blank=True, null=True)  # Field name made lowercase.
    cxcl9 = models.FloatField(db_column='CXCL9', blank=True, null=True)  # Field name made lowercase.
    cxcl10 = models.FloatField(db_column='CXCL10', blank=True, null=True)  # Field name made lowercase.
    cxcl11 = models.FloatField(db_column='CXCL11', blank=True, null=True)  # Field name made lowercase.
    hpse = models.FloatField(db_column='HPSE', blank=True, null=True)  # Field name made lowercase.
    spp1 = models.FloatField(db_column='SPP1', blank=True, null=True)  # Field name made lowercase.
    adh1b = models.FloatField(db_column='ADH1B', blank=True, null=True)  # Field name made lowercase.
    egf = models.FloatField(db_column='EGF', blank=True, null=True)  # Field name made lowercase.
    alpk1 = models.FloatField(db_column='ALPK1', blank=True, null=True)  # Field name made lowercase.
    fabp2 = models.FloatField(db_column='FABP2', blank=True, null=True)  # Field name made lowercase.
    pde5a = models.FloatField(db_column='PDE5A', blank=True, null=True)  # Field name made lowercase.
    setd7 = models.FloatField(db_column='SETD7', blank=True, null=True)  # Field name made lowercase.
    smad1 = models.FloatField(db_column='SMAD1', blank=True, null=True)  # Field name made lowercase.
    ednra = models.FloatField(db_column='EDNRA', blank=True, null=True)  # Field name made lowercase.
    nr3c2 = models.FloatField(db_column='NR3C2', blank=True, null=True)  # Field name made lowercase.
    tlr2 = models.FloatField(db_column='TLR2', blank=True, null=True)  # Field name made lowercase.
    npy5r = models.FloatField(db_column='NPY5R', blank=True, null=True)  # Field name made lowercase.
    fbxo8 = models.FloatField(db_column='FBXO8', blank=True, null=True)  # Field name made lowercase.
    vegfc = models.FloatField(db_column='VEGFC', blank=True, null=True)  # Field name made lowercase.
    acsl1 = models.FloatField(db_column='ACSL1', blank=True, null=True)  # Field name made lowercase.
    sorbs2 = models.FloatField(db_column='SORBS2', blank=True, null=True)  # Field name made lowercase.
    f11 = models.FloatField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    basp1 = models.FloatField(db_column='BASP1', blank=True, null=True)  # Field name made lowercase.
    ptger4 = models.FloatField(db_column='PTGER4', blank=True, null=True)  # Field name made lowercase.
    prkaa1 = models.FloatField(db_column='PRKAA1', blank=True, null=True)  # Field name made lowercase.
    ghr = models.FloatField(db_column='GHR', blank=True, null=True)  # Field name made lowercase.
    itga2 = models.FloatField(db_column='ITGA2', blank=True, null=True)  # Field name made lowercase.
    cdk7 = models.FloatField(db_column='CDK7', blank=True, null=True)  # Field name made lowercase.
    f2r = models.FloatField(db_column='F2R', blank=True, null=True)  # Field name made lowercase.
    erap2 = models.FloatField(db_column='ERAP2', blank=True, null=True)  # Field name made lowercase.
    apc = models.FloatField(db_column='APC', blank=True, null=True)  # Field name made lowercase.
    tnfaip8 = models.FloatField(db_column='TNFAIP8', blank=True, null=True)  # Field name made lowercase.
    vdac1 = models.FloatField(db_column='VDAC1', blank=True, null=True)  # Field name made lowercase.
    pdgfrb = models.FloatField(db_column='PDGFRB', blank=True, null=True)  # Field name made lowercase.
    cd74 = models.FloatField(db_column='CD74', blank=True, null=True)  # Field name made lowercase.
    sparc = models.FloatField(db_column='SPARC', blank=True, null=True)  # Field name made lowercase.
    ebf1 = models.FloatField(db_column='EBF1', blank=True, null=True)  # Field name made lowercase.
    gfpt2 = models.FloatField(db_column='GFPT2', blank=True, null=True)  # Field name made lowercase.
    rreb1 = models.FloatField(db_column='RREB1', blank=True, null=True)  # Field name made lowercase.
    edn1 = models.FloatField(db_column='EDN1', blank=True, null=True)  # Field name made lowercase.
    cdkal1 = models.FloatField(db_column='CDKAL1', blank=True, null=True)  # Field name made lowercase.
    hfe = models.FloatField(db_column='HFE', blank=True, null=True)  # Field name made lowercase.
    hla_a = models.FloatField(db_column='HLA-A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  # Field name made lowercase.
    tnf = models.FloatField(db_column='TNF', blank=True, null=True)  # Field name made lowercase.
    hspa1a = models.FloatField(db_column='HSPA1A', blank=True, null=True)  # Field name made lowercase.
    hspa1b = models.FloatField(db_column='HSPA1B', blank=True, null=True)  # Field name made lowercase.
    hla_dqa1 = models.FloatField(db_column='HLA-DQA1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mapk14 = models.FloatField(db_column='MAPK14', blank=True, null=True)  # Field name made lowercase.
    cdkn1a = models.FloatField(db_column='CDKN1A', blank=True, null=True)  # Field name made lowercase.
    glo1 = models.FloatField(db_column='GLO1', blank=True, null=True)  # Field name made lowercase.
    vegfa = models.FloatField(db_column='VEGFA', blank=True, null=True)  # Field name made lowercase.
    cd2ap = models.FloatField(db_column='CD2AP', blank=True, null=True)  # Field name made lowercase.
    cnr1 = models.FloatField(db_column='CNR1', blank=True, null=True)  # Field name made lowercase.
    enpp1 = models.FloatField(db_column='ENPP1', blank=True, null=True)  # Field name made lowercase.
    ctgf = models.FloatField(db_column='CTGF', blank=True, null=True)  # Field name made lowercase.
    rps12 = models.FloatField(db_column='RPS12', blank=True, null=True)  # Field name made lowercase.
    sgk1 = models.FloatField(db_column='SGK1', blank=True, null=True)  # Field name made lowercase.
    map3k5 = models.FloatField(db_column='MAP3K5', blank=True, null=True)  # Field name made lowercase.
    cited2 = models.FloatField(db_column='CITED2', blank=True, null=True)  # Field name made lowercase.
    utrn = models.FloatField(db_column='UTRN', blank=True, null=True)  # Field name made lowercase.
    mthfd1l = models.FloatField(db_column='MTHFD1L', blank=True, null=True)  # Field name made lowercase.
    vip = models.FloatField(db_column='VIP', blank=True, null=True)  # Field name made lowercase.
    sod2 = models.FloatField(db_column='SOD2', blank=True, null=True)  # Field name made lowercase.
    lpa = models.FloatField(db_column='LPA', blank=True, null=True)  # Field name made lowercase.
    thbs2 = models.FloatField(db_column='THBS2', blank=True, null=True)  # Field name made lowercase.
    pdgfa = models.FloatField(db_column='PDGFA', blank=True, null=True)  # Field name made lowercase.
    il6 = models.FloatField(db_column='IL6', blank=True, null=True)  # Field name made lowercase.
    npy = models.FloatField(db_column='NPY', blank=True, null=True)  # Field name made lowercase.
    jazf1 = models.FloatField(db_column='JAZF1', blank=True, null=True)  # Field name made lowercase.
    cpvl = models.FloatField(db_column='CPVL', blank=True, null=True)  # Field name made lowercase.
    aqp1 = models.FloatField(db_column='AQP1', blank=True, null=True)  # Field name made lowercase.
    elmo1 = models.FloatField(db_column='ELMO1', blank=True, null=True)  # Field name made lowercase.
    igfbp3 = models.FloatField(db_column='IGFBP3', blank=True, null=True)  # Field name made lowercase.
    egfr = models.FloatField(db_column='EGFR', blank=True, null=True)  # Field name made lowercase.
    eln = models.FloatField(db_column='ELN', blank=True, null=True)  # Field name made lowercase.
    ncf1 = models.FloatField(db_column='NCF1', blank=True, null=True)  # Field name made lowercase.
    hspb1 = models.FloatField(db_column='HSPB1', blank=True, null=True)  # Field name made lowercase.
    sema3a = models.FloatField(db_column='SEMA3A', blank=True, null=True)  # Field name made lowercase.
    pon3 = models.FloatField(db_column='PON3', blank=True, null=True)  # Field name made lowercase.
    pon2 = models.FloatField(db_column='PON2', blank=True, null=True)  # Field name made lowercase.
    nampt = models.FloatField(db_column='NAMPT', blank=True, null=True)  # Field name made lowercase.
    cav1 = models.FloatField(db_column='CAV1', blank=True, null=True)  # Field name made lowercase.
    lep = models.FloatField(db_column='LEP', blank=True, null=True)  # Field name made lowercase.
    akr1b1 = models.FloatField(db_column='AKR1B1', blank=True, null=True)  # Field name made lowercase.
    akr1b10 = models.FloatField(db_column='AKR1B10', blank=True, null=True)  # Field name made lowercase.
    pip = models.FloatField(db_column='PIP', blank=True, null=True)  # Field name made lowercase.
    rarres2 = models.FloatField(db_column='RARRES2', blank=True, null=True)  # Field name made lowercase.
    nos3 = models.FloatField(db_column='NOS3', blank=True, null=True)  # Field name made lowercase.
    angpt2 = models.FloatField(db_column='ANGPT2', blank=True, null=True)  # Field name made lowercase.
    defa1 = models.FloatField(db_column='DEFA1', blank=True, null=True)  # Field name made lowercase.
    lpl = models.FloatField(db_column='LPL', blank=True, null=True)  # Field name made lowercase.
    ebf2 = models.FloatField(db_column='EBF2', blank=True, null=True)  # Field name made lowercase.
    adrb3 = models.FloatField(db_column='ADRB3', blank=True, null=True)  # Field name made lowercase.
    eif4ebp1 = models.FloatField(db_column='EIF4EBP1', blank=True, null=True)  # Field name made lowercase.
    fgfr1 = models.FloatField(db_column='FGFR1', blank=True, null=True)  # Field name made lowercase.
    crh = models.FloatField(db_column='CRH', blank=True, null=True)  # Field name made lowercase.
    sgk3 = models.FloatField(db_column='SGK3', blank=True, null=True)  # Field name made lowercase.
    fabp5 = models.FloatField(db_column='FABP5', blank=True, null=True)  # Field name made lowercase.
    fabp4 = models.FloatField(db_column='FABP4', blank=True, null=True)  # Field name made lowercase.
    mmp16 = models.FloatField(db_column='MMP16', blank=True, null=True)  # Field name made lowercase.
    ncald = models.FloatField(db_column='NCALD', blank=True, null=True)  # Field name made lowercase.
    klf10 = models.FloatField(db_column='KLF10', blank=True, null=True)  # Field name made lowercase.
    enpp2 = models.FloatField(db_column='ENPP2', blank=True, null=True)  # Field name made lowercase.
    pvt1 = models.FloatField(db_column='PVT1', blank=True, null=True)  # Field name made lowercase.
    jak2 = models.FloatField(db_column='JAK2', blank=True, null=True)  # Field name made lowercase.
    psip1 = models.FloatField(db_column='PSIP1', blank=True, null=True)  # Field name made lowercase.
    plin2 = models.FloatField(db_column='PLIN2', blank=True, null=True)  # Field name made lowercase.
    rps6 = models.FloatField(db_column='RPS6', blank=True, null=True)  # Field name made lowercase.
    aldh1a1 = models.FloatField(db_column='ALDH1A1', blank=True, null=True)  # Field name made lowercase.
    frmd3 = models.FloatField(db_column='FRMD3', blank=True, null=True)  # Field name made lowercase.
    gas1 = models.FloatField(db_column='GAS1', blank=True, null=True)  # Field name made lowercase.
    baat = models.FloatField(db_column='BAAT', blank=True, null=True)  # Field name made lowercase.
    abca1 = models.FloatField(db_column='ABCA1', blank=True, null=True)  # Field name made lowercase.
    txn = models.FloatField(db_column='TXN', blank=True, null=True)  # Field name made lowercase.
    ambp = models.FloatField(db_column='AMBP', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    hspa5 = models.FloatField(db_column='HSPA5', blank=True, null=True)  # Field name made lowercase.
    angptl2 = models.FloatField(db_column='ANGPTL2', blank=True, null=True)  # Field name made lowercase.
    ptges = models.FloatField(db_column='PTGES', blank=True, null=True)  # Field name made lowercase.
    tsc1 = models.FloatField(db_column='TSC1', blank=True, null=True)  # Field name made lowercase.
    abo = models.FloatField(db_column='ABO', blank=True, null=True)  # Field name made lowercase.
    adamts13 = models.FloatField(db_column='ADAMTS13', blank=True, null=True)  # Field name made lowercase.
    ptgds = models.FloatField(db_column='PTGDS', blank=True, null=True)  # Field name made lowercase.
    klf6 = models.FloatField(db_column='KLF6', blank=True, null=True)  # Field name made lowercase.
    cdc123 = models.FloatField(db_column='CDC123', blank=True, null=True)  # Field name made lowercase.
    bambi = models.FloatField(db_column='BAMBI', blank=True, null=True)  # Field name made lowercase.
    cxcl12 = models.FloatField(db_column='CXCL12', blank=True, null=True)  # Field name made lowercase.
    mbl2 = models.FloatField(db_column='MBL2', blank=True, null=True)  # Field name made lowercase.
    tfam = models.FloatField(db_column='TFAM', blank=True, null=True)  # Field name made lowercase.
    sirt1 = models.FloatField(db_column='SIRT1', blank=True, null=True)  # Field name made lowercase.
    srgn = models.FloatField(db_column='SRGN', blank=True, null=True)  # Field name made lowercase.
    unc5b = models.FloatField(db_column='UNC5B', blank=True, null=True)  # Field name made lowercase.
    adk = models.FloatField(db_column='ADK', blank=True, null=True)  # Field name made lowercase.
    pten = models.FloatField(db_column='PTEN', blank=True, null=True)  # Field name made lowercase.
    rbp4 = models.FloatField(db_column='RBP4', blank=True, null=True)  # Field name made lowercase.
    cyp2c19 = models.FloatField(db_column='CYP2C19', blank=True, null=True)  # Field name made lowercase.
    entpd1 = models.FloatField(db_column='ENTPD1', blank=True, null=True)  # Field name made lowercase.
    tcf7l2 = models.FloatField(db_column='TCF7L2', blank=True, null=True)  # Field name made lowercase.
    bnip3 = models.FloatField(db_column='BNIP3', blank=True, null=True)  # Field name made lowercase.
    igf2 = models.FloatField(db_column='IGF2', blank=True, null=True)  # Field name made lowercase.
    ins = models.FloatField(db_column='INS', blank=True, null=True)  # Field name made lowercase.
    th = models.FloatField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    kcnq1 = models.FloatField(db_column='KCNQ1', blank=True, null=True)  # Field name made lowercase.
    hbg2 = models.FloatField(db_column='HBG2', blank=True, null=True)  # Field name made lowercase.
    smpd1 = models.FloatField(db_column='SMPD1', blank=True, null=True)  # Field name made lowercase.
    ilk = models.FloatField(db_column='ILK', blank=True, null=True)  # Field name made lowercase.
    adm = models.FloatField(db_column='ADM', blank=True, null=True)  # Field name made lowercase.
    pth = models.FloatField(db_column='PTH', blank=True, null=True)  # Field name made lowercase.
    nucb2 = models.FloatField(db_column='NUCB2', blank=True, null=True)  # Field name made lowercase.
    kcnj11 = models.FloatField(db_column='KCNJ11', blank=True, null=True)  # Field name made lowercase.
    saa1 = models.FloatField(db_column='SAA1', blank=True, null=True)  # Field name made lowercase.
    bdnf = models.FloatField(db_column='BDNF', blank=True, null=True)  # Field name made lowercase.
    wt1 = models.FloatField(db_column='WT1', blank=True, null=True)  # Field name made lowercase.
    cd59 = models.FloatField(db_column='CD59', blank=True, null=True)  # Field name made lowercase.
    pdhx = models.FloatField(db_column='PDHX', blank=True, null=True)  # Field name made lowercase.
    traf6 = models.FloatField(db_column='TRAF6', blank=True, null=True)  # Field name made lowercase.
    api5 = models.FloatField(db_column='API5', blank=True, null=True)  # Field name made lowercase.
    nr1h3 = models.FloatField(db_column='NR1H3', blank=True, null=True)  # Field name made lowercase.
    ndufs3 = models.FloatField(db_column='NDUFS3', blank=True, null=True)  # Field name made lowercase.
    folh1 = models.FloatField(db_column='FOLH1', blank=True, null=True)  # Field name made lowercase.
    aplnr = models.FloatField(db_column='APLNR', blank=True, null=True)  # Field name made lowercase.
    p2rx3 = models.FloatField(db_column='P2RX3', blank=True, null=True)  # Field name made lowercase.
    cntf = models.FloatField(db_column='CNTF', blank=True, null=True)  # Field name made lowercase.
    fads1 = models.FloatField(db_column='FADS1', blank=True, null=True)  # Field name made lowercase.
    fads2 = models.FloatField(db_column='FADS2', blank=True, null=True)  # Field name made lowercase.
    fkbp2 = models.FloatField(db_column='FKBP2', blank=True, null=True)  # Field name made lowercase.
    syvn1 = models.FloatField(db_column='SYVN1', blank=True, null=True)  # Field name made lowercase.
    pc = models.FloatField(db_column='PC', blank=True, null=True)  # Field name made lowercase.
    dhcr7 = models.FloatField(db_column='DHCR7', blank=True, null=True)  # Field name made lowercase.
    prcp = models.FloatField(db_column='PRCP', blank=True, null=True)  # Field name made lowercase.
    nox4 = models.FloatField(db_column='NOX4', blank=True, null=True)  # Field name made lowercase.
    pdgfd = models.FloatField(db_column='PDGFD', blank=True, null=True)  # Field name made lowercase.
    atm = models.FloatField(db_column='ATM', blank=True, null=True)  # Field name made lowercase.
    il18 = models.FloatField(db_column='IL18', blank=True, null=True)  # Field name made lowercase.
    apoa1 = models.FloatField(db_column='APOA1', blank=True, null=True)  # Field name made lowercase.
    hyou1 = models.FloatField(db_column='HYOU1', blank=True, null=True)  # Field name made lowercase.
    esam = models.FloatField(db_column='ESAM', blank=True, null=True)  # Field name made lowercase.
    fkbp4 = models.FloatField(db_column='FKBP4', blank=True, null=True)  # Field name made lowercase.
    fgf23 = models.FloatField(db_column='FGF23', blank=True, null=True)  # Field name made lowercase.
    ntf3 = models.FloatField(db_column='NTF3', blank=True, null=True)  # Field name made lowercase.
    vwf = models.FloatField(db_column='VWF', blank=True, null=True)  # Field name made lowercase.
    cd9 = models.FloatField(db_column='CD9', blank=True, null=True)  # Field name made lowercase.
    gapdh = models.FloatField(db_column='GAPDH', blank=True, null=True)  # Field name made lowercase.
    cd4 = models.FloatField(db_column='CD4', blank=True, null=True)  # Field name made lowercase.
    gnb3 = models.FloatField(db_column='GNB3', blank=True, null=True)  # Field name made lowercase.
    cd163 = models.FloatField(db_column='CD163', blank=True, null=True)  # Field name made lowercase.
    slc2a3 = models.FloatField(db_column='SLC2A3', blank=True, null=True)  # Field name made lowercase.
    cd69 = models.FloatField(db_column='CD69', blank=True, null=True)  # Field name made lowercase.
    irak4 = models.FloatField(db_column='IRAK4', blank=True, null=True)  # Field name made lowercase.
    vdr = models.FloatField(db_column='VDR', blank=True, null=True)  # Field name made lowercase.
    aqp5 = models.FloatField(db_column='AQP5', blank=True, null=True)  # Field name made lowercase.
    acvrl1 = models.FloatField(db_column='ACVRL1', blank=True, null=True)  # Field name made lowercase.
    nfe2 = models.FloatField(db_column='NFE2', blank=True, null=True)  # Field name made lowercase.
    cd63 = models.FloatField(db_column='CD63', blank=True, null=True)  # Field name made lowercase.
    erbb3 = models.FloatField(db_column='ERBB3', blank=True, null=True)  # Field name made lowercase.
    ddit3 = models.FloatField(db_column='DDIT3', blank=True, null=True)  # Field name made lowercase.
    ifng = models.FloatField(db_column='IFNG', blank=True, null=True)  # Field name made lowercase.
    nts = models.FloatField(db_column='NTS', blank=True, null=True)  # Field name made lowercase.
    igf1 = models.FloatField(db_column='IGF1', blank=True, null=True)  # Field name made lowercase.
    acacb = models.FloatField(db_column='ACACB', blank=True, null=True)  # Field name made lowercase.
    trpv4 = models.FloatField(db_column='TRPV4', blank=True, null=True)  # Field name made lowercase.
    atp2a2 = models.FloatField(db_column='ATP2A2', blank=True, null=True)  # Field name made lowercase.
    aldh2 = models.FloatField(db_column='ALDH2', blank=True, null=True)  # Field name made lowercase.
    nos1 = models.FloatField(db_column='NOS1', blank=True, null=True)  # Field name made lowercase.
    pebp1 = models.FloatField(db_column='PEBP1', blank=True, null=True)  # Field name made lowercase.
    psmd9 = models.FloatField(db_column='PSMD9', blank=True, null=True)  # Field name made lowercase.
    scarb1 = models.FloatField(db_column='SCARB1', blank=True, null=True)  # Field name made lowercase.
    p2rx2 = models.FloatField(db_column='P2RX2', blank=True, null=True)  # Field name made lowercase.
    alox5ap = models.FloatField(db_column='ALOX5AP', blank=True, null=True)  # Field name made lowercase.
    kl = models.FloatField(db_column='KL', blank=True, null=True)  # Field name made lowercase.
    postn = models.FloatField(db_column='POSTN', blank=True, null=True)  # Field name made lowercase.
    foxo1 = models.FloatField(db_column='FOXO1', blank=True, null=True)  # Field name made lowercase.
    htr2a = models.FloatField(db_column='HTR2A', blank=True, null=True)  # Field name made lowercase.
    gpc5 = models.FloatField(db_column='GPC5', blank=True, null=True)  # Field name made lowercase.
    irs2 = models.FloatField(db_column='IRS2', blank=True, null=True)  # Field name made lowercase.
    gas6 = models.FloatField(db_column='GAS6', blank=True, null=True)  # Field name made lowercase.
    ang = models.FloatField(db_column='ANG', blank=True, null=True)  # Field name made lowercase.
    mmp14 = models.FloatField(db_column='MMP14', blank=True, null=True)  # Field name made lowercase.
    ltb4r2 = models.FloatField(db_column='LTB4R2', blank=True, null=True)  # Field name made lowercase.
    nfkbia = models.FloatField(db_column='NFKBIA', blank=True, null=True)  # Field name made lowercase.
    bmp4 = models.FloatField(db_column='BMP4', blank=True, null=True)  # Field name made lowercase.
    rtn1 = models.FloatField(db_column='RTN1', blank=True, null=True)  # Field name made lowercase.
    pgf = models.FloatField(db_column='PGF', blank=True, null=True)  # Field name made lowercase.
    ngb = models.FloatField(db_column='NGB', blank=True, null=True)  # Field name made lowercase.
    ahsa1 = models.FloatField(db_column='AHSA1', blank=True, null=True)  # Field name made lowercase.
    bdkrb2 = models.FloatField(db_column='BDKRB2', blank=True, null=True)  # Field name made lowercase.
    bdkrb1 = models.FloatField(db_column='BDKRB1', blank=True, null=True)  # Field name made lowercase.
    akt1 = models.FloatField(db_column='AKT1', blank=True, null=True)  # Field name made lowercase.
    grem1 = models.FloatField(db_column='GREM1', blank=True, null=True)  # Field name made lowercase.
    thbs1 = models.FloatField(db_column='THBS1', blank=True, null=True)  # Field name made lowercase.
    pak6 = models.FloatField(db_column='PAK6', blank=True, null=True)  # Field name made lowercase.
    b2m = models.FloatField(db_column='B2M', blank=True, null=True)  # Field name made lowercase.
    myo5c = models.FloatField(db_column='MYO5C', blank=True, null=True)  # Field name made lowercase.
    onecut1 = models.FloatField(db_column='ONECUT1', blank=True, null=True)  # Field name made lowercase.
    adam10 = models.FloatField(db_column='ADAM10', blank=True, null=True)  # Field name made lowercase.
    ctsh = models.FloatField(db_column='CTSH', blank=True, null=True)  # Field name made lowercase.
    plin1 = models.FloatField(db_column='PLIN1', blank=True, null=True)  # Field name made lowercase.
    igf1r = models.FloatField(db_column='IGF1R', blank=True, null=True)  # Field name made lowercase.
    mrpl28 = models.FloatField(db_column='MRPL28', blank=True, null=True)  # Field name made lowercase.
    cacna1h = models.FloatField(db_column='CACNA1H', blank=True, null=True)  # Field name made lowercase.
    pdpk1 = models.FloatField(db_column='PDPK1', blank=True, null=True)  # Field name made lowercase.
    ercc4 = models.FloatField(db_column='ERCC4', blank=True, null=True)  # Field name made lowercase.
    smg1 = models.FloatField(db_column='SMG1', blank=True, null=True)  # Field name made lowercase.
    itgam = models.FloatField(db_column='ITGAM', blank=True, null=True)  # Field name made lowercase.
    fto = models.FloatField(db_column='FTO', blank=True, null=True)  # Field name made lowercase.
    mmp2 = models.FloatField(db_column='MMP2', blank=True, null=True)  # Field name made lowercase.
    slc12a3 = models.FloatField(db_column='SLC12A3', blank=True, null=True)  # Field name made lowercase.
    cetp = models.FloatField(db_column='CETP', blank=True, null=True)  # Field name made lowercase.
    cx3cl1 = models.FloatField(db_column='CX3CL1', blank=True, null=True)  # Field name made lowercase.
    cdh1 = models.FloatField(db_column='CDH1', blank=True, null=True)  # Field name made lowercase.
    nqo1 = models.FloatField(db_column='NQO1', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    znrf1 = models.FloatField(db_column='ZNRF1', blank=True, null=True)  # Field name made lowercase.
    cyba = models.FloatField(db_column='CYBA', blank=True, null=True)  # Field name made lowercase.
    tubb3 = models.FloatField(db_column='TUBB3', blank=True, null=True)  # Field name made lowercase.
    crk = models.FloatField(db_column='CRK', blank=True, null=True)  # Field name made lowercase.
    serpinf2 = models.FloatField(db_column='SERPINF2', blank=True, null=True)  # Field name made lowercase.
    serpinf1 = models.FloatField(db_column='SERPINF1', blank=True, null=True)  # Field name made lowercase.
    trpv3 = models.FloatField(db_column='TRPV3', blank=True, null=True)  # Field name made lowercase.
    cxcl16 = models.FloatField(db_column='CXCL16', blank=True, null=True)  # Field name made lowercase.
    slc2a4 = models.FloatField(db_column='SLC2A4', blank=True, null=True)  # Field name made lowercase.
    cd68 = models.FloatField(db_column='CD68', blank=True, null=True)  # Field name made lowercase.
    shbg = models.FloatField(db_column='SHBG', blank=True, null=True)  # Field name made lowercase.
    pmp22 = models.FloatField(db_column='PMP22', blank=True, null=True)  # Field name made lowercase.
    srebf1 = models.FloatField(db_column='SREBF1', blank=True, null=True)  # Field name made lowercase.
    mapk7 = models.FloatField(db_column='MAPK7', blank=True, null=True)  # Field name made lowercase.
    ccl2 = models.FloatField(db_column='CCL2', blank=True, null=True)  # Field name made lowercase.
    ccl5 = models.FloatField(db_column='CCL5', blank=True, null=True)  # Field name made lowercase.
    hnf1b = models.FloatField(db_column='HNF1B', blank=True, null=True)  # Field name made lowercase.
    erbb2 = models.FloatField(db_column='ERBB2', blank=True, null=True)  # Field name made lowercase.
    fkbp10 = models.FloatField(db_column='FKBP10', blank=True, null=True)  # Field name made lowercase.
    stat5a = models.FloatField(db_column='STAT5A', blank=True, null=True)  # Field name made lowercase.
    stat3 = models.FloatField(db_column='STAT3', blank=True, null=True)  # Field name made lowercase.
    naglu = models.FloatField(db_column='NAGLU', blank=True, null=True)  # Field name made lowercase.
    aoc2 = models.FloatField(db_column='AOC2', blank=True, null=True)  # Field name made lowercase.
    aoc3 = models.FloatField(db_column='AOC3', blank=True, null=True)  # Field name made lowercase.
    ppy = models.FloatField(db_column='PPY', blank=True, null=True)  # Field name made lowercase.
    sth = models.FloatField(db_column='STH', blank=True, null=True)  # Field name made lowercase.
    itgb3 = models.FloatField(db_column='ITGB3', blank=True, null=True)  # Field name made lowercase.
    gip = models.FloatField(db_column='GIP', blank=True, null=True)  # Field name made lowercase.
    mpo = models.FloatField(db_column='MPO', blank=True, null=True)  # Field name made lowercase.
    pecam1 = models.FloatField(db_column='PECAM1', blank=True, null=True)  # Field name made lowercase.
    sox9 = models.FloatField(db_column='SOX9', blank=True, null=True)  # Field name made lowercase.
    timp2 = models.FloatField(db_column='TIMP2', blank=True, null=True)  # Field name made lowercase.
    dcxr = models.FloatField(db_column='DCXR', blank=True, null=True)  # Field name made lowercase.
    fasn = models.FloatField(db_column='FASN', blank=True, null=True)  # Field name made lowercase.
    colec12 = models.FloatField(db_column='COLEC12', blank=True, null=True)  # Field name made lowercase.
    adcyap1 = models.FloatField(db_column='ADCYAP1', blank=True, null=True)  # Field name made lowercase.
    smad7 = models.FloatField(db_column='SMAD7', blank=True, null=True)  # Field name made lowercase.
    nedd4l = models.FloatField(db_column='NEDD4L', blank=True, null=True)  # Field name made lowercase.
    mc4r = models.FloatField(db_column='MC4R', blank=True, null=True)  # Field name made lowercase.
    bcl2 = models.FloatField(db_column='BCL2', blank=True, null=True)  # Field name made lowercase.
    cndp2 = models.FloatField(db_column='CNDP2', blank=True, null=True)  # Field name made lowercase.
    znf236 = models.FloatField(db_column='ZNF236', blank=True, null=True)  # Field name made lowercase.
    stk11 = models.FloatField(db_column='STK11', blank=True, null=True)  # Field name made lowercase.
    sirt6 = models.FloatField(db_column='SIRT6', blank=True, null=True)  # Field name made lowercase.
    uhrf1 = models.FloatField(db_column='UHRF1', blank=True, null=True)  # Field name made lowercase.
    timm44 = models.FloatField(db_column='TIMM44', blank=True, null=True)  # Field name made lowercase.
    angptl4 = models.FloatField(db_column='ANGPTL4', blank=True, null=True)  # Field name made lowercase.
    dnmt1 = models.FloatField(db_column='DNMT1', blank=True, null=True)  # Field name made lowercase.
    icam1 = models.FloatField(db_column='ICAM1', blank=True, null=True)  # Field name made lowercase.
    ldlr = models.FloatField(db_column='LDLR', blank=True, null=True)  # Field name made lowercase.
    epor = models.FloatField(db_column='EPOR', blank=True, null=True)  # Field name made lowercase.
    prdx2 = models.FloatField(db_column='PRDX2', blank=True, null=True)  # Field name made lowercase.
    ptger1 = models.FloatField(db_column='PTGER1', blank=True, null=True)  # Field name made lowercase.
    unc13a = models.FloatField(db_column='UNC13A', blank=True, null=True)  # Field name made lowercase.
    gdf15 = models.FloatField(db_column='GDF15', blank=True, null=True)  # Field name made lowercase.
    fkbp8 = models.FloatField(db_column='FKBP8', blank=True, null=True)  # Field name made lowercase.
    usf2 = models.FloatField(db_column='USF2', blank=True, null=True)  # Field name made lowercase.
    ffar1 = models.FloatField(db_column='FFAR1', blank=True, null=True)  # Field name made lowercase.
    ffar2 = models.FloatField(db_column='FFAR2', blank=True, null=True)  # Field name made lowercase.
    nphs1 = models.FloatField(db_column='NPHS1', blank=True, null=True)  # Field name made lowercase.
    tgfb1 = models.FloatField(db_column='TGFB1', blank=True, null=True)  # Field name made lowercase.
    xrcc1 = models.FloatField(db_column='XRCC1', blank=True, null=True)  # Field name made lowercase.
    ercc1 = models.FloatField(db_column='ERCC1', blank=True, null=True)  # Field name made lowercase.
    gipr = models.FloatField(db_column='GIPR', blank=True, null=True)  # Field name made lowercase.
    fgf21 = models.FloatField(db_column='FGF21', blank=True, null=True)  # Field name made lowercase.
    clec11a = models.FloatField(db_column='CLEC11A', blank=True, null=True)  # Field name made lowercase.
    fpr1 = models.FloatField(db_column='FPR1', blank=True, null=True)  # Field name made lowercase.
    trib3 = models.FloatField(db_column='TRIB3', blank=True, null=True)  # Field name made lowercase.
    bmp2 = models.FloatField(db_column='BMP2', blank=True, null=True)  # Field name made lowercase.
    thbd = models.FloatField(db_column='THBD', blank=True, null=True)  # Field name made lowercase.
    cst3 = models.FloatField(db_column='CST3', blank=True, null=True)  # Field name made lowercase.
    id1 = models.FloatField(db_column='ID1', blank=True, null=True)  # Field name made lowercase.
    src = models.FloatField(db_column='SRC', blank=True, null=True)  # Field name made lowercase.
    mafb = models.FloatField(db_column='MAFB', blank=True, null=True)  # Field name made lowercase.
    sgk2 = models.FloatField(db_column='SGK2', blank=True, null=True)  # Field name made lowercase.
    hnf4a = models.FloatField(db_column='HNF4A', blank=True, null=True)  # Field name made lowercase.
    pltp = models.FloatField(db_column='PLTP', blank=True, null=True)  # Field name made lowercase.
    mmp9 = models.FloatField(db_column='MMP9', blank=True, null=True)  # Field name made lowercase.
    cd40 = models.FloatField(db_column='CD40', blank=True, null=True)  # Field name made lowercase.
    ptpn1 = models.FloatField(db_column='PTPN1', blank=True, null=True)  # Field name made lowercase.
    cyp24a1 = models.FloatField(db_column='CYP24A1', blank=True, null=True)  # Field name made lowercase.
    rcan1 = models.FloatField(db_column='RCAN1', blank=True, null=True)  # Field name made lowercase.
    abcg1 = models.FloatField(db_column='ABCG1', blank=True, null=True)  # Field name made lowercase.
    prmt2 = models.FloatField(db_column='PRMT2', blank=True, null=True)  # Field name made lowercase.
    comt = models.FloatField(db_column='COMT', blank=True, null=True)  # Field name made lowercase.
    mapk1 = models.FloatField(db_column='MAPK1', blank=True, null=True)  # Field name made lowercase.
    mif = models.FloatField(db_column='MIF', blank=True, null=True)  # Field name made lowercase.
    ggt1 = models.FloatField(db_column='GGT1', blank=True, null=True)  # Field name made lowercase.
    xbp1 = models.FloatField(db_column='XBP1', blank=True, null=True)  # Field name made lowercase.
    osm = models.FloatField(db_column='OSM', blank=True, null=True)  # Field name made lowercase.
    limk2 = models.FloatField(db_column='LIMK2', blank=True, null=True)  # Field name made lowercase.
    sfi1 = models.FloatField(db_column='SFI1', blank=True, null=True)  # Field name made lowercase.
    timp3 = models.FloatField(db_column='TIMP3', blank=True, null=True)  # Field name made lowercase.
    hmox1 = models.FloatField(db_column='HMOX1', blank=True, null=True)  # Field name made lowercase.
    apol1 = models.FloatField(db_column='APOL1', blank=True, null=True)  # Field name made lowercase.
    myh9 = models.FloatField(db_column='MYH9', blank=True, null=True)  # Field name made lowercase.
    pdgfb = models.FloatField(db_column='PDGFB', blank=True, null=True)  # Field name made lowercase.
    atf4 = models.FloatField(db_column='ATF4', blank=True, null=True)  # Field name made lowercase.
    tspo = models.FloatField(db_column='TSPO', blank=True, null=True)  # Field name made lowercase.
    miox = models.FloatField(db_column='MIOX', blank=True, null=True)  # Field name made lowercase.
    prdx4 = models.FloatField(db_column='PRDX4', blank=True, null=True)  # Field name made lowercase.
    gk = models.FloatField(db_column='GK', blank=True, null=True)  # Field name made lowercase.
    rgn = models.FloatField(db_column='RGN', blank=True, null=True)  # Field name made lowercase.
    timp1 = models.FloatField(db_column='TIMP1', blank=True, null=True)  # Field name made lowercase.
    clcn5 = models.FloatField(db_column='CLCN5', blank=True, null=True)  # Field name made lowercase.
    ar = models.FloatField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    foxo4 = models.FloatField(db_column='FOXO4', blank=True, null=True)  # Field name made lowercase.
    rps6ka6 = models.FloatField(db_column='RPS6KA6', blank=True, null=True)  # Field name made lowercase.
    nox1 = models.FloatField(db_column='NOX1', blank=True, null=True)  # Field name made lowercase.
    xiap = models.FloatField(db_column='XIAP', blank=True, null=True)  # Field name made lowercase.
    cd40lg = models.FloatField(db_column='CD40LG', blank=True, null=True)  # Field name made lowercase.
    l1cam = models.FloatField(db_column='L1CAM', blank=True, null=True)  # Field name made lowercase.
    irak1 = models.FloatField(db_column='IRAK1', blank=True, null=True)  # Field name made lowercase.
    g6pd = models.FloatField(db_column='G6PD', blank=True, null=True)  # Field name made lowercase.
    f8 = models.FloatField(db_column='F8', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diaco_tissue_brain_cerebellum'


class DiacoTissueBrainCortex(models.Model):
    subjid = models.CharField(db_column='SUBJID', max_length=50, primary_key=True)  # Field name made lowercase.
    sampid = models.CharField(db_column='SAMPID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sesso = models.CharField(db_column='Sesso', max_length=1)  # Field name made lowercase.
    eta = models.CharField(db_column='Età', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errfi1 = models.FloatField(db_column='ERRFI1', blank=True, null=True)  # Field name made lowercase.
    mad2l2 = models.FloatField(db_column='MAD2L2', blank=True, null=True)  # Field name made lowercase.
    mthfr = models.FloatField(db_column='MTHFR', blank=True, null=True)  # Field name made lowercase.
    nppa = models.FloatField(db_column='NPPA', blank=True, null=True)  # Field name made lowercase.
    tnfrsf1b = models.FloatField(db_column='TNFRSF1B', blank=True, null=True)  # Field name made lowercase.
    pla2g2a = models.FloatField(db_column='PLA2G2A', blank=True, null=True)  # Field name made lowercase.
    alpl = models.FloatField(db_column='ALPL', blank=True, null=True)  # Field name made lowercase.
    hspg2 = models.FloatField(db_column='HSPG2', blank=True, null=True)  # Field name made lowercase.
    cnr2 = models.FloatField(db_column='CNR2', blank=True, null=True)  # Field name made lowercase.
    slc9a1 = models.FloatField(db_column='SLC9A1', blank=True, null=True)  # Field name made lowercase.
    col8a2 = models.FloatField(db_column='COL8A2', blank=True, null=True)  # Field name made lowercase.
    cap1 = models.FloatField(db_column='CAP1', blank=True, null=True)  # Field name made lowercase.
    slc2a1 = models.FloatField(db_column='SLC2A1', blank=True, null=True)  # Field name made lowercase.
    cyp2j2 = models.FloatField(db_column='CYP2J2', blank=True, null=True)  # Field name made lowercase.
    ddah1 = models.FloatField(db_column='DDAH1', blank=True, null=True)  # Field name made lowercase.
    cyr61 = models.FloatField(db_column='CYR61', blank=True, null=True)  # Field name made lowercase.
    ngf = models.FloatField(db_column='NGF', blank=True, null=True)  # Field name made lowercase.
    hmgcs2 = models.FloatField(db_column='HMGCS2', blank=True, null=True)  # Field name made lowercase.
    ctss = models.FloatField(db_column='CTSS', blank=True, null=True)  # Field name made lowercase.
    s100a12 = models.FloatField(db_column='S100A12', blank=True, null=True)  # Field name made lowercase.
    lmna = models.FloatField(db_column='LMNA', blank=True, null=True)  # Field name made lowercase.
    cd247 = models.FloatField(db_column='CD247', blank=True, null=True)  # Field name made lowercase.
    sele = models.FloatField(db_column='SELE', blank=True, null=True)  # Field name made lowercase.
    fmo3 = models.FloatField(db_column='FMO3', blank=True, null=True)  # Field name made lowercase.
    prdx6 = models.FloatField(db_column='PRDX6', blank=True, null=True)  # Field name made lowercase.
    glul = models.FloatField(db_column='GLUL', blank=True, null=True)  # Field name made lowercase.
    lamc1 = models.FloatField(db_column='LAMC1', blank=True, null=True)  # Field name made lowercase.
    ptgs2 = models.FloatField(db_column='PTGS2', blank=True, null=True)  # Field name made lowercase.
    chi3l1 = models.FloatField(db_column='CHI3L1', blank=True, null=True)  # Field name made lowercase.
    chit1 = models.FloatField(db_column='CHIT1', blank=True, null=True)  # Field name made lowercase.
    fmod = models.FloatField(db_column='FMOD', blank=True, null=True)  # Field name made lowercase.
    il10 = models.FloatField(db_column='IL10', blank=True, null=True)  # Field name made lowercase.
    pfkfb2 = models.FloatField(db_column='PFKFB2', blank=True, null=True)  # Field name made lowercase.
    cd34 = models.FloatField(db_column='CD34', blank=True, null=True)  # Field name made lowercase.
    cog2 = models.FloatField(db_column='COG2', blank=True, null=True)  # Field name made lowercase.
    nlrp3 = models.FloatField(db_column='NLRP3', blank=True, null=True)  # Field name made lowercase.
    rock2 = models.FloatField(db_column='ROCK2', blank=True, null=True)  # Field name made lowercase.
    apob = models.FloatField(db_column='APOB', blank=True, null=True)  # Field name made lowercase.
    pomc = models.FloatField(db_column='POMC', blank=True, null=True)  # Field name made lowercase.
    gckr = models.FloatField(db_column='GCKR', blank=True, null=True)  # Field name made lowercase.
    plekhh2 = models.FloatField(db_column='PLEKHH2', blank=True, null=True)  # Field name made lowercase.
    prkce = models.FloatField(db_column='PRKCE', blank=True, null=True)  # Field name made lowercase.
    pigf = models.FloatField(db_column='PIGF', blank=True, null=True)  # Field name made lowercase.
    msh2 = models.FloatField(db_column='MSH2', blank=True, null=True)  # Field name made lowercase.
    gfpt1 = models.FloatField(db_column='GFPT1', blank=True, null=True)  # Field name made lowercase.
    tacr1 = models.FloatField(db_column='TACR1', blank=True, null=True)  # Field name made lowercase.
    reg1a = models.FloatField(db_column='REG1A', blank=True, null=True)  # Field name made lowercase.
    eif2ak3 = models.FloatField(db_column='EIF2AK3', blank=True, null=True)  # Field name made lowercase.
    adra2b = models.FloatField(db_column='ADRA2B', blank=True, null=True)  # Field name made lowercase.
    il1b = models.FloatField(db_column='IL1B', blank=True, null=True)  # Field name made lowercase.
    proc = models.FloatField(db_column='PROC', blank=True, null=True)  # Field name made lowercase.
    polr2d = models.FloatField(db_column='POLR2D', blank=True, null=True)  # Field name made lowercase.
    zeb2 = models.FloatField(db_column='ZEB2', blank=True, null=True)  # Field name made lowercase.
    acvr1c = models.FloatField(db_column='ACVR1C', blank=True, null=True)  # Field name made lowercase.
    dpp4 = models.FloatField(db_column='DPP4', blank=True, null=True)  # Field name made lowercase.
    nfe2l2 = models.FloatField(db_column='NFE2L2', blank=True, null=True)  # Field name made lowercase.
    igfbp5 = models.FloatField(db_column='IGFBP5', blank=True, null=True)  # Field name made lowercase.
    ccl20 = models.FloatField(db_column='CCL20', blank=True, null=True)  # Field name made lowercase.
    hdac4 = models.FloatField(db_column='HDAC4', blank=True, null=True)  # Field name made lowercase.
    capn10 = models.FloatField(db_column='CAPN10', blank=True, null=True)  # Field name made lowercase.
    ghrl = models.FloatField(db_column='GHRL', blank=True, null=True)  # Field name made lowercase.
    pparg = models.FloatField(db_column='PPARG', blank=True, null=True)  # Field name made lowercase.
    raf1 = models.FloatField(db_column='RAF1', blank=True, null=True)  # Field name made lowercase.
    myd88 = models.FloatField(db_column='MYD88', blank=True, null=True)  # Field name made lowercase.
    cx3cr1 = models.FloatField(db_column='CX3CR1', blank=True, null=True)  # Field name made lowercase.
    cck = models.FloatField(db_column='CCK', blank=True, null=True)  # Field name made lowercase.
    exosc7 = models.FloatField(db_column='EXOSC7', blank=True, null=True)  # Field name made lowercase.
    ccr1 = models.FloatField(db_column='CCR1', blank=True, null=True)  # Field name made lowercase.
    ccr5 = models.FloatField(db_column='CCR5', blank=True, null=True)  # Field name made lowercase.
    gpx1 = models.FloatField(db_column='GPX1', blank=True, null=True)  # Field name made lowercase.
    rhoa = models.FloatField(db_column='RHOA', blank=True, null=True)  # Field name made lowercase.
    cish = models.FloatField(db_column='CISH', blank=True, null=True)  # Field name made lowercase.
    tkt = models.FloatField(db_column='TKT', blank=True, null=True)  # Field name made lowercase.
    appl1 = models.FloatField(db_column='APPL1', blank=True, null=True)  # Field name made lowercase.
    slmap = models.FloatField(db_column='SLMAP', blank=True, null=True)  # Field name made lowercase.
    col8a1 = models.FloatField(db_column='COL8A1', blank=True, null=True)  # Field name made lowercase.
    cd47 = models.FloatField(db_column='CD47', blank=True, null=True)  # Field name made lowercase.
    gap43 = models.FloatField(db_column='GAP43', blank=True, null=True)  # Field name made lowercase.
    cd80 = models.FloatField(db_column='CD80', blank=True, null=True)  # Field name made lowercase.
    rho = models.FloatField(db_column='RHO', blank=True, null=True)  # Field name made lowercase.
    trh = models.FloatField(db_column='TRH', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='TF', blank=True, null=True)  # Field name made lowercase.
    rbp1 = models.FloatField(db_column='RBP1', blank=True, null=True)  # Field name made lowercase.
    trpc1 = models.FloatField(db_column='TRPC1', blank=True, null=True)  # Field name made lowercase.
    agtr1 = models.FloatField(db_column='AGTR1', blank=True, null=True)  # Field name made lowercase.
    sucnr1 = models.FloatField(db_column='SUCNR1', blank=True, null=True)  # Field name made lowercase.
    p2ry1 = models.FloatField(db_column='P2RY1', blank=True, null=True)  # Field name made lowercase.
    mme = models.FloatField(db_column='MME', blank=True, null=True)  # Field name made lowercase.
    slc2a2 = models.FloatField(db_column='SLC2A2', blank=True, null=True)  # Field name made lowercase.
    pik3ca = models.FloatField(db_column='PIK3CA', blank=True, null=True)  # Field name made lowercase.
    parl = models.FloatField(db_column='PARL', blank=True, null=True)  # Field name made lowercase.
    ahsg = models.FloatField(db_column='AHSG', blank=True, null=True)  # Field name made lowercase.
    adipoq = models.FloatField(db_column='ADIPOQ', blank=True, null=True)  # Field name made lowercase.
    spon2 = models.FloatField(db_column='SPON2', blank=True, null=True)  # Field name made lowercase.
    wfs1 = models.FloatField(db_column='WFS1', blank=True, null=True)  # Field name made lowercase.
    cd38 = models.FloatField(db_column='CD38', blank=True, null=True)  # Field name made lowercase.
    prom1 = models.FloatField(db_column='PROM1', blank=True, null=True)  # Field name made lowercase.
    ppargc1a = models.FloatField(db_column='PPARGC1A', blank=True, null=True)  # Field name made lowercase.
    igfbp7 = models.FloatField(db_column='IGFBP7', blank=True, null=True)  # Field name made lowercase.
    cxcl5 = models.FloatField(db_column='CXCL5', blank=True, null=True)  # Field name made lowercase.
    cxcl9 = models.FloatField(db_column='CXCL9', blank=True, null=True)  # Field name made lowercase.
    cxcl10 = models.FloatField(db_column='CXCL10', blank=True, null=True)  # Field name made lowercase.
    cxcl11 = models.FloatField(db_column='CXCL11', blank=True, null=True)  # Field name made lowercase.
    hpse = models.FloatField(db_column='HPSE', blank=True, null=True)  # Field name made lowercase.
    spp1 = models.FloatField(db_column='SPP1', blank=True, null=True)  # Field name made lowercase.
    adh1b = models.FloatField(db_column='ADH1B', blank=True, null=True)  # Field name made lowercase.
    egf = models.FloatField(db_column='EGF', blank=True, null=True)  # Field name made lowercase.
    alpk1 = models.FloatField(db_column='ALPK1', blank=True, null=True)  # Field name made lowercase.
    fabp2 = models.FloatField(db_column='FABP2', blank=True, null=True)  # Field name made lowercase.
    pde5a = models.FloatField(db_column='PDE5A', blank=True, null=True)  # Field name made lowercase.
    setd7 = models.FloatField(db_column='SETD7', blank=True, null=True)  # Field name made lowercase.
    smad1 = models.FloatField(db_column='SMAD1', blank=True, null=True)  # Field name made lowercase.
    ednra = models.FloatField(db_column='EDNRA', blank=True, null=True)  # Field name made lowercase.
    nr3c2 = models.FloatField(db_column='NR3C2', blank=True, null=True)  # Field name made lowercase.
    tlr2 = models.FloatField(db_column='TLR2', blank=True, null=True)  # Field name made lowercase.
    npy5r = models.FloatField(db_column='NPY5R', blank=True, null=True)  # Field name made lowercase.
    fbxo8 = models.FloatField(db_column='FBXO8', blank=True, null=True)  # Field name made lowercase.
    vegfc = models.FloatField(db_column='VEGFC', blank=True, null=True)  # Field name made lowercase.
    acsl1 = models.FloatField(db_column='ACSL1', blank=True, null=True)  # Field name made lowercase.
    sorbs2 = models.FloatField(db_column='SORBS2', blank=True, null=True)  # Field name made lowercase.
    f11 = models.FloatField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    basp1 = models.FloatField(db_column='BASP1', blank=True, null=True)  # Field name made lowercase.
    ptger4 = models.FloatField(db_column='PTGER4', blank=True, null=True)  # Field name made lowercase.
    prkaa1 = models.FloatField(db_column='PRKAA1', blank=True, null=True)  # Field name made lowercase.
    ghr = models.FloatField(db_column='GHR', blank=True, null=True)  # Field name made lowercase.
    itga2 = models.FloatField(db_column='ITGA2', blank=True, null=True)  # Field name made lowercase.
    cdk7 = models.FloatField(db_column='CDK7', blank=True, null=True)  # Field name made lowercase.
    f2r = models.FloatField(db_column='F2R', blank=True, null=True)  # Field name made lowercase.
    erap2 = models.FloatField(db_column='ERAP2', blank=True, null=True)  # Field name made lowercase.
    apc = models.FloatField(db_column='APC', blank=True, null=True)  # Field name made lowercase.
    tnfaip8 = models.FloatField(db_column='TNFAIP8', blank=True, null=True)  # Field name made lowercase.
    vdac1 = models.FloatField(db_column='VDAC1', blank=True, null=True)  # Field name made lowercase.
    pdgfrb = models.FloatField(db_column='PDGFRB', blank=True, null=True)  # Field name made lowercase.
    cd74 = models.FloatField(db_column='CD74', blank=True, null=True)  # Field name made lowercase.
    sparc = models.FloatField(db_column='SPARC', blank=True, null=True)  # Field name made lowercase.
    ebf1 = models.FloatField(db_column='EBF1', blank=True, null=True)  # Field name made lowercase.
    gfpt2 = models.FloatField(db_column='GFPT2', blank=True, null=True)  # Field name made lowercase.
    rreb1 = models.FloatField(db_column='RREB1', blank=True, null=True)  # Field name made lowercase.
    edn1 = models.FloatField(db_column='EDN1', blank=True, null=True)  # Field name made lowercase.
    cdkal1 = models.FloatField(db_column='CDKAL1', blank=True, null=True)  # Field name made lowercase.
    hfe = models.FloatField(db_column='HFE', blank=True, null=True)  # Field name made lowercase.
    hla_a = models.FloatField(db_column='HLA-A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  # Field name made lowercase.
    tnf = models.FloatField(db_column='TNF', blank=True, null=True)  # Field name made lowercase.
    hspa1a = models.FloatField(db_column='HSPA1A', blank=True, null=True)  # Field name made lowercase.
    hspa1b = models.FloatField(db_column='HSPA1B', blank=True, null=True)  # Field name made lowercase.
    hla_dqa1 = models.FloatField(db_column='HLA-DQA1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mapk14 = models.FloatField(db_column='MAPK14', blank=True, null=True)  # Field name made lowercase.
    cdkn1a = models.FloatField(db_column='CDKN1A', blank=True, null=True)  # Field name made lowercase.
    glo1 = models.FloatField(db_column='GLO1', blank=True, null=True)  # Field name made lowercase.
    vegfa = models.FloatField(db_column='VEGFA', blank=True, null=True)  # Field name made lowercase.
    cd2ap = models.FloatField(db_column='CD2AP', blank=True, null=True)  # Field name made lowercase.
    cnr1 = models.FloatField(db_column='CNR1', blank=True, null=True)  # Field name made lowercase.
    enpp1 = models.FloatField(db_column='ENPP1', blank=True, null=True)  # Field name made lowercase.
    ctgf = models.FloatField(db_column='CTGF', blank=True, null=True)  # Field name made lowercase.
    rps12 = models.FloatField(db_column='RPS12', blank=True, null=True)  # Field name made lowercase.
    sgk1 = models.FloatField(db_column='SGK1', blank=True, null=True)  # Field name made lowercase.
    map3k5 = models.FloatField(db_column='MAP3K5', blank=True, null=True)  # Field name made lowercase.
    cited2 = models.FloatField(db_column='CITED2', blank=True, null=True)  # Field name made lowercase.
    utrn = models.FloatField(db_column='UTRN', blank=True, null=True)  # Field name made lowercase.
    mthfd1l = models.FloatField(db_column='MTHFD1L', blank=True, null=True)  # Field name made lowercase.
    vip = models.FloatField(db_column='VIP', blank=True, null=True)  # Field name made lowercase.
    sod2 = models.FloatField(db_column='SOD2', blank=True, null=True)  # Field name made lowercase.
    lpa = models.FloatField(db_column='LPA', blank=True, null=True)  # Field name made lowercase.
    thbs2 = models.FloatField(db_column='THBS2', blank=True, null=True)  # Field name made lowercase.
    pdgfa = models.FloatField(db_column='PDGFA', blank=True, null=True)  # Field name made lowercase.
    il6 = models.FloatField(db_column='IL6', blank=True, null=True)  # Field name made lowercase.
    npy = models.FloatField(db_column='NPY', blank=True, null=True)  # Field name made lowercase.
    jazf1 = models.FloatField(db_column='JAZF1', blank=True, null=True)  # Field name made lowercase.
    cpvl = models.FloatField(db_column='CPVL', blank=True, null=True)  # Field name made lowercase.
    aqp1 = models.FloatField(db_column='AQP1', blank=True, null=True)  # Field name made lowercase.
    elmo1 = models.FloatField(db_column='ELMO1', blank=True, null=True)  # Field name made lowercase.
    igfbp3 = models.FloatField(db_column='IGFBP3', blank=True, null=True)  # Field name made lowercase.
    egfr = models.FloatField(db_column='EGFR', blank=True, null=True)  # Field name made lowercase.
    eln = models.FloatField(db_column='ELN', blank=True, null=True)  # Field name made lowercase.
    ncf1 = models.FloatField(db_column='NCF1', blank=True, null=True)  # Field name made lowercase.
    hspb1 = models.FloatField(db_column='HSPB1', blank=True, null=True)  # Field name made lowercase.
    sema3a = models.FloatField(db_column='SEMA3A', blank=True, null=True)  # Field name made lowercase.
    pon3 = models.FloatField(db_column='PON3', blank=True, null=True)  # Field name made lowercase.
    pon2 = models.FloatField(db_column='PON2', blank=True, null=True)  # Field name made lowercase.
    nampt = models.FloatField(db_column='NAMPT', blank=True, null=True)  # Field name made lowercase.
    cav1 = models.FloatField(db_column='CAV1', blank=True, null=True)  # Field name made lowercase.
    lep = models.FloatField(db_column='LEP', blank=True, null=True)  # Field name made lowercase.
    akr1b1 = models.FloatField(db_column='AKR1B1', blank=True, null=True)  # Field name made lowercase.
    akr1b10 = models.FloatField(db_column='AKR1B10', blank=True, null=True)  # Field name made lowercase.
    pip = models.FloatField(db_column='PIP', blank=True, null=True)  # Field name made lowercase.
    rarres2 = models.FloatField(db_column='RARRES2', blank=True, null=True)  # Field name made lowercase.
    nos3 = models.FloatField(db_column='NOS3', blank=True, null=True)  # Field name made lowercase.
    angpt2 = models.FloatField(db_column='ANGPT2', blank=True, null=True)  # Field name made lowercase.
    defa1 = models.FloatField(db_column='DEFA1', blank=True, null=True)  # Field name made lowercase.
    lpl = models.FloatField(db_column='LPL', blank=True, null=True)  # Field name made lowercase.
    ebf2 = models.FloatField(db_column='EBF2', blank=True, null=True)  # Field name made lowercase.
    adrb3 = models.FloatField(db_column='ADRB3', blank=True, null=True)  # Field name made lowercase.
    eif4ebp1 = models.FloatField(db_column='EIF4EBP1', blank=True, null=True)  # Field name made lowercase.
    fgfr1 = models.FloatField(db_column='FGFR1', blank=True, null=True)  # Field name made lowercase.
    crh = models.FloatField(db_column='CRH', blank=True, null=True)  # Field name made lowercase.
    sgk3 = models.FloatField(db_column='SGK3', blank=True, null=True)  # Field name made lowercase.
    fabp5 = models.FloatField(db_column='FABP5', blank=True, null=True)  # Field name made lowercase.
    fabp4 = models.FloatField(db_column='FABP4', blank=True, null=True)  # Field name made lowercase.
    mmp16 = models.FloatField(db_column='MMP16', blank=True, null=True)  # Field name made lowercase.
    ncald = models.FloatField(db_column='NCALD', blank=True, null=True)  # Field name made lowercase.
    klf10 = models.FloatField(db_column='KLF10', blank=True, null=True)  # Field name made lowercase.
    enpp2 = models.FloatField(db_column='ENPP2', blank=True, null=True)  # Field name made lowercase.
    pvt1 = models.FloatField(db_column='PVT1', blank=True, null=True)  # Field name made lowercase.
    jak2 = models.FloatField(db_column='JAK2', blank=True, null=True)  # Field name made lowercase.
    psip1 = models.FloatField(db_column='PSIP1', blank=True, null=True)  # Field name made lowercase.
    plin2 = models.FloatField(db_column='PLIN2', blank=True, null=True)  # Field name made lowercase.
    rps6 = models.FloatField(db_column='RPS6', blank=True, null=True)  # Field name made lowercase.
    aldh1a1 = models.FloatField(db_column='ALDH1A1', blank=True, null=True)  # Field name made lowercase.
    frmd3 = models.FloatField(db_column='FRMD3', blank=True, null=True)  # Field name made lowercase.
    gas1 = models.FloatField(db_column='GAS1', blank=True, null=True)  # Field name made lowercase.
    baat = models.FloatField(db_column='BAAT', blank=True, null=True)  # Field name made lowercase.
    abca1 = models.FloatField(db_column='ABCA1', blank=True, null=True)  # Field name made lowercase.
    txn = models.FloatField(db_column='TXN', blank=True, null=True)  # Field name made lowercase.
    ambp = models.FloatField(db_column='AMBP', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    hspa5 = models.FloatField(db_column='HSPA5', blank=True, null=True)  # Field name made lowercase.
    angptl2 = models.FloatField(db_column='ANGPTL2', blank=True, null=True)  # Field name made lowercase.
    ptges = models.FloatField(db_column='PTGES', blank=True, null=True)  # Field name made lowercase.
    tsc1 = models.FloatField(db_column='TSC1', blank=True, null=True)  # Field name made lowercase.
    abo = models.FloatField(db_column='ABO', blank=True, null=True)  # Field name made lowercase.
    adamts13 = models.FloatField(db_column='ADAMTS13', blank=True, null=True)  # Field name made lowercase.
    ptgds = models.FloatField(db_column='PTGDS', blank=True, null=True)  # Field name made lowercase.
    klf6 = models.FloatField(db_column='KLF6', blank=True, null=True)  # Field name made lowercase.
    cdc123 = models.FloatField(db_column='CDC123', blank=True, null=True)  # Field name made lowercase.
    bambi = models.FloatField(db_column='BAMBI', blank=True, null=True)  # Field name made lowercase.
    cxcl12 = models.FloatField(db_column='CXCL12', blank=True, null=True)  # Field name made lowercase.
    mbl2 = models.FloatField(db_column='MBL2', blank=True, null=True)  # Field name made lowercase.
    tfam = models.FloatField(db_column='TFAM', blank=True, null=True)  # Field name made lowercase.
    sirt1 = models.FloatField(db_column='SIRT1', blank=True, null=True)  # Field name made lowercase.
    srgn = models.FloatField(db_column='SRGN', blank=True, null=True)  # Field name made lowercase.
    unc5b = models.FloatField(db_column='UNC5B', blank=True, null=True)  # Field name made lowercase.
    adk = models.FloatField(db_column='ADK', blank=True, null=True)  # Field name made lowercase.
    pten = models.FloatField(db_column='PTEN', blank=True, null=True)  # Field name made lowercase.
    rbp4 = models.FloatField(db_column='RBP4', blank=True, null=True)  # Field name made lowercase.
    cyp2c19 = models.FloatField(db_column='CYP2C19', blank=True, null=True)  # Field name made lowercase.
    entpd1 = models.FloatField(db_column='ENTPD1', blank=True, null=True)  # Field name made lowercase.
    tcf7l2 = models.FloatField(db_column='TCF7L2', blank=True, null=True)  # Field name made lowercase.
    bnip3 = models.FloatField(db_column='BNIP3', blank=True, null=True)  # Field name made lowercase.
    igf2 = models.FloatField(db_column='IGF2', blank=True, null=True)  # Field name made lowercase.
    ins = models.FloatField(db_column='INS', blank=True, null=True)  # Field name made lowercase.
    th = models.FloatField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    kcnq1 = models.FloatField(db_column='KCNQ1', blank=True, null=True)  # Field name made lowercase.
    hbg2 = models.FloatField(db_column='HBG2', blank=True, null=True)  # Field name made lowercase.
    smpd1 = models.FloatField(db_column='SMPD1', blank=True, null=True)  # Field name made lowercase.
    ilk = models.FloatField(db_column='ILK', blank=True, null=True)  # Field name made lowercase.
    adm = models.FloatField(db_column='ADM', blank=True, null=True)  # Field name made lowercase.
    pth = models.FloatField(db_column='PTH', blank=True, null=True)  # Field name made lowercase.
    nucb2 = models.FloatField(db_column='NUCB2', blank=True, null=True)  # Field name made lowercase.
    kcnj11 = models.FloatField(db_column='KCNJ11', blank=True, null=True)  # Field name made lowercase.
    saa1 = models.FloatField(db_column='SAA1', blank=True, null=True)  # Field name made lowercase.
    bdnf = models.FloatField(db_column='BDNF', blank=True, null=True)  # Field name made lowercase.
    wt1 = models.FloatField(db_column='WT1', blank=True, null=True)  # Field name made lowercase.
    cd59 = models.FloatField(db_column='CD59', blank=True, null=True)  # Field name made lowercase.
    pdhx = models.FloatField(db_column='PDHX', blank=True, null=True)  # Field name made lowercase.
    traf6 = models.FloatField(db_column='TRAF6', blank=True, null=True)  # Field name made lowercase.
    api5 = models.FloatField(db_column='API5', blank=True, null=True)  # Field name made lowercase.
    nr1h3 = models.FloatField(db_column='NR1H3', blank=True, null=True)  # Field name made lowercase.
    ndufs3 = models.FloatField(db_column='NDUFS3', blank=True, null=True)  # Field name made lowercase.
    folh1 = models.FloatField(db_column='FOLH1', blank=True, null=True)  # Field name made lowercase.
    aplnr = models.FloatField(db_column='APLNR', blank=True, null=True)  # Field name made lowercase.
    p2rx3 = models.FloatField(db_column='P2RX3', blank=True, null=True)  # Field name made lowercase.
    cntf = models.FloatField(db_column='CNTF', blank=True, null=True)  # Field name made lowercase.
    fads1 = models.FloatField(db_column='FADS1', blank=True, null=True)  # Field name made lowercase.
    fads2 = models.FloatField(db_column='FADS2', blank=True, null=True)  # Field name made lowercase.
    fkbp2 = models.FloatField(db_column='FKBP2', blank=True, null=True)  # Field name made lowercase.
    syvn1 = models.FloatField(db_column='SYVN1', blank=True, null=True)  # Field name made lowercase.
    pc = models.FloatField(db_column='PC', blank=True, null=True)  # Field name made lowercase.
    dhcr7 = models.FloatField(db_column='DHCR7', blank=True, null=True)  # Field name made lowercase.
    prcp = models.FloatField(db_column='PRCP', blank=True, null=True)  # Field name made lowercase.
    nox4 = models.FloatField(db_column='NOX4', blank=True, null=True)  # Field name made lowercase.
    pdgfd = models.FloatField(db_column='PDGFD', blank=True, null=True)  # Field name made lowercase.
    atm = models.FloatField(db_column='ATM', blank=True, null=True)  # Field name made lowercase.
    il18 = models.FloatField(db_column='IL18', blank=True, null=True)  # Field name made lowercase.
    apoa1 = models.FloatField(db_column='APOA1', blank=True, null=True)  # Field name made lowercase.
    hyou1 = models.FloatField(db_column='HYOU1', blank=True, null=True)  # Field name made lowercase.
    esam = models.FloatField(db_column='ESAM', blank=True, null=True)  # Field name made lowercase.
    fkbp4 = models.FloatField(db_column='FKBP4', blank=True, null=True)  # Field name made lowercase.
    fgf23 = models.FloatField(db_column='FGF23', blank=True, null=True)  # Field name made lowercase.
    ntf3 = models.FloatField(db_column='NTF3', blank=True, null=True)  # Field name made lowercase.
    vwf = models.FloatField(db_column='VWF', blank=True, null=True)  # Field name made lowercase.
    cd9 = models.FloatField(db_column='CD9', blank=True, null=True)  # Field name made lowercase.
    gapdh = models.FloatField(db_column='GAPDH', blank=True, null=True)  # Field name made lowercase.
    cd4 = models.FloatField(db_column='CD4', blank=True, null=True)  # Field name made lowercase.
    gnb3 = models.FloatField(db_column='GNB3', blank=True, null=True)  # Field name made lowercase.
    cd163 = models.FloatField(db_column='CD163', blank=True, null=True)  # Field name made lowercase.
    slc2a3 = models.FloatField(db_column='SLC2A3', blank=True, null=True)  # Field name made lowercase.
    cd69 = models.FloatField(db_column='CD69', blank=True, null=True)  # Field name made lowercase.
    irak4 = models.FloatField(db_column='IRAK4', blank=True, null=True)  # Field name made lowercase.
    vdr = models.FloatField(db_column='VDR', blank=True, null=True)  # Field name made lowercase.
    aqp5 = models.FloatField(db_column='AQP5', blank=True, null=True)  # Field name made lowercase.
    acvrl1 = models.FloatField(db_column='ACVRL1', blank=True, null=True)  # Field name made lowercase.
    nfe2 = models.FloatField(db_column='NFE2', blank=True, null=True)  # Field name made lowercase.
    cd63 = models.FloatField(db_column='CD63', blank=True, null=True)  # Field name made lowercase.
    erbb3 = models.FloatField(db_column='ERBB3', blank=True, null=True)  # Field name made lowercase.
    ddit3 = models.FloatField(db_column='DDIT3', blank=True, null=True)  # Field name made lowercase.
    ifng = models.FloatField(db_column='IFNG', blank=True, null=True)  # Field name made lowercase.
    nts = models.FloatField(db_column='NTS', blank=True, null=True)  # Field name made lowercase.
    igf1 = models.FloatField(db_column='IGF1', blank=True, null=True)  # Field name made lowercase.
    acacb = models.FloatField(db_column='ACACB', blank=True, null=True)  # Field name made lowercase.
    trpv4 = models.FloatField(db_column='TRPV4', blank=True, null=True)  # Field name made lowercase.
    atp2a2 = models.FloatField(db_column='ATP2A2', blank=True, null=True)  # Field name made lowercase.
    aldh2 = models.FloatField(db_column='ALDH2', blank=True, null=True)  # Field name made lowercase.
    nos1 = models.FloatField(db_column='NOS1', blank=True, null=True)  # Field name made lowercase.
    pebp1 = models.FloatField(db_column='PEBP1', blank=True, null=True)  # Field name made lowercase.
    psmd9 = models.FloatField(db_column='PSMD9', blank=True, null=True)  # Field name made lowercase.
    scarb1 = models.FloatField(db_column='SCARB1', blank=True, null=True)  # Field name made lowercase.
    p2rx2 = models.FloatField(db_column='P2RX2', blank=True, null=True)  # Field name made lowercase.
    alox5ap = models.FloatField(db_column='ALOX5AP', blank=True, null=True)  # Field name made lowercase.
    kl = models.FloatField(db_column='KL', blank=True, null=True)  # Field name made lowercase.
    postn = models.FloatField(db_column='POSTN', blank=True, null=True)  # Field name made lowercase.
    foxo1 = models.FloatField(db_column='FOXO1', blank=True, null=True)  # Field name made lowercase.
    htr2a = models.FloatField(db_column='HTR2A', blank=True, null=True)  # Field name made lowercase.
    gpc5 = models.FloatField(db_column='GPC5', blank=True, null=True)  # Field name made lowercase.
    irs2 = models.FloatField(db_column='IRS2', blank=True, null=True)  # Field name made lowercase.
    gas6 = models.FloatField(db_column='GAS6', blank=True, null=True)  # Field name made lowercase.
    ang = models.FloatField(db_column='ANG', blank=True, null=True)  # Field name made lowercase.
    mmp14 = models.FloatField(db_column='MMP14', blank=True, null=True)  # Field name made lowercase.
    ltb4r2 = models.FloatField(db_column='LTB4R2', blank=True, null=True)  # Field name made lowercase.
    nfkbia = models.FloatField(db_column='NFKBIA', blank=True, null=True)  # Field name made lowercase.
    bmp4 = models.FloatField(db_column='BMP4', blank=True, null=True)  # Field name made lowercase.
    rtn1 = models.FloatField(db_column='RTN1', blank=True, null=True)  # Field name made lowercase.
    pgf = models.FloatField(db_column='PGF', blank=True, null=True)  # Field name made lowercase.
    ngb = models.FloatField(db_column='NGB', blank=True, null=True)  # Field name made lowercase.
    ahsa1 = models.FloatField(db_column='AHSA1', blank=True, null=True)  # Field name made lowercase.
    bdkrb2 = models.FloatField(db_column='BDKRB2', blank=True, null=True)  # Field name made lowercase.
    bdkrb1 = models.FloatField(db_column='BDKRB1', blank=True, null=True)  # Field name made lowercase.
    akt1 = models.FloatField(db_column='AKT1', blank=True, null=True)  # Field name made lowercase.
    grem1 = models.FloatField(db_column='GREM1', blank=True, null=True)  # Field name made lowercase.
    thbs1 = models.FloatField(db_column='THBS1', blank=True, null=True)  # Field name made lowercase.
    pak6 = models.FloatField(db_column='PAK6', blank=True, null=True)  # Field name made lowercase.
    b2m = models.FloatField(db_column='B2M', blank=True, null=True)  # Field name made lowercase.
    myo5c = models.FloatField(db_column='MYO5C', blank=True, null=True)  # Field name made lowercase.
    onecut1 = models.FloatField(db_column='ONECUT1', blank=True, null=True)  # Field name made lowercase.
    adam10 = models.FloatField(db_column='ADAM10', blank=True, null=True)  # Field name made lowercase.
    ctsh = models.FloatField(db_column='CTSH', blank=True, null=True)  # Field name made lowercase.
    plin1 = models.FloatField(db_column='PLIN1', blank=True, null=True)  # Field name made lowercase.
    igf1r = models.FloatField(db_column='IGF1R', blank=True, null=True)  # Field name made lowercase.
    mrpl28 = models.FloatField(db_column='MRPL28', blank=True, null=True)  # Field name made lowercase.
    cacna1h = models.FloatField(db_column='CACNA1H', blank=True, null=True)  # Field name made lowercase.
    pdpk1 = models.FloatField(db_column='PDPK1', blank=True, null=True)  # Field name made lowercase.
    ercc4 = models.FloatField(db_column='ERCC4', blank=True, null=True)  # Field name made lowercase.
    smg1 = models.FloatField(db_column='SMG1', blank=True, null=True)  # Field name made lowercase.
    itgam = models.FloatField(db_column='ITGAM', blank=True, null=True)  # Field name made lowercase.
    fto = models.FloatField(db_column='FTO', blank=True, null=True)  # Field name made lowercase.
    mmp2 = models.FloatField(db_column='MMP2', blank=True, null=True)  # Field name made lowercase.
    slc12a3 = models.FloatField(db_column='SLC12A3', blank=True, null=True)  # Field name made lowercase.
    cetp = models.FloatField(db_column='CETP', blank=True, null=True)  # Field name made lowercase.
    cx3cl1 = models.FloatField(db_column='CX3CL1', blank=True, null=True)  # Field name made lowercase.
    cdh1 = models.FloatField(db_column='CDH1', blank=True, null=True)  # Field name made lowercase.
    nqo1 = models.FloatField(db_column='NQO1', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    znrf1 = models.FloatField(db_column='ZNRF1', blank=True, null=True)  # Field name made lowercase.
    cyba = models.FloatField(db_column='CYBA', blank=True, null=True)  # Field name made lowercase.
    tubb3 = models.FloatField(db_column='TUBB3', blank=True, null=True)  # Field name made lowercase.
    crk = models.FloatField(db_column='CRK', blank=True, null=True)  # Field name made lowercase.
    serpinf2 = models.FloatField(db_column='SERPINF2', blank=True, null=True)  # Field name made lowercase.
    serpinf1 = models.FloatField(db_column='SERPINF1', blank=True, null=True)  # Field name made lowercase.
    trpv3 = models.FloatField(db_column='TRPV3', blank=True, null=True)  # Field name made lowercase.
    cxcl16 = models.FloatField(db_column='CXCL16', blank=True, null=True)  # Field name made lowercase.
    slc2a4 = models.FloatField(db_column='SLC2A4', blank=True, null=True)  # Field name made lowercase.
    cd68 = models.FloatField(db_column='CD68', blank=True, null=True)  # Field name made lowercase.
    shbg = models.FloatField(db_column='SHBG', blank=True, null=True)  # Field name made lowercase.
    pmp22 = models.FloatField(db_column='PMP22', blank=True, null=True)  # Field name made lowercase.
    srebf1 = models.FloatField(db_column='SREBF1', blank=True, null=True)  # Field name made lowercase.
    mapk7 = models.FloatField(db_column='MAPK7', blank=True, null=True)  # Field name made lowercase.
    ccl2 = models.FloatField(db_column='CCL2', blank=True, null=True)  # Field name made lowercase.
    ccl5 = models.FloatField(db_column='CCL5', blank=True, null=True)  # Field name made lowercase.
    hnf1b = models.FloatField(db_column='HNF1B', blank=True, null=True)  # Field name made lowercase.
    erbb2 = models.FloatField(db_column='ERBB2', blank=True, null=True)  # Field name made lowercase.
    fkbp10 = models.FloatField(db_column='FKBP10', blank=True, null=True)  # Field name made lowercase.
    stat5a = models.FloatField(db_column='STAT5A', blank=True, null=True)  # Field name made lowercase.
    stat3 = models.FloatField(db_column='STAT3', blank=True, null=True)  # Field name made lowercase.
    naglu = models.FloatField(db_column='NAGLU', blank=True, null=True)  # Field name made lowercase.
    aoc2 = models.FloatField(db_column='AOC2', blank=True, null=True)  # Field name made lowercase.
    aoc3 = models.FloatField(db_column='AOC3', blank=True, null=True)  # Field name made lowercase.
    ppy = models.FloatField(db_column='PPY', blank=True, null=True)  # Field name made lowercase.
    sth = models.FloatField(db_column='STH', blank=True, null=True)  # Field name made lowercase.
    itgb3 = models.FloatField(db_column='ITGB3', blank=True, null=True)  # Field name made lowercase.
    gip = models.FloatField(db_column='GIP', blank=True, null=True)  # Field name made lowercase.
    mpo = models.FloatField(db_column='MPO', blank=True, null=True)  # Field name made lowercase.
    pecam1 = models.FloatField(db_column='PECAM1', blank=True, null=True)  # Field name made lowercase.
    sox9 = models.FloatField(db_column='SOX9', blank=True, null=True)  # Field name made lowercase.
    timp2 = models.FloatField(db_column='TIMP2', blank=True, null=True)  # Field name made lowercase.
    dcxr = models.FloatField(db_column='DCXR', blank=True, null=True)  # Field name made lowercase.
    fasn = models.FloatField(db_column='FASN', blank=True, null=True)  # Field name made lowercase.
    colec12 = models.FloatField(db_column='COLEC12', blank=True, null=True)  # Field name made lowercase.
    adcyap1 = models.FloatField(db_column='ADCYAP1', blank=True, null=True)  # Field name made lowercase.
    smad7 = models.FloatField(db_column='SMAD7', blank=True, null=True)  # Field name made lowercase.
    nedd4l = models.FloatField(db_column='NEDD4L', blank=True, null=True)  # Field name made lowercase.
    mc4r = models.FloatField(db_column='MC4R', blank=True, null=True)  # Field name made lowercase.
    bcl2 = models.FloatField(db_column='BCL2', blank=True, null=True)  # Field name made lowercase.
    cndp2 = models.FloatField(db_column='CNDP2', blank=True, null=True)  # Field name made lowercase.
    znf236 = models.FloatField(db_column='ZNF236', blank=True, null=True)  # Field name made lowercase.
    stk11 = models.FloatField(db_column='STK11', blank=True, null=True)  # Field name made lowercase.
    sirt6 = models.FloatField(db_column='SIRT6', blank=True, null=True)  # Field name made lowercase.
    uhrf1 = models.FloatField(db_column='UHRF1', blank=True, null=True)  # Field name made lowercase.
    timm44 = models.FloatField(db_column='TIMM44', blank=True, null=True)  # Field name made lowercase.
    angptl4 = models.FloatField(db_column='ANGPTL4', blank=True, null=True)  # Field name made lowercase.
    dnmt1 = models.FloatField(db_column='DNMT1', blank=True, null=True)  # Field name made lowercase.
    icam1 = models.FloatField(db_column='ICAM1', blank=True, null=True)  # Field name made lowercase.
    ldlr = models.FloatField(db_column='LDLR', blank=True, null=True)  # Field name made lowercase.
    epor = models.FloatField(db_column='EPOR', blank=True, null=True)  # Field name made lowercase.
    prdx2 = models.FloatField(db_column='PRDX2', blank=True, null=True)  # Field name made lowercase.
    ptger1 = models.FloatField(db_column='PTGER1', blank=True, null=True)  # Field name made lowercase.
    unc13a = models.FloatField(db_column='UNC13A', blank=True, null=True)  # Field name made lowercase.
    gdf15 = models.FloatField(db_column='GDF15', blank=True, null=True)  # Field name made lowercase.
    fkbp8 = models.FloatField(db_column='FKBP8', blank=True, null=True)  # Field name made lowercase.
    usf2 = models.FloatField(db_column='USF2', blank=True, null=True)  # Field name made lowercase.
    ffar1 = models.FloatField(db_column='FFAR1', blank=True, null=True)  # Field name made lowercase.
    ffar2 = models.FloatField(db_column='FFAR2', blank=True, null=True)  # Field name made lowercase.
    nphs1 = models.FloatField(db_column='NPHS1', blank=True, null=True)  # Field name made lowercase.
    tgfb1 = models.FloatField(db_column='TGFB1', blank=True, null=True)  # Field name made lowercase.
    xrcc1 = models.FloatField(db_column='XRCC1', blank=True, null=True)  # Field name made lowercase.
    ercc1 = models.FloatField(db_column='ERCC1', blank=True, null=True)  # Field name made lowercase.
    gipr = models.FloatField(db_column='GIPR', blank=True, null=True)  # Field name made lowercase.
    fgf21 = models.FloatField(db_column='FGF21', blank=True, null=True)  # Field name made lowercase.
    clec11a = models.FloatField(db_column='CLEC11A', blank=True, null=True)  # Field name made lowercase.
    fpr1 = models.FloatField(db_column='FPR1', blank=True, null=True)  # Field name made lowercase.
    trib3 = models.FloatField(db_column='TRIB3', blank=True, null=True)  # Field name made lowercase.
    bmp2 = models.FloatField(db_column='BMP2', blank=True, null=True)  # Field name made lowercase.
    thbd = models.FloatField(db_column='THBD', blank=True, null=True)  # Field name made lowercase.
    cst3 = models.FloatField(db_column='CST3', blank=True, null=True)  # Field name made lowercase.
    id1 = models.FloatField(db_column='ID1', blank=True, null=True)  # Field name made lowercase.
    src = models.FloatField(db_column='SRC', blank=True, null=True)  # Field name made lowercase.
    mafb = models.FloatField(db_column='MAFB', blank=True, null=True)  # Field name made lowercase.
    sgk2 = models.FloatField(db_column='SGK2', blank=True, null=True)  # Field name made lowercase.
    hnf4a = models.FloatField(db_column='HNF4A', blank=True, null=True)  # Field name made lowercase.
    pltp = models.FloatField(db_column='PLTP', blank=True, null=True)  # Field name made lowercase.
    mmp9 = models.FloatField(db_column='MMP9', blank=True, null=True)  # Field name made lowercase.
    cd40 = models.FloatField(db_column='CD40', blank=True, null=True)  # Field name made lowercase.
    ptpn1 = models.FloatField(db_column='PTPN1', blank=True, null=True)  # Field name made lowercase.
    cyp24a1 = models.FloatField(db_column='CYP24A1', blank=True, null=True)  # Field name made lowercase.
    rcan1 = models.FloatField(db_column='RCAN1', blank=True, null=True)  # Field name made lowercase.
    abcg1 = models.FloatField(db_column='ABCG1', blank=True, null=True)  # Field name made lowercase.
    prmt2 = models.FloatField(db_column='PRMT2', blank=True, null=True)  # Field name made lowercase.
    comt = models.FloatField(db_column='COMT', blank=True, null=True)  # Field name made lowercase.
    mapk1 = models.FloatField(db_column='MAPK1', blank=True, null=True)  # Field name made lowercase.
    mif = models.FloatField(db_column='MIF', blank=True, null=True)  # Field name made lowercase.
    ggt1 = models.FloatField(db_column='GGT1', blank=True, null=True)  # Field name made lowercase.
    xbp1 = models.FloatField(db_column='XBP1', blank=True, null=True)  # Field name made lowercase.
    osm = models.FloatField(db_column='OSM', blank=True, null=True)  # Field name made lowercase.
    limk2 = models.FloatField(db_column='LIMK2', blank=True, null=True)  # Field name made lowercase.
    sfi1 = models.FloatField(db_column='SFI1', blank=True, null=True)  # Field name made lowercase.
    timp3 = models.FloatField(db_column='TIMP3', blank=True, null=True)  # Field name made lowercase.
    hmox1 = models.FloatField(db_column='HMOX1', blank=True, null=True)  # Field name made lowercase.
    apol1 = models.FloatField(db_column='APOL1', blank=True, null=True)  # Field name made lowercase.
    myh9 = models.FloatField(db_column='MYH9', blank=True, null=True)  # Field name made lowercase.
    pdgfb = models.FloatField(db_column='PDGFB', blank=True, null=True)  # Field name made lowercase.
    atf4 = models.FloatField(db_column='ATF4', blank=True, null=True)  # Field name made lowercase.
    tspo = models.FloatField(db_column='TSPO', blank=True, null=True)  # Field name made lowercase.
    miox = models.FloatField(db_column='MIOX', blank=True, null=True)  # Field name made lowercase.
    prdx4 = models.FloatField(db_column='PRDX4', blank=True, null=True)  # Field name made lowercase.
    gk = models.FloatField(db_column='GK', blank=True, null=True)  # Field name made lowercase.
    rgn = models.FloatField(db_column='RGN', blank=True, null=True)  # Field name made lowercase.
    timp1 = models.FloatField(db_column='TIMP1', blank=True, null=True)  # Field name made lowercase.
    clcn5 = models.FloatField(db_column='CLCN5', blank=True, null=True)  # Field name made lowercase.
    ar = models.FloatField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    foxo4 = models.FloatField(db_column='FOXO4', blank=True, null=True)  # Field name made lowercase.
    rps6ka6 = models.FloatField(db_column='RPS6KA6', blank=True, null=True)  # Field name made lowercase.
    nox1 = models.FloatField(db_column='NOX1', blank=True, null=True)  # Field name made lowercase.
    xiap = models.FloatField(db_column='XIAP', blank=True, null=True)  # Field name made lowercase.
    cd40lg = models.FloatField(db_column='CD40LG', blank=True, null=True)  # Field name made lowercase.
    l1cam = models.FloatField(db_column='L1CAM', blank=True, null=True)  # Field name made lowercase.
    irak1 = models.FloatField(db_column='IRAK1', blank=True, null=True)  # Field name made lowercase.
    g6pd = models.FloatField(db_column='G6PD', blank=True, null=True)  # Field name made lowercase.
    f8 = models.FloatField(db_column='F8', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diaco_tissue_brain_cortex'


class DiacoTissueBrainFrontalCortexBa9(models.Model):
    subjid = models.CharField(db_column='SUBJID', max_length=50, primary_key=True)  # Field name made lowercase.
    sampid = models.CharField(db_column='SAMPID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sesso = models.CharField(db_column='Sesso', max_length=1)  # Field name made lowercase.
    eta = models.CharField(db_column='Età', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errfi1 = models.FloatField(db_column='ERRFI1', blank=True, null=True)  # Field name made lowercase.
    mad2l2 = models.FloatField(db_column='MAD2L2', blank=True, null=True)  # Field name made lowercase.
    mthfr = models.FloatField(db_column='MTHFR', blank=True, null=True)  # Field name made lowercase.
    nppa = models.FloatField(db_column='NPPA', blank=True, null=True)  # Field name made lowercase.
    tnfrsf1b = models.FloatField(db_column='TNFRSF1B', blank=True, null=True)  # Field name made lowercase.
    pla2g2a = models.FloatField(db_column='PLA2G2A', blank=True, null=True)  # Field name made lowercase.
    alpl = models.FloatField(db_column='ALPL', blank=True, null=True)  # Field name made lowercase.
    hspg2 = models.FloatField(db_column='HSPG2', blank=True, null=True)  # Field name made lowercase.
    cnr2 = models.FloatField(db_column='CNR2', blank=True, null=True)  # Field name made lowercase.
    slc9a1 = models.FloatField(db_column='SLC9A1', blank=True, null=True)  # Field name made lowercase.
    col8a2 = models.FloatField(db_column='COL8A2', blank=True, null=True)  # Field name made lowercase.
    cap1 = models.FloatField(db_column='CAP1', blank=True, null=True)  # Field name made lowercase.
    slc2a1 = models.FloatField(db_column='SLC2A1', blank=True, null=True)  # Field name made lowercase.
    cyp2j2 = models.FloatField(db_column='CYP2J2', blank=True, null=True)  # Field name made lowercase.
    ddah1 = models.FloatField(db_column='DDAH1', blank=True, null=True)  # Field name made lowercase.
    cyr61 = models.FloatField(db_column='CYR61', blank=True, null=True)  # Field name made lowercase.
    ngf = models.FloatField(db_column='NGF', blank=True, null=True)  # Field name made lowercase.
    hmgcs2 = models.FloatField(db_column='HMGCS2', blank=True, null=True)  # Field name made lowercase.
    ctss = models.FloatField(db_column='CTSS', blank=True, null=True)  # Field name made lowercase.
    s100a12 = models.FloatField(db_column='S100A12', blank=True, null=True)  # Field name made lowercase.
    lmna = models.FloatField(db_column='LMNA', blank=True, null=True)  # Field name made lowercase.
    cd247 = models.FloatField(db_column='CD247', blank=True, null=True)  # Field name made lowercase.
    sele = models.FloatField(db_column='SELE', blank=True, null=True)  # Field name made lowercase.
    fmo3 = models.FloatField(db_column='FMO3', blank=True, null=True)  # Field name made lowercase.
    prdx6 = models.FloatField(db_column='PRDX6', blank=True, null=True)  # Field name made lowercase.
    glul = models.FloatField(db_column='GLUL', blank=True, null=True)  # Field name made lowercase.
    lamc1 = models.FloatField(db_column='LAMC1', blank=True, null=True)  # Field name made lowercase.
    ptgs2 = models.FloatField(db_column='PTGS2', blank=True, null=True)  # Field name made lowercase.
    chi3l1 = models.FloatField(db_column='CHI3L1', blank=True, null=True)  # Field name made lowercase.
    chit1 = models.FloatField(db_column='CHIT1', blank=True, null=True)  # Field name made lowercase.
    fmod = models.FloatField(db_column='FMOD', blank=True, null=True)  # Field name made lowercase.
    il10 = models.FloatField(db_column='IL10', blank=True, null=True)  # Field name made lowercase.
    pfkfb2 = models.FloatField(db_column='PFKFB2', blank=True, null=True)  # Field name made lowercase.
    cd34 = models.FloatField(db_column='CD34', blank=True, null=True)  # Field name made lowercase.
    cog2 = models.FloatField(db_column='COG2', blank=True, null=True)  # Field name made lowercase.
    nlrp3 = models.FloatField(db_column='NLRP3', blank=True, null=True)  # Field name made lowercase.
    rock2 = models.FloatField(db_column='ROCK2', blank=True, null=True)  # Field name made lowercase.
    apob = models.FloatField(db_column='APOB', blank=True, null=True)  # Field name made lowercase.
    pomc = models.FloatField(db_column='POMC', blank=True, null=True)  # Field name made lowercase.
    gckr = models.FloatField(db_column='GCKR', blank=True, null=True)  # Field name made lowercase.
    plekhh2 = models.FloatField(db_column='PLEKHH2', blank=True, null=True)  # Field name made lowercase.
    prkce = models.FloatField(db_column='PRKCE', blank=True, null=True)  # Field name made lowercase.
    pigf = models.FloatField(db_column='PIGF', blank=True, null=True)  # Field name made lowercase.
    msh2 = models.FloatField(db_column='MSH2', blank=True, null=True)  # Field name made lowercase.
    gfpt1 = models.FloatField(db_column='GFPT1', blank=True, null=True)  # Field name made lowercase.
    tacr1 = models.FloatField(db_column='TACR1', blank=True, null=True)  # Field name made lowercase.
    reg1a = models.FloatField(db_column='REG1A', blank=True, null=True)  # Field name made lowercase.
    eif2ak3 = models.FloatField(db_column='EIF2AK3', blank=True, null=True)  # Field name made lowercase.
    adra2b = models.FloatField(db_column='ADRA2B', blank=True, null=True)  # Field name made lowercase.
    il1b = models.FloatField(db_column='IL1B', blank=True, null=True)  # Field name made lowercase.
    proc = models.FloatField(db_column='PROC', blank=True, null=True)  # Field name made lowercase.
    polr2d = models.FloatField(db_column='POLR2D', blank=True, null=True)  # Field name made lowercase.
    zeb2 = models.FloatField(db_column='ZEB2', blank=True, null=True)  # Field name made lowercase.
    acvr1c = models.FloatField(db_column='ACVR1C', blank=True, null=True)  # Field name made lowercase.
    dpp4 = models.FloatField(db_column='DPP4', blank=True, null=True)  # Field name made lowercase.
    nfe2l2 = models.FloatField(db_column='NFE2L2', blank=True, null=True)  # Field name made lowercase.
    igfbp5 = models.FloatField(db_column='IGFBP5', blank=True, null=True)  # Field name made lowercase.
    ccl20 = models.FloatField(db_column='CCL20', blank=True, null=True)  # Field name made lowercase.
    hdac4 = models.FloatField(db_column='HDAC4', blank=True, null=True)  # Field name made lowercase.
    capn10 = models.FloatField(db_column='CAPN10', blank=True, null=True)  # Field name made lowercase.
    ghrl = models.FloatField(db_column='GHRL', blank=True, null=True)  # Field name made lowercase.
    pparg = models.FloatField(db_column='PPARG', blank=True, null=True)  # Field name made lowercase.
    raf1 = models.FloatField(db_column='RAF1', blank=True, null=True)  # Field name made lowercase.
    myd88 = models.FloatField(db_column='MYD88', blank=True, null=True)  # Field name made lowercase.
    cx3cr1 = models.FloatField(db_column='CX3CR1', blank=True, null=True)  # Field name made lowercase.
    cck = models.FloatField(db_column='CCK', blank=True, null=True)  # Field name made lowercase.
    exosc7 = models.FloatField(db_column='EXOSC7', blank=True, null=True)  # Field name made lowercase.
    ccr1 = models.FloatField(db_column='CCR1', blank=True, null=True)  # Field name made lowercase.
    ccr5 = models.FloatField(db_column='CCR5', blank=True, null=True)  # Field name made lowercase.
    gpx1 = models.FloatField(db_column='GPX1', blank=True, null=True)  # Field name made lowercase.
    rhoa = models.FloatField(db_column='RHOA', blank=True, null=True)  # Field name made lowercase.
    cish = models.FloatField(db_column='CISH', blank=True, null=True)  # Field name made lowercase.
    tkt = models.FloatField(db_column='TKT', blank=True, null=True)  # Field name made lowercase.
    appl1 = models.FloatField(db_column='APPL1', blank=True, null=True)  # Field name made lowercase.
    slmap = models.FloatField(db_column='SLMAP', blank=True, null=True)  # Field name made lowercase.
    col8a1 = models.FloatField(db_column='COL8A1', blank=True, null=True)  # Field name made lowercase.
    cd47 = models.FloatField(db_column='CD47', blank=True, null=True)  # Field name made lowercase.
    gap43 = models.FloatField(db_column='GAP43', blank=True, null=True)  # Field name made lowercase.
    cd80 = models.FloatField(db_column='CD80', blank=True, null=True)  # Field name made lowercase.
    rho = models.FloatField(db_column='RHO', blank=True, null=True)  # Field name made lowercase.
    trh = models.FloatField(db_column='TRH', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='TF', blank=True, null=True)  # Field name made lowercase.
    rbp1 = models.FloatField(db_column='RBP1', blank=True, null=True)  # Field name made lowercase.
    trpc1 = models.FloatField(db_column='TRPC1', blank=True, null=True)  # Field name made lowercase.
    agtr1 = models.FloatField(db_column='AGTR1', blank=True, null=True)  # Field name made lowercase.
    sucnr1 = models.FloatField(db_column='SUCNR1', blank=True, null=True)  # Field name made lowercase.
    p2ry1 = models.FloatField(db_column='P2RY1', blank=True, null=True)  # Field name made lowercase.
    mme = models.FloatField(db_column='MME', blank=True, null=True)  # Field name made lowercase.
    slc2a2 = models.FloatField(db_column='SLC2A2', blank=True, null=True)  # Field name made lowercase.
    pik3ca = models.FloatField(db_column='PIK3CA', blank=True, null=True)  # Field name made lowercase.
    parl = models.FloatField(db_column='PARL', blank=True, null=True)  # Field name made lowercase.
    ahsg = models.FloatField(db_column='AHSG', blank=True, null=True)  # Field name made lowercase.
    adipoq = models.FloatField(db_column='ADIPOQ', blank=True, null=True)  # Field name made lowercase.
    spon2 = models.FloatField(db_column='SPON2', blank=True, null=True)  # Field name made lowercase.
    wfs1 = models.FloatField(db_column='WFS1', blank=True, null=True)  # Field name made lowercase.
    cd38 = models.FloatField(db_column='CD38', blank=True, null=True)  # Field name made lowercase.
    prom1 = models.FloatField(db_column='PROM1', blank=True, null=True)  # Field name made lowercase.
    ppargc1a = models.FloatField(db_column='PPARGC1A', blank=True, null=True)  # Field name made lowercase.
    igfbp7 = models.FloatField(db_column='IGFBP7', blank=True, null=True)  # Field name made lowercase.
    cxcl5 = models.FloatField(db_column='CXCL5', blank=True, null=True)  # Field name made lowercase.
    cxcl9 = models.FloatField(db_column='CXCL9', blank=True, null=True)  # Field name made lowercase.
    cxcl10 = models.FloatField(db_column='CXCL10', blank=True, null=True)  # Field name made lowercase.
    cxcl11 = models.FloatField(db_column='CXCL11', blank=True, null=True)  # Field name made lowercase.
    hpse = models.FloatField(db_column='HPSE', blank=True, null=True)  # Field name made lowercase.
    spp1 = models.FloatField(db_column='SPP1', blank=True, null=True)  # Field name made lowercase.
    adh1b = models.FloatField(db_column='ADH1B', blank=True, null=True)  # Field name made lowercase.
    egf = models.FloatField(db_column='EGF', blank=True, null=True)  # Field name made lowercase.
    alpk1 = models.FloatField(db_column='ALPK1', blank=True, null=True)  # Field name made lowercase.
    fabp2 = models.FloatField(db_column='FABP2', blank=True, null=True)  # Field name made lowercase.
    pde5a = models.FloatField(db_column='PDE5A', blank=True, null=True)  # Field name made lowercase.
    setd7 = models.FloatField(db_column='SETD7', blank=True, null=True)  # Field name made lowercase.
    smad1 = models.FloatField(db_column='SMAD1', blank=True, null=True)  # Field name made lowercase.
    ednra = models.FloatField(db_column='EDNRA', blank=True, null=True)  # Field name made lowercase.
    nr3c2 = models.FloatField(db_column='NR3C2', blank=True, null=True)  # Field name made lowercase.
    tlr2 = models.FloatField(db_column='TLR2', blank=True, null=True)  # Field name made lowercase.
    npy5r = models.FloatField(db_column='NPY5R', blank=True, null=True)  # Field name made lowercase.
    fbxo8 = models.FloatField(db_column='FBXO8', blank=True, null=True)  # Field name made lowercase.
    vegfc = models.FloatField(db_column='VEGFC', blank=True, null=True)  # Field name made lowercase.
    acsl1 = models.FloatField(db_column='ACSL1', blank=True, null=True)  # Field name made lowercase.
    sorbs2 = models.FloatField(db_column='SORBS2', blank=True, null=True)  # Field name made lowercase.
    f11 = models.FloatField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    basp1 = models.FloatField(db_column='BASP1', blank=True, null=True)  # Field name made lowercase.
    ptger4 = models.FloatField(db_column='PTGER4', blank=True, null=True)  # Field name made lowercase.
    prkaa1 = models.FloatField(db_column='PRKAA1', blank=True, null=True)  # Field name made lowercase.
    ghr = models.FloatField(db_column='GHR', blank=True, null=True)  # Field name made lowercase.
    itga2 = models.FloatField(db_column='ITGA2', blank=True, null=True)  # Field name made lowercase.
    cdk7 = models.FloatField(db_column='CDK7', blank=True, null=True)  # Field name made lowercase.
    f2r = models.FloatField(db_column='F2R', blank=True, null=True)  # Field name made lowercase.
    erap2 = models.FloatField(db_column='ERAP2', blank=True, null=True)  # Field name made lowercase.
    apc = models.FloatField(db_column='APC', blank=True, null=True)  # Field name made lowercase.
    tnfaip8 = models.FloatField(db_column='TNFAIP8', blank=True, null=True)  # Field name made lowercase.
    vdac1 = models.FloatField(db_column='VDAC1', blank=True, null=True)  # Field name made lowercase.
    pdgfrb = models.FloatField(db_column='PDGFRB', blank=True, null=True)  # Field name made lowercase.
    cd74 = models.FloatField(db_column='CD74', blank=True, null=True)  # Field name made lowercase.
    sparc = models.FloatField(db_column='SPARC', blank=True, null=True)  # Field name made lowercase.
    ebf1 = models.FloatField(db_column='EBF1', blank=True, null=True)  # Field name made lowercase.
    gfpt2 = models.FloatField(db_column='GFPT2', blank=True, null=True)  # Field name made lowercase.
    rreb1 = models.FloatField(db_column='RREB1', blank=True, null=True)  # Field name made lowercase.
    edn1 = models.FloatField(db_column='EDN1', blank=True, null=True)  # Field name made lowercase.
    cdkal1 = models.FloatField(db_column='CDKAL1', blank=True, null=True)  # Field name made lowercase.
    hfe = models.FloatField(db_column='HFE', blank=True, null=True)  # Field name made lowercase.
    hla_a = models.FloatField(db_column='HLA-A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  # Field name made lowercase.
    tnf = models.FloatField(db_column='TNF', blank=True, null=True)  # Field name made lowercase.
    hspa1a = models.FloatField(db_column='HSPA1A', blank=True, null=True)  # Field name made lowercase.
    hspa1b = models.FloatField(db_column='HSPA1B', blank=True, null=True)  # Field name made lowercase.
    hla_dqa1 = models.FloatField(db_column='HLA-DQA1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mapk14 = models.FloatField(db_column='MAPK14', blank=True, null=True)  # Field name made lowercase.
    cdkn1a = models.FloatField(db_column='CDKN1A', blank=True, null=True)  # Field name made lowercase.
    glo1 = models.FloatField(db_column='GLO1', blank=True, null=True)  # Field name made lowercase.
    vegfa = models.FloatField(db_column='VEGFA', blank=True, null=True)  # Field name made lowercase.
    cd2ap = models.FloatField(db_column='CD2AP', blank=True, null=True)  # Field name made lowercase.
    cnr1 = models.FloatField(db_column='CNR1', blank=True, null=True)  # Field name made lowercase.
    enpp1 = models.FloatField(db_column='ENPP1', blank=True, null=True)  # Field name made lowercase.
    ctgf = models.FloatField(db_column='CTGF', blank=True, null=True)  # Field name made lowercase.
    rps12 = models.FloatField(db_column='RPS12', blank=True, null=True)  # Field name made lowercase.
    sgk1 = models.FloatField(db_column='SGK1', blank=True, null=True)  # Field name made lowercase.
    map3k5 = models.FloatField(db_column='MAP3K5', blank=True, null=True)  # Field name made lowercase.
    cited2 = models.FloatField(db_column='CITED2', blank=True, null=True)  # Field name made lowercase.
    utrn = models.FloatField(db_column='UTRN', blank=True, null=True)  # Field name made lowercase.
    mthfd1l = models.FloatField(db_column='MTHFD1L', blank=True, null=True)  # Field name made lowercase.
    vip = models.FloatField(db_column='VIP', blank=True, null=True)  # Field name made lowercase.
    sod2 = models.FloatField(db_column='SOD2', blank=True, null=True)  # Field name made lowercase.
    lpa = models.FloatField(db_column='LPA', blank=True, null=True)  # Field name made lowercase.
    thbs2 = models.FloatField(db_column='THBS2', blank=True, null=True)  # Field name made lowercase.
    pdgfa = models.FloatField(db_column='PDGFA', blank=True, null=True)  # Field name made lowercase.
    il6 = models.FloatField(db_column='IL6', blank=True, null=True)  # Field name made lowercase.
    npy = models.FloatField(db_column='NPY', blank=True, null=True)  # Field name made lowercase.
    jazf1 = models.FloatField(db_column='JAZF1', blank=True, null=True)  # Field name made lowercase.
    cpvl = models.FloatField(db_column='CPVL', blank=True, null=True)  # Field name made lowercase.
    aqp1 = models.FloatField(db_column='AQP1', blank=True, null=True)  # Field name made lowercase.
    elmo1 = models.FloatField(db_column='ELMO1', blank=True, null=True)  # Field name made lowercase.
    igfbp3 = models.FloatField(db_column='IGFBP3', blank=True, null=True)  # Field name made lowercase.
    egfr = models.FloatField(db_column='EGFR', blank=True, null=True)  # Field name made lowercase.
    eln = models.FloatField(db_column='ELN', blank=True, null=True)  # Field name made lowercase.
    ncf1 = models.FloatField(db_column='NCF1', blank=True, null=True)  # Field name made lowercase.
    hspb1 = models.FloatField(db_column='HSPB1', blank=True, null=True)  # Field name made lowercase.
    sema3a = models.FloatField(db_column='SEMA3A', blank=True, null=True)  # Field name made lowercase.
    pon3 = models.FloatField(db_column='PON3', blank=True, null=True)  # Field name made lowercase.
    pon2 = models.FloatField(db_column='PON2', blank=True, null=True)  # Field name made lowercase.
    nampt = models.FloatField(db_column='NAMPT', blank=True, null=True)  # Field name made lowercase.
    cav1 = models.FloatField(db_column='CAV1', blank=True, null=True)  # Field name made lowercase.
    lep = models.FloatField(db_column='LEP', blank=True, null=True)  # Field name made lowercase.
    akr1b1 = models.FloatField(db_column='AKR1B1', blank=True, null=True)  # Field name made lowercase.
    akr1b10 = models.FloatField(db_column='AKR1B10', blank=True, null=True)  # Field name made lowercase.
    pip = models.FloatField(db_column='PIP', blank=True, null=True)  # Field name made lowercase.
    rarres2 = models.FloatField(db_column='RARRES2', blank=True, null=True)  # Field name made lowercase.
    nos3 = models.FloatField(db_column='NOS3', blank=True, null=True)  # Field name made lowercase.
    angpt2 = models.FloatField(db_column='ANGPT2', blank=True, null=True)  # Field name made lowercase.
    defa1 = models.FloatField(db_column='DEFA1', blank=True, null=True)  # Field name made lowercase.
    lpl = models.FloatField(db_column='LPL', blank=True, null=True)  # Field name made lowercase.
    ebf2 = models.FloatField(db_column='EBF2', blank=True, null=True)  # Field name made lowercase.
    adrb3 = models.FloatField(db_column='ADRB3', blank=True, null=True)  # Field name made lowercase.
    eif4ebp1 = models.FloatField(db_column='EIF4EBP1', blank=True, null=True)  # Field name made lowercase.
    fgfr1 = models.FloatField(db_column='FGFR1', blank=True, null=True)  # Field name made lowercase.
    crh = models.FloatField(db_column='CRH', blank=True, null=True)  # Field name made lowercase.
    sgk3 = models.FloatField(db_column='SGK3', blank=True, null=True)  # Field name made lowercase.
    fabp5 = models.FloatField(db_column='FABP5', blank=True, null=True)  # Field name made lowercase.
    fabp4 = models.FloatField(db_column='FABP4', blank=True, null=True)  # Field name made lowercase.
    mmp16 = models.FloatField(db_column='MMP16', blank=True, null=True)  # Field name made lowercase.
    ncald = models.FloatField(db_column='NCALD', blank=True, null=True)  # Field name made lowercase.
    klf10 = models.FloatField(db_column='KLF10', blank=True, null=True)  # Field name made lowercase.
    enpp2 = models.FloatField(db_column='ENPP2', blank=True, null=True)  # Field name made lowercase.
    pvt1 = models.FloatField(db_column='PVT1', blank=True, null=True)  # Field name made lowercase.
    jak2 = models.FloatField(db_column='JAK2', blank=True, null=True)  # Field name made lowercase.
    psip1 = models.FloatField(db_column='PSIP1', blank=True, null=True)  # Field name made lowercase.
    plin2 = models.FloatField(db_column='PLIN2', blank=True, null=True)  # Field name made lowercase.
    rps6 = models.FloatField(db_column='RPS6', blank=True, null=True)  # Field name made lowercase.
    aldh1a1 = models.FloatField(db_column='ALDH1A1', blank=True, null=True)  # Field name made lowercase.
    frmd3 = models.FloatField(db_column='FRMD3', blank=True, null=True)  # Field name made lowercase.
    gas1 = models.FloatField(db_column='GAS1', blank=True, null=True)  # Field name made lowercase.
    baat = models.FloatField(db_column='BAAT', blank=True, null=True)  # Field name made lowercase.
    abca1 = models.FloatField(db_column='ABCA1', blank=True, null=True)  # Field name made lowercase.
    txn = models.FloatField(db_column='TXN', blank=True, null=True)  # Field name made lowercase.
    ambp = models.FloatField(db_column='AMBP', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    hspa5 = models.FloatField(db_column='HSPA5', blank=True, null=True)  # Field name made lowercase.
    angptl2 = models.FloatField(db_column='ANGPTL2', blank=True, null=True)  # Field name made lowercase.
    ptges = models.FloatField(db_column='PTGES', blank=True, null=True)  # Field name made lowercase.
    tsc1 = models.FloatField(db_column='TSC1', blank=True, null=True)  # Field name made lowercase.
    abo = models.FloatField(db_column='ABO', blank=True, null=True)  # Field name made lowercase.
    adamts13 = models.FloatField(db_column='ADAMTS13', blank=True, null=True)  # Field name made lowercase.
    ptgds = models.FloatField(db_column='PTGDS', blank=True, null=True)  # Field name made lowercase.
    klf6 = models.FloatField(db_column='KLF6', blank=True, null=True)  # Field name made lowercase.
    cdc123 = models.FloatField(db_column='CDC123', blank=True, null=True)  # Field name made lowercase.
    bambi = models.FloatField(db_column='BAMBI', blank=True, null=True)  # Field name made lowercase.
    cxcl12 = models.FloatField(db_column='CXCL12', blank=True, null=True)  # Field name made lowercase.
    mbl2 = models.FloatField(db_column='MBL2', blank=True, null=True)  # Field name made lowercase.
    tfam = models.FloatField(db_column='TFAM', blank=True, null=True)  # Field name made lowercase.
    sirt1 = models.FloatField(db_column='SIRT1', blank=True, null=True)  # Field name made lowercase.
    srgn = models.FloatField(db_column='SRGN', blank=True, null=True)  # Field name made lowercase.
    unc5b = models.FloatField(db_column='UNC5B', blank=True, null=True)  # Field name made lowercase.
    adk = models.FloatField(db_column='ADK', blank=True, null=True)  # Field name made lowercase.
    pten = models.FloatField(db_column='PTEN', blank=True, null=True)  # Field name made lowercase.
    rbp4 = models.FloatField(db_column='RBP4', blank=True, null=True)  # Field name made lowercase.
    cyp2c19 = models.FloatField(db_column='CYP2C19', blank=True, null=True)  # Field name made lowercase.
    entpd1 = models.FloatField(db_column='ENTPD1', blank=True, null=True)  # Field name made lowercase.
    tcf7l2 = models.FloatField(db_column='TCF7L2', blank=True, null=True)  # Field name made lowercase.
    bnip3 = models.FloatField(db_column='BNIP3', blank=True, null=True)  # Field name made lowercase.
    igf2 = models.FloatField(db_column='IGF2', blank=True, null=True)  # Field name made lowercase.
    ins = models.FloatField(db_column='INS', blank=True, null=True)  # Field name made lowercase.
    th = models.FloatField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    kcnq1 = models.FloatField(db_column='KCNQ1', blank=True, null=True)  # Field name made lowercase.
    hbg2 = models.FloatField(db_column='HBG2', blank=True, null=True)  # Field name made lowercase.
    smpd1 = models.FloatField(db_column='SMPD1', blank=True, null=True)  # Field name made lowercase.
    ilk = models.FloatField(db_column='ILK', blank=True, null=True)  # Field name made lowercase.
    adm = models.FloatField(db_column='ADM', blank=True, null=True)  # Field name made lowercase.
    pth = models.FloatField(db_column='PTH', blank=True, null=True)  # Field name made lowercase.
    nucb2 = models.FloatField(db_column='NUCB2', blank=True, null=True)  # Field name made lowercase.
    kcnj11 = models.FloatField(db_column='KCNJ11', blank=True, null=True)  # Field name made lowercase.
    saa1 = models.FloatField(db_column='SAA1', blank=True, null=True)  # Field name made lowercase.
    bdnf = models.FloatField(db_column='BDNF', blank=True, null=True)  # Field name made lowercase.
    wt1 = models.FloatField(db_column='WT1', blank=True, null=True)  # Field name made lowercase.
    cd59 = models.FloatField(db_column='CD59', blank=True, null=True)  # Field name made lowercase.
    pdhx = models.FloatField(db_column='PDHX', blank=True, null=True)  # Field name made lowercase.
    traf6 = models.FloatField(db_column='TRAF6', blank=True, null=True)  # Field name made lowercase.
    api5 = models.FloatField(db_column='API5', blank=True, null=True)  # Field name made lowercase.
    nr1h3 = models.FloatField(db_column='NR1H3', blank=True, null=True)  # Field name made lowercase.
    ndufs3 = models.FloatField(db_column='NDUFS3', blank=True, null=True)  # Field name made lowercase.
    folh1 = models.FloatField(db_column='FOLH1', blank=True, null=True)  # Field name made lowercase.
    aplnr = models.FloatField(db_column='APLNR', blank=True, null=True)  # Field name made lowercase.
    p2rx3 = models.FloatField(db_column='P2RX3', blank=True, null=True)  # Field name made lowercase.
    cntf = models.FloatField(db_column='CNTF', blank=True, null=True)  # Field name made lowercase.
    fads1 = models.FloatField(db_column='FADS1', blank=True, null=True)  # Field name made lowercase.
    fads2 = models.FloatField(db_column='FADS2', blank=True, null=True)  # Field name made lowercase.
    fkbp2 = models.FloatField(db_column='FKBP2', blank=True, null=True)  # Field name made lowercase.
    syvn1 = models.FloatField(db_column='SYVN1', blank=True, null=True)  # Field name made lowercase.
    pc = models.FloatField(db_column='PC', blank=True, null=True)  # Field name made lowercase.
    dhcr7 = models.FloatField(db_column='DHCR7', blank=True, null=True)  # Field name made lowercase.
    prcp = models.FloatField(db_column='PRCP', blank=True, null=True)  # Field name made lowercase.
    nox4 = models.FloatField(db_column='NOX4', blank=True, null=True)  # Field name made lowercase.
    pdgfd = models.FloatField(db_column='PDGFD', blank=True, null=True)  # Field name made lowercase.
    atm = models.FloatField(db_column='ATM', blank=True, null=True)  # Field name made lowercase.
    il18 = models.FloatField(db_column='IL18', blank=True, null=True)  # Field name made lowercase.
    apoa1 = models.FloatField(db_column='APOA1', blank=True, null=True)  # Field name made lowercase.
    hyou1 = models.FloatField(db_column='HYOU1', blank=True, null=True)  # Field name made lowercase.
    esam = models.FloatField(db_column='ESAM', blank=True, null=True)  # Field name made lowercase.
    fkbp4 = models.FloatField(db_column='FKBP4', blank=True, null=True)  # Field name made lowercase.
    fgf23 = models.FloatField(db_column='FGF23', blank=True, null=True)  # Field name made lowercase.
    ntf3 = models.FloatField(db_column='NTF3', blank=True, null=True)  # Field name made lowercase.
    vwf = models.FloatField(db_column='VWF', blank=True, null=True)  # Field name made lowercase.
    cd9 = models.FloatField(db_column='CD9', blank=True, null=True)  # Field name made lowercase.
    gapdh = models.FloatField(db_column='GAPDH', blank=True, null=True)  # Field name made lowercase.
    cd4 = models.FloatField(db_column='CD4', blank=True, null=True)  # Field name made lowercase.
    gnb3 = models.FloatField(db_column='GNB3', blank=True, null=True)  # Field name made lowercase.
    cd163 = models.FloatField(db_column='CD163', blank=True, null=True)  # Field name made lowercase.
    slc2a3 = models.FloatField(db_column='SLC2A3', blank=True, null=True)  # Field name made lowercase.
    cd69 = models.FloatField(db_column='CD69', blank=True, null=True)  # Field name made lowercase.
    irak4 = models.FloatField(db_column='IRAK4', blank=True, null=True)  # Field name made lowercase.
    vdr = models.FloatField(db_column='VDR', blank=True, null=True)  # Field name made lowercase.
    aqp5 = models.FloatField(db_column='AQP5', blank=True, null=True)  # Field name made lowercase.
    acvrl1 = models.FloatField(db_column='ACVRL1', blank=True, null=True)  # Field name made lowercase.
    nfe2 = models.FloatField(db_column='NFE2', blank=True, null=True)  # Field name made lowercase.
    cd63 = models.FloatField(db_column='CD63', blank=True, null=True)  # Field name made lowercase.
    erbb3 = models.FloatField(db_column='ERBB3', blank=True, null=True)  # Field name made lowercase.
    ddit3 = models.FloatField(db_column='DDIT3', blank=True, null=True)  # Field name made lowercase.
    ifng = models.FloatField(db_column='IFNG', blank=True, null=True)  # Field name made lowercase.
    nts = models.FloatField(db_column='NTS', blank=True, null=True)  # Field name made lowercase.
    igf1 = models.FloatField(db_column='IGF1', blank=True, null=True)  # Field name made lowercase.
    acacb = models.FloatField(db_column='ACACB', blank=True, null=True)  # Field name made lowercase.
    trpv4 = models.FloatField(db_column='TRPV4', blank=True, null=True)  # Field name made lowercase.
    atp2a2 = models.FloatField(db_column='ATP2A2', blank=True, null=True)  # Field name made lowercase.
    aldh2 = models.FloatField(db_column='ALDH2', blank=True, null=True)  # Field name made lowercase.
    nos1 = models.FloatField(db_column='NOS1', blank=True, null=True)  # Field name made lowercase.
    pebp1 = models.FloatField(db_column='PEBP1', blank=True, null=True)  # Field name made lowercase.
    psmd9 = models.FloatField(db_column='PSMD9', blank=True, null=True)  # Field name made lowercase.
    scarb1 = models.FloatField(db_column='SCARB1', blank=True, null=True)  # Field name made lowercase.
    p2rx2 = models.FloatField(db_column='P2RX2', blank=True, null=True)  # Field name made lowercase.
    alox5ap = models.FloatField(db_column='ALOX5AP', blank=True, null=True)  # Field name made lowercase.
    kl = models.FloatField(db_column='KL', blank=True, null=True)  # Field name made lowercase.
    postn = models.FloatField(db_column='POSTN', blank=True, null=True)  # Field name made lowercase.
    foxo1 = models.FloatField(db_column='FOXO1', blank=True, null=True)  # Field name made lowercase.
    htr2a = models.FloatField(db_column='HTR2A', blank=True, null=True)  # Field name made lowercase.
    gpc5 = models.FloatField(db_column='GPC5', blank=True, null=True)  # Field name made lowercase.
    irs2 = models.FloatField(db_column='IRS2', blank=True, null=True)  # Field name made lowercase.
    gas6 = models.FloatField(db_column='GAS6', blank=True, null=True)  # Field name made lowercase.
    ang = models.FloatField(db_column='ANG', blank=True, null=True)  # Field name made lowercase.
    mmp14 = models.FloatField(db_column='MMP14', blank=True, null=True)  # Field name made lowercase.
    ltb4r2 = models.FloatField(db_column='LTB4R2', blank=True, null=True)  # Field name made lowercase.
    nfkbia = models.FloatField(db_column='NFKBIA', blank=True, null=True)  # Field name made lowercase.
    bmp4 = models.FloatField(db_column='BMP4', blank=True, null=True)  # Field name made lowercase.
    rtn1 = models.FloatField(db_column='RTN1', blank=True, null=True)  # Field name made lowercase.
    pgf = models.FloatField(db_column='PGF', blank=True, null=True)  # Field name made lowercase.
    ngb = models.FloatField(db_column='NGB', blank=True, null=True)  # Field name made lowercase.
    ahsa1 = models.FloatField(db_column='AHSA1', blank=True, null=True)  # Field name made lowercase.
    bdkrb2 = models.FloatField(db_column='BDKRB2', blank=True, null=True)  # Field name made lowercase.
    bdkrb1 = models.FloatField(db_column='BDKRB1', blank=True, null=True)  # Field name made lowercase.
    akt1 = models.FloatField(db_column='AKT1', blank=True, null=True)  # Field name made lowercase.
    grem1 = models.FloatField(db_column='GREM1', blank=True, null=True)  # Field name made lowercase.
    thbs1 = models.FloatField(db_column='THBS1', blank=True, null=True)  # Field name made lowercase.
    pak6 = models.FloatField(db_column='PAK6', blank=True, null=True)  # Field name made lowercase.
    b2m = models.FloatField(db_column='B2M', blank=True, null=True)  # Field name made lowercase.
    myo5c = models.FloatField(db_column='MYO5C', blank=True, null=True)  # Field name made lowercase.
    onecut1 = models.FloatField(db_column='ONECUT1', blank=True, null=True)  # Field name made lowercase.
    adam10 = models.FloatField(db_column='ADAM10', blank=True, null=True)  # Field name made lowercase.
    ctsh = models.FloatField(db_column='CTSH', blank=True, null=True)  # Field name made lowercase.
    plin1 = models.FloatField(db_column='PLIN1', blank=True, null=True)  # Field name made lowercase.
    igf1r = models.FloatField(db_column='IGF1R', blank=True, null=True)  # Field name made lowercase.
    mrpl28 = models.FloatField(db_column='MRPL28', blank=True, null=True)  # Field name made lowercase.
    cacna1h = models.FloatField(db_column='CACNA1H', blank=True, null=True)  # Field name made lowercase.
    pdpk1 = models.FloatField(db_column='PDPK1', blank=True, null=True)  # Field name made lowercase.
    ercc4 = models.FloatField(db_column='ERCC4', blank=True, null=True)  # Field name made lowercase.
    smg1 = models.FloatField(db_column='SMG1', blank=True, null=True)  # Field name made lowercase.
    itgam = models.FloatField(db_column='ITGAM', blank=True, null=True)  # Field name made lowercase.
    fto = models.FloatField(db_column='FTO', blank=True, null=True)  # Field name made lowercase.
    mmp2 = models.FloatField(db_column='MMP2', blank=True, null=True)  # Field name made lowercase.
    slc12a3 = models.FloatField(db_column='SLC12A3', blank=True, null=True)  # Field name made lowercase.
    cetp = models.FloatField(db_column='CETP', blank=True, null=True)  # Field name made lowercase.
    cx3cl1 = models.FloatField(db_column='CX3CL1', blank=True, null=True)  # Field name made lowercase.
    cdh1 = models.FloatField(db_column='CDH1', blank=True, null=True)  # Field name made lowercase.
    nqo1 = models.FloatField(db_column='NQO1', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    znrf1 = models.FloatField(db_column='ZNRF1', blank=True, null=True)  # Field name made lowercase.
    cyba = models.FloatField(db_column='CYBA', blank=True, null=True)  # Field name made lowercase.
    tubb3 = models.FloatField(db_column='TUBB3', blank=True, null=True)  # Field name made lowercase.
    crk = models.FloatField(db_column='CRK', blank=True, null=True)  # Field name made lowercase.
    serpinf2 = models.FloatField(db_column='SERPINF2', blank=True, null=True)  # Field name made lowercase.
    serpinf1 = models.FloatField(db_column='SERPINF1', blank=True, null=True)  # Field name made lowercase.
    trpv3 = models.FloatField(db_column='TRPV3', blank=True, null=True)  # Field name made lowercase.
    cxcl16 = models.FloatField(db_column='CXCL16', blank=True, null=True)  # Field name made lowercase.
    slc2a4 = models.FloatField(db_column='SLC2A4', blank=True, null=True)  # Field name made lowercase.
    cd68 = models.FloatField(db_column='CD68', blank=True, null=True)  # Field name made lowercase.
    shbg = models.FloatField(db_column='SHBG', blank=True, null=True)  # Field name made lowercase.
    pmp22 = models.FloatField(db_column='PMP22', blank=True, null=True)  # Field name made lowercase.
    srebf1 = models.FloatField(db_column='SREBF1', blank=True, null=True)  # Field name made lowercase.
    mapk7 = models.FloatField(db_column='MAPK7', blank=True, null=True)  # Field name made lowercase.
    ccl2 = models.FloatField(db_column='CCL2', blank=True, null=True)  # Field name made lowercase.
    ccl5 = models.FloatField(db_column='CCL5', blank=True, null=True)  # Field name made lowercase.
    hnf1b = models.FloatField(db_column='HNF1B', blank=True, null=True)  # Field name made lowercase.
    erbb2 = models.FloatField(db_column='ERBB2', blank=True, null=True)  # Field name made lowercase.
    fkbp10 = models.FloatField(db_column='FKBP10', blank=True, null=True)  # Field name made lowercase.
    stat5a = models.FloatField(db_column='STAT5A', blank=True, null=True)  # Field name made lowercase.
    stat3 = models.FloatField(db_column='STAT3', blank=True, null=True)  # Field name made lowercase.
    naglu = models.FloatField(db_column='NAGLU', blank=True, null=True)  # Field name made lowercase.
    aoc2 = models.FloatField(db_column='AOC2', blank=True, null=True)  # Field name made lowercase.
    aoc3 = models.FloatField(db_column='AOC3', blank=True, null=True)  # Field name made lowercase.
    ppy = models.FloatField(db_column='PPY', blank=True, null=True)  # Field name made lowercase.
    sth = models.FloatField(db_column='STH', blank=True, null=True)  # Field name made lowercase.
    itgb3 = models.FloatField(db_column='ITGB3', blank=True, null=True)  # Field name made lowercase.
    gip = models.FloatField(db_column='GIP', blank=True, null=True)  # Field name made lowercase.
    mpo = models.FloatField(db_column='MPO', blank=True, null=True)  # Field name made lowercase.
    pecam1 = models.FloatField(db_column='PECAM1', blank=True, null=True)  # Field name made lowercase.
    sox9 = models.FloatField(db_column='SOX9', blank=True, null=True)  # Field name made lowercase.
    timp2 = models.FloatField(db_column='TIMP2', blank=True, null=True)  # Field name made lowercase.
    dcxr = models.FloatField(db_column='DCXR', blank=True, null=True)  # Field name made lowercase.
    fasn = models.FloatField(db_column='FASN', blank=True, null=True)  # Field name made lowercase.
    colec12 = models.FloatField(db_column='COLEC12', blank=True, null=True)  # Field name made lowercase.
    adcyap1 = models.FloatField(db_column='ADCYAP1', blank=True, null=True)  # Field name made lowercase.
    smad7 = models.FloatField(db_column='SMAD7', blank=True, null=True)  # Field name made lowercase.
    nedd4l = models.FloatField(db_column='NEDD4L', blank=True, null=True)  # Field name made lowercase.
    mc4r = models.FloatField(db_column='MC4R', blank=True, null=True)  # Field name made lowercase.
    bcl2 = models.FloatField(db_column='BCL2', blank=True, null=True)  # Field name made lowercase.
    cndp2 = models.FloatField(db_column='CNDP2', blank=True, null=True)  # Field name made lowercase.
    znf236 = models.FloatField(db_column='ZNF236', blank=True, null=True)  # Field name made lowercase.
    stk11 = models.FloatField(db_column='STK11', blank=True, null=True)  # Field name made lowercase.
    sirt6 = models.FloatField(db_column='SIRT6', blank=True, null=True)  # Field name made lowercase.
    uhrf1 = models.FloatField(db_column='UHRF1', blank=True, null=True)  # Field name made lowercase.
    timm44 = models.FloatField(db_column='TIMM44', blank=True, null=True)  # Field name made lowercase.
    angptl4 = models.FloatField(db_column='ANGPTL4', blank=True, null=True)  # Field name made lowercase.
    dnmt1 = models.FloatField(db_column='DNMT1', blank=True, null=True)  # Field name made lowercase.
    icam1 = models.FloatField(db_column='ICAM1', blank=True, null=True)  # Field name made lowercase.
    ldlr = models.FloatField(db_column='LDLR', blank=True, null=True)  # Field name made lowercase.
    epor = models.FloatField(db_column='EPOR', blank=True, null=True)  # Field name made lowercase.
    prdx2 = models.FloatField(db_column='PRDX2', blank=True, null=True)  # Field name made lowercase.
    ptger1 = models.FloatField(db_column='PTGER1', blank=True, null=True)  # Field name made lowercase.
    unc13a = models.FloatField(db_column='UNC13A', blank=True, null=True)  # Field name made lowercase.
    gdf15 = models.FloatField(db_column='GDF15', blank=True, null=True)  # Field name made lowercase.
    fkbp8 = models.FloatField(db_column='FKBP8', blank=True, null=True)  # Field name made lowercase.
    usf2 = models.FloatField(db_column='USF2', blank=True, null=True)  # Field name made lowercase.
    ffar1 = models.FloatField(db_column='FFAR1', blank=True, null=True)  # Field name made lowercase.
    ffar2 = models.FloatField(db_column='FFAR2', blank=True, null=True)  # Field name made lowercase.
    nphs1 = models.FloatField(db_column='NPHS1', blank=True, null=True)  # Field name made lowercase.
    tgfb1 = models.FloatField(db_column='TGFB1', blank=True, null=True)  # Field name made lowercase.
    xrcc1 = models.FloatField(db_column='XRCC1', blank=True, null=True)  # Field name made lowercase.
    ercc1 = models.FloatField(db_column='ERCC1', blank=True, null=True)  # Field name made lowercase.
    gipr = models.FloatField(db_column='GIPR', blank=True, null=True)  # Field name made lowercase.
    fgf21 = models.FloatField(db_column='FGF21', blank=True, null=True)  # Field name made lowercase.
    clec11a = models.FloatField(db_column='CLEC11A', blank=True, null=True)  # Field name made lowercase.
    fpr1 = models.FloatField(db_column='FPR1', blank=True, null=True)  # Field name made lowercase.
    trib3 = models.FloatField(db_column='TRIB3', blank=True, null=True)  # Field name made lowercase.
    bmp2 = models.FloatField(db_column='BMP2', blank=True, null=True)  # Field name made lowercase.
    thbd = models.FloatField(db_column='THBD', blank=True, null=True)  # Field name made lowercase.
    cst3 = models.FloatField(db_column='CST3', blank=True, null=True)  # Field name made lowercase.
    id1 = models.FloatField(db_column='ID1', blank=True, null=True)  # Field name made lowercase.
    src = models.FloatField(db_column='SRC', blank=True, null=True)  # Field name made lowercase.
    mafb = models.FloatField(db_column='MAFB', blank=True, null=True)  # Field name made lowercase.
    sgk2 = models.FloatField(db_column='SGK2', blank=True, null=True)  # Field name made lowercase.
    hnf4a = models.FloatField(db_column='HNF4A', blank=True, null=True)  # Field name made lowercase.
    pltp = models.FloatField(db_column='PLTP', blank=True, null=True)  # Field name made lowercase.
    mmp9 = models.FloatField(db_column='MMP9', blank=True, null=True)  # Field name made lowercase.
    cd40 = models.FloatField(db_column='CD40', blank=True, null=True)  # Field name made lowercase.
    ptpn1 = models.FloatField(db_column='PTPN1', blank=True, null=True)  # Field name made lowercase.
    cyp24a1 = models.FloatField(db_column='CYP24A1', blank=True, null=True)  # Field name made lowercase.
    rcan1 = models.FloatField(db_column='RCAN1', blank=True, null=True)  # Field name made lowercase.
    abcg1 = models.FloatField(db_column='ABCG1', blank=True, null=True)  # Field name made lowercase.
    prmt2 = models.FloatField(db_column='PRMT2', blank=True, null=True)  # Field name made lowercase.
    comt = models.FloatField(db_column='COMT', blank=True, null=True)  # Field name made lowercase.
    mapk1 = models.FloatField(db_column='MAPK1', blank=True, null=True)  # Field name made lowercase.
    mif = models.FloatField(db_column='MIF', blank=True, null=True)  # Field name made lowercase.
    ggt1 = models.FloatField(db_column='GGT1', blank=True, null=True)  # Field name made lowercase.
    xbp1 = models.FloatField(db_column='XBP1', blank=True, null=True)  # Field name made lowercase.
    osm = models.FloatField(db_column='OSM', blank=True, null=True)  # Field name made lowercase.
    limk2 = models.FloatField(db_column='LIMK2', blank=True, null=True)  # Field name made lowercase.
    sfi1 = models.FloatField(db_column='SFI1', blank=True, null=True)  # Field name made lowercase.
    timp3 = models.FloatField(db_column='TIMP3', blank=True, null=True)  # Field name made lowercase.
    hmox1 = models.FloatField(db_column='HMOX1', blank=True, null=True)  # Field name made lowercase.
    apol1 = models.FloatField(db_column='APOL1', blank=True, null=True)  # Field name made lowercase.
    myh9 = models.FloatField(db_column='MYH9', blank=True, null=True)  # Field name made lowercase.
    pdgfb = models.FloatField(db_column='PDGFB', blank=True, null=True)  # Field name made lowercase.
    atf4 = models.FloatField(db_column='ATF4', blank=True, null=True)  # Field name made lowercase.
    tspo = models.FloatField(db_column='TSPO', blank=True, null=True)  # Field name made lowercase.
    miox = models.FloatField(db_column='MIOX', blank=True, null=True)  # Field name made lowercase.
    prdx4 = models.FloatField(db_column='PRDX4', blank=True, null=True)  # Field name made lowercase.
    gk = models.FloatField(db_column='GK', blank=True, null=True)  # Field name made lowercase.
    rgn = models.FloatField(db_column='RGN', blank=True, null=True)  # Field name made lowercase.
    timp1 = models.FloatField(db_column='TIMP1', blank=True, null=True)  # Field name made lowercase.
    clcn5 = models.FloatField(db_column='CLCN5', blank=True, null=True)  # Field name made lowercase.
    ar = models.FloatField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    foxo4 = models.FloatField(db_column='FOXO4', blank=True, null=True)  # Field name made lowercase.
    rps6ka6 = models.FloatField(db_column='RPS6KA6', blank=True, null=True)  # Field name made lowercase.
    nox1 = models.FloatField(db_column='NOX1', blank=True, null=True)  # Field name made lowercase.
    xiap = models.FloatField(db_column='XIAP', blank=True, null=True)  # Field name made lowercase.
    cd40lg = models.FloatField(db_column='CD40LG', blank=True, null=True)  # Field name made lowercase.
    l1cam = models.FloatField(db_column='L1CAM', blank=True, null=True)  # Field name made lowercase.
    irak1 = models.FloatField(db_column='IRAK1', blank=True, null=True)  # Field name made lowercase.
    g6pd = models.FloatField(db_column='G6PD', blank=True, null=True)  # Field name made lowercase.
    f8 = models.FloatField(db_column='F8', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diaco_tissue_brain_frontal_cortex_ba9'


class DiacoTissueLiver(models.Model):
    subjid = models.CharField(db_column='SUBJID', max_length=50, primary_key=True)  # Field name made lowercase.
    sampid = models.CharField(db_column='SAMPID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sesso = models.CharField(db_column='Sesso', max_length=1)  # Field name made lowercase.
    eta = models.CharField(db_column='Età', max_length=50, blank=True, null=True)  # Field name made lowercase.
    classificazione_morte = models.CharField(db_column='Classificazione morte', max_length=230)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    errfi1 = models.FloatField(db_column='ERRFI1', blank=True, null=True)  # Field name made lowercase.
    mad2l2 = models.FloatField(db_column='MAD2L2', blank=True, null=True)  # Field name made lowercase.
    mthfr = models.FloatField(db_column='MTHFR', blank=True, null=True)  # Field name made lowercase.
    nppa = models.FloatField(db_column='NPPA', blank=True, null=True)  # Field name made lowercase.
    tnfrsf1b = models.FloatField(db_column='TNFRSF1B', blank=True, null=True)  # Field name made lowercase.
    pla2g2a = models.FloatField(db_column='PLA2G2A', blank=True, null=True)  # Field name made lowercase.
    alpl = models.FloatField(db_column='ALPL', blank=True, null=True)  # Field name made lowercase.
    hspg2 = models.FloatField(db_column='HSPG2', blank=True, null=True)  # Field name made lowercase.
    cnr2 = models.FloatField(db_column='CNR2', blank=True, null=True)  # Field name made lowercase.
    slc9a1 = models.FloatField(db_column='SLC9A1', blank=True, null=True)  # Field name made lowercase.
    col8a2 = models.FloatField(db_column='COL8A2', blank=True, null=True)  # Field name made lowercase.
    cap1 = models.FloatField(db_column='CAP1', blank=True, null=True)  # Field name made lowercase.
    slc2a1 = models.FloatField(db_column='SLC2A1', blank=True, null=True)  # Field name made lowercase.
    cyp2j2 = models.FloatField(db_column='CYP2J2', blank=True, null=True)  # Field name made lowercase.
    ddah1 = models.FloatField(db_column='DDAH1', blank=True, null=True)  # Field name made lowercase.
    cyr61 = models.FloatField(db_column='CYR61', blank=True, null=True)  # Field name made lowercase.
    ngf = models.FloatField(db_column='NGF', blank=True, null=True)  # Field name made lowercase.
    hmgcs2 = models.FloatField(db_column='HMGCS2', blank=True, null=True)  # Field name made lowercase.
    ctss = models.FloatField(db_column='CTSS', blank=True, null=True)  # Field name made lowercase.
    s100a12 = models.FloatField(db_column='S100A12', blank=True, null=True)  # Field name made lowercase.
    lmna = models.FloatField(db_column='LMNA', blank=True, null=True)  # Field name made lowercase.
    cd247 = models.FloatField(db_column='CD247', blank=True, null=True)  # Field name made lowercase.
    sele = models.FloatField(db_column='SELE', blank=True, null=True)  # Field name made lowercase.
    fmo3 = models.FloatField(db_column='FMO3', blank=True, null=True)  # Field name made lowercase.
    prdx6 = models.FloatField(db_column='PRDX6', blank=True, null=True)  # Field name made lowercase.
    glul = models.FloatField(db_column='GLUL', blank=True, null=True)  # Field name made lowercase.
    lamc1 = models.FloatField(db_column='LAMC1', blank=True, null=True)  # Field name made lowercase.
    ptgs2 = models.FloatField(db_column='PTGS2', blank=True, null=True)  # Field name made lowercase.
    chi3l1 = models.FloatField(db_column='CHI3L1', blank=True, null=True)  # Field name made lowercase.
    chit1 = models.FloatField(db_column='CHIT1', blank=True, null=True)  # Field name made lowercase.
    fmod = models.FloatField(db_column='FMOD', blank=True, null=True)  # Field name made lowercase.
    il10 = models.FloatField(db_column='IL10', blank=True, null=True)  # Field name made lowercase.
    pfkfb2 = models.FloatField(db_column='PFKFB2', blank=True, null=True)  # Field name made lowercase.
    cd34 = models.FloatField(db_column='CD34', blank=True, null=True)  # Field name made lowercase.
    cog2 = models.FloatField(db_column='COG2', blank=True, null=True)  # Field name made lowercase.
    nlrp3 = models.FloatField(db_column='NLRP3', blank=True, null=True)  # Field name made lowercase.
    rock2 = models.FloatField(db_column='ROCK2', blank=True, null=True)  # Field name made lowercase.
    apob = models.FloatField(db_column='APOB', blank=True, null=True)  # Field name made lowercase.
    pomc = models.FloatField(db_column='POMC', blank=True, null=True)  # Field name made lowercase.
    gckr = models.FloatField(db_column='GCKR', blank=True, null=True)  # Field name made lowercase.
    plekhh2 = models.FloatField(db_column='PLEKHH2', blank=True, null=True)  # Field name made lowercase.
    prkce = models.FloatField(db_column='PRKCE', blank=True, null=True)  # Field name made lowercase.
    pigf = models.FloatField(db_column='PIGF', blank=True, null=True)  # Field name made lowercase.
    msh2 = models.FloatField(db_column='MSH2', blank=True, null=True)  # Field name made lowercase.
    gfpt1 = models.FloatField(db_column='GFPT1', blank=True, null=True)  # Field name made lowercase.
    tacr1 = models.FloatField(db_column='TACR1', blank=True, null=True)  # Field name made lowercase.
    reg1a = models.FloatField(db_column='REG1A', blank=True, null=True)  # Field name made lowercase.
    eif2ak3 = models.FloatField(db_column='EIF2AK3', blank=True, null=True)  # Field name made lowercase.
    adra2b = models.FloatField(db_column='ADRA2B', blank=True, null=True)  # Field name made lowercase.
    il1b = models.FloatField(db_column='IL1B', blank=True, null=True)  # Field name made lowercase.
    proc = models.FloatField(db_column='PROC', blank=True, null=True)  # Field name made lowercase.
    polr2d = models.FloatField(db_column='POLR2D', blank=True, null=True)  # Field name made lowercase.
    zeb2 = models.FloatField(db_column='ZEB2', blank=True, null=True)  # Field name made lowercase.
    acvr1c = models.FloatField(db_column='ACVR1C', blank=True, null=True)  # Field name made lowercase.
    dpp4 = models.FloatField(db_column='DPP4', blank=True, null=True)  # Field name made lowercase.
    nfe2l2 = models.FloatField(db_column='NFE2L2', blank=True, null=True)  # Field name made lowercase.
    igfbp5 = models.FloatField(db_column='IGFBP5', blank=True, null=True)  # Field name made lowercase.
    ccl20 = models.FloatField(db_column='CCL20', blank=True, null=True)  # Field name made lowercase.
    hdac4 = models.FloatField(db_column='HDAC4', blank=True, null=True)  # Field name made lowercase.
    capn10 = models.FloatField(db_column='CAPN10', blank=True, null=True)  # Field name made lowercase.
    ghrl = models.FloatField(db_column='GHRL', blank=True, null=True)  # Field name made lowercase.
    pparg = models.FloatField(db_column='PPARG', blank=True, null=True)  # Field name made lowercase.
    raf1 = models.FloatField(db_column='RAF1', blank=True, null=True)  # Field name made lowercase.
    myd88 = models.FloatField(db_column='MYD88', blank=True, null=True)  # Field name made lowercase.
    cx3cr1 = models.FloatField(db_column='CX3CR1', blank=True, null=True)  # Field name made lowercase.
    cck = models.FloatField(db_column='CCK', blank=True, null=True)  # Field name made lowercase.
    exosc7 = models.FloatField(db_column='EXOSC7', blank=True, null=True)  # Field name made lowercase.
    ccr1 = models.FloatField(db_column='CCR1', blank=True, null=True)  # Field name made lowercase.
    ccr5 = models.FloatField(db_column='CCR5', blank=True, null=True)  # Field name made lowercase.
    gpx1 = models.FloatField(db_column='GPX1', blank=True, null=True)  # Field name made lowercase.
    rhoa = models.FloatField(db_column='RHOA', blank=True, null=True)  # Field name made lowercase.
    cish = models.FloatField(db_column='CISH', blank=True, null=True)  # Field name made lowercase.
    tkt = models.FloatField(db_column='TKT', blank=True, null=True)  # Field name made lowercase.
    appl1 = models.FloatField(db_column='APPL1', blank=True, null=True)  # Field name made lowercase.
    slmap = models.FloatField(db_column='SLMAP', blank=True, null=True)  # Field name made lowercase.
    col8a1 = models.FloatField(db_column='COL8A1', blank=True, null=True)  # Field name made lowercase.
    cd47 = models.FloatField(db_column='CD47', blank=True, null=True)  # Field name made lowercase.
    gap43 = models.FloatField(db_column='GAP43', blank=True, null=True)  # Field name made lowercase.
    cd80 = models.FloatField(db_column='CD80', blank=True, null=True)  # Field name made lowercase.
    rho = models.FloatField(db_column='RHO', blank=True, null=True)  # Field name made lowercase.
    trh = models.FloatField(db_column='TRH', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='TF', blank=True, null=True)  # Field name made lowercase.
    rbp1 = models.FloatField(db_column='RBP1', blank=True, null=True)  # Field name made lowercase.
    trpc1 = models.FloatField(db_column='TRPC1', blank=True, null=True)  # Field name made lowercase.
    agtr1 = models.FloatField(db_column='AGTR1', blank=True, null=True)  # Field name made lowercase.
    sucnr1 = models.FloatField(db_column='SUCNR1', blank=True, null=True)  # Field name made lowercase.
    p2ry1 = models.FloatField(db_column='P2RY1', blank=True, null=True)  # Field name made lowercase.
    mme = models.FloatField(db_column='MME', blank=True, null=True)  # Field name made lowercase.
    slc2a2 = models.FloatField(db_column='SLC2A2', blank=True, null=True)  # Field name made lowercase.
    pik3ca = models.FloatField(db_column='PIK3CA', blank=True, null=True)  # Field name made lowercase.
    parl = models.FloatField(db_column='PARL', blank=True, null=True)  # Field name made lowercase.
    ahsg = models.FloatField(db_column='AHSG', blank=True, null=True)  # Field name made lowercase.
    adipoq = models.FloatField(db_column='ADIPOQ', blank=True, null=True)  # Field name made lowercase.
    spon2 = models.FloatField(db_column='SPON2', blank=True, null=True)  # Field name made lowercase.
    wfs1 = models.FloatField(db_column='WFS1', blank=True, null=True)  # Field name made lowercase.
    cd38 = models.FloatField(db_column='CD38', blank=True, null=True)  # Field name made lowercase.
    prom1 = models.FloatField(db_column='PROM1', blank=True, null=True)  # Field name made lowercase.
    ppargc1a = models.FloatField(db_column='PPARGC1A', blank=True, null=True)  # Field name made lowercase.
    igfbp7 = models.FloatField(db_column='IGFBP7', blank=True, null=True)  # Field name made lowercase.
    cxcl5 = models.FloatField(db_column='CXCL5', blank=True, null=True)  # Field name made lowercase.
    cxcl9 = models.FloatField(db_column='CXCL9', blank=True, null=True)  # Field name made lowercase.
    cxcl10 = models.FloatField(db_column='CXCL10', blank=True, null=True)  # Field name made lowercase.
    cxcl11 = models.FloatField(db_column='CXCL11', blank=True, null=True)  # Field name made lowercase.
    hpse = models.FloatField(db_column='HPSE', blank=True, null=True)  # Field name made lowercase.
    spp1 = models.FloatField(db_column='SPP1', blank=True, null=True)  # Field name made lowercase.
    adh1b = models.FloatField(db_column='ADH1B', blank=True, null=True)  # Field name made lowercase.
    egf = models.FloatField(db_column='EGF', blank=True, null=True)  # Field name made lowercase.
    alpk1 = models.FloatField(db_column='ALPK1', blank=True, null=True)  # Field name made lowercase.
    fabp2 = models.FloatField(db_column='FABP2', blank=True, null=True)  # Field name made lowercase.
    pde5a = models.FloatField(db_column='PDE5A', blank=True, null=True)  # Field name made lowercase.
    setd7 = models.FloatField(db_column='SETD7', blank=True, null=True)  # Field name made lowercase.
    smad1 = models.FloatField(db_column='SMAD1', blank=True, null=True)  # Field name made lowercase.
    ednra = models.FloatField(db_column='EDNRA', blank=True, null=True)  # Field name made lowercase.
    nr3c2 = models.FloatField(db_column='NR3C2', blank=True, null=True)  # Field name made lowercase.
    tlr2 = models.FloatField(db_column='TLR2', blank=True, null=True)  # Field name made lowercase.
    npy5r = models.FloatField(db_column='NPY5R', blank=True, null=True)  # Field name made lowercase.
    fbxo8 = models.FloatField(db_column='FBXO8', blank=True, null=True)  # Field name made lowercase.
    vegfc = models.FloatField(db_column='VEGFC', blank=True, null=True)  # Field name made lowercase.
    acsl1 = models.FloatField(db_column='ACSL1', blank=True, null=True)  # Field name made lowercase.
    sorbs2 = models.FloatField(db_column='SORBS2', blank=True, null=True)  # Field name made lowercase.
    f11 = models.FloatField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    basp1 = models.FloatField(db_column='BASP1', blank=True, null=True)  # Field name made lowercase.
    ptger4 = models.FloatField(db_column='PTGER4', blank=True, null=True)  # Field name made lowercase.
    prkaa1 = models.FloatField(db_column='PRKAA1', blank=True, null=True)  # Field name made lowercase.
    ghr = models.FloatField(db_column='GHR', blank=True, null=True)  # Field name made lowercase.
    itga2 = models.FloatField(db_column='ITGA2', blank=True, null=True)  # Field name made lowercase.
    cdk7 = models.FloatField(db_column='CDK7', blank=True, null=True)  # Field name made lowercase.
    f2r = models.FloatField(db_column='F2R', blank=True, null=True)  # Field name made lowercase.
    erap2 = models.FloatField(db_column='ERAP2', blank=True, null=True)  # Field name made lowercase.
    apc = models.FloatField(db_column='APC', blank=True, null=True)  # Field name made lowercase.
    tnfaip8 = models.FloatField(db_column='TNFAIP8', blank=True, null=True)  # Field name made lowercase.
    vdac1 = models.FloatField(db_column='VDAC1', blank=True, null=True)  # Field name made lowercase.
    pdgfrb = models.FloatField(db_column='PDGFRB', blank=True, null=True)  # Field name made lowercase.
    cd74 = models.FloatField(db_column='CD74', blank=True, null=True)  # Field name made lowercase.
    sparc = models.FloatField(db_column='SPARC', blank=True, null=True)  # Field name made lowercase.
    ebf1 = models.FloatField(db_column='EBF1', blank=True, null=True)  # Field name made lowercase.
    gfpt2 = models.FloatField(db_column='GFPT2', blank=True, null=True)  # Field name made lowercase.
    rreb1 = models.FloatField(db_column='RREB1', blank=True, null=True)  # Field name made lowercase.
    edn1 = models.FloatField(db_column='EDN1', blank=True, null=True)  # Field name made lowercase.
    cdkal1 = models.FloatField(db_column='CDKAL1', blank=True, null=True)  # Field name made lowercase.
    hfe = models.FloatField(db_column='HFE', blank=True, null=True)  # Field name made lowercase.
    hla_a = models.FloatField(db_column='HLA-A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lta = models.FloatField(db_column='LTA', blank=True, null=True)  # Field name made lowercase.
    tnf = models.FloatField(db_column='TNF', blank=True, null=True)  # Field name made lowercase.
    hspa1a = models.FloatField(db_column='HSPA1A', blank=True, null=True)  # Field name made lowercase.
    hspa1b = models.FloatField(db_column='HSPA1B', blank=True, null=True)  # Field name made lowercase.
    hla_dqa1 = models.FloatField(db_column='HLA-DQA1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mapk14 = models.FloatField(db_column='MAPK14', blank=True, null=True)  # Field name made lowercase.
    cdkn1a = models.FloatField(db_column='CDKN1A', blank=True, null=True)  # Field name made lowercase.
    glo1 = models.FloatField(db_column='GLO1', blank=True, null=True)  # Field name made lowercase.
    vegfa = models.FloatField(db_column='VEGFA', blank=True, null=True)  # Field name made lowercase.
    cd2ap = models.FloatField(db_column='CD2AP', blank=True, null=True)  # Field name made lowercase.
    cnr1 = models.FloatField(db_column='CNR1', blank=True, null=True)  # Field name made lowercase.
    enpp1 = models.FloatField(db_column='ENPP1', blank=True, null=True)  # Field name made lowercase.
    ctgf = models.FloatField(db_column='CTGF', blank=True, null=True)  # Field name made lowercase.
    rps12 = models.FloatField(db_column='RPS12', blank=True, null=True)  # Field name made lowercase.
    sgk1 = models.FloatField(db_column='SGK1', blank=True, null=True)  # Field name made lowercase.
    map3k5 = models.FloatField(db_column='MAP3K5', blank=True, null=True)  # Field name made lowercase.
    cited2 = models.FloatField(db_column='CITED2', blank=True, null=True)  # Field name made lowercase.
    utrn = models.FloatField(db_column='UTRN', blank=True, null=True)  # Field name made lowercase.
    mthfd1l = models.FloatField(db_column='MTHFD1L', blank=True, null=True)  # Field name made lowercase.
    vip = models.FloatField(db_column='VIP', blank=True, null=True)  # Field name made lowercase.
    sod2 = models.FloatField(db_column='SOD2', blank=True, null=True)  # Field name made lowercase.
    lpa = models.FloatField(db_column='LPA', blank=True, null=True)  # Field name made lowercase.
    thbs2 = models.FloatField(db_column='THBS2', blank=True, null=True)  # Field name made lowercase.
    pdgfa = models.FloatField(db_column='PDGFA', blank=True, null=True)  # Field name made lowercase.
    il6 = models.FloatField(db_column='IL6', blank=True, null=True)  # Field name made lowercase.
    npy = models.FloatField(db_column='NPY', blank=True, null=True)  # Field name made lowercase.
    jazf1 = models.FloatField(db_column='JAZF1', blank=True, null=True)  # Field name made lowercase.
    cpvl = models.FloatField(db_column='CPVL', blank=True, null=True)  # Field name made lowercase.
    aqp1 = models.FloatField(db_column='AQP1', blank=True, null=True)  # Field name made lowercase.
    elmo1 = models.FloatField(db_column='ELMO1', blank=True, null=True)  # Field name made lowercase.
    igfbp3 = models.FloatField(db_column='IGFBP3', blank=True, null=True)  # Field name made lowercase.
    egfr = models.FloatField(db_column='EGFR', blank=True, null=True)  # Field name made lowercase.
    eln = models.FloatField(db_column='ELN', blank=True, null=True)  # Field name made lowercase.
    ncf1 = models.FloatField(db_column='NCF1', blank=True, null=True)  # Field name made lowercase.
    hspb1 = models.FloatField(db_column='HSPB1', blank=True, null=True)  # Field name made lowercase.
    sema3a = models.FloatField(db_column='SEMA3A', blank=True, null=True)  # Field name made lowercase.
    pon3 = models.FloatField(db_column='PON3', blank=True, null=True)  # Field name made lowercase.
    pon2 = models.FloatField(db_column='PON2', blank=True, null=True)  # Field name made lowercase.
    nampt = models.FloatField(db_column='NAMPT', blank=True, null=True)  # Field name made lowercase.
    cav1 = models.FloatField(db_column='CAV1', blank=True, null=True)  # Field name made lowercase.
    lep = models.FloatField(db_column='LEP', blank=True, null=True)  # Field name made lowercase.
    akr1b1 = models.FloatField(db_column='AKR1B1', blank=True, null=True)  # Field name made lowercase.
    akr1b10 = models.FloatField(db_column='AKR1B10', blank=True, null=True)  # Field name made lowercase.
    pip = models.FloatField(db_column='PIP', blank=True, null=True)  # Field name made lowercase.
    rarres2 = models.FloatField(db_column='RARRES2', blank=True, null=True)  # Field name made lowercase.
    nos3 = models.FloatField(db_column='NOS3', blank=True, null=True)  # Field name made lowercase.
    angpt2 = models.FloatField(db_column='ANGPT2', blank=True, null=True)  # Field name made lowercase.
    defa1 = models.FloatField(db_column='DEFA1', blank=True, null=True)  # Field name made lowercase.
    lpl = models.FloatField(db_column='LPL', blank=True, null=True)  # Field name made lowercase.
    ebf2 = models.FloatField(db_column='EBF2', blank=True, null=True)  # Field name made lowercase.
    adrb3 = models.FloatField(db_column='ADRB3', blank=True, null=True)  # Field name made lowercase.
    eif4ebp1 = models.FloatField(db_column='EIF4EBP1', blank=True, null=True)  # Field name made lowercase.
    fgfr1 = models.FloatField(db_column='FGFR1', blank=True, null=True)  # Field name made lowercase.
    crh = models.FloatField(db_column='CRH', blank=True, null=True)  # Field name made lowercase.
    sgk3 = models.FloatField(db_column='SGK3', blank=True, null=True)  # Field name made lowercase.
    fabp5 = models.FloatField(db_column='FABP5', blank=True, null=True)  # Field name made lowercase.
    fabp4 = models.FloatField(db_column='FABP4', blank=True, null=True)  # Field name made lowercase.
    mmp16 = models.FloatField(db_column='MMP16', blank=True, null=True)  # Field name made lowercase.
    ncald = models.FloatField(db_column='NCALD', blank=True, null=True)  # Field name made lowercase.
    klf10 = models.FloatField(db_column='KLF10', blank=True, null=True)  # Field name made lowercase.
    enpp2 = models.FloatField(db_column='ENPP2', blank=True, null=True)  # Field name made lowercase.
    pvt1 = models.FloatField(db_column='PVT1', blank=True, null=True)  # Field name made lowercase.
    jak2 = models.FloatField(db_column='JAK2', blank=True, null=True)  # Field name made lowercase.
    psip1 = models.FloatField(db_column='PSIP1', blank=True, null=True)  # Field name made lowercase.
    plin2 = models.FloatField(db_column='PLIN2', blank=True, null=True)  # Field name made lowercase.
    rps6 = models.FloatField(db_column='RPS6', blank=True, null=True)  # Field name made lowercase.
    aldh1a1 = models.FloatField(db_column='ALDH1A1', blank=True, null=True)  # Field name made lowercase.
    frmd3 = models.FloatField(db_column='FRMD3', blank=True, null=True)  # Field name made lowercase.
    gas1 = models.FloatField(db_column='GAS1', blank=True, null=True)  # Field name made lowercase.
    baat = models.FloatField(db_column='BAAT', blank=True, null=True)  # Field name made lowercase.
    abca1 = models.FloatField(db_column='ABCA1', blank=True, null=True)  # Field name made lowercase.
    txn = models.FloatField(db_column='TXN', blank=True, null=True)  # Field name made lowercase.
    ambp = models.FloatField(db_column='AMBP', blank=True, null=True)  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5', blank=True, null=True)  # Field name made lowercase.
    hspa5 = models.FloatField(db_column='HSPA5', blank=True, null=True)  # Field name made lowercase.
    angptl2 = models.FloatField(db_column='ANGPTL2', blank=True, null=True)  # Field name made lowercase.
    ptges = models.FloatField(db_column='PTGES', blank=True, null=True)  # Field name made lowercase.
    tsc1 = models.FloatField(db_column='TSC1', blank=True, null=True)  # Field name made lowercase.
    abo = models.FloatField(db_column='ABO', blank=True, null=True)  # Field name made lowercase.
    adamts13 = models.FloatField(db_column='ADAMTS13', blank=True, null=True)  # Field name made lowercase.
    ptgds = models.FloatField(db_column='PTGDS', blank=True, null=True)  # Field name made lowercase.
    klf6 = models.FloatField(db_column='KLF6', blank=True, null=True)  # Field name made lowercase.
    cdc123 = models.FloatField(db_column='CDC123', blank=True, null=True)  # Field name made lowercase.
    bambi = models.FloatField(db_column='BAMBI', blank=True, null=True)  # Field name made lowercase.
    cxcl12 = models.FloatField(db_column='CXCL12', blank=True, null=True)  # Field name made lowercase.
    mbl2 = models.FloatField(db_column='MBL2', blank=True, null=True)  # Field name made lowercase.
    tfam = models.FloatField(db_column='TFAM', blank=True, null=True)  # Field name made lowercase.
    sirt1 = models.FloatField(db_column='SIRT1', blank=True, null=True)  # Field name made lowercase.
    srgn = models.FloatField(db_column='SRGN', blank=True, null=True)  # Field name made lowercase.
    unc5b = models.FloatField(db_column='UNC5B', blank=True, null=True)  # Field name made lowercase.
    adk = models.FloatField(db_column='ADK', blank=True, null=True)  # Field name made lowercase.
    pten = models.FloatField(db_column='PTEN', blank=True, null=True)  # Field name made lowercase.
    rbp4 = models.FloatField(db_column='RBP4', blank=True, null=True)  # Field name made lowercase.
    cyp2c19 = models.FloatField(db_column='CYP2C19', blank=True, null=True)  # Field name made lowercase.
    entpd1 = models.FloatField(db_column='ENTPD1', blank=True, null=True)  # Field name made lowercase.
    tcf7l2 = models.FloatField(db_column='TCF7L2', blank=True, null=True)  # Field name made lowercase.
    bnip3 = models.FloatField(db_column='BNIP3', blank=True, null=True)  # Field name made lowercase.
    igf2 = models.FloatField(db_column='IGF2', blank=True, null=True)  # Field name made lowercase.
    ins = models.FloatField(db_column='INS', blank=True, null=True)  # Field name made lowercase.
    th = models.FloatField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    kcnq1 = models.FloatField(db_column='KCNQ1', blank=True, null=True)  # Field name made lowercase.
    hbg2 = models.FloatField(db_column='HBG2', blank=True, null=True)  # Field name made lowercase.
    smpd1 = models.FloatField(db_column='SMPD1', blank=True, null=True)  # Field name made lowercase.
    ilk = models.FloatField(db_column='ILK', blank=True, null=True)  # Field name made lowercase.
    adm = models.FloatField(db_column='ADM', blank=True, null=True)  # Field name made lowercase.
    pth = models.FloatField(db_column='PTH', blank=True, null=True)  # Field name made lowercase.
    nucb2 = models.FloatField(db_column='NUCB2', blank=True, null=True)  # Field name made lowercase.
    kcnj11 = models.FloatField(db_column='KCNJ11', blank=True, null=True)  # Field name made lowercase.
    saa1 = models.FloatField(db_column='SAA1', blank=True, null=True)  # Field name made lowercase.
    bdnf = models.FloatField(db_column='BDNF', blank=True, null=True)  # Field name made lowercase.
    wt1 = models.FloatField(db_column='WT1', blank=True, null=True)  # Field name made lowercase.
    cd59 = models.FloatField(db_column='CD59', blank=True, null=True)  # Field name made lowercase.
    pdhx = models.FloatField(db_column='PDHX', blank=True, null=True)  # Field name made lowercase.
    traf6 = models.FloatField(db_column='TRAF6', blank=True, null=True)  # Field name made lowercase.
    api5 = models.FloatField(db_column='API5', blank=True, null=True)  # Field name made lowercase.
    nr1h3 = models.FloatField(db_column='NR1H3', blank=True, null=True)  # Field name made lowercase.
    ndufs3 = models.FloatField(db_column='NDUFS3', blank=True, null=True)  # Field name made lowercase.
    folh1 = models.FloatField(db_column='FOLH1', blank=True, null=True)  # Field name made lowercase.
    aplnr = models.FloatField(db_column='APLNR', blank=True, null=True)  # Field name made lowercase.
    p2rx3 = models.FloatField(db_column='P2RX3', blank=True, null=True)  # Field name made lowercase.
    cntf = models.FloatField(db_column='CNTF', blank=True, null=True)  # Field name made lowercase.
    fads1 = models.FloatField(db_column='FADS1', blank=True, null=True)  # Field name made lowercase.
    fads2 = models.FloatField(db_column='FADS2', blank=True, null=True)  # Field name made lowercase.
    fkbp2 = models.FloatField(db_column='FKBP2', blank=True, null=True)  # Field name made lowercase.
    syvn1 = models.FloatField(db_column='SYVN1', blank=True, null=True)  # Field name made lowercase.
    pc = models.FloatField(db_column='PC', blank=True, null=True)  # Field name made lowercase.
    dhcr7 = models.FloatField(db_column='DHCR7', blank=True, null=True)  # Field name made lowercase.
    prcp = models.FloatField(db_column='PRCP', blank=True, null=True)  # Field name made lowercase.
    nox4 = models.FloatField(db_column='NOX4', blank=True, null=True)  # Field name made lowercase.
    pdgfd = models.FloatField(db_column='PDGFD', blank=True, null=True)  # Field name made lowercase.
    atm = models.FloatField(db_column='ATM', blank=True, null=True)  # Field name made lowercase.
    il18 = models.FloatField(db_column='IL18', blank=True, null=True)  # Field name made lowercase.
    apoa1 = models.FloatField(db_column='APOA1', blank=True, null=True)  # Field name made lowercase.
    hyou1 = models.FloatField(db_column='HYOU1', blank=True, null=True)  # Field name made lowercase.
    esam = models.FloatField(db_column='ESAM', blank=True, null=True)  # Field name made lowercase.
    fkbp4 = models.FloatField(db_column='FKBP4', blank=True, null=True)  # Field name made lowercase.
    fgf23 = models.FloatField(db_column='FGF23', blank=True, null=True)  # Field name made lowercase.
    ntf3 = models.FloatField(db_column='NTF3', blank=True, null=True)  # Field name made lowercase.
    vwf = models.FloatField(db_column='VWF', blank=True, null=True)  # Field name made lowercase.
    cd9 = models.FloatField(db_column='CD9', blank=True, null=True)  # Field name made lowercase.
    gapdh = models.FloatField(db_column='GAPDH', blank=True, null=True)  # Field name made lowercase.
    cd4 = models.FloatField(db_column='CD4', blank=True, null=True)  # Field name made lowercase.
    gnb3 = models.FloatField(db_column='GNB3', blank=True, null=True)  # Field name made lowercase.
    cd163 = models.FloatField(db_column='CD163', blank=True, null=True)  # Field name made lowercase.
    slc2a3 = models.FloatField(db_column='SLC2A3', blank=True, null=True)  # Field name made lowercase.
    cd69 = models.FloatField(db_column='CD69', blank=True, null=True)  # Field name made lowercase.
    irak4 = models.FloatField(db_column='IRAK4', blank=True, null=True)  # Field name made lowercase.
    vdr = models.FloatField(db_column='VDR', blank=True, null=True)  # Field name made lowercase.
    aqp5 = models.FloatField(db_column='AQP5', blank=True, null=True)  # Field name made lowercase.
    acvrl1 = models.FloatField(db_column='ACVRL1', blank=True, null=True)  # Field name made lowercase.
    nfe2 = models.FloatField(db_column='NFE2', blank=True, null=True)  # Field name made lowercase.
    cd63 = models.FloatField(db_column='CD63', blank=True, null=True)  # Field name made lowercase.
    erbb3 = models.FloatField(db_column='ERBB3', blank=True, null=True)  # Field name made lowercase.
    ddit3 = models.FloatField(db_column='DDIT3', blank=True, null=True)  # Field name made lowercase.
    ifng = models.FloatField(db_column='IFNG', blank=True, null=True)  # Field name made lowercase.
    nts = models.FloatField(db_column='NTS', blank=True, null=True)  # Field name made lowercase.
    igf1 = models.FloatField(db_column='IGF1', blank=True, null=True)  # Field name made lowercase.
    acacb = models.FloatField(db_column='ACACB', blank=True, null=True)  # Field name made lowercase.
    trpv4 = models.FloatField(db_column='TRPV4', blank=True, null=True)  # Field name made lowercase.
    atp2a2 = models.FloatField(db_column='ATP2A2', blank=True, null=True)  # Field name made lowercase.
    aldh2 = models.FloatField(db_column='ALDH2', blank=True, null=True)  # Field name made lowercase.
    nos1 = models.FloatField(db_column='NOS1', blank=True, null=True)  # Field name made lowercase.
    pebp1 = models.FloatField(db_column='PEBP1', blank=True, null=True)  # Field name made lowercase.
    psmd9 = models.FloatField(db_column='PSMD9', blank=True, null=True)  # Field name made lowercase.
    scarb1 = models.FloatField(db_column='SCARB1', blank=True, null=True)  # Field name made lowercase.
    p2rx2 = models.FloatField(db_column='P2RX2', blank=True, null=True)  # Field name made lowercase.
    alox5ap = models.FloatField(db_column='ALOX5AP', blank=True, null=True)  # Field name made lowercase.
    kl = models.FloatField(db_column='KL', blank=True, null=True)  # Field name made lowercase.
    postn = models.FloatField(db_column='POSTN', blank=True, null=True)  # Field name made lowercase.
    foxo1 = models.FloatField(db_column='FOXO1', blank=True, null=True)  # Field name made lowercase.
    htr2a = models.FloatField(db_column='HTR2A', blank=True, null=True)  # Field name made lowercase.
    gpc5 = models.FloatField(db_column='GPC5', blank=True, null=True)  # Field name made lowercase.
    irs2 = models.FloatField(db_column='IRS2', blank=True, null=True)  # Field name made lowercase.
    gas6 = models.FloatField(db_column='GAS6', blank=True, null=True)  # Field name made lowercase.
    ang = models.FloatField(db_column='ANG', blank=True, null=True)  # Field name made lowercase.
    mmp14 = models.FloatField(db_column='MMP14', blank=True, null=True)  # Field name made lowercase.
    ltb4r2 = models.FloatField(db_column='LTB4R2', blank=True, null=True)  # Field name made lowercase.
    nfkbia = models.FloatField(db_column='NFKBIA', blank=True, null=True)  # Field name made lowercase.
    bmp4 = models.FloatField(db_column='BMP4', blank=True, null=True)  # Field name made lowercase.
    rtn1 = models.FloatField(db_column='RTN1', blank=True, null=True)  # Field name made lowercase.
    pgf = models.FloatField(db_column='PGF', blank=True, null=True)  # Field name made lowercase.
    ngb = models.FloatField(db_column='NGB', blank=True, null=True)  # Field name made lowercase.
    ahsa1 = models.FloatField(db_column='AHSA1', blank=True, null=True)  # Field name made lowercase.
    bdkrb2 = models.FloatField(db_column='BDKRB2', blank=True, null=True)  # Field name made lowercase.
    bdkrb1 = models.FloatField(db_column='BDKRB1', blank=True, null=True)  # Field name made lowercase.
    akt1 = models.FloatField(db_column='AKT1', blank=True, null=True)  # Field name made lowercase.
    grem1 = models.FloatField(db_column='GREM1', blank=True, null=True)  # Field name made lowercase.
    thbs1 = models.FloatField(db_column='THBS1', blank=True, null=True)  # Field name made lowercase.
    pak6 = models.FloatField(db_column='PAK6', blank=True, null=True)  # Field name made lowercase.
    b2m = models.FloatField(db_column='B2M', blank=True, null=True)  # Field name made lowercase.
    myo5c = models.FloatField(db_column='MYO5C', blank=True, null=True)  # Field name made lowercase.
    onecut1 = models.FloatField(db_column='ONECUT1', blank=True, null=True)  # Field name made lowercase.
    adam10 = models.FloatField(db_column='ADAM10', blank=True, null=True)  # Field name made lowercase.
    ctsh = models.FloatField(db_column='CTSH', blank=True, null=True)  # Field name made lowercase.
    plin1 = models.FloatField(db_column='PLIN1', blank=True, null=True)  # Field name made lowercase.
    igf1r = models.FloatField(db_column='IGF1R', blank=True, null=True)  # Field name made lowercase.
    mrpl28 = models.FloatField(db_column='MRPL28', blank=True, null=True)  # Field name made lowercase.
    cacna1h = models.FloatField(db_column='CACNA1H', blank=True, null=True)  # Field name made lowercase.
    pdpk1 = models.FloatField(db_column='PDPK1', blank=True, null=True)  # Field name made lowercase.
    ercc4 = models.FloatField(db_column='ERCC4', blank=True, null=True)  # Field name made lowercase.
    smg1 = models.FloatField(db_column='SMG1', blank=True, null=True)  # Field name made lowercase.
    itgam = models.FloatField(db_column='ITGAM', blank=True, null=True)  # Field name made lowercase.
    fto = models.FloatField(db_column='FTO', blank=True, null=True)  # Field name made lowercase.
    mmp2 = models.FloatField(db_column='MMP2', blank=True, null=True)  # Field name made lowercase.
    slc12a3 = models.FloatField(db_column='SLC12A3', blank=True, null=True)  # Field name made lowercase.
    cetp = models.FloatField(db_column='CETP', blank=True, null=True)  # Field name made lowercase.
    cx3cl1 = models.FloatField(db_column='CX3CL1', blank=True, null=True)  # Field name made lowercase.
    cdh1 = models.FloatField(db_column='CDH1', blank=True, null=True)  # Field name made lowercase.
    nqo1 = models.FloatField(db_column='NQO1', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    znrf1 = models.FloatField(db_column='ZNRF1', blank=True, null=True)  # Field name made lowercase.
    cyba = models.FloatField(db_column='CYBA', blank=True, null=True)  # Field name made lowercase.
    tubb3 = models.FloatField(db_column='TUBB3', blank=True, null=True)  # Field name made lowercase.
    crk = models.FloatField(db_column='CRK', blank=True, null=True)  # Field name made lowercase.
    serpinf2 = models.FloatField(db_column='SERPINF2', blank=True, null=True)  # Field name made lowercase.
    serpinf1 = models.FloatField(db_column='SERPINF1', blank=True, null=True)  # Field name made lowercase.
    trpv3 = models.FloatField(db_column='TRPV3', blank=True, null=True)  # Field name made lowercase.
    cxcl16 = models.FloatField(db_column='CXCL16', blank=True, null=True)  # Field name made lowercase.
    slc2a4 = models.FloatField(db_column='SLC2A4', blank=True, null=True)  # Field name made lowercase.
    cd68 = models.FloatField(db_column='CD68', blank=True, null=True)  # Field name made lowercase.
    shbg = models.FloatField(db_column='SHBG', blank=True, null=True)  # Field name made lowercase.
    pmp22 = models.FloatField(db_column='PMP22', blank=True, null=True)  # Field name made lowercase.
    srebf1 = models.FloatField(db_column='SREBF1', blank=True, null=True)  # Field name made lowercase.
    mapk7 = models.FloatField(db_column='MAPK7', blank=True, null=True)  # Field name made lowercase.
    ccl2 = models.FloatField(db_column='CCL2', blank=True, null=True)  # Field name made lowercase.
    ccl5 = models.FloatField(db_column='CCL5', blank=True, null=True)  # Field name made lowercase.
    hnf1b = models.FloatField(db_column='HNF1B', blank=True, null=True)  # Field name made lowercase.
    erbb2 = models.FloatField(db_column='ERBB2', blank=True, null=True)  # Field name made lowercase.
    fkbp10 = models.FloatField(db_column='FKBP10', blank=True, null=True)  # Field name made lowercase.
    stat5a = models.FloatField(db_column='STAT5A', blank=True, null=True)  # Field name made lowercase.
    stat3 = models.FloatField(db_column='STAT3', blank=True, null=True)  # Field name made lowercase.
    naglu = models.FloatField(db_column='NAGLU', blank=True, null=True)  # Field name made lowercase.
    aoc2 = models.FloatField(db_column='AOC2', blank=True, null=True)  # Field name made lowercase.
    aoc3 = models.FloatField(db_column='AOC3', blank=True, null=True)  # Field name made lowercase.
    ppy = models.FloatField(db_column='PPY', blank=True, null=True)  # Field name made lowercase.
    sth = models.FloatField(db_column='STH', blank=True, null=True)  # Field name made lowercase.
    itgb3 = models.FloatField(db_column='ITGB3', blank=True, null=True)  # Field name made lowercase.
    gip = models.FloatField(db_column='GIP', blank=True, null=True)  # Field name made lowercase.
    mpo = models.FloatField(db_column='MPO', blank=True, null=True)  # Field name made lowercase.
    pecam1 = models.FloatField(db_column='PECAM1', blank=True, null=True)  # Field name made lowercase.
    sox9 = models.FloatField(db_column='SOX9', blank=True, null=True)  # Field name made lowercase.
    timp2 = models.FloatField(db_column='TIMP2', blank=True, null=True)  # Field name made lowercase.
    dcxr = models.FloatField(db_column='DCXR', blank=True, null=True)  # Field name made lowercase.
    fasn = models.FloatField(db_column='FASN', blank=True, null=True)  # Field name made lowercase.
    colec12 = models.FloatField(db_column='COLEC12', blank=True, null=True)  # Field name made lowercase.
    adcyap1 = models.FloatField(db_column='ADCYAP1', blank=True, null=True)  # Field name made lowercase.
    smad7 = models.FloatField(db_column='SMAD7', blank=True, null=True)  # Field name made lowercase.
    nedd4l = models.FloatField(db_column='NEDD4L', blank=True, null=True)  # Field name made lowercase.
    mc4r = models.FloatField(db_column='MC4R', blank=True, null=True)  # Field name made lowercase.
    bcl2 = models.FloatField(db_column='BCL2', blank=True, null=True)  # Field name made lowercase.
    cndp2 = models.FloatField(db_column='CNDP2', blank=True, null=True)  # Field name made lowercase.
    znf236 = models.FloatField(db_column='ZNF236', blank=True, null=True)  # Field name made lowercase.
    stk11 = models.FloatField(db_column='STK11', blank=True, null=True)  # Field name made lowercase.
    sirt6 = models.FloatField(db_column='SIRT6', blank=True, null=True)  # Field name made lowercase.
    uhrf1 = models.FloatField(db_column='UHRF1', blank=True, null=True)  # Field name made lowercase.
    timm44 = models.FloatField(db_column='TIMM44', blank=True, null=True)  # Field name made lowercase.
    angptl4 = models.FloatField(db_column='ANGPTL4', blank=True, null=True)  # Field name made lowercase.
    dnmt1 = models.FloatField(db_column='DNMT1', blank=True, null=True)  # Field name made lowercase.
    icam1 = models.FloatField(db_column='ICAM1', blank=True, null=True)  # Field name made lowercase.
    ldlr = models.FloatField(db_column='LDLR', blank=True, null=True)  # Field name made lowercase.
    epor = models.FloatField(db_column='EPOR', blank=True, null=True)  # Field name made lowercase.
    prdx2 = models.FloatField(db_column='PRDX2', blank=True, null=True)  # Field name made lowercase.
    ptger1 = models.FloatField(db_column='PTGER1', blank=True, null=True)  # Field name made lowercase.
    unc13a = models.FloatField(db_column='UNC13A', blank=True, null=True)  # Field name made lowercase.
    gdf15 = models.FloatField(db_column='GDF15', blank=True, null=True)  # Field name made lowercase.
    fkbp8 = models.FloatField(db_column='FKBP8', blank=True, null=True)  # Field name made lowercase.
    usf2 = models.FloatField(db_column='USF2', blank=True, null=True)  # Field name made lowercase.
    ffar1 = models.FloatField(db_column='FFAR1', blank=True, null=True)  # Field name made lowercase.
    ffar2 = models.FloatField(db_column='FFAR2', blank=True, null=True)  # Field name made lowercase.
    nphs1 = models.FloatField(db_column='NPHS1', blank=True, null=True)  # Field name made lowercase.
    tgfb1 = models.FloatField(db_column='TGFB1', blank=True, null=True)  # Field name made lowercase.
    xrcc1 = models.FloatField(db_column='XRCC1', blank=True, null=True)  # Field name made lowercase.
    ercc1 = models.FloatField(db_column='ERCC1', blank=True, null=True)  # Field name made lowercase.
    gipr = models.FloatField(db_column='GIPR', blank=True, null=True)  # Field name made lowercase.
    fgf21 = models.FloatField(db_column='FGF21', blank=True, null=True)  # Field name made lowercase.
    clec11a = models.FloatField(db_column='CLEC11A', blank=True, null=True)  # Field name made lowercase.
    fpr1 = models.FloatField(db_column='FPR1', blank=True, null=True)  # Field name made lowercase.
    trib3 = models.FloatField(db_column='TRIB3', blank=True, null=True)  # Field name made lowercase.
    bmp2 = models.FloatField(db_column='BMP2', blank=True, null=True)  # Field name made lowercase.
    thbd = models.FloatField(db_column='THBD', blank=True, null=True)  # Field name made lowercase.
    cst3 = models.FloatField(db_column='CST3', blank=True, null=True)  # Field name made lowercase.
    id1 = models.FloatField(db_column='ID1', blank=True, null=True)  # Field name made lowercase.
    src = models.FloatField(db_column='SRC', blank=True, null=True)  # Field name made lowercase.
    mafb = models.FloatField(db_column='MAFB', blank=True, null=True)  # Field name made lowercase.
    sgk2 = models.FloatField(db_column='SGK2', blank=True, null=True)  # Field name made lowercase.
    hnf4a = models.FloatField(db_column='HNF4A', blank=True, null=True)  # Field name made lowercase.
    pltp = models.FloatField(db_column='PLTP', blank=True, null=True)  # Field name made lowercase.
    mmp9 = models.FloatField(db_column='MMP9', blank=True, null=True)  # Field name made lowercase.
    cd40 = models.FloatField(db_column='CD40', blank=True, null=True)  # Field name made lowercase.
    ptpn1 = models.FloatField(db_column='PTPN1', blank=True, null=True)  # Field name made lowercase.
    cyp24a1 = models.FloatField(db_column='CYP24A1', blank=True, null=True)  # Field name made lowercase.
    rcan1 = models.FloatField(db_column='RCAN1', blank=True, null=True)  # Field name made lowercase.
    abcg1 = models.FloatField(db_column='ABCG1', blank=True, null=True)  # Field name made lowercase.
    prmt2 = models.FloatField(db_column='PRMT2', blank=True, null=True)  # Field name made lowercase.
    comt = models.FloatField(db_column='COMT', blank=True, null=True)  # Field name made lowercase.
    mapk1 = models.FloatField(db_column='MAPK1', blank=True, null=True)  # Field name made lowercase.
    mif = models.FloatField(db_column='MIF', blank=True, null=True)  # Field name made lowercase.
    ggt1 = models.FloatField(db_column='GGT1', blank=True, null=True)  # Field name made lowercase.
    xbp1 = models.FloatField(db_column='XBP1', blank=True, null=True)  # Field name made lowercase.
    osm = models.FloatField(db_column='OSM', blank=True, null=True)  # Field name made lowercase.
    limk2 = models.FloatField(db_column='LIMK2', blank=True, null=True)  # Field name made lowercase.
    sfi1 = models.FloatField(db_column='SFI1', blank=True, null=True)  # Field name made lowercase.
    timp3 = models.FloatField(db_column='TIMP3', blank=True, null=True)  # Field name made lowercase.
    hmox1 = models.FloatField(db_column='HMOX1', blank=True, null=True)  # Field name made lowercase.
    apol1 = models.FloatField(db_column='APOL1', blank=True, null=True)  # Field name made lowercase.
    myh9 = models.FloatField(db_column='MYH9', blank=True, null=True)  # Field name made lowercase.
    pdgfb = models.FloatField(db_column='PDGFB', blank=True, null=True)  # Field name made lowercase.
    atf4 = models.FloatField(db_column='ATF4', blank=True, null=True)  # Field name made lowercase.
    tspo = models.FloatField(db_column='TSPO', blank=True, null=True)  # Field name made lowercase.
    miox = models.FloatField(db_column='MIOX', blank=True, null=True)  # Field name made lowercase.
    prdx4 = models.FloatField(db_column='PRDX4', blank=True, null=True)  # Field name made lowercase.
    gk = models.FloatField(db_column='GK', blank=True, null=True)  # Field name made lowercase.
    rgn = models.FloatField(db_column='RGN', blank=True, null=True)  # Field name made lowercase.
    timp1 = models.FloatField(db_column='TIMP1', blank=True, null=True)  # Field name made lowercase.
    clcn5 = models.FloatField(db_column='CLCN5', blank=True, null=True)  # Field name made lowercase.
    ar = models.FloatField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    foxo4 = models.FloatField(db_column='FOXO4', blank=True, null=True)  # Field name made lowercase.
    rps6ka6 = models.FloatField(db_column='RPS6KA6', blank=True, null=True)  # Field name made lowercase.
    nox1 = models.FloatField(db_column='NOX1', blank=True, null=True)  # Field name made lowercase.
    xiap = models.FloatField(db_column='XIAP', blank=True, null=True)  # Field name made lowercase.
    cd40lg = models.FloatField(db_column='CD40LG', blank=True, null=True)  # Field name made lowercase.
    l1cam = models.FloatField(db_column='L1CAM', blank=True, null=True)  # Field name made lowercase.
    irak1 = models.FloatField(db_column='IRAK1', blank=True, null=True)  # Field name made lowercase.
    g6pd = models.FloatField(db_column='G6PD', blank=True, null=True)  # Field name made lowercase.
    f8 = models.FloatField(db_column='F8', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diaco_tissue_liver'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class GeneMedianTpm(models.Model):
    id = models.BigAutoField(db_column='Id',primary_key=True)  # Field name made lowercase.
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


class ListaGeni(models.Model):
    id = models.BigIntegerField(primary_key=True)
    codice = models.TextField(blank=True, null=True)
    gene = models.CharField(max_length=50, blank=True, null=True)
    riferimento_gtex_tissue = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lista_geni'


class RelationAttributesPhenotypes(models.Model):
    subjid = models.CharField(db_column='SUBJID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sampid = models.CharField(db_column='SAMPID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sesso = models.CharField(db_column='Sesso', max_length=1)  # Field name made lowercase.
    eta = models.CharField(db_column='Età', max_length=50, blank=True, null=True)  # Field name made lowercase.
    classificazione_morte = models.CharField(db_column='Classificazione morte', max_length=230)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'relation_attributes_phenotypes'


class SampleAttributesDs(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sampid = models.CharField(db_column='SAMPID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smatsscr = models.IntegerField(db_column='SMATSSCR', blank=True, null=True)  # Field name made lowercase.
    smcenter = models.CharField(db_column='SMCENTER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smpthnts = models.CharField(db_column='SMPTHNTS', max_length=512, blank=True, null=True)  # Field name made lowercase.
    smrin = models.IntegerField(db_column='SMRIN', blank=True, null=True)  # Field name made lowercase.
    smts = models.CharField(db_column='SMTS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smtsd = models.CharField(db_column='SMTSD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smubrid = models.CharField(db_column='SMUBRID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smtsisch = models.IntegerField(db_column='SMTSISCH', blank=True, null=True)  # Field name made lowercase.
    smtspax = models.IntegerField(db_column='SMTSPAX', blank=True, null=True)  # Field name made lowercase.
    smnabtch = models.CharField(db_column='SMNABTCH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smnabtcht = models.CharField(db_column='SMNABTCHT', max_length=64, blank=True, null=True)  # Field name made lowercase.
    smnabtchd = models.CharField(db_column='SMNABTCHD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smgebtch = models.CharField(db_column='SMGEBTCH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smgebtchd = models.CharField(db_column='SMGEBTCHD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smgebtcht = models.CharField(db_column='SMGEBTCHT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smafrze = models.CharField(db_column='SMAFRZE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smgtc = models.CharField(db_column='SMGTC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sme2mprt = models.IntegerField(db_column='SME2MPRT', blank=True, null=True)  # Field name made lowercase.
    smchmprs = models.FloatField(db_column='SMCHMPRS', blank=True, null=True)  # Field name made lowercase.
    smntrart = models.IntegerField(db_column='SMNTRART', blank=True, null=True)  # Field name made lowercase.
    smnumgps = models.CharField(db_column='SMNUMGPS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smmaprt = models.IntegerField(db_column='SMMAPRT', blank=True, null=True)  # Field name made lowercase.
    smexncrt = models.IntegerField(db_column='SMEXNCRT', blank=True, null=True)  # Field name made lowercase.
    sm550nrm = models.CharField(db_column='SM550NRM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smgnsdtc = models.IntegerField(db_column='SMGNSDTC', blank=True, null=True)  # Field name made lowercase.
    smunmprt = models.IntegerField(db_column='SMUNMPRT', blank=True, null=True)  # Field name made lowercase.
    sm350nrm = models.CharField(db_column='SM350NRM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smrdlgth = models.IntegerField(db_column='SMRDLGTH', blank=True, null=True)  # Field name made lowercase.
    smmncpb = models.CharField(db_column='SMMNCPB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sme1mmrt = models.IntegerField(db_column='SME1MMRT', blank=True, null=True)  # Field name made lowercase.
    smsflgth = models.IntegerField(db_column='SMSFLGTH', blank=True, null=True)  # Field name made lowercase.
    smestlbs = models.IntegerField(db_column='SMESTLBS', blank=True, null=True)  # Field name made lowercase.
    smmppd = models.CharField(db_column='SMMPPD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smnterrt = models.IntegerField(db_column='SMNTERRT', blank=True, null=True)  # Field name made lowercase.
    smrrnanm = models.CharField(db_column='SMRRNANM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smrdttl = models.CharField(db_column='SMRDTTL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smvqcfl = models.CharField(db_column='SMVQCFL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smmncv = models.CharField(db_column='SMMNCV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smtrscpt = models.IntegerField(db_column='SMTRSCPT', blank=True, null=True)  # Field name made lowercase.
    smmppdpr = models.CharField(db_column='SMMPPDPR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smcglgth = models.CharField(db_column='SMCGLGTH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smgappct = models.CharField(db_column='SMGAPPCT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smunpdrd = models.IntegerField(db_column='SMUNPDRD', blank=True, null=True)  # Field name made lowercase.
    smntrnrt = models.IntegerField(db_column='SMNTRNRT', blank=True, null=True)  # Field name made lowercase.
    smmpunrt = models.IntegerField(db_column='SMMPUNRT', blank=True, null=True)  # Field name made lowercase.
    smexpeff = models.IntegerField(db_column='SMEXPEFF', blank=True, null=True)  # Field name made lowercase.
    smmppdun = models.CharField(db_column='SMMPPDUN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sme2mmrt = models.IntegerField(db_column='SME2MMRT', blank=True, null=True)  # Field name made lowercase.
    sme2anti = models.CharField(db_column='SME2ANTI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smaltalg = models.CharField(db_column='SMALTALG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sme2snse = models.CharField(db_column='SME2SNSE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smmflgth = models.IntegerField(db_column='SMMFLGTH', blank=True, null=True)  # Field name made lowercase.
    sme1anti = models.CharField(db_column='SME1ANTI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smspltrd = models.CharField(db_column='SMSPLTRD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smbsmmrt = models.IntegerField(db_column='SMBSMMRT', blank=True, null=True)  # Field name made lowercase.
    sme1snse = models.CharField(db_column='SME1SNSE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sme1pcts = models.IntegerField(db_column='SME1PCTS', blank=True, null=True)  # Field name made lowercase.
    smrrnart = models.IntegerField(db_column='SMRRNART', blank=True, null=True)  # Field name made lowercase.
    sme1mprt = models.IntegerField(db_column='SME1MPRT', blank=True, null=True)  # Field name made lowercase.
    smnum5cd = models.CharField(db_column='SMNUM5CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smdpmprt = models.IntegerField(db_column='SMDPMPRT', blank=True, null=True)  # Field name made lowercase.
    sme2pcts = models.IntegerField(db_column='SME2PCTS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sample_attributes_ds'


class SubjectPhenotypesDd(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    subjid = models.CharField(db_column='SUBJID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(db_column='SEX', blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='AGE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dthhrdy = models.IntegerField(db_column='DTHHRDY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subject_phenotypes_dd'


class ListaTabelle(models.Model):
    tessuto = models.CharField(db_column='Tessuto', max_length=36)  # Field name made lowercase.
    tabella = models.CharField(db_column='Tabella', max_length=35, primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lista_tabelle'
