# Register your models here.
from django.contrib import admin
from .models import Etp, Pcp, UnidadHidrologica, CalculoModelo
from builtins import all

# Register your models here.

#admin.site.register(ETP)
@admin.register(UnidadHidrologica)
class UnidadHidrologicaAdmin(admin.ModelAdmin):
    all
#admin.site.register(Pcp)

@admin.register(CalculoModelo)
class CalculoModelo(admin.ModelAdmin):
    all