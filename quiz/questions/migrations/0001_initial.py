# Generated by Django 3.0.11 on 2021-01-24 19:06

import django.contrib.postgres.fields
import django.contrib.postgres.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(help_text='Question statement', max_length=255, verbose_name='Question statement')),
                ('choices', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=3, validators=[django.contrib.postgres.validators.ArrayMinLengthValidator(3)])),
                ('correct_choice_index', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2)])),
                ('categories', models.ManyToManyField(help_text='Question ctegories', related_name='questions', to='categories.Category', verbose_name='Question ctegories')),
            ],
        ),
    ]
