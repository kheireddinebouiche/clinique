from django.db import models
from django.contrib.auth.models import User


class Profession(models.Model):
    designation = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name="Profession"
        verbose_name_plural = "Professions"

    def __str__(self):
        return self.designation

class Medecins(models.Model):
    nom = models.CharField(max_length=100, blank=True, null=True)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    prefession = models.ForeignKey(Profession, blank=True, null=True, on_delete=models.DO_NOTHING)
    adresse = models.CharField(max_length=200, blank=True, null=True)
    tel = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name="Medecin"
        verbose_name_plural = "Medecins"

    def __str__(self):
        return self.nom


