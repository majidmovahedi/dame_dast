# Generated by Django 5.0 on 2024-02-25 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_ads_userbookmark'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ads',
            new_name='Advertise',
        ),
    ]
