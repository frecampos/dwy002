from django.contrib import admin
from .models import SliderIndex,SliderGaleria,MisionVision,Insumos

# Register your models here.
class SliderIndexAdmi(admin.ModelAdmin):
    list_display=['ident','imagen']
    search_fields = ['ident']
    list_per_page = 3
class InsumosAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","descripcion","stock"]
    search_fields = ["nombre","descripcion"]
    list_per_page = 3

admin.site.register(SliderIndex,SliderIndexAdmi)
admin.site.register(SliderGaleria)
admin.site.register(MisionVision)
admin.site.register(Insumos, InsumosAdmin)
