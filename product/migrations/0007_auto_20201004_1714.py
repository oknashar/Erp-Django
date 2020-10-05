# Generated by Django 3.1.1 on 2020-10-04 15:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True, verbose_name='متاح'),
        ),
        migrations.AddField(
            model_name='product',
            name='date_published',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='تاريخ الاضافه'),
            preserve_default=False,
        ),
    ]