# Generated by Django 4.0.4 on 2022-07-14 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_rename_address_customer_mailaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.book'),
        ),
    ]