# Generated by Django 4.0.6 on 2022-07-15 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_rename_services_service'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fir',
            new_name='FIRs',
        ),
    ]