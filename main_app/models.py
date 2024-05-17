from django.db import models
from django.contrib.auth.models import User
from datetime import date 

OCCASION = (
    ('CR', 'CHRISTMAS'),
    ('NY', 'NEW YEAR'),
    ('EA', 'EASTER') 
    )

# Create your models here.

class Rivers(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Country(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    population = models.IntegerField()
    Rivers = models.ManyToManyField(Rivers)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    

    def __str__(self):
        return self.name
    
class Holidays(models.Model):
    date = models.DateField('Holiday date')
    occasion = models.CharField ( max_length=2,
        choices=OCCASION,
        default=OCCASION[0][0]
    )

    Country= models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__ (self):
        return f"{self.get_occasion_display()} on {self.date}"
    

    class Meta:
        ordering = ['-date']

        
