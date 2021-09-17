from django.db import models


# Create your models here.
class Form(models.Model):

    name = models.CharField(max_length=60)
    rollNa = models.CharField(max_length=15)
    dept = models.CharField(max_length=30)
    addmission = models.DateField()
    iamge = models.ImageField(upload_to='pics')

