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


class Employer(models.Model):
    username = models.CharField(max_length=20, null=False, primary_key=True)
    password = models.CharField(max_length=20, null=False)
    location = models.CharField(max_length=50, choices=Locations, default='india')
    bank = models.CharField(max_length=50, choices=Banks, default='a')
    account = models.CharField(max_length=20, null=False)
    denomination = models.CharField(max_length=50, choices=Denominations, default='rupees')

class Employee(models.Model):
    username = models.CharField(max_length=20, null=False, primary_key=True)
    password = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=30, null=True)
    contractId = models.PositiveIntegerField(null=True)
    location = models.CharField(max_length=50, choices=Locations, default='india')
    bank = models.CharField(max_length=50, choices=Banks, default='a')
    account = models.CharField(max_length=20, null=False)
    denomination = models.CharField(max_length=50, choices=Denominations, default='rupees')
    withdraw_amount = models.PositiveIntegerField(null=False, default=0)
    worked_amount = models.PositiveIntegerField(null = False, default=0)
    given_amount = models.PositiveIntegerField(null=False, default =0)

class Transactions_request(models.Model):
    username_er = models.CharField(max_length=20, null=True)
    username_ee = models.CharField(max_length=20, null=True)
    bank_employer = models.CharField(max_length=50, choices=Banks, default='a')
    bank_employee = models.CharField(max_length=50, choices=Banks, default='a')
    bank_account_employer = models.CharField(max_length=20, null=False)
    bank_account_employee = models.CharField(max_length=20, null=False)
    country_employer = models.CharField(max_length=50, choices=Locations, default='india')
    country_employee = models.CharField(max_length=50, choices=Locations, default='india')
    amount = models.PositiveIntegerField(null=False)
    den_employee = models.CharField(max_length=50, choices=Denominations, default='rupees')
    den_employer = models.CharField(max_length=50, choices=Denominations, default='rupees')
    status = models.PositiveIntegerField(null=True)


class Advance_requests(models.Model):
    employeeID = models.PositiveIntegerField(null=False)
    Amount = models.PositiveIntegerField(null=False)

class Advance_approvals(models.Model):
    employeeID = models.PositiveIntegerField(null=False)
    Amount = models.PositiveIntegerField(null=False)
    Interval = models.PositiveIntegerField(null=False)
    Timer = models.PositiveIntegerField(null=False)

class Withdraw_approvals(models.Model):
    employeeID = models.PositiveIntegerField(null=False)
    Amount = models.PositiveIntegerField(null=False)
    Interval = models.PositiveIntegerField(null=False)
    Timer = models.PositiveIntegerField(null=False)

class Contract_Requests(models.Model):
    username_er = models.CharField(max_length=20, null=True)
    username_ee = models.CharField(max_length=20, null=True)
    type = models.CharField(max_length=50, choices=Types, default='regular')
    salary = models.PositiveIntegerField(null=True)
    interval = models.PositiveIntegerField(null=False)
    approval = models.PositiveIntegerField(null=False,default=0)
    ctc = models.PositiveIntegerField(null=True)
    timer = models.PositiveIntegerField(null=False, default = 0)

