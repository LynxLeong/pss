from __future__ import unicode_literals
from django.db import models
from geoposition import Geoposition
from geoposition.fields import GeopositionField

class User(models.Model):
    """
    Model representing user
    """
    genderchoices = (
        ('male', 'Male'),
        ('female', 'Female'),
    )


    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=15)
    #dob = models.DateField
    gender = models.CharField(max_length=6, choices=genderchoices, default='male')
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.username

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class ReportedCases(models.Model):
    """
    Model representing reported cases
    """
    vectors = (
        ('aedes', 'Aedes Mosquito'),
        ('rat', 'Rat'),
    )

    amount = (
        ('5', '1 - 10'),
        ('18', '11 - 25'),
        ('38', '26 - 50'),
        ('75', '51 - 100'),
    )
    #case_id = models.CharField(max_length=30)
    #case_user = models.CharField(max_length=15)
    #case_date = models.DateTimeField(auto_now_add=True)
    Vector = models.CharField(max_length=10, choices=vectors, default='aedes')
    Vector_Number = models.IntegerField(choices=amount, default='5')
    Latitude = models.DecimalField(max_digits=25, decimal_places=20, null=True)
    Longitude = models.DecimalField(max_digits=25, decimal_places=20, null=True)
