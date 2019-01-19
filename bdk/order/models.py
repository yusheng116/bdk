from django.db import models

# Create your models here.
class Order(models.Model):
    name1=models.CharField(max_length=128)
    name2=models.CharField(max_length=128)
    country=models.CharField(max_length=128)
    PT=models.CharField(max_length=128)
    ADR=models.CharField(max_length=128)
    phone=models.CharField(max_length=128)
    number=models.CharField(max_length=128)
    email=models.CharField(max_length=128)
    shoes=models.CharField(max_length=128)
    SD=models.CharField(max_length=128)

    def __str__(self):
        return self.name1
