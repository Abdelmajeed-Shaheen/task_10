# Generated by Django 2.1.5 on 2020-02-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_auto_20200217_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=4),
        ),
    ]
