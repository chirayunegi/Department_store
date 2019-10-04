# Generated by Django 2.2 on 2019-10-03 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_exp_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='product',
            name='exp_date',
            field=models.DateTimeField(default=''),
        ),
    ]
