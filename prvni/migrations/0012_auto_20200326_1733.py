# Generated by Django 3.0.1 on 2020-03-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prvni', '0011_auto_20200326_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majitele',
            name='cena',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='majitele',
            name='cena_les',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='majitele',
            name='cena_pole',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='majitele',
            name='cena_rok',
            field=models.IntegerField(default=0),
        ),
    ]