from django.db import models
from django.contrib.auth.models import User

SEXE ={
    ('f', 'Femme'),
    ('h', 'Homme'),
}

class Patients(models.Model):
    created_by = models.OneToOneField(User, on_delete=models.CASCADE)

    nom = models.CharField(max_length=100, null=True, blank=True)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    adresse = models.CharField(max_length=1000, null=True, blank=True)

    sexe = models.CharField(max_length=1, choices=SEXE, blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)

    nss = models.CharField(max_length=24,blank=True, null=True)
    nin = models.CharField(max_length=100,blank=True, null=True)
     

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name="Patient"
        verbose_name_plural = "Patients"

    def __str__(self):
        return self.nom
