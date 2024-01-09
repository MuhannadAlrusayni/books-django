# Generated by Django 5.0.1 on 2024-01-08 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('FIC', 'Fiction'), ('NVL', 'Novel'), ('HRR', 'Horror')], max_length=3),
        ),
    ]