# Generated by Django 4.0.1 on 2022-02-08 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0003_brand_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]