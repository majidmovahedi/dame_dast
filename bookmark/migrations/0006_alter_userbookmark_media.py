# Generated by Django 5.0.2 on 2024-03-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0005_alter_userbookmark_link_alter_userbookmark_media_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbookmark',
            name='media',
            field=models.TextField(blank=True, null=True),
        ),
    ]
