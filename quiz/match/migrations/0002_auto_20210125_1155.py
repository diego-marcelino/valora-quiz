# Generated by Django 3.0.11 on 2021-01-25 11:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='questions_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), null=True, size=10),
        ),
    ]