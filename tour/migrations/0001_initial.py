# Generated by Django 5.1 on 2024-10-15 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': 'availableDate',
                'verbose_name_plural': 'availableDates',
            },
        ),
        migrations.CreateModel(
            name='Deparment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'deparment',
                'verbose_name_plural': 'deparments',
            },
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'municipality',
                'verbose_name_plural': 'municipaiyties',
            },
        ),
        migrations.CreateModel(
            name='TourCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'tourCategory',
                'verbose_name_plural': 'tourCategories',
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('images', models.ImageField(blank=True, null=True, upload_to='tour')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('availableDate', models.ManyToManyField(to='tour.availabledate')),
                ('deparment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.deparment')),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.municipality')),
                ('categories', models.ManyToManyField(to='tour.tourcategory')),
            ],
            options={
                'verbose_name': 'tour',
                'verbose_name_plural': 'tours',
            },
        ),
    ]
