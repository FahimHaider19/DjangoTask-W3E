# Generated by Django 4.2.4 on 2023-08-28 06:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceApp', '0004_product_titleimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='developer',
            field=models.CharField(default='Anonymous', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='Anonymous', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(9999.0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='publisher',
            field=models.CharField(default='Anonymous', max_length=200),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(default='Anonymous', max_length=10000),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.CharField(default='Anonymous', max_length=200),
        ),
    ]
