from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100,unique=True)
    address = models.TextField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
