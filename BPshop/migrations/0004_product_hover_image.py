# Generated by Django 3.2.9 on 2021-11-19 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BPshop', '0003_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hover_image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
    ]