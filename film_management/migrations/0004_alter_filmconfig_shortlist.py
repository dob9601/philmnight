# Generated by Django 3.2 on 2021-10-20 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_management', '0003_rename_voting_period_length_filmconfig_voting_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmconfig',
            name='shortlist',
            field=models.ManyToManyField(blank=True, to='film_management.Film'),
        ),
    ]
