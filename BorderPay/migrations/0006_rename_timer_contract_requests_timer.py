# Generated by Django 5.0.4 on 2024-04-28 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BorderPay', '0005_delete_contract_contract_requests_timer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract_requests',
            old_name='Timer',
            new_name='timer',
        ),
    ]