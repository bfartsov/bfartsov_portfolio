# Generated by Django 3.1.4 on 2020-12-09 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_about_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='name',
            new_name='farts_name',
        ),
        migrations.AddField(
            model_name='about',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
