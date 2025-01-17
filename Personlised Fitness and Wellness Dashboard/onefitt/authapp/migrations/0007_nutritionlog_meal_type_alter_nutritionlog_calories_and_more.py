# Generated by Django 5.1.4 on 2024-12-23 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_moodlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutritionlog',
            name='meal_type',
            field=models.CharField(default='Lunch', max_length=50),
        ),
        migrations.AlterField(
            model_name='nutritionlog',
            name='calories',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='nutritionlog',
            name='food_item',
            field=models.CharField(max_length=200),
        ),
    ]
