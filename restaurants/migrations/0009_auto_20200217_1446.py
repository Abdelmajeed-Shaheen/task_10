# Generated by Django 2.1.5 on 2020-02-17 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_auto_20200217_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
    ]
