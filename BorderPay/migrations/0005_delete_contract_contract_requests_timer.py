# Generated by Django 5.0.4 on 2024-04-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BorderPay', '0004_employee_denomination_employee_withdraw_amount_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contract',
        ),
        migrations.AddField(
            model_name='contract_requests',
            name='Timer',
            field=models.PositiveIntegerField(default=0),
        ),
    ]