# Generated by Django 3.1.2 on 2020-10-25 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_of_dispatch',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
