from django.db import models

class Hojas(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,
    verbose_name='Nombre',default=0)
    price =models.PositiveIntegerField(verbose_name='Precio',default=0)
    imagen = models.ImageField(upload_to='hojitas/',
    null=True,verbose_name='Imagen')
    description=models.TextField(null=True,verbose_name='Descripción')

    def _str_(self):
        fila="Nombre: "+self.name+" - " + "Precio: " +str(self.price)+ " Descripción: " +self.description
        return fila

    def delete(self,using=None,keep_parents=False): 
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

    class Meta:
        verbose_name = "Hoja"          
        verbose_name_plural = "Hojas"