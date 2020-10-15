from django.contrib import admin
from .models import SliderIndex,SliderGaleria,MisionVision,Insumos

# Register your models here.
class SliderIndexAdmi(admin.ModelAdmin):
    list_display=['ident','imagen']
    search_fields = ['ident']
    list_per_page = 3

admin.site.register(SliderIndex,SliderIndexAdmi)
admin.site.register(SliderGaleria)
admin.site.register(MisionVision)
admin.site.register(Insumos)
