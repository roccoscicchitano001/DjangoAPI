import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GeneMedianTpmComponent } from './gene-median-tpm.component';

describe('GeneMedianTpmComponent', () => {
  let component: GeneMedianTpmComponent;
  let fixture: ComponentFixture<GeneMedianTpmComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GeneMedianTpmComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GeneMedianTpmComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
