# Generated by Django 3.2.9 on 2021-11-19 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BPshop', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name_plural': 'Продукты'},
        ),
    ]
