# Generated by Django 2.2.3 on 2019-07-22 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='برند')),
            ],
            options={
                'verbose_name_plural': 'برندها',
            },
        ),
        migrations.CreateModel(
            name='types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نوع محصول')),
                ('unit', models.CharField(max_length=20, verbose_name='واحد اندازه گیری')),
            ],
            options={
                'verbose_name_plural': 'انواع محصولات',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='نام')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('image', models.ImageField(default='tools/default.jpg', upload_to='tools')),
                ('sizes', models.CharField(max_length=20, null=True, verbose_name='سایزها')),
                ('rate', models.IntegerField()),
                ('Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.types')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.brands')),
            ],
            options={
                'verbose_name_plural': 'محصولات',
            },
        ),
    ]
