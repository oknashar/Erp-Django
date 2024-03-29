# Generated by Django 3.1.1 on 2020-10-05 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0005_auto_20201003_1228'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0010_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.SlugField(blank=True, max_length=20, null=True, unique=True, verbose_name='الباركود'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='المنتج')),
            ],
            options={
                'verbose_name': 'OrderItem',
                'verbose_name_plural': 'OrderItems',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='وقت البيع')),
                ('ordered', models.BooleanField(default=False)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employe.employe', verbose_name='البائع')),
                ('items', models.ManyToManyField(to='product.OrderItem', verbose_name='المنتجات المباعه')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='الكاشير')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
