# Generated by Django 2.1.7 on 2019-03-26 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190325_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_role', to='roles.Role'),
        ),
    ]
