# Generated by Django 4.2.11 on 2024-04-26 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trangchu', '0009_remove_giohang_complete_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='giohang_items',
            name='gia',
            field=models.IntegerField(null=True),
        ),
    ]
