# Generated by Django 3.1.7 on 2021-04-01 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=3)),
                ('number', models.CharField(max_length=11)),
                ('street_address', models.CharField(max_length=100)),
                ('street_address_2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('amount', models.CharField(max_length=10)),
                ('mop', models.CharField(choices=[('cc', 'Credit Card'), ('ot', 'Online Banking'), ('pp', 'PayPal')], default='', max_length=3)),
                ('account_no', models.CharField(max_length=18)),
                ('same', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('confirm', models.BooleanField(default=False)),
            ],
        ),
    ]
