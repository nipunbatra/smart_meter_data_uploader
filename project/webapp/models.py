from django.db import models

# Create your models here.
class EnergyData(models.Model):
	FILE=models.FileField(upload_to='Data',null=True)
	
