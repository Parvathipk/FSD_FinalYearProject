# Generated by Django 5.1.4 on 2024-12-23 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_nutritionlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutritionlog',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
