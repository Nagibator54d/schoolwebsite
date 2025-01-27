# Generated by Django 5.0.6 on 2024-05-21 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images5/')),
            ],
            options={
                'verbose_name': 'О Школе',
                'verbose_name_plural': 'О Школе',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images4/')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статья',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('image', models.ImageField(upload_to='images2/')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images3/')),
            ],
            options={
                'verbose_name': 'Педагоги',
                'verbose_name_plural': 'Педагоги',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('description', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolwebsite.category')),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
