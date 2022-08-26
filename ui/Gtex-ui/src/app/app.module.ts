import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { GeneMedianTpmComponent } from './gene-median-tpm/gene-median-tpm.component';
import { SampleAttributesDsComponent } from './sample-attributes-ds/sample-attributes-ds.component';
import { SubjectPhenotypesDdComponent } from './subject-phenotypes-dd/subject-phenotypes-dd.component';

import {HttpClientModule} from '@angular/common/http';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    GeneMedianTpmComponent,
    SampleAttributesDsComponent,
    SubjectPhenotypesDdComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
