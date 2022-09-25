import { Component, OnInit } from '@angular/core';

import { environment } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-query-builder',
  templateUrl: './query-builder.component.html',
  styleUrls: ['./query-builder.component.css']
})
export class QueryBuilderComponent implements OnInit {

  p:number = 1;

  constructor(private http:HttpClient) {
    this.tabellaScelta;
  }

   //Select
  ERRFI1:boolean = false;  
  MAD2L2:boolean = false;  
  MTHFR:boolean = false;  
  NPPA:boolean = false;  
  TNFRSF1B:boolean = false;  
  PLA2G2A:boolean = false;  
  ALPL:boolean = false;  
  HSPG2:boolean = false;  
  CNR2:boolean = false;  
  SLC9A1:boolean = false;  
  COL8A2:boolean = false;  
  CAP1:boolean = false;  
  SLC2A1:boolean = false;  
  CYP2J2:boolean = false;  
  DDAH1:boolean = false;  
  CYR61:boolean = false;  
  NGF:boolean = false;  
  HMGCS2:boolean = false;  
  CTSS:boolean = false;  
  S100A12:boolean = false;  
  LMNA:boolean = false;  
  CD247:boolean = false;  
  SELE:boolean = false;  
  FMO3:boolean = false;  
  PRDX6:boolean = false;  
  GLUL:boolean = false;  
  LAMC1:boolean = false;  
  PTGS2:boolean = false;  
  CHI3L1:boolean = false;  
  CHIT1:boolean = false;  
  FMOD:boolean = false;  
  IL10:boolean = false;  
  PFKFB2:boolean = false;  
  CD34:boolean = false;  
  COG2:boolean = false;  
  NLRP3:boolean = false;  
  ROCK2:boolean = false;  
  APOB:boolean = false;  
  POMC:boolean = false;  
  GCKR:boolean = false;  
  PLEKHH2:boolean = false;  
  PRKCE:boolean = false;  
  PIGF:boolean = false;  
  MSH2:boolean = false;  
  GFPT1:boolean = false;  
  TACR1:boolean = false;  
  REG1A:boolean = false;  
  EIF2AK3:boolean = false;  
  ADRA2B:boolean = false;  
  IL1B:boolean = false;  
  PROC:boolean = false;  
  POLR2D:boolean = false;  
  ZEB2:boolean = false;  
  ACVR1C:boolean = false;  
  DPP4:boolean = false;  
  NFE2L2:boolean = false;  
  IGFBP5:boolean = false;  
  CCL20:boolean = false;  
  HDAC4:boolean = false;  
  CAPN10:boolean = false;  
  GHRL:boolean = false;  
  PPARG:boolean = false;  
  RAF1:boolean = false;  
  MYD88:boolean = false;  
  CX3CR1:boolean = false;  
  CCK:boolean = false;  
  EXOSC7:boolean = false;  
  CCR1:boolean = false;  
  CCR5:boolean = false;  
  GPX1:boolean = false;  
  RHOA:boolean = false;  
  CISH:boolean = false;  
  TKT:boolean = false;  
  APPL1:boolean = false;  
  SLMAP:boolean = false;  
  COL8A1:boolean = false;  
  CD47:boolean = false;  
  GAP43:boolean = false;  
  CD80:boolean = false;  
  RHO:boolean = false;  
  TRH:boolean = false;  
  TF:boolean = false;  
  RBP1:boolean = false;  
  TRPC1:boolean = false;  
  AGTR1:boolean = false;  
  SUCNR1:boolean = false;  
  P2RY1:boolean = false;  
  MME:boolean = false;  
  SLC2A2:boolean = false;  
  PIK3CA:boolean = false;  
  PARL:boolean = false;  
  AHSG:boolean = false;  
  ADIPOQ:boolean = false;  
  SPON2:boolean = false;  
  WFS1:boolean = false;  
  CD38:boolean = false;  
  PROM1:boolean = false;  
  PPARGC1A:boolean = false;  
  IGFBP7:boolean = false;  
  CXCL5:boolean = false;  
  CXCL9:boolean = false;  
  CXCL10:boolean = false;  
  CXCL11:boolean = false;  
  HPSE:boolean = false;  
  SPP1:boolean = false;  
  ADH1B:boolean = false;  
  EGF:boolean = false;  
  ALPK1:boolean = false;  
  FABP2:boolean = false;  
  PDE5A:boolean = false;  
  SETD7:boolean = false;  
  SMAD1:boolean = false;  
  EDNRA:boolean = false;  
  NR3C2:boolean = false;  
  TLR2:boolean = false;  
  NPY5R:boolean = false;  
  FBXO8:boolean = false;  
  VEGFC:boolean = false;  
  ACSL1:boolean = false;  
  SORBS2:boolean = false;  
  F11:boolean = false;  
  BASP1:boolean = false;  
  PTGER4:boolean = false;  
  PRKAA1:boolean = false;  
  GHR:boolean = false;  
  ITGA2:boolean = false;  
  CDK7:boolean = false;  
  F2R:boolean = false;  
  ERAP2:boolean = false;  
  APC:boolean = false;  
  TNFAIP8:boolean = false;  
  VDAC1:boolean = false;  
  PDGFRB:boolean = false;  
  CD74:boolean = false;  
  SPARC:boolean = false;  
  EBF1:boolean = false;  
  GFPT2:boolean = false;  
  RREB1:boolean = false;  
  EDN1:boolean = false;  
  CDKAL1:boolean = false;  
  HFE:boolean = false;  
  HLA_A:boolean = false;  
  LTA:boolean = false;  
  TNF:boolean = false;  
  HSPA1A:boolean = false;  
  HSPA1B:boolean = false;  
  HLA_DQA1:boolean = false;  
  MAPK14:boolean = false;  
  CDKN1A:boolean = false;  
  GLO1:boolean = false;  
  VEGFA:boolean = false;  
  CD2AP:boolean = false;  
  CNR1:boolean = false;  
  ENPP1:boolean = false;  
  CTGF:boolean = false;  
  RPS12:boolean = false;  
  SGK1:boolean = false;  
  MAP3K5:boolean = false;  
  CITED2:boolean = false;  
  UTRN:boolean = false;  
  MTHFD1L:boolean = false;  
  VIP:boolean = false;  
  SOD2:boolean = false;  
  LPA:boolean = false;  
  THBS2:boolean = false;  
  PDGFA:boolean = false;  
  IL6:boolean = false;  
  NPY:boolean = false;  
  JAZF1:boolean = false;  
  CPVL:boolean = false;  
  AQP1:boolean = false;  
  ELMO1:boolean = false;  
  IGFBP3:boolean = false;  
  EGFR:boolean = false;  
  ELN:boolean = false;  
  NCF1:boolean = false;  
  HSPB1:boolean = false;  
  SEMA3A:boolean = false;  
  PON3:boolean = false;  
  PON2:boolean = false;  
  NAMPT:boolean = false;  
  CAV1:boolean = false;  
  LEP:boolean = false;  
  AKR1B1:boolean = false;  
  AKR1B10:boolean = false;  
  PIP:boolean = false;  
  RARRES2:boolean = false;  
  NOS3:boolean = false;  
  ANGPT2:boolean = false;  
  DEFA1:boolean = false;  
  LPL:boolean = false;  
  EBF2:boolean = false;  
  ADRB3:boolean = false;  
  EIF4EBP1:boolean = false;  
  FGFR1:boolean = false;  
  CRH:boolean = false;  
  SGK3:boolean = false;  
  FABP5:boolean = false;  
  FABP4:boolean = false;  
  MMP16:boolean = false;  
  NCALD:boolean = false;  
  KLF10:boolean = false;  
  ENPP2:boolean = false;  
  PVT1:boolean = false;  
  JAK2:boolean = false;  
  PSIP1:boolean = false;  
  PLIN2:boolean = false;  
  RPS6:boolean = false;  
  ALDH1A1:boolean = false;  
  FRMD3:boolean = false;  
  GAS1:boolean = false;  
  BAAT:boolean = false;  
  ABCA1:boolean = false;  
  TXN:boolean = false;  
  AMBP:boolean = false;  
  C5:boolean = false;  
  HSPA5:boolean = false;  
  ANGPTL2:boolean = false;  
  PTGES:boolean = false;  
  TSC1:boolean = false;  
  ABO:boolean = false;  
  ADAMTS13:boolean = false;  
  PTGDS:boolean = false;  
  KLF6:boolean = false;  
  CDC123:boolean = false;  
  BAMBI:boolean = false;  
  CXCL12:boolean = false;  
  MBL2:boolean = false;  
  TFAM:boolean = false;  
  SIRT1:boolean = false;  
  SRGN:boolean = false;  
  UNC5B:boolean = false;  
  ADK:boolean = false;  
  PTEN:boolean = false;  
  RBP4:boolean = false;  
  CYP2C19:boolean = false;  
  ENTPD1:boolean = false;  
  TCF7L2:boolean = false;  
  BNIP3:boolean = false;  
  IGF2:boolean = false;  
  INS:boolean = false;  
  TH:boolean = false;  
  KCNQ1:boolean = false;  
  HBG2:boolean = false;  
  SMPD1:boolean = false;  
  ILK:boolean = false;  
  ADM:boolean = false;  
  PTH:boolean = false;  
  NUCB2:boolean = false;  
  KCNJ11:boolean = false;  
  SAA1:boolean = false;  
  BDNF:boolean = false;  
  WT1:boolean = false;  
  CD59:boolean = false;  
  PDHX:boolean = false;  
  TRAF6:boolean = false;  
  API5:boolean = false;  
  NR1H3:boolean = false;  
  NDUFS3:boolean = false;  
  FOLH1:boolean = false;  
  APLNR:boolean = false;  
  P2RX3:boolean = false;  
  CNTF:boolean = false;  
  FADS1:boolean = false;  
  FADS2:boolean = false;  
  FKBP2:boolean = false;  
  SYVN1:boolean = false;  
  PC:boolean = false;  
  DHCR7:boolean = false;  
  PRCP:boolean = false;  
  NOX4:boolean = false;  
  PDGFD:boolean = false;  
  ATM:boolean = false;  
  IL18:boolean = false;  
  APOA1:boolean = false;  
  HYOU1:boolean = false;  
  ESAM:boolean = false;  
  FKBP4:boolean = false;  
  FGF23:boolean = false;  
  NTF3:boolean = false;  
  VWF:boolean = false;  
  CD9:boolean = false;  
  GAPDH:boolean = false;  
  CD4:boolean = false;  
  GNB3:boolean = false;  
  CD163:boolean = false;  
  SLC2A3:boolean = false;  
  CD69:boolean = false;  
  IRAK4:boolean = false;  
  VDR:boolean = false;  
  AQP5:boolean = false;  
  ACVRL1:boolean = false;  
  NFE2:boolean = false;  
  CD63:boolean = false;  
  ERBB3:boolean = false;  
  DDIT3:boolean = false;  
  IFNG:boolean = false;  
  NTS:boolean = false;  
  IGF1:boolean = false;  
  ACACB:boolean = false;  
  TRPV4:boolean = false;  
  ATP2A2:boolean = false;  
  ALDH2:boolean = false;  
  NOS1:boolean = false;  
  PEBP1:boolean = false;  
  PSMD9:boolean = false;  
  SCARB1:boolean = false;  
  P2RX2:boolean = false;  
  ALOX5AP:boolean = false;  
  KL:boolean = false;  
  POSTN:boolean = false;  
  FOXO1:boolean = false;  
  HTR2A:boolean = false;  
  GPC5:boolean = false;  
  IRS2:boolean = false;  
  GAS6:boolean = false;  
  ANG:boolean = false;  
  MMP14:boolean = false;  
  LTB4R2:boolean = false;  
  NFKBIA:boolean = false;  
  BMP4:boolean = false;  
  RTN1:boolean = false;  
  PGF:boolean = false;  
  NGB:boolean = false;  
  AHSA1:boolean = false;  
  BDKRB2:boolean = false;  
  BDKRB1:boolean = false;  
  AKT1:boolean = false;  
  GREM1:boolean = false;  
  THBS1:boolean = false;  
  PAK6:boolean = false;  
  B2M:boolean = false;  
  MYO5C:boolean = false;  
  ONECUT1:boolean = false;  
  ADAM10:boolean = false;  
  CTSH:boolean = false;  
  PLIN1:boolean = false;  
  IGF1R:boolean = false;  
  MRPL28:boolean = false;  
  CACNA1H:boolean = false;  
  PDPK1:boolean = false;  
  ERCC4:boolean = false;  
  SMG1:boolean = false;  
  ITGAM:boolean = false;  
  FTO:boolean = false;  
  MMP2:boolean = false;  
  SLC12A3:boolean = false;  
  CETP:boolean = false;  
  CX3CL1:boolean = false;  
  CDH1:boolean = false;  
  NQO1:boolean = false;  
  HP:boolean = false;  
  ZNRF1:boolean = false;  
  CYBA:boolean = false;  
  TUBB3:boolean = false;  
  CRK:boolean = false;  
  SERPINF2:boolean = false;  
  SERPINF1:boolean = false;  
  TRPV3:boolean = false;  
  CXCL16:boolean = false;  
  SLC2A4:boolean = false;  
  CD68:boolean = false;  
  SHBG:boolean = false;  
  PMP22:boolean = false;  
  SREBF1:boolean = false;  
  MAPK7:boolean = false;  
  CCL2:boolean = false;  
  CCL5:boolean = false;  
  HNF1B:boolean = false;  
  ERBB2:boolean = false;  
  FKBP10:boolean = false;  
  STAT5A:boolean = false;  
  STAT3:boolean = false;  
  NAGLU:boolean = false;  
  AOC2:boolean = false;  
  AOC3:boolean = false;  
  PPY:boolean = false;  
  STH:boolean = false;  
  ITGB3:boolean = false;  
  GIP:boolean = false;  
  MPO:boolean = false;  
  PECAM1:boolean = false;  
  SOX9:boolean = false;  
  TIMP2:boolean = false;  
  DCXR:boolean = false;  
  FASN:boolean = false;  
  COLEC12:boolean = false;  
  ADCYAP1:boolean = false;  
  SMAD7:boolean = false;  
  NEDD4L:boolean = false;  
  MC4R:boolean = false;  
  BCL2:boolean = false;  
  CNDP2:boolean = false;  
  ZNF236:boolean = false;  
  STK11:boolean = false;  
  SIRT6:boolean = false;  
  UHRF1:boolean = false;  
  TIMM44:boolean = false;  
  ANGPTL4:boolean = false;  
  DNMT1:boolean = false;  
  ICAM1:boolean = false;  
  LDLR:boolean = false;  
  EPOR:boolean = false;  
  PRDX2:boolean = false;  
  PTGER1:boolean = false;  
  UNC13A:boolean = false;  
  GDF15:boolean = false;  
  FKBP8:boolean = false;  
  USF2:boolean = false;  
  FFAR1:boolean = false;  
  FFAR2:boolean = false;  
  NPHS1:boolean = false;  
  TGFB1:boolean = false;  
  XRCC1:boolean = false;  
  ERCC1:boolean = false;  
  GIPR:boolean = false;  
  FGF21:boolean = false;  
  CLEC11A:boolean = false;  
  FPR1:boolean = false;  
  TRIB3:boolean = false;  
  BMP2:boolean = false;  
  THBD:boolean = false;  
  CST3:boolean = false;  
  ID1:boolean = false;  
  SRC:boolean = false;  
  MAFB:boolean = false;  
  SGK2:boolean = false;  
  HNF4A:boolean = false;  
  PLTP:boolean = false;  
  MMP9:boolean = false;  
  CD40:boolean = false;  
  PTPN1:boolean = false;  
  CYP24A1:boolean = false;  
  RCAN1:boolean = false;  
  ABCG1:boolean = false;  
  PRMT2:boolean = false;  
  COMT:boolean = false;  
  MAPK1:boolean = false;  
  MIF:boolean = false;  
  GGT1:boolean = false;  
  XBP1:boolean = false;  
  OSM:boolean = false;  
  LIMK2:boolean = false;  
  SFI1:boolean = false;  
  TIMP3:boolean = false;  
  HMOX1:boolean = false;  
  APOL1:boolean = false;  
  MYH9:boolean = false;  
  PDGFB:boolean = false;  
  ATF4:boolean = false;  
  TSPO:boolean = false;  
  MIOX:boolean = false;  
  PRDX4:boolean = false;  
  GK:boolean = false;  
  RGN:boolean = false;  
  TIMP1:boolean = false;  
  CLCN5:boolean = false;  
  AR:boolean = false;  
  FOXO4:boolean = false;  
  RPS6KA6:boolean = false;  
  NOX1:boolean = false;  
  XIAP:boolean = false;  
  CD40LG:boolean = false;  
  L1CAM:boolean = false;  
  IRAK1:boolean = false;  
  G6PD:boolean = false;  
  F8:boolean = false;  
  
  //from
  listaTabelle:any=[];
  tabellaScelta:any="";
  tessutoVisualizzato="";
  risultato:any=[];
  disabled:boolean = false;

  page = 1;

  ngOnInit(): void {
    this.refreshList();
  }

  refreshList(){
    this.http.get<any>(environment.API_URL+'listaTabelle')
    .subscribe(data=>{
      this.listaTabelle=data;
    })
  }
  
  setTabella(elemento:any,tessuto:any){
    this.tessutoVisualizzato=tessuto;
    this.tabellaScelta=elemento;
  }

  clear(){
    window.location.reload();
  }

  showTable(){
    if(this.tabellaScelta!=null&&this.tabellaScelta!=""){
      this.disabled=true;
      this.http.get<any>(environment.API_URL+this.tabellaScelta).subscribe(data=>{this.risultato=data;})
    }
    else{
      alert("Select at least one tissue!");
    }
    
  }

}
