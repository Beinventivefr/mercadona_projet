from django.db import models

# Create your models here.
class Catergory(models.Model):
    wording = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Catergory'
        verbose_name_plural = 'Catergories'


