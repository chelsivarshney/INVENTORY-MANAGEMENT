# Generated by Django 4.1.7 on 2023-05-17 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_remove_product_barcode_product_qr_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='asset',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sno',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
