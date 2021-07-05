from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Album(models.Model):
    artista = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    fecha_salida = models.DateField()
    num_estrellas = models.IntegerField()
    imagen = models.ImageField(upload_to='album_pics', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('album_Detallar', kwargs={'pk': self.pk})


