# Generated by Django 3.1.1 on 2020-09-30 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='telephone',
            field=models.TextField(default='not have one', max_length=14),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employe',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
