# Generated by Django 3.0.14 on 2021-12-11 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20211211_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='PunchinDetails',
            fields=[
                ('id', models.IntegerField(auto_created=True, db_column='punch_id', primary_key=True, serialize=False)),
                ('punchinTime', models.DateTimeField(db_column='date_and_time_of_punch')),
                ('empid', models.ForeignKey(db_column='emp_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Employee')),
            ],
        ),
    ]
