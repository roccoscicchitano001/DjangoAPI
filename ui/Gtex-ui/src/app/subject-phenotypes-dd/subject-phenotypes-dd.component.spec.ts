import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SubjectPhenotypesDdComponent } from './subject-phenotypes-dd.component';

describe('SubjectPhenotypesDdComponent', () => {
  let component: SubjectPhenotypesDdComponent;
  let fixture: ComponentFixture<SubjectPhenotypesDdComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SubjectPhenotypesDdComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SubjectPhenotypesDdComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
