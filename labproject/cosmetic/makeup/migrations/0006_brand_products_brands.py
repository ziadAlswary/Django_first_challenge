# Generated by Django 4.0.1 on 2022-02-08 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0005_remove_products_brands_delete_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('orgin', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='brands',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='makeup.brand'),
            preserve_default=False,
        ),
    ]
