# Generated by Django 4.1.2 on 2022-11-12 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='avaliable',
            new_name='available',
        ),
    ]
