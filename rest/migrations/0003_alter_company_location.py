# Generated by Django 4.2.4 on 2023-08-14 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_company_company_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(default='Bangalore', max_length=50),
        ),
    ]