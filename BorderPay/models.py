from django.db import models

Locations =    [('India', 'India'),
               ('Usa', 'Usa'),
               ('Canada','Canada'),
               ('Netherlands', 'Netherlands'),
               ('Austarlia','Australia')
               ]

Banks =        [('A', 'A'),
               ('B', 'B'),
               ('C','C'),
               ('D', 'D'),
               ('E','E')
               ]

Denominations = [('Rupees','Rupees'),
                 ('Dollar','Dollar'),
                 ('Euro','Euro')
                ]


# Create your models here.
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Location = models.CharField(
        max_length=50, choices=Locations, default='India')
    Bank = models.CharField(
        max_length=50, choices=Banks, default='A')
    Denomination = models.CharField(
        max_length=50, choices=Denominations, default='Rupees')
    
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Location = models.CharField(
        max_length=50, choices=Locations, default='India')
    Bank = models.CharField(
        max_length=50, choices=Banks, default='A')
    Denomination = models.CharField(
        max_length=50, choices=Denominations, default='Rupees')
