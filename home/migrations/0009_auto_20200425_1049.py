# Generated by Django 3.0.4 on 2020-04-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200425_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testmodel',
            name='height',
        ),
        migrations.RemoveField(
            model_name='testmodel',
            name='width',
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]