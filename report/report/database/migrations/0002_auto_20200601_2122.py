# Generated by Django 2.2.3 on 2020-06-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db',
            name='data',
            field=models.TextField(default='[]'),
        ),
    ]
