# Generated by Django 5.1.1 on 2024-11-15 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='grade',
            field=models.CharField(choices=[('A-', 'A-'), ('A', 'A'), ('A+', 'A+'), ('B-', 'B-'), ('B', 'B'), ('B+', 'B+'), ('C-', 'C-'), ('C', 'C'), ('C+', 'C+'), ('D-', 'D-'), ('D', 'D'), ('D+', 'D+'), ('F', 'F')], max_length=2),
        ),
    ]
