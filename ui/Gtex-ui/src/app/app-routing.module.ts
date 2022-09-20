import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { QueryBuilderComponent } from './query-builder/query-builder.component';


const routes: Routes = [
  {path:'home',component:HomeComponent},
  {path:'query-builder',component:QueryBuilderComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
