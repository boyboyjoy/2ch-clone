# Generated by Django 3.0.4 on 2020-04-25 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='image',
            field=models.ImageField(height_field=100, upload_to='images', width_field=100),
        ),
    ]
