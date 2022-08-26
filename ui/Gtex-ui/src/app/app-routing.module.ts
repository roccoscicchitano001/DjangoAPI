import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { GeneMedianTpmComponent } from './gene-median-tpm/gene-median-tpm.component';
import { SampleAttributesDsComponent } from './sample-attributes-ds/sample-attributes-ds.component';
import { SubjectPhenotypesDdComponent } from './subject-phenotypes-dd/subject-phenotypes-dd.component';

const routes: Routes = [
  {path:'home',component:HomeComponent},
  {path:'gene-median-tpm',component:GeneMedianTpmComponent},
  {path:'sample-attributes-ds',component:SampleAttributesDsComponent},
  {path:'subject-phenotypes-dd',component:SubjectPhenotypesDdComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
