from django.db import models

Location =    [('India', 'India'),
               ('Usa', 'Usa'),
               ('Canada','Canada'),
               ('Netherlands', 'Netherlands'),
               ('Austarlia','Australia')
               ]

Banks =    [('A', 'A'),
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
    Location = models.CharField(max_length=40)
    Bank = models.CharField(max_length=20)
    Denomination = models.CharField(
        max_length=50, choices=departments, default='Cardiologist')
