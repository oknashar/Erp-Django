# Generated by Django 3.1.1 on 2020-10-05 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0005_auto_20201003_1228'),
        ('product', '0012_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='emp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employe.employe', verbose_name='البائع'),
        ),
    ]