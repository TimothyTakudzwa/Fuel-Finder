# Generated by Django 2.2.7 on 2019-11-23 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191123_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='suppliercontact',
            name='cellphone',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
