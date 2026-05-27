from django.db import models

class Hojas(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100,
    verbose_name='Nombre',default=None)
    precio=models.PositiveIntegerField(verbose_name='Precio',default=0)
    imagen=models.ImageField(upload_to='imagenes/',
    null=True,verbose_name='Imagen')
    descripcion=models.TextField(null=True,verbose_name='Descripción')

    def __str__(self):
        fila="Nombre:"+self.nombre + " - " + "Precio:" + str(self.precio) + " Descripción:" + self.descripcion
        return fila

    def delete(self,using=None,keep_parents=False): 
        self.imagen.storage.delete(self.imagen.name)
        super().delete()