# Generated by Django 3.0.14 on 2021-12-11 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='deptContactPerson',
            field=models.CharField(db_column='dept_contact_person', max_length=100),
        ),
    ]