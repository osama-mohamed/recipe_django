# Generated by Django 3.2.9 on 2021-12-07 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipeingredientimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredientimage',
            name='extracted',
            field=models.TextField(blank=True, null=True),
        ),
    ]
