# Generated by Django 4.1.7 on 2023-04-24 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='cart_id',
            new_name='cart',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='dish_id',
            new_name='dish',
        ),
    ]
