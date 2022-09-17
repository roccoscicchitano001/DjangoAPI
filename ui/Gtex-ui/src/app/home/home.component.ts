import { Component, OnInit } from '@angular/core';

import { environment } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  p:number = 1;


  constructor(private http:HttpClient) { }

  geni:any=[];

  geniSenzaFiltri:any=[];

  page = 1;

  //Nomi delle colonne
  geneName="";
  geneCode="";

  //Filtri sulle colonne
  geneNameFilter="";
  geneCodeFilter="";

  ngOnInit(): void {
    this.refreshList();
  }

  refreshList(){
    this.http.get<any>(environment.API_URL+'listaGeni')
    .subscribe(data=>{
      this.geni=data;
      this.geniSenzaFiltri=data;
    })
  }

  FilterFn(){
    var GeneCodeFilter=this.geneCodeFilter;
    var GeneNameFilter=this.geneNameFilter;


    this.geni=this.geniSenzaFiltri.filter(
      function(el:any){
        return el.gene.toString().toLowerCase().includes(
          GeneNameFilter.toString().trim().toLowerCase()
        )&& 
          el.codice.toString().toLowerCase().includes(
            GeneCodeFilter.toString().trim().toLowerCase())
      }
    );
  }

  sortResult(prop:any,asc:any){
    this.geni=this.geniSenzaFiltri.sort(function(a:any,b:any){
      if(asc){
        return (a[prop]>b[prop])?1:((a[prop]<b[prop])?-1:0);
      }
      else{
        return (b[prop]>a[prop])?1:((b[prop]<a[prop])?-1:0);
      }
    });
  }


}
