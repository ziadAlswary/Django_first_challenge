# Generated by Django 4.0.1 on 2022-02-08 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0010_alter_brand_s_lug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='s_lug',
        ),
    ]