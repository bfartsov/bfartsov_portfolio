# Generated by Django 3.1.4 on 2020-12-09 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_portfolio_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='about',
            field=models.TextField(max_length=255),
        ),
    ]