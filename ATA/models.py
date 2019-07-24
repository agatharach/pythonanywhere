from django.db import models

# Create your models here.
class Mentor (models.Model):
    nama = models.CharField(max_length=225)
    pengalaman = models.CharField(max_length=225)
    motto = models.TextField()
    photo = models.URLField(max_length=225)

class Mentee (models.Model):
    nama = models.CharField(max_length=225)
    motto = models.TextField()
    photo = models.URLField(max_length=225)

class Blog (models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    date_create = models.DateField()
    photo = models.URLField(max_length=225)