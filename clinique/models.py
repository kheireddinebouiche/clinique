from django.db import models



class Informations(models.Model):
    designation = models.CharField(max_length=100, blank=True, null=True)


    class Meta:
        verbose_name="Information"
        verbose_name_plural = "Informations"

    def __str__(self):
        return self.designation

