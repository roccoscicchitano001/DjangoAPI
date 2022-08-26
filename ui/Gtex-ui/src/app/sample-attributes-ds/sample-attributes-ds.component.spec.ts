import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SampleAttributesDsComponent } from './sample-attributes-ds.component';

describe('SampleAttributesDsComponent', () => {
  let component: SampleAttributesDsComponent;
  let fixture: ComponentFixture<SampleAttributesDsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SampleAttributesDsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SampleAttributesDsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
