# Generated by Django 3.1.4 on 2020-12-09 12:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20201209_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
