# Generated by Django 3.1.4 on 2021-05-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asd', '0002_auto_20210509_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='album_pics'),
        ),
    ]
