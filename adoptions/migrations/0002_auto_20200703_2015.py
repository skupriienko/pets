# Generated by Django 3.0.8 on 2020-07-03 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='vaccination',
            new_name='vaccinations',
        ),
    ]
