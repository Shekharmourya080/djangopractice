# Generated by Django 3.0.14 on 2021-12-11 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211211_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='deptId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Department'),
        ),
    ]