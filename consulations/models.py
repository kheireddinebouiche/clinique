from django.db import models
from patients.models import *
from django.contrib.auth.models import User


class Medicament(models.Model):
    designation = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name="Medicament"
        verbose_name_plural = "Medicaments"

    def __str__(self):
        return self.designation


class TypeConsultation(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name="Type de consultation"
        verbose_name_plural="Types de consultations"

    def __str__(self):
        return self.description


class Consultation(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patients,blank=True, null=True, on_delete=models.CASCADE)

    motif = models.TextField(max_length=2000, blank=True, null=True)
    resultat = models.TextField(max_length=2000, blank=True, null=True)

    date_consultation = models.DateTimeField(auto_now_add=True,blank=True, null=True)


    class Meta:
        verbose_name="Consultation"
        verbose_name_plural="Consultations"
    
    def __str__(self):
        return self.patient


class RendezVous(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patients,blank=True, null=True, on_delete=models.CASCADE)

    motif = models.TextField(max_length=2000, blank=True, null=True)

    date_rendez = models.DateTimeField(auto_now_add=True)

    is_approved = models.BooleanField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name="Rendez Vous"
        verbose_name_plural="Liste des rendez-vous"
    
    def __str__(self):
        return self.patient


# class OrdonnanceItem(models.Model):
#     user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
#     medicament = models.ForeignKey(Medicament, null=True, blank=True, on_delete=models.CASCADE)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name="Ligne Ordonnance"
#         verbose_name_plural = "Lignes Ordonnances"

#     def __str__(self):
#         return self.medicament

# class Ordonnance(models.Model):
#     pass