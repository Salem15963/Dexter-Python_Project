# Generated by Django 2.2.4 on 2022-10-11 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dexterapp', '0002_appointment_national_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='dexterapp.Clinic'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_bith',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_visit_date',
            field=models.DateField(null=True),
        ),
    ]