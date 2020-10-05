# Generated by Django 3.1.1 on 2020-09-30 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('salary', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Employe',
                'verbose_name_plural': 'Employes',
            },
        ),
        migrations.CreateModel(
            name='Absense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateIn', models.DateTimeField(auto_now=True)),
                ('dateOut', models.DateTimeField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employe.employe')),
            ],
            options={
                'verbose_name': 'absense',
                'verbose_name_plural': 'absenses',
            },
        ),
    ]
