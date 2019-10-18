from django.db import models

# Create your models here.
class Agenda(models.Model):

    name = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)

    def __str__(self):
        return self.name

