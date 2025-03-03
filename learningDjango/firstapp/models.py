from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    
#One to Many Relationship
class Review(models.Model):
    fk = models.ForeignKey(Firstapp,on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(default='')
    date_added = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.user.username}\'s review on {self.fk.name}'

# Many to Many Relationship

class Store(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    products = models.ManyToManyField(Firstapp, related_name='stores')

    def __str__(self):
        return self.name
    
# One to One Relationship

class Profile(models.Model):
    user = models.OneToOneField(Firstapp,on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(default='')

    def __str__(self):
        return f'{self.user.name}\'s profile'