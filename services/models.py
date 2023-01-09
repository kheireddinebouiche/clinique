from django.db import models
from medecins.models import *

class Service(models.Model):
    designation = models.CharField(max_length=100, null=True)
    responsable = models.ForeignKey(Medecins, null=True, blank=True, on_delete=models.DO_NOTHING)



    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name="Service"
        verbose_name_plural="Services"

    def __str__(self):
        return self.designation


