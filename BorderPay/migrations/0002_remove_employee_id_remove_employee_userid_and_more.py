# Generated by Django 5.0.4 on 2024-04-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BorderPay', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='userID',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='withdraw_amount',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='userID',
        ),
        migrations.AddField(
            model_name='employee',
            name='given_amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employer',
            name='username',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
