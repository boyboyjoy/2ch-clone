# Generated by Django 3.0.4 on 2020-04-25 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200425_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]