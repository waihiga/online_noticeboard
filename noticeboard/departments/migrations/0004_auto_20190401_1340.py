# Generated by Django 2.1.7 on 2019-04-01 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0003_department_hod_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='hod_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hod_departments', to=settings.AUTH_USER_MODEL),
        ),
    ]