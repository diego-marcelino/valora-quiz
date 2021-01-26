# Generated by Django 3.0.11 on 2021-01-25 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['player__username'],
            },
        ),
        migrations.CreateModel(
            name='CategoryScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(help_text='Question ctegories', on_delete=django.db.models.deletion.CASCADE, to='categories.Category', verbose_name='Question ctegories')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_scores', to='ranking.Profile')),
            ],
        ),
    ]