# Generated by Django 3.2.9 on 2021-12-04 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipeingredient_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='quantity_as_float',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
