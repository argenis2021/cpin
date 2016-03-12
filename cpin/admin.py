from django.contrib import admin
from cpin.models import Punto, Usuario
from cpin.models import Organizacion

class PuntoAdmin(admin.ModelAdmin):
    search_fields = ('id','Enlace',
        'Descripcion')
    list_display = ('id','Descripcion','f_entrega','Enlace','Usuario')
    list_filter = ('Descripcion','id','Usuario')
admin.site.register(Punto, PuntoAdmin)

 #admin.site.register(Punto)
admin.site.register(Usuario)
admin.site.register(Organizacion)
