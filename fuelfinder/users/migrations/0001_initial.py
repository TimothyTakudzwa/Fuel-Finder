<<<<<<< HEAD
# Generated by Django 2.2.7 on 2019-11-22 16:32
=======
# Generated by Django 2.2.7 on 2019-11-22 15:32
>>>>>>> 5809ad207947a0c3c4c7a8c5cfe992366f59e7eb

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
=======
            name='SupplierUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('last_name', models.CharField(max_length=50, unique=True)),
>>>>>>> 5809ad207947a0c3c4c7a8c5cfe992366f59e7eb
                ('email', models.CharField(max_length=50, unique=True)),
                ('created_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
