# Generated by Django 4.2.11 on 2024-04-20 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trangchu', '0002_khachhang_netflix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khachhang',
            name='Netflix',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True),
        ),
    ]
