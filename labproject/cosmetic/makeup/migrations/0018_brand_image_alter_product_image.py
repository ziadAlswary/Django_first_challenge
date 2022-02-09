# Generated by Django 4.0.1 on 2022-02-09 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0017_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(default='', upload_to='images/brands'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/products'),
        ),
    ]