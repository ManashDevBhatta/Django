from django.db import models
from django.utils import timezone

# Create your models here.

class Firstapp(models.Model):
    NAME_TYPE_CHOICE = [
        ('MDB','Manash Dev Bhatta'),
        ('SBB','Surya Bahadur Bhandari'),
        ('KK','Karna Kumar'),
    ]
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='firstappimg')
    date_added = models.DateTimeField(default=timezone.now)
    superheros = models.CharField(max_length=10,choices=NAME_TYPE_CHOICE)
    description = models.TextField(default='')


    def __str__(self):
        return self.name