# Generated by Django 3.1.4 on 2020-12-09 12:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='about',
            field=models.CharField(default=django.utils.timezone.now, max_length=2558),
            preserve_default=False,
        ),
    ]
