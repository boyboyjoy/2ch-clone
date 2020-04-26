# Generated by Django 3.0.4 on 2020-04-25 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_testmodel_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='height',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='width',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='image',
            field=models.ImageField(height_field=models.IntegerField(default=100), upload_to='media/', width_field=models.IntegerField(default=100)),
        ),
    ]