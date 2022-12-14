# Generated by Django 4.1.2 on 2022-11-04 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0002_alter_product_options_alter_stock_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['address'], 'verbose_name': 'Адрес склада', 'verbose_name_plural': 'Адреса'},
        ),
        migrations.AlterField(
            model_name='stock',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='stock',
            name='products',
            field=models.ManyToManyField(through='logistic.StockProduct', to='logistic.product'),
        ),
        migrations.AlterField(
            model_name='stockproduct',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='logistic.stock', verbose_name='Склады'),
        ),
    ]
