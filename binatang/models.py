from django.db import models

# Create your models here.
class NamaHewan(models.Model):
    nama_hewan = models.CharField(max_length=255)
    species =  models.CharField(max_length=17)
    berat = models.CharField(max_length=17)
    umur = models.PositiveIntegerField()
