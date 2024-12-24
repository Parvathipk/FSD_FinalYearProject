# Generated by Django 5.1.4 on 2024-12-23 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_remove_workoutlog_notes_workoutlog_calories_burned_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutlog',
            name='workout_type',
            field=models.CharField(choices=[('Cardio', 'Cardio'), ('Strength', 'Strength'), ('Yoga', 'Yoga'), ('Swimming', 'Swimming'), ('Cycling', 'Cycling')], max_length=100),
        ),
    ]