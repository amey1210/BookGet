# Generated by Django 2.1 on 2018-10-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='shop/static/products/%y/%m/%d'),
        ),
    ]
