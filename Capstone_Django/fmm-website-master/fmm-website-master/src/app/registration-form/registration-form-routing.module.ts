import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { RegistrationFormComponent } from './registration-form.component';

const routes: Routes = [
  {
    path: '',
    component: RegistrationFormComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class RegistrationFormComponentRoutingModule {}
