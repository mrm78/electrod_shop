# Generated by Django 2.2.3 on 2019-07-22 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190722_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='سایزها'),
        ),
    ]