# Generated by Django 4.2 on 2025-01-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('middleware', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageaccesslog',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]