# Generated by Django 3.1.2 on 2020-11-02 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20201102_2235'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productvariant',
            unique_together={('product', 'size')},
        ),
    ]
