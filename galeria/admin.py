from django.contrib import admin

from galeria.models import Fotografia

# Register your models here.

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('categoria', 'usuario' )
    list_editable = ('publicada',)
    list_per_page =1
    
admin.site.register(Fotografia, ListandoFotografias)

