# Generated by Django 3.0.1 on 2020-03-26 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prvni', '0008_auto_20200326_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majitele',
            name='cena',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='majitele',
            name='cena_les',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='majitele',
            name='cena_pole',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='majitele',
            name='cena_rok',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10),
        ),
    ]
