# Generated by Django 3.0.8 on 2020-08-01 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('patient_name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Others')], max_length=1)),
                ('dob', models.TextField()),
                ('approx_dob', models.DateField()),
                ('phone', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slip_id', models.CharField(max_length=15, unique=True)),
                ('phone', models.CharField(max_length=45, null=True)),
                ('report_no', models.CharField(max_length=3)),
                ('date', models.DateField(auto_now_add=True)),
                ('address', models.CharField(max_length=1000, null=True)),
                ('date_of_admission', models.DateField()),
                ('date_of_operation', models.DateField()),
                ('date_of_discharge', models.DateField()),
                ('diagnosis', models.CharField(blank=True, max_length=1000, null=True)),
                ('complain', models.CharField(blank=True, max_length=1000, null=True)),
                ('investigation', models.TextField(blank=True, null=True)),
                ('ot_procedure', models.CharField(blank=True, max_length=500, null=True)),
                ('advice', models.TextField(blank=True, null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slip.Patient')),
            ],
        ),
    ]
