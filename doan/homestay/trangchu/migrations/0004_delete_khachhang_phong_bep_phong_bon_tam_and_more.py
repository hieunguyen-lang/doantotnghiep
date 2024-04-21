# Generated by Django 4.2.11 on 2024-04-20 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trangchu', '0003_alter_khachhang_netflix'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Khachhang',
        ),
        migrations.AddField(
            model_name='phong',
            name='Bep',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True),
        ),
        migrations.AddField(
            model_name='phong',
            name='Bon_tam',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True),
        ),
        migrations.AddField(
            model_name='phong',
            name='Netflix',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True),
        ),
    ]