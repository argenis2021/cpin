from django.db import models
class Organizacion(models.Model):
    nombre_organizacion = models.CharField(max_length=120)
    Direccion = models.CharField(max_length=120)
    Proceso = models.CharField(max_length=120)
    def __unicode__(self):
        return u'%s' % (
            self.nombre_organizacion,
            )
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=120)
    usuario_red = models.CharField(max_length=170)
    Organizacion = models.ForeignKey(Organizacion, blank=True)
    #organizaciones = models.ManyToManyField(Organizacion)
    
    def __unicode__(self):
        return u'%s' % (
            self.nombre_usuario)
    #def lista_organizaciones(self):
        #return ', '.join([x.nombre_organizacion for x in self.organizaciones.all()])
class Punto(models.Model):
    Descripcion = models.CharField(max_length=150)
    f_entrega = models.DateField()
    Enlace = models.URLField()
    Usuario = models.ForeignKey(Usuario, blank=True)
    def __unicode__(self):
        return u'%s' % (
            self.Descripcion,
            )
