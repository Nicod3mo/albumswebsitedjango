# Generated by Django 3.1.4 on 2021-05-10 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]