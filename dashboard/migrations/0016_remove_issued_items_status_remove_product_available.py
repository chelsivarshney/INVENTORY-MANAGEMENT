# Generated by Django 4.1.7 on 2023-04-30 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_remove_issued_items_accepted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issued_items',
            name='status',
        ),
        migrations.RemoveField(
            model_name='product',
            name='available',
        ),
    ]
