# Generated by Django 5.0.1 on 2024-02-07 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caterapp', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_cater',
            field=models.BooleanField(default=False, verbose_name='is_cater'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_user',
            field=models.BooleanField(default=False, verbose_name='user'),
        ),
    ]
