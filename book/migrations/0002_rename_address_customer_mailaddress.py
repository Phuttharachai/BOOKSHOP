# Generated by Django 4.0.4 on 2022-07-14 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='address',
            new_name='mailaddress',
        ),
    ]