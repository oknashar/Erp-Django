# Generated by Django 3.1.1 on 2020-10-05 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20201005_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='الكميه'),
        ),
    ]
