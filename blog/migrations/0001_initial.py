# Generated by Django 3.1.2 on 2020-11-06 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('useraccount', '0002_auto_20201104_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True)),
                ('subtitle', models.CharField(max_length=180, null=True)),
                ('slug', models.CharField(max_length=240, null=True)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('title_image_url_1', models.URLField(blank=True, max_length=1024, null=True)),
                ('content_image_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('content_image_url_1', models.URLField(blank=True, max_length=1024, null=True)),
                ('content_image_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('content_image_url_2', models.URLField(blank=True, max_length=1024, null=True)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='useraccount.useraccount')),
            ],
        ),
    ]
