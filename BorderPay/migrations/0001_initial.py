# Generated by Django 5.0.4 on 2024-05-01 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advance_approvals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username_ee', models.CharField(max_length=20, null=True)),
                ('username_er', models.CharField(max_length=20, null=True)),
                ('amount', models.PositiveIntegerField()),
                ('interval', models.PositiveIntegerField()),
                ('timer', models.PositiveIntegerField(default=1000)),
                ('duration', models.PositiveIntegerField()),
                ('status', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Advance_requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, null=True)),
                ('Amount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contract_Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username_er', models.CharField(max_length=20, null=True)),
                ('username_ee', models.CharField(max_length=20, null=True)),
                ('type', models.CharField(choices=[('need', 'need'), ('regular', 'regular')], default='regular', max_length=50)),
                ('salary', models.PositiveIntegerField(null=True)),
                ('interval', models.PositiveIntegerField()),
                ('approval', models.PositiveIntegerField(default=0)),
                ('ctc', models.PositiveIntegerField(null=True)),
                ('timer', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30, null=True)),
                ('contractId', models.PositiveIntegerField(null=True)),
                ('location', models.CharField(choices=[('india', 'india'), ('usa', 'usa'), ('canada', 'canada'), ('netherlands', 'netherlands'), ('austarlia', 'australia')], default='india', max_length=50)),
                ('bank', models.CharField(choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'), ('e', 'e')], default='a', max_length=50)),
                ('account', models.CharField(max_length=20)),
                ('denomination', models.CharField(choices=[('rupees', 'rupees'), ('dollar', 'dollar'), ('euro', 'euro')], default='rupees', max_length=50)),
                ('withdraw_amount', models.PositiveIntegerField(default=0)),
                ('worked_amount', models.PositiveIntegerField(default=0)),
                ('given_amount', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('location', models.CharField(choices=[('india', 'india'), ('usa', 'usa'), ('canada', 'canada'), ('netherlands', 'netherlands'), ('austarlia', 'australia')], default='india', max_length=50)),
                ('bank', models.CharField(choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'), ('e', 'e')], default='a', max_length=50)),
                ('account', models.CharField(max_length=20)),
                ('denomination', models.CharField(choices=[('rupees', 'rupees'), ('dollar', 'dollar'), ('euro', 'euro')], default='rupees', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username_er', models.CharField(max_length=20, null=True)),
                ('username_ee', models.CharField(max_length=20, null=True)),
                ('bank_employer', models.CharField(choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'), ('e', 'e')], default='a', max_length=50)),
                ('bank_employee', models.CharField(choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'), ('e', 'e')], default='a', max_length=50)),
                ('bank_account_employer', models.CharField(max_length=20)),
                ('bank_account_employee', models.CharField(max_length=20)),
                ('country_employer', models.CharField(choices=[('india', 'india'), ('usa', 'usa'), ('canada', 'canada'), ('netherlands', 'netherlands'), ('austarlia', 'australia')], default='india', max_length=50)),
                ('country_employee', models.CharField(choices=[('india', 'india'), ('usa', 'usa'), ('canada', 'canada'), ('netherlands', 'netherlands'), ('austarlia', 'australia')], default='india', max_length=50)),
                ('amount', models.PositiveIntegerField()),
                ('den_employee', models.CharField(choices=[('rupees', 'rupees'), ('dollar', 'dollar'), ('euro', 'euro')], default='rupees', max_length=50)),
                ('den_employer', models.CharField(choices=[('rupees', 'rupees'), ('dollar', 'dollar'), ('euro', 'euro')], default='rupees', max_length=50)),
                ('status', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw_approvals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, null=True)),
                ('Amount', models.PositiveIntegerField()),
                ('Interval', models.PositiveIntegerField()),
                ('Timer', models.PositiveIntegerField()),
            ],
        ),
    ]
