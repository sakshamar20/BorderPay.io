from django.db import models

Locations =    [('india', 'india'),
               ('usa', 'usa'),
               ('canada','canada'),
               ('netherlands', 'netherlands'),
               ('austarlia','australia')
               ]

Banks =        [('a', 'a'),
               ('b', 'b'),
               ('c','c'),
               ('d', 'd'),
               ('e','e')
               ]

Denominations = [('rupees','rupees'),
                 ('dollar','dollar'),
                 ('euro','euro')
                ]

Types = [('need','need'),
         ('regular','regular')
        ]

Tips = [('employer','employer'),
        ('employee','employee')
        ]

class Employer(models.Model):
    userID = models.PositiveIntegerField(null=True)
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)
    location = models.CharField(
        max_length=50, choices=Locations, default='india')
    bank = models.CharField(
        max_length=50, choices=Banks, default='a')
    account = models.CharField(max_length=20, null=False) 
    denomination = models.CharField(
        max_length=50, choices=Denominations, default='rupees')
    
class Employee(models.Model):
    userID = models.PositiveIntegerField(null=False)
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)
    contractId = models.PositiveIntegerField(null=True)
    Location = models.CharField(
        max_length=50, choices=Locations, default='india')
    Bank = models.CharField(
        max_length=50, choices=Banks, default='a')
    Bank_account = models.CharField(max_length=20, null=False)
    Denomination = models.CharField(
        max_length=50, choices=Denominations, default='rupees')
    Withdraw_amount = models.PositiveIntegerField


class Transactions_request(models.Model):
    Bank_employer = models.CharField(
        max_length=50, choices=Banks, default='a')
    Bank_employee = models.CharField(
        max_length=50, choices=Banks, default='a')
    Bank_account_employer = models.CharField(max_length=20, null=False)
    Bank_account_employee = models.CharField(max_length=20, null=False)
    Country_employer = models.CharField(

        max_length=50, choices=Locations, default='india')
    Country_employee = models.CharField(
        max_length=50, choices=Locations, default='india')
    Amount = models.PositiveIntegerField(null=False)


class Contract(models.Model):
    employerID = models.PositiveIntegerField(null=False)
    employeeID = models.PositiveIntegerField(null=False)
    Type = models.CharField(
        max_length=50, choices=Types, default='regular')
    Salary = models.PositiveIntegerField(null=False)
    Interval = models.PositiveIntegerField(null=False)
    Timer = models.PositiveIntegerField(null=False)

class Advance_requests:
    employeeID = models.PositiveIntegerField(null=False)
    Amount = models.PositiveIntegerField(null=False)

class Advance_approvals:
    employeeID = models.PositiveIntegerField(null=False)
    Amount = models.PositiveIntegerField(null=False)
    Interval = models.PositiveIntegerField(null=False)
    Timer = models.PositiveIntegerField(null=False)

class Withdraw_approvals:
    employeeID = models.PositiveIntegerField(null=False)
    Amount = models.PositiveIntegerField(null=False)
    Interval = models.PositiveIntegerField(null=False)
    Timer = models.PositiveIntegerField(null=False)

class Contract_Requests:
    employerID = models.PositiveIntegerField(null=False)
    employeeID = models.PositiveIntegerField(null=False)
    Type = models.CharField(
        max_length=50, choices=Types, default='regular')
    Salary = models.PositiveIntegerField(null=False)
    Interval = models.PositiveIntegerField(null=False)
