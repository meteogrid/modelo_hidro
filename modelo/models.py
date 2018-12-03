from django.db import models
from django.conf import settings
from datetime import datetime

import json

# Create your models here.
class Etp(models.Model):
    Unidad = models.ForeignKey('UnidadHidrologica', on_delete=models.CASCADE)
    Fecha = models.DateField()
    Etp = models.DecimalField(max_digits=6, decimal_places=2)  
 
    class Meta:
        verbose_name_plural = 'etp_tb'

    
class Pcp(models.Model):
    Unidad = models.ForeignKey('UnidadHidrologica', on_delete=models.CASCADE)
    Fecha = models.DateField()
    Pcp = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        verbose_name_plural = 'pcp_tb'

class DatosGeneradosUnidad(models.Model):
    Unidad = models.ForeignKey('UnidadHidrologica', on_delete=models.CASCADE)
    Fecha = models.DateField()
    Pcp = models.DecimalField(max_digits=6, decimal_places=2)
    Etp = models.DecimalField(max_digits=6, decimal_places=2) 
  
class UnidadHidrologica(models.Model):
    Id = models.CharField(max_length=5, primary_key=True)
    Hd_Area = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Hd_Msnm = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Cs_Ssm = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Cs_Suz = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Cs_SIz = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True) 
    Cs_UZL0 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Cs_UZL1 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Cs_UZL2 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Bh_Pcorr = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Bh_Pcalt = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Bh_FC = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Bh_LP = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Bh_Beta = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Bh_Cflux = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Hes_K0 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Hes_K1 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Hes_K2 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Hes_K3 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    HeI_K4 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    HeI_PERC = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    HeI_MAXBIAS = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    
class CalculoModelo(models.Model):
    Unidad = models.ForeignKey('UnidadHidrologica', on_delete=models.CASCADE)
    fecha = models.DateField(blank=True, null=True)
    p_ajustada = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    dQ = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    duz = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    SSm = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ETR = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Delta_ssm = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    SUZ2 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Perc = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Delta_Suz = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    SIz = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Q0 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Q1 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Q2 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Q3 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Delta_Suz_prima = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Q4 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Q_gen = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Caudal = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    Delta_SIz = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def toJson(self):
        model_data = {'Unidad':self.Unidad.Id, 'fecha':self.fecha, 'p_ajustada':self.p_ajustada, 'dQ':self.dQ,
            'duz':self.duz, 'SSm':self.SSm, 'ETR':self.ETR, 'Delta_ssm':self.Delta_ssm, 'SUZ2':self.SUZ2, 
            'Perc':self.Perc, 'Delta_Suz':self.Delta_Suz, 'SIz':self.SIz, 'Q0':self.Q0, 'Q1':self.Q1, 'Q2':self.Q2,
            'Q3':self.Q3, 'Delta_Suz_prima':self.Delta_Suz_prima, 'Q4':self.Q4, 'Q_gen':self.Q_gen, 'Caudal':self.Caudal,
            'Delta_SIz':self.Delta_SIz}
        return model_data    
    
