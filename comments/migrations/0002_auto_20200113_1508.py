# Generated by Django 3.0.2 on 2020-01-13 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='aproved',
            new_name='approved',
        ),
    ]