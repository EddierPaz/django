from django.db import models

class Hojas(models.Model):
    name = models.CharField('name sheet', max_length=100)
    price = models.FloatField('price sheet')
    imagen = models.ImageField(upload_to='hojitas')
    description = models.TextField('description sheet')

    def __str__(self):
        return f"{self.name} - {self.price}"